# HuggingFace Daily Papers Archive

Automatically fetch and archive [Hugging Face Daily Papers](https://huggingface.co/papers) via GitHub Actions.

## Structure

```
papers/
└── 2026/
    └── 03/
        ├── 2026-03-17.md    # human-readable markdown
        └── 2026-03-17.json  # structured data
```

Each daily file contains:

- **ArXiv ID** with links to both ArXiv and HuggingFace
- **Title**
- **Authors**
- **Organization**
- **Published / Submitted dates**
- **Upvotes**
- **Abstract**
- **Links** (GitHub repo, project page if available)

Papers are sorted by upvotes (descending).

## Automation

A GitHub Actions workflow runs daily at **08:00 UTC**, fetches the day's papers, and commits them to this repo.

### Manual trigger

You can also trigger the workflow manually via GitHub Actions UI with:

- **date**: a specific date in `YYYY-MM-DD` format
- **backfill**: number of days to backfill

### Local usage

```bash
# fetch today's papers
python scripts/fetch_papers.py

# fetch papers for a specific date
python scripts/fetch_papers.py 2026-03-17

# backfill the last 7 days
python scripts/fetch_papers.py --backfill 7

# backfill 7 days starting from a specific date
python scripts/fetch_papers.py 2026-03-15 --backfill 7
```

No external dependencies required — uses only Python standard library.

## License

MIT
