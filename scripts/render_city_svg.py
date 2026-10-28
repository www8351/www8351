"""Render assets/contrib-city.svg from data/contributions.json.

Standard library only. Every day of the year becomes a building on an
oblique grid: weeks run left to right, weekdays recede from Sunday at the
front to Saturday at the back. Height follows the square root of the day's
count, colour follows GitHub's level. The city rises in a wave, holds,
sinks and repeats on a 10 second loop. Set STATIC=1 to emit the final
frame without animation.

    python scripts/render_city_svg.py
"""

from __future__ import annotations

import json
import math
import os
from datetime import date
from pathlib import Path

from fetch_contributions import placeholder_days
from render_heatmap_svg import DATA, LEVELS, PAD, TILE_STYLE, WIDTH, _sunday, stamp, summary
from svgterm import MUTED, TEXT, TITLE_BAR, window

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "assets" / "contrib-city.svg"

WEEK = (14.0, 1.2)  # screen step from one week to the next
DEPTH = (5.2, -4.6)  # screen step from one weekday to the next, receding
FILL = 0.78  # share of each grid step a footprint covers
MAX_H = 120.0
MIN_H = 3.0
LABEL_RISE = 22.0  # leader line above the tallest roof

CYCLE = 10.0
RISE_SPREAD = 1.8  # last building starts rising this long after the first
SINK_SPREAD = 0.5


def shade(hex_colour: str, factor: float) -> str:
    """Scale an #rrggbb colour, clamped to the valid range."""
    rgb = [int(hex_colour[i : i + 2], 16) for i in (1, 3, 5)]
    return "#" + "".join(f"{min(255, round(c * factor)):02x}" for c in rgb)


def point(w: float, r: float) -> tuple[float, float]:
    return w * WEEK[0] + r * DEPTH[0], w * WEEK[1] + r * DEPTH[1]


def height(count: int, best: int) -> float:
    if count <= 0 or best <= 0:
        return 0.0
    return max(MIN_H, MAX_H * math.sqrt(count) / math.sqrt(best))


def poly(points: list[tuple[float, float]], fill: str) -> str:
    return f'<polygon points="{" ".join(f"{x:.1f},{y:.1f}" for x, y in points)}" fill="{fill}"/>'


def place(days: list[dict]) -> list[dict]:
    """Grid position and height for each day, in back to front draw order."""
    sunday = _sunday(days)
    best = max(d["count"] for d in days)
    lots = []
    for d in days:
        day = date.fromisoformat(d["date"])
        lots.append({
            "day": d,
            "week": (day.toordinal() - sunday) // 7,
            "row": (day.weekday() + 1) % 7,
            "h": height(d["count"], best),
        })
    lots.sort(key=lambda b: (-b["row"], b["week"]))
    return lots


def building(b: dict, ox: float, oy: float, weeks: int, animate: bool) -> str:
    """One lot: a flat ground tile, plus a three-faced building on active days."""
    ax, ay = point(b["week"], b["row"])
    ax, ay = ax + ox, ay + oy
    wx, wy = WEEK[0] * FILL, WEEK[1] * FILL
    dx, dy = DEPTH[0] * FILL, DEPTH[1] * FILL
    a, bb, c, d = (ax, ay), (ax + wx, ay + wy), (ax + wx + dx, ay + wy + dy), (ax + dx, ay + dy)
    tip = f'<title>{b["day"]["count"]} on {b["day"]["date"]}</title>'
    ground = poly([a, bb, c, d], LEVELS[0])
    h = b["h"]
    if not h:
        return f"<g>{tip}{ground}</g>"

    colour = LEVELS[min(4, max(1, b["day"]["level"]))]
    up = lambda p: (p[0], p[1] - h)  # noqa: E731
    faces = (
        poly([a, bb, up(bb), up(a)], colour)
        + poly([bb, c, up(c), up(bb)], shade(colour, 0.7))
        + poly([up(a), up(bb), up(c), up(d)], shade(colour, 1.35))
    )
    if not animate:
        return f"<g>{tip}{ground}{faces}</g>"
    # Wave from the front-left corner, back and across the year.
    t = (b["week"] + 2 * b["row"]) / (weeks - 1 + 12)
    origin = f"transform-origin:0 {bb[1]:.1f}px"
    return (
        f"<g>{tip}{ground}"
        f'<g class="s" style="{origin};animation-delay:{t * SINK_SPREAD:.3f}s">'
        f'<g class="r" style="{origin};animation-delay:{t * RISE_SPREAD:.3f}s">{faces}</g></g></g>'
    )


