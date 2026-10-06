"""Shared pieces for the terminal-styled profile SVGs.

Every SVG is self-contained: no external fonts, no scripts, no remote
images. GitHub renders SVGs through <img>, which runs SMIL and CSS
keyframe animations but blocks everything external.
"""

from __future__ import annotations

from xml.sax.saxutils import escape

MONO = (
    "ui-monospace, SFMono-Regular, 'SF Mono', Menlo, Consolas, "
    "'Liberation Mono', 'DejaVu Sans Mono', monospace"
)

BG = "#0d1117"
PANEL = "#161b22"
BORDER = "#30363d"
TEXT = "#c9d1d9"
MUTED = "#8b949e"
GREEN = "#3fb950"
CYAN = "#79c0ff"
YELLOW = "#d29922"
RED = "#f85149"

TITLE_BAR = 34


def esc(text: str) -> str:
    return escape(text, {'"': "&quot;"})


def window(width: int, height: int, title: str, body: str, style: str = "") -> str:
    """Wrap body markup in a terminal window with a title bar."""
    dots = "".join(
        f'<circle cx="{20 + i * 18}" cy="{TITLE_BAR / 2}" r="5.5" fill="{c}"/>'
        for i, c in enumerate((RED, YELLOW, GREEN))
    )
    return (
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="{height}" '
        f'viewBox="0 0 {width} {height}" role="img" aria-label="{esc(title)}">\n'
        f"<style>text{{font-family:{MONO};}}{style}</style>\n"
        f'<rect x="0.5" y="0.5" width="{width - 1}" height="{height - 1}" rx="12" '
        f'fill="{BG}" stroke="{BORDER}"/>\n'
        f'<path d="M0.5 {TITLE_BAR} H{width - 0.5}" stroke="{BORDER}"/>\n'
        f"{dots}\n"
        f'<text x="{width / 2}" y="{TITLE_BAR / 2 + 4}" font-size="12" fill="{MUTED}" '
        f'text-anchor="middle">{esc(title)}</text>\n'
        f"{body}\n</svg>\n"
    )
