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

## Data Source & Credit

All paper metadata (titles, authors, abstracts, upvotes, etc.) is sourced from
[Hugging Face Daily Papers](https://huggingface.co/papers), which aggregates
submissions from the research community. The original paper content is hosted on
[arXiv](https://arxiv.org/) and is subject to each paper's own license
(typically CC BY or similar open-access terms).

This repository is an **unofficial archive** and is not affiliated with or
endorsed by Hugging Face or arXiv.

## License

The archiving scripts in this repository are released under the
[MIT License](LICENSE). The archived paper metadata originates from publicly
accessible sources (Hugging Face and arXiv) and is redistributed here for
research and educational purposes with full attribution. All rights to the
original paper content remain with their respective authors and publishers.
If you are an author and wish to have your metadata removed, please
[open an issue](https://github.com/joe0731/hf_paper_watch_dog/issues).
