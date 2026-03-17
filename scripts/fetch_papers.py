#!/usr/bin/env python3
"""
fetch daily papers from huggingface and archive them as markdown + json.

usage:
    python fetch_papers.py                    # fetch today's papers
    python fetch_papers.py 2026-03-17         # fetch papers for a specific date
    python fetch_papers.py --backfill 7       # backfill last 7 days
"""

import argparse
import json
import logging
import os
import sys
import time
from datetime import datetime, timedelta, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
)
logger = logging.getLogger(__name__)

HF_API_BASE = "https://huggingface.co/api/daily_papers"
ARXIV_ABS_BASE = "https://arxiv.org/abs"
HF_PAPER_BASE = "https://huggingface.co/papers"

MAX_RETRIES = 3
RETRY_DELAY_SECONDS = 5
MAX_BACKFILL_DAYS = 365


def fetch_json(url: str) -> list | dict | None:
    """fetch json from a url with retries."""
    for attempt in range(1, MAX_RETRIES + 1):
        try:
            req = Request(url, headers={"User-Agent": "hf-paper-rss-bot/1.0"})
            with urlopen(req, timeout=30) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except (HTTPError, URLError, TimeoutError) as e:
            logger.warning("attempt %d/%d failed for %s: %s", attempt, MAX_RETRIES, url, e)
            if attempt < MAX_RETRIES:
                time.sleep(RETRY_DELAY_SECONDS)
    logger.error("all retries exhausted for %s", url)
    return None


def parse_authors(authors_raw: list[dict]) -> list[str]:
    """extract author names from api response."""
    names = []
    for a in authors_raw:
        if a.get("hidden"):
            continue
        name = a.get("name", "").strip()
        if name:
            names.append(name)
    return names


def format_date(iso_str: str | None) -> str:
    """convert iso datetime string to YYYY-MM-DD."""
    if not iso_str:
        return "N/A"
    try:
        dt = datetime.fromisoformat(iso_str.replace("Z", "+00:00"))
        return dt.strftime("%Y-%m-%d")
    except (ValueError, AttributeError):
        return iso_str


def build_paper_record(item: dict) -> dict:
    """build a normalized paper record from an api item."""
    paper = item.get("paper", {})
    arxiv_id = paper.get("id", "")
    authors = parse_authors(paper.get("authors", []))

    org = item.get("organization") or paper.get("organization")
    org_name = ""
    org_fullname = ""
    if org:
        org_name = org.get("name", "")
        org_fullname = org.get("fullname", "")

    submitted_by = item.get("submittedBy", {})
    submitter_name = submitted_by.get("fullname", "") or submitted_by.get("name", "")

    return {
        "arxiv_id": arxiv_id,
        "title": paper.get("title", ""),
        "authors": authors,
        "abstract": paper.get("summary", "") or item.get("summary", ""),
        "published_at": format_date(paper.get("publishedAt")),
        "submitted_at": format_date(paper.get("submittedOnDailyAt")),
        "submitted_by": submitter_name,
        "upvotes": paper.get("upvotes", 0),
        "organization": org_fullname or org_name,
        "github_repo": paper.get("githubRepo", ""),
        "project_page": paper.get("projectPage", ""),
        "hf_url": f"{HF_PAPER_BASE}/{arxiv_id}" if arxiv_id else "",
        "arxiv_url": f"{ARXIV_ABS_BASE}/{arxiv_id}" if arxiv_id else "",
    }


def render_markdown(date_str: str, records: list[dict]) -> str:
    """render paper records as a markdown document."""
    lines = [
        f"# Daily Papers - {date_str}",
        "",
        f"> source: [Hugging Face Daily Papers](https://huggingface.co/papers/date/{date_str})",
        "",
        f"Total papers: {len(records)}",
        "",
        "---",
        "",
    ]

    for i, r in enumerate(records, 1):
        lines.append(f"## {i}. [{r['title']}]({r['hf_url']})")
        lines.append("")
        lines.append(f"**ArXiv ID**: [{r['arxiv_id']}]({r['arxiv_url']})")
        lines.append("")

        if r["organization"]:
            lines.append(f"**Organization**: {r['organization']}")
            lines.append("")

        authors_str = ", ".join(r["authors"])
        lines.append(f"**Authors**: {authors_str}")
        lines.append("")

        lines.append(f"**Published**: {r['published_at']} | **Submitted**: {r['submitted_at']} by {r['submitted_by']}")
        lines.append("")

        lines.append(f"**Upvotes**: {r['upvotes']}")
        lines.append("")

        link_parts = []
        if r["github_repo"]:
            link_parts.append(f"[GitHub]({r['github_repo']})")
        if r["project_page"]:
            link_parts.append(f"[Project Page]({r['project_page']})")
        if link_parts:
            lines.append(f"**Links**: {' | '.join(link_parts)}")
            lines.append("")

        lines.append("### Abstract")
        lines.append("")
        lines.append(r["abstract"])
        lines.append("")
        lines.append("---")
        lines.append("")

    return "\n".join(lines)


