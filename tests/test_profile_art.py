"""Tests for the profile art scripts. Standard library only:

    python -m unittest discover -s tests
"""

from __future__ import annotations

import sys
import tempfile
import unittest
import xml.etree.ElementTree as ET
from datetime import date, timedelta
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "scripts"))

import fetch_contributions as fc  # noqa: E402
import render_heatmap_svg as rh  # noqa: E402
import render_whoami_svg as rw  # noqa: E402


def calendar_html(counts: list[int], start: date, total_line: str | None = "1,096") -> str:
    """Mimic the markup of github.com/users/<user>/contributions."""
    cells, tips = [], []
    for i, n in enumerate(counts):
        day = start + timedelta(days=i)
        cid = f"contribution-day-component-{(day.weekday() + 1) % 7}-{i // 7}"
        level = 0 if n == 0 else min(4, 1 + n // 10)
        cells.append(
            f'<td tabindex="0" data-ix="{i // 7}" aria-selected="false" style="width: 10px" '
            f'data-date="{day.isoformat()}" id="{cid}" data-level="{level}" role="gridcell" '
            f'data-view-component="true" class="ContributionCalendar-day"></td>'
        )
        text = "No contributions" if n == 0 else f"{n:,} contribution{'s' if n != 1 else ''}"
        tips.append(
            f'<tool-tip id="tooltip-{i}" for="{cid}" popover="manual" data-direction="n" '
            f'data-type="label" data-view-component="true" class="sr-only position-absolute">'
            f"{text} on {day:%B} {day.day}th.</tool-tip>"
        )
    total = ""
    if total_line is not None:
        total = (
            '<h2 id="js-contribution-activity-description" class="f4 text-normal mb-2">\n'
            f"      {total_line}\n      contributions\n        in the last year\n</h2>"
        )
    return f"<div>{total}<table><tbody><tr>{''.join(cells)}</tr></tbody></table>{''.join(tips)}</div>"


START = date(2025, 10, 5)


class ParseTests(unittest.TestCase):
    def test_reads_counts_levels_and_total(self) -> None:
        counts = [0] * 371
        counts[10], counts[11], counts[200] = 3, 1, 1234
        days, total = fc.parse(calendar_html(counts, START))
        self.assertEqual(len(days), 371)
        self.assertEqual(total, 1096)
        self.assertEqual(days[0]["date"], "2025-10-05")
        self.assertEqual([d["count"] for d in days], counts)
        self.assertEqual(days[200]["level"], 4)

    def test_total_missing_falls_back_to_none(self) -> None:
        _, total = fc.parse(calendar_html([1, 0, 2], START, total_line=None))
        self.assertIsNone(total)

    def test_cell_without_tooltip_is_an_error(self) -> None:
        html = calendar_html([1, 2], START).replace('for="contribution-day-component-1-0"', 'for="x"')
        with self.assertRaises(ValueError):
            fc.parse(html)


class StatsTests(unittest.TestCase):
    def days(self, counts: list[int]) -> list[dict]:
        return [
            {"date": (START + timedelta(days=i)).isoformat(), "count": n, "level": 1 if n else 0}
            for i, n in enumerate(counts)
        ]

    def test_streaks_and_best_day(self) -> None:
        s = fc.stats(self.days([1, 1, 1, 0, 5, 2, 0, 1, 1]), None)
        self.assertEqual(s["total"], 12)
        self.assertEqual(s["active_days"], 7)
        self.assertEqual(s["longest_streak"]["days"], 3)
        self.assertEqual(s["current_streak"]["days"], 2)
        self.assertEqual(s["best_day"], {"date": "2025-10-09", "count": 5})

    def test_zero_today_keeps_yesterdays_streak(self) -> None:
        s = fc.stats(self.days([0, 1, 1, 0]), 2)
        self.assertEqual(s["current_streak"]["days"], 2)
        self.assertEqual(s["total"], 2)

    def test_two_idle_days_end_the_streak(self) -> None:
        s = fc.stats(self.days([1, 1, 0, 0]), None)
        self.assertEqual(s["current_streak"]["days"], 0)

    def test_empty_year(self) -> None:
        s = fc.stats(self.days([0] * 10), None)
        self.assertEqual(s["longest_streak"]["days"], 0)
        self.assertEqual(s["best_day"]["count"], 0)


class MainTests(unittest.TestCase):
    def test_short_page_fails_instead_of_writing(self) -> None:
        with tempfile.TemporaryDirectory() as tmp:
            page = Path(tmp) / "page.html"
            page.write_text(calendar_html([1] * 20, START), encoding="utf-8")
            out = Path(tmp) / "out.json"
            old_out, old_argv = fc.OUT, sys.argv
            fc.OUT, sys.argv = out, ["fetch", "--html", str(page), "--user", "x"]
            try:
                self.assertEqual(fc.main(), 1)
            finally:
                fc.OUT, sys.argv = old_out, old_argv
            self.assertFalse(out.exists())


class RenderTests(unittest.TestCase):
    def assert_svg(self, markup: str) -> ET.Element:
        root = ET.fromstring(markup)
        self.assertTrue(root.tag.endswith("svg"))
        self.assertNotIn("<script", markup)
        self.assertNotIn("http", markup.replace("http://www.w3.org/2000/svg", ""))
        return root

    def test_heatmap_with_data(self) -> None:
        counts = [i % 7 for i in range(371)]
        days, total = fc.parse(calendar_html(counts, START))
        data = {"user": "www8351", "generated_at": "2026-10-06T00:00:00Z", "stats": fc.stats(days, total), "days": days}
        for animate in (True, False):
            root = self.assert_svg(rh.render(data, animate))
            rects = [e for e in root.iter() if e.tag.endswith("rect") and e.find("{http://www.w3.org/2000/svg}title") is not None]
            self.assertEqual(len(rects), 371)

    def test_heatmap_placeholder_spans_53_weeks(self) -> None:
        days = fc.placeholder_days(date(2026, 10, 6))
        self.assertEqual(date.fromisoformat(days[0]["date"]).weekday(), 6)  # a Sunday
        self.assertEqual(days[-1]["date"], "2026-10-06")
        _, weeks = rh.grid(days, 0, 0, False)
        self.assertEqual(weeks, 53)
        self.assert_svg(rh.render(None))

    def test_heatmap_fits_a_54_week_calendar(self) -> None:
        # Sunday start, Saturday end: 378 days span 54 week columns.
        days = [
            {"date": (date(2025, 10, 5) + timedelta(days=i)).isoformat(), "count": 1, "level": 1}
            for i in range(378)
        ]
        self.assertEqual(rh.week_count(days), 54)
        data = {"user": "x", "generated_at": "2026-10-06T00:00:00Z", "stats": fc.stats(days, None), "days": days}
        root = self.assert_svg(rh.render(data, False))
        cells = [e for e in root.iter() if e.tag.endswith("rect") and e.find("{http://www.w3.org/2000/svg}title") is not None]
        self.assertEqual(len(cells), 378)
        left = min(float(e.get("x")) for e in cells)
        right = max(float(e.get("x")) + rh.CELL for e in cells)
        self.assertGreaterEqual(left, rh.PAD)
        self.assertLessEqual(right, rh.WIDTH - rh.PAD)

    def test_whoami(self) -> None:
        lines = ["  .:-=+*#%@", "", " <&> \"q\""]
        for animate in (True, False):
            root = self.assert_svg(rw.render(lines, animate))
            texts = "".join(e.text or "" for e in root.iter() if e.tag.endswith("text"))
            self.assertIn("<&>", texts)


if __name__ == "__main__":
    unittest.main()
