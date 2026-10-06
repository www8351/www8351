"""Render assets/whoami.svg: the ASCII portrait beside a neofetch-style card.

Standard library only. Reads data/portrait.txt (made by make_ascii.py).
Portrait rows wipe in left to right, card lines slide in, then everything
holds still. Set STATIC=1 to emit the final frame without animation.

    python scripts/render_whoami_svg.py
"""

from __future__ import annotations

import os
from pathlib import Path

from svgterm import BORDER, CYAN, GREEN, MUTED, TEXT, TITLE_BAR, esc, window

ROOT = Path(__file__).resolve().parent.parent
PORTRAIT = ROOT / "data" / "portrait.txt"
OUT = ROOT / "assets" / "whoami.svg"

USER = "refael@github"

CARD: list[tuple[str, str]] = [
    ("Name", "Refael Malka"),
    ("Role", "Systems Engineer"),
    ("Focus", "Trading · SaaS · DevOps"),
    ("Now", "Account Guardian, MT5 risk lock"),
    ("Lang", "Python · TypeScript · Bash · MQL5"),
    ("Web", "React 19 · Next.js 16 · Express 5"),
    ("Infra", "Docker · OpenTofu · Jenkins · Actions"),
    ("Quality", "mypy strict · pytest · coverage gates"),
    ("Rule", "Real-money paths off by default"),
    ("Shell", "PowerShell · hardened Linux"),
    ("Location", "Israel"),
]

PALETTE = ["#484f58", "#f85149", "#3fb950", "#d29922", "#58a6ff", "#bc8cff", "#39c5cf", "#e6edf3"]

WIDTH = 900
PAD = 22
ART_W = 380
ROW_STAGGER = 0.04
ROW_DUR = 0.35
CARD_X = PAD + ART_W + 34
KEY_W = 92
CARD_LINE_H = 25
NBSP = "\u00a0"
ART = "#e6edf3"


def portrait(lines: list[str], animate: bool) -> tuple[str, str]:
    cell_w = ART_W / max(len(line) for line in lines)
    line_h = cell_w * 2
    defs, rows = [], []
    top = TITLE_BAR + PAD
    for i, line in enumerate(lines):
        if not line.strip():
            continue
        y = top + (i + 1) * line_h - line_h * 0.2
        w = len(line) * cell_w
        text = esc(line.replace(" ", NBSP))
        clip = ""
        if animate:
            delay = i * ROW_STAGGER
            total = delay + ROW_DUR
            defs.append(
                f'<clipPath id="r{i}"><rect x="{PAD}" y="{y - line_h:.2f}" height="{line_h * 1.3:.2f}" width="0">'
                f'<animate attributeName="width" values="0;0;{w + 2}" '
                f'keyTimes="0;{delay / total:.4f};1" dur="{total:.2f}s" fill="freeze"/>'
                f"</rect></clipPath>"
            )
            clip = f' clip-path="url(#r{i})"'
        rows.append(
            f'<text x="{PAD}" y="{y:.2f}" textLength="{w:.2f}" lengthAdjust="spacingAndGlyphs"'
            f'{clip} xml:space="preserve">{text}</text>'
        )
    body = f'<g font-size="{line_h * 0.95:.2f}" font-weight="700" fill="{ART}">' + "".join(rows) + "</g>"
    return "".join(defs), body


def card(animate: bool) -> tuple[str, int]:
    out = []
    y = TITLE_BAR + PAD + 20
    step = 0

    def line(markup: str) -> None:
        nonlocal step
        cls = f' class="ln" style="animation-delay:{0.3 + step * 0.1:.2f}s"' if animate else ""
        out.append(f"<g{cls}>{markup}</g>")
        step += 1

    line(f'<text x="{CARD_X}" y="{y}" font-size="17" font-weight="700" fill="{GREEN}">{USER}</text>')
    y += 14
    line(f'<text x="{CARD_X}" y="{y}" font-size="14" fill="{MUTED}">{"-" * len(USER)}</text>')
    y += CARD_LINE_H
    for key, value in CARD:
        line(
            f'<text x="{CARD_X}" y="{y}" font-size="14.5" font-weight="700" fill="{CYAN}">{esc(key)}</text>'
            f'<text x="{CARD_X + KEY_W}" y="{y}" font-size="14.5" fill="{TEXT}">{esc(value)}</text>'
        )
        y += CARD_LINE_H
    y += 4
    blocks = "".join(
        f'<rect x="{CARD_X + i * 30}" y="{y - 14}" width="26" height="16" rx="2" fill="{c}"/>'
        for i, c in enumerate(PALETTE)
    )
    line(blocks)
    y += 34
    cursor_cls = ' class="cur"' if animate else ""
    line(
        f'<text x="{CARD_X}" y="{y}" font-size="14.5" fill="{GREEN}">{USER} <tspan fill="{CYAN}">~</tspan>'
        f' <tspan fill="{TEXT}">$ </tspan><tspan{cursor_cls} fill="{TEXT}">\u2588</tspan></text>'
    )
    return "".join(out), y


def render(lines: list[str], animate: bool = True) -> str:
    defs, art = portrait(lines, animate)
    card_markup, card_bottom = card(animate)
    art_bottom = TITLE_BAR + PAD + len(lines) * ART_W / max(len(line) for line in lines) * 2
    height = int(max(art_bottom, card_bottom) + PAD + 6)
    divider = (
        f'<path d="M{PAD + ART_W + 16} {TITLE_BAR + PAD} V{height - PAD}" '
        f'stroke="{BORDER}" stroke-dasharray="2 4"/>'
    )
    style = ""
    if animate:
        style = (
            "@keyframes in{from{opacity:0;transform:translateX(-8px)}to{opacity:1;transform:none}}"
            ".ln{animation:in .45s ease-out both}"
            "@keyframes blink{50%{opacity:0}}"
            ".cur{animation:blink 1.1s step-end 2.2s infinite}"
        )
    body = f"<defs>{defs}</defs>{art}{divider}{card_markup}"
    return window(WIDTH, height, f"{USER}: ~ $ whoami", body, style)


def main() -> None:
    lines = PORTRAIT.read_text(encoding="utf-8").splitlines()
    animate = os.environ.get("STATIC") != "1"
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(render(lines, animate), encoding="utf-8")
    print(f"wrote {OUT}")


if __name__ == "__main__":
    main()
