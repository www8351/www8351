"""Render assets/contrib-heatmap.svg from data/contributions.json.

Standard library only. Cells drop in on a diagonal sweep once, then hold.
Without a data file it draws a blank year that the first workflow run
replaces. Set STATIC=1 to emit the final frame without animation.

    python scripts/render_heatmap_svg.py
"""

from __future__ import annotations

import json
import os
from datetime import date
from pathlib import Path

from fetch_contributions import placeholder_days
from svgterm import BORDER, GREEN, MUTED, PANEL, TEXT, TITLE_BAR, esc, window

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data" / "contributions.json"
OUT = ROOT / "assets" / "contrib-heatmap.svg"

LEVELS = ["#161b22", "#0e4429", "#006d32", "#26a641", "#39d353"]

WIDTH = 900
PAD = 22
CELL = 12
GAP = 3
PITCH = CELL + GAP
LABEL_W = 34
MONTHS = "Jan Feb Mar Apr May Jun Jul Aug Sep Oct Nov Dec".split()


def short(day: str | None) -> str:
    if not day:
        return ""
    d = date.fromisoformat(day)
    return f"{MONTHS[d.month - 1]} {d.day}"


def plural(n: int) -> str:
    return "day" if n == 1 else "days"


def _sunday(days: list[dict]) -> int:
    first = date.fromisoformat(days[0]["date"])
    return first.toordinal() - (first.weekday() + 1) % 7


def week_count(days: list[dict]) -> int:
    """Week columns the calendar spans, usually 53, sometimes 54."""
    last = date.fromisoformat(days[-1]["date"]).toordinal()
    return (last - _sunday(days)) // 7 + 1


def grid(days: list[dict], x0: float, y0: float, animate: bool) -> tuple[str, int]:
    sunday = _sunday(days)
    cells, months = [], []
    last_label_week = -4
    prev_month = None
    weeks = 0
    for d in days:
        day = date.fromisoformat(d["date"])
        week = (day.toordinal() - sunday) // 7
        row = (day.weekday() + 1) % 7
        weeks = max(weeks, week + 1)
        x = x0 + week * PITCH
        y = y0 + row * PITCH
        anim = f' class="c" style="animation-delay:{(week + row) * 0.012:.3f}s"' if animate else ""
        cells.append(
            f'<rect{anim} x="{x}" y="{y}" width="{CELL}" height="{CELL}" rx="2.5" '
            f'fill="{LEVELS[min(4, max(0, d["level"]))]}"><title>{d["count"]} on {d["date"]}</title></rect>'
        )
        if row == 0 or d is days[0]:
            if day.month != prev_month and week - last_label_week >= 3:
                months.append(
                    f'<text x="{x}" y="{y0 - 8}" font-size="11" fill="{MUTED}">{MONTHS[day.month - 1]}</text>'
                )
                last_label_week = week
            prev_month = day.month
    labels = "".join(
        f'<text x="{x0 - 8}" y="{y0 + r * PITCH + CELL - 2}" font-size="10" fill="{MUTED}" '
        f'text-anchor="end">{name}</text>'
        for r, name in ((1, "Mon"), (3, "Wed"), (5, "Fri"))
    )
    return "".join(months) + labels + "".join(cells), weeks


def tile(x: float, y: float, w: float, label: str, value: str, unit: str, sub: str, delay: float, animate: bool) -> str:
    anim = f' class="t" style="animation-delay:{delay:.2f}s"' if animate else ""
    return (
        f"<g{anim}>"
        f'<rect x="{x}" y="{y}" width="{w}" height="66" rx="8" fill="{PANEL}" stroke="{BORDER}"/>'
        f'<text x="{x + 12}" y="{y + 20}" font-size="11" fill="{MUTED}">$ {esc(label)}</text>'
        f'<text x="{x + 12}" y="{y + 46}" font-size="22" font-weight="700" fill="{GREEN}">{esc(value)}'
        f'<tspan font-size="12" font-weight="400" fill="{MUTED}"> {esc(unit)}</tspan></text>'
        f'<text x="{x + 12}" y="{y + 60}" font-size="10" fill="{MUTED}">{esc(sub)}</text>'
        "</g>"
    )