def get_output_dir(base_dir: Path, date_str: str) -> Path:
    """get the output directory based on year/month structure."""
    parts = date_str.split("-")
    if len(parts) < 2:
        raise ValueError(f"invalid date format: {date_str}")
    year, month = parts[0], parts[1]
    return base_dir / year / month


def fetch_and_save(date_str: str, base_dir: Path) -> bool:
    """fetch papers for a given date and save to files."""
    url = f"{HF_API_BASE}?date={date_str}"
    logger.info("fetching papers for %s from %s", date_str, url)

    data = fetch_json(url)
    if data is None:
        logger.error("failed to fetch data for %s", date_str)
        return False

    if not isinstance(data, list):
        logger.error("unexpected response type: %s", type(data))
        return False

    if len(data) == 0:
        logger.warning("no papers found for %s, skipping", date_str)
        return True

    records = [build_paper_record(item) for item in data]
    records.sort(key=lambda r: r["upvotes"], reverse=True)

    out_dir = get_output_dir(base_dir, date_str)
    out_dir.mkdir(parents=True, exist_ok=True)

    md_path = out_dir / f"{date_str}.md"
    md_content = render_markdown(date_str, records)
    md_path.write_text(md_content, encoding="utf-8")
    logger.info("saved markdown: %s (%d papers)", md_path, len(records))

    json_path = out_dir / f"{date_str}.json"
    json_content = {
        "date": date_str,
        "total": len(records),
        "source": f"https://huggingface.co/papers/date/{date_str}",
        "papers": records,
    }
    json_path.write_text(
        json.dumps(json_content, indent=2, ensure_ascii=False),
        encoding="utf-8",
    )
    logger.info("saved json: %s", json_path)

    return True


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="fetch hf daily papers")
    parser.add_argument(
        "date",
        nargs="?",
        default=None,
        help="date in YYYY-MM-DD format (default: today)",
    )
    parser.add_argument(
        "--backfill",
        type=int,
        default=0,
        help="backfill N days starting from today (or from the given date)",
    )
    parser.add_argument(
        "--output-dir",
        type=str,
        default=None,
        help="base output directory (default: papers/ in repo root)",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    if args.output_dir:
        base_dir = Path(args.output_dir)
    else:
        repo_root = Path(__file__).resolve().parent.parent
        base_dir = repo_root / "papers"

    if args.date:
        try:
            start_date = datetime.strptime(args.date, "%Y-%m-%d")
        except ValueError:
            logger.error("invalid date format: %s (expected YYYY-MM-DD)", args.date)
            sys.exit(1)
    else:
        start_date = datetime.now(timezone.utc)

    dates = []
    if args.backfill > 0:
        if args.backfill > MAX_BACKFILL_DAYS:
            logger.error(
                "backfill %d exceeds maximum of %d days",
                args.backfill,
                MAX_BACKFILL_DAYS,
            )
            sys.exit(1)
        for i in range(args.backfill):
            d = start_date - timedelta(days=i)
            dates.append(d.strftime("%Y-%m-%d"))
    else:
        dates.append(start_date.strftime("%Y-%m-%d"))

    success_count = 0
    fail_count = 0
    for date_str in dates:
        ok = fetch_and_save(date_str, base_dir)
        if ok:
            success_count += 1
        else:
            fail_count += 1
        if len(dates) > 1:
            time.sleep(1)

    logger.info("done: %d succeeded, %d failed", success_count, fail_count)
    if fail_count > 0:
        sys.exit(1)


if __name__ == "__main__":
    main()
