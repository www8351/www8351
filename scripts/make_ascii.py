"""Convert a portrait photo into a monochrome ASCII grid.

Runs locally, only when the photo changes. Needs Pillow:

    pip install pillow
    python scripts/make_ascii.py photo.jpg

Writes data/portrait.txt, which render_whoami_svg.py turns into the SVG.
The art is drawn light on dark, so bright pixels get dense glyphs and the
dark background maps to spaces. Works best on a photo with a dark,
plain background.
"""

from __future__ import annotations

import argparse
from pathlib import Path

from PIL import Image, ImageFilter, ImageOps

# dark (blank) -> bright (dense)
RAMP = " .`:-=+*cs#%@"

# A monospace cell is roughly twice as tall as it is wide.
CELL_ASPECT = 2.0

OUT = Path(__file__).resolve().parent.parent / "data" / "portrait.txt"


def to_ascii(img: Image.Image, cols: int, gamma: float, floor: int, bg: int = 25) -> list[str]:
    gray = ImageOps.grayscale(img)
    side = min(gray.size)
    left = (gray.width - side) // 2
    top = (gray.height - side) // 2
    gray = gray.crop((left, top, left + side, top + side))

    # Equalize the subject only. A dark face on a black background has
    # its tones bunched together; spreading them is what makes the
    # features readable. The background is pinned to black.
    subject = gray.point(lambda v: 255 if v > bg else 0)
    gray = ImageOps.equalize(gray, mask=subject)
    gray.paste(0, mask=ImageOps.invert(subject))
    gray = gray.filter(ImageFilter.UnsharpMask(radius=2, percent=120, threshold=2))

    rows = round(cols / CELL_ASPECT)
    small = gray.resize((cols, rows), Image.LANCZOS)

    last = len(RAMP) - 1
    lines = []
    for y in range(rows):
        chars = []
        for x in range(cols):
            v = small.getpixel((x, y))
            if v < floor:
                chars.append(" ")
                continue
            t = ((v - floor) / (255 - floor)) ** gamma
            chars.append(RAMP[min(last, max(1, round(t * last)))])
        lines.append("".join(chars).rstrip())
    return lines


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("photo", type=Path)
    ap.add_argument("--cols", type=int, default=110)
    ap.add_argument("--gamma", type=float, default=1.0, help="below 1 lifts mid tones")
    ap.add_argument("--floor", type=int, default=30, help="pixels darker than this become spaces")
    args = ap.parse_args()

    with Image.open(args.photo) as img:
        lines = to_ascii(img, args.cols, args.gamma, args.floor)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text("\n".join(lines) + "\n", encoding="utf-8")
    print(f"wrote {OUT} ({args.cols}x{len(lines)})")


if __name__ == "__main__":
    main()
