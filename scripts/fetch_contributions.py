"""Fetch the public contribution calendar and write data/contributions.json.

Standard library only, no token. GitHub serves the calendar as public HTML
at https://github.com/users/<user>/contributions, the same fragment the
profile page loads.

    python scripts/fetch_contributions.py [--user www8351]

Exits non-zero when the page cannot be parsed, so a format change on
GitHub's side fails the workflow instead of committing an empty graph.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import urllib.request
from datetime import date, datetime, timedelta, timezone
from html.parser import HTMLParser
from pathlib import Path

OUT = Path(__file__).resolve().parent.parent / "data" / "contributions.json"
URL = "https://github.com/users/{user}/contributions"
MIN_DAYS = 300

COUNT_RE = re.compile(r"^\s*(\d[\d,]*)\s+contributions?\b", re.I)
TOTAL_RE = re.compile(r"([\d,]+)\s+contributions?\s+in the last year", re.I)


class CalendarParser(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.cells: dict[str, tuple[str, int]] = {}
        self.tips: dict[str, str] = {}
        self._tip_for: str | None = None
        self._tip_text: list[str] = []
        self._in_total = False
        self._total_text: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        a = {k: v or "" for k, v in attrs}
        if tag == "td" and "data-date" in a and "ContributionCalendar-day" in a.get("class", ""):
            self.cells[a.get("id", a["data-date"])] = (a["data-date"], int(a.get("data-level") or 0))
        elif tag == "tool-tip" and a.get("for"):
            self._tip_for = a["for"]
            self._tip_text = []
        elif tag == "h2" and a.get("id") == "js-contribution-activity-description":
            self._in_total = True

    def handle_endtag(self, tag: str) -> None:
        if tag == "tool-tip" and self._tip_for:
            self.tips[self._tip_for] = "".join(self._tip_text).strip()
            self._tip_for = None
        elif tag == "h2":
            self._in_total = False

    def handle_data(self, data: str) -> None:
        if self._tip_for:
            self._tip_text.append(data)
        if self._in_total:
            self._total_text.append(data)

    @property
    def total_text(self) -> str:
        return " ".join("".join(self._total_text).split())


def parse(html: str) -> tuple[list[dict], int | None]:
    p = CalendarParser()
    p.feed(html)
    days = []
    for cell_id, (day, level) in p.cells.items():
        tip = p.tips.get(cell_id)
        if tip is None:
            raise ValueError(f"no tooltip for {cell_id} ({day})")
        m = COUNT_RE.match(tip)
        count = int(m.group(1).replace(",", "")) if m else 0
        days.append({"date": day, "count": count, "level": level})
    days.sort(key=lambda d: d["date"])
    m = TOTAL_RE.search(p.total_text)
    total = int(m.group(1).replace(",", "")) if m else None
    return days, total


def _runs(days: list[dict]) -> list[tuple[int, int]]:
    """(start index, length) of every run of consecutive active days."""
    runs, start = [], None
    for i, d in enumerate(days):
        if d["count"] > 0 and start is None:
            start = i
        elif d["count"] == 0 and start is not None:
            runs.append((start, i - start))
            start = None
    if start is not None:
        runs.append((start, len(days) - start))
    return runs


def stats(days: list[dict], total: int | None) -> dict:
    runs = _runs(days)
    longest = max(runs, key=lambda r: r[1], default=(0, 0))
    # A zero today does not break the streak yet; the day is not over.
    end = len(days) - 1
    if days and days[end]["count"] == 0:
        end -= 1
    current = next((r for r in runs if r[0] + r[1] - 1 == end), None)
    best = max(days, key=lambda d: d["count"], default={"date": "", "count": 0})

    def span(run: tuple[int, int] | None) -> dict:
        if not run or run[1] == 0:
            return {"days": 0, "from": None, "to": None}
        return {"days": run[1], "from": days[run[0]]["date"], "to": days[run[0] + run[1] - 1]["date"]}

    return {
        "total": total if total is not None else sum(d["count"] for d in days),
        "active_days": sum(1 for d in days if d["count"] > 0),
        "current_streak": span(current),
        "longest_streak": span(longest),
        "best_day": {"date": best["date"], "count": best["count"]},
    }


def fetch(user: str) -> str:
    req = urllib.request.Request(URL.format(user=user), headers={"User-Agent": "profile-art-refresh"})
    with urllib.request.urlopen(req, timeout=30) as resp:
        return resp.read().decode("utf-8")


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("--user", default=os.environ.get("GITHUB_REPOSITORY_OWNER", "www8351"))
    ap.add_argument("--html", type=Path, help="parse a saved page instead of fetching")
    args = ap.parse_args()

    html = args.html.read_text(encoding="utf-8") if args.html else fetch(args.user)
    days, total = parse(html)
    if len(days) < MIN_DAYS:
        print(f"parsed only {len(days)} days, expected a full year; page format changed?", file=sys.stderr)
        return 1

    data = {
        "user": args.user,
        "generated_at": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "stats": stats(days, total),
        "days": days,
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(data, indent=1) + "\n", encoding="utf-8")
    s = data["stats"]
    print(f"wrote {OUT}: {len(days)} days, {s['total']} contributions")
    return 0


def placeholder_days(today: date | None = None) -> list[dict]:
    """A blank year, used before the first real fetch."""
    today = today or date.today()
    start = today - timedelta(days=364 + (today.weekday() + 1) % 7)
    return [
        {"date": (start + timedelta(days=i)).isoformat(), "count": 0, "level": 0}
        for i in range((today - start).days + 1)
    ]


if __name__ == "__main__":
    sys.exit(main())