def render(data: dict | None, animate: bool = True) -> str:
    days = data["days"] if data else placeholder_days()
    s = data["stats"] if data else None

    grid_w = week_count(days) * PITCH - GAP
    x0 = (WIDTH - LABEL_W - grid_w) / 2 + LABEL_W
    y0 = TITLE_BAR + PAD + 18
    cells, _ = grid(days, x0, y0, animate)

    y = y0 + 7 * PITCH + 14
    if s:
        caption = f"{s['total']:,} contributions in the last year"
    else:
        caption = "Waiting for the first daily refresh"
    legend_x = x0 + grid_w - 5 * PITCH - 34
    legend = (
        f'<text x="{legend_x - 6}" y="{y + 4}" font-size="10" fill="{MUTED}" text-anchor="end">Less</text>'
        + "".join(
            f'<rect x="{legend_x + i * PITCH}" y="{y - 6}" width="{CELL}" height="{CELL}" rx="2.5" fill="{c}"/>'
            for i, c in enumerate(LEVELS)
        )
        + f'<text x="{legend_x + 5 * PITCH + 4}" y="{y + 4}" font-size="10" fill="{MUTED}">More</text>'
    )
    footer = f'<text x="{x0}" y="{y + 4}" font-size="12" fill="{TEXT}">{esc(caption)}</text>' + legend

    ty = y + 22
    gap = 12
    tw = (grid_w + LABEL_W - 3 * gap) / 4
    tx = x0 - LABEL_W
    if s:
        cur, lon, best = s["current_streak"], s["longest_streak"], s["best_day"]
        tiles = [
            ("contributions", f"{s['total']:,}", "", f"{s['active_days']} active days"),
            ("current streak", str(cur["days"]), plural(cur["days"]), f"{short(cur['from'])} to {short(cur['to'])}" if cur["days"] else "starts today"),
            ("longest streak", str(lon["days"]), plural(lon["days"]), f"{short(lon['from'])} to {short(lon['to'])}" if lon["days"] else ""),
            ("best day", str(best["count"]), "", short(best["date"])),
        ]
    else:
        tiles = [(name, "--", "", "") for name in ("contributions", "current streak", "longest streak", "best day")]
    tiles_markup = "".join(
        tile(tx + i * (tw + gap), ty, tw, *t, delay=0.9 + i * 0.12, animate=animate) for i, t in enumerate(tiles)
    )

    height = int(ty + 66 + PAD)
    stamp = ""
    if data:
        stamp = (
            f'<text x="{WIDTH - 16}" y="{TITLE_BAR / 2 + 4}" font-size="10" fill="{MUTED}" '
            f'text-anchor="end">updated {esc(data["generated_at"][:10])}</text>'
        )
    style = ""
    if animate:
        style = (
            "@keyframes drop{from{opacity:0;transform:translateY(-6px)}to{opacity:1;transform:none}}"
            ".c{animation:drop .35s ease-out both}"
            "@keyframes up{from{opacity:0;transform:translateY(6px)}to{opacity:1;transform:none}}"
            ".t{animation:up .4s ease-out both}"
        )
    user = data["user"] if data else "www8351"
    title = f"refael@github: ~ $ ./contributions.sh {user}"
    return window(WIDTH, height, title, stamp + cells + footer + tiles_markup, style)


def main() -> None:
    data = json.loads(DATA.read_text(encoding="utf-8")) if DATA.exists() else None
    animate = os.environ.get("STATIC") != "1"
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(render(data, animate), encoding="utf-8")
    print(f"wrote {OUT}" + ("" if data else " (blank, no data yet)"))


if __name__ == "__main__":
    main()