def roof_centre(b: dict, ox: float, oy: float) -> tuple[float, float]:
    x, y = point(b["week"] + FILL / 2, b["row"] + FILL / 2)
    return x + ox, y + oy - b["h"]


def label(b: dict, ox: float, oy: float, animate: bool) -> str:
    x, y = roof_centre(b, ox, oy)
    anim = ' class="l"' if animate else ""
    return (
        f"<g{anim}>"
        f'<path d="M{x:.1f} {y - 3:.1f} V{y - LABEL_RISE:.1f}" stroke="{MUTED}" stroke-dasharray="2 2"/>'
        f'<circle cx="{x:.1f}" cy="{y - 3:.1f}" r="2" fill="{TEXT}"/>'
        f'<text x="{x:.1f}" y="{y - LABEL_RISE - 5:.1f}" font-size="11" fill="{TEXT}" '
        f'text-anchor="middle">Best Day</text>'
        "</g>"
    )


def bounds(lots: list[dict], weeks: int, tallest: dict | None) -> tuple[float, float, float, float]:
    """Screen box of the whole city, label included, before offsetting."""
    xs, ys = [], []
    for w, r in ((0, 0), (weeks - 1 + FILL, 0), (0, 6 + FILL), (weeks - 1 + FILL, 6 + FILL)):
        x, y = point(w, r)
        xs.append(x)
        ys.append(y)
    for b in lots:
        if b["h"]:
            ys.append(point(b["week"], b["row"] + FILL)[1] - b["h"])
    if tallest:
        ys.append(roof_centre(tallest, 0, 0)[1] - LABEL_RISE - 16)
    return min(xs), min(ys), max(xs), max(ys)


def style() -> str:
    pct = lambda s: f"{s / CYCLE * 100:.2f}%"  # noqa: E731
    return (
        ".r,.s{transform-box:view-box}"
        f".r{{animation:rise {CYCLE}s ease-out infinite both}}"
        f"@keyframes rise{{0%{{transform:scaleY(0)}}{pct(0.7)}{{transform:scaleY(1)}}"
        f"{pct(9.59)}{{transform:scaleY(1)}}{pct(9.6)},100%{{transform:scaleY(0)}}}}"
        f".s{{animation:sink {CYCLE}s ease-in infinite both}}"
        f"@keyframes sink{{0%,{pct(8.5)}{{transform:scaleY(1)}}{pct(9.0)},100%{{transform:scaleY(0)}}}}"
        f".l{{animation:tag {CYCLE}s linear infinite both}}"
        f"@keyframes tag{{0%,{pct(2.5)}{{opacity:0}}{pct(3.0)},{pct(8.0)}{{opacity:1}}{pct(8.4)},100%{{opacity:0}}}}"
        + TILE_STYLE
        + "@media (prefers-reduced-motion:reduce){.r,.s,.l,.t{animation:none}}"
    )


def render(data: dict | None, animate: bool = True) -> str:
    days = data["days"] if data else placeholder_days()
    s = data["stats"] if data else None

    lots = place(days)
    weeks = max(b["week"] for b in lots) + 1
    tallest = max(lots, key=lambda b: b["h"])
    tallest = tallest if tallest["h"] else None

    left, top, right, bottom = bounds(lots, weeks, tallest)
    ox = (WIDTH - (right - left)) / 2 - left
    oy = TITLE_BAR + PAD - top

    city = "".join(building(b, ox, oy, weeks, animate) for b in lots)
    if tallest:
        city += label(tallest, ox, oy, animate)

    footer, end = summary(s, 2 * PAD, WIDTH - 4 * PAD, bottom + oy + 26, 2.5, animate)
    user = data["user"] if data else "www8351"
    title = f"refael@github: ~ $ ./contributions.sh {user}"
    return window(WIDTH, int(end + PAD), title, stamp(data) + city + footer, style() if animate else "")


def main() -> None:
    data = json.loads(DATA.read_text(encoding="utf-8")) if DATA.exists() else None
    animate = os.environ.get("STATIC") != "1"
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(render(data, animate), encoding="utf-8")
    print(f"wrote {OUT}" + ("" if data else " (blank, no data yet)"))


if __name__ == "__main__":
    main()
