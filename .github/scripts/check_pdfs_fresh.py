#!/usr/bin/env python3
"""Fail if a committed printable is older than the HTML it came from.

The email sequences link straight at these PDFs, so a stale one means a reader
is handed corrected copy on the site and the uncorrected version in their inbox.
That has already happened once.

Rendered PDFs are not byte-stable — Chrome stamps a creation date and a document
ID into every run — so this compares a hash of each *source* instead: the HTML,
its local stylesheets, the embedded-fonts CSS and the print zoom (see
render_pdf.source_digest). The manifest is written by render_all_pdfs.py; if any
of those has changed since, the hashes diverge and the PDF needs re-rendering.
"""
import json
import sys
from pathlib import Path

from guide_inventory import SHEETS
from render_pdf import effective_zoom, print_scales, source_digest

ROOT = Path(__file__).resolve().parents[2]
MANIFEST = ROOT / "products" / "guides-pdf" / ".sources.json"


def current() -> dict:
    scales = print_scales()
    return {stem: source_digest(ROOT / src, effective_zoom(stem, scales))
            for src, stem in SHEETS}


def main() -> int:
    if not MANIFEST.exists():
        print("no .sources.json — run render_all_pdfs.py once to create it",
              file=sys.stderr)
        return 1

    recorded = json.loads(MANIFEST.read_text())
    now = current()
    stale = sorted(k for k in now if recorded.get(k) != now[k])
    missing = sorted(k for k in now
                     if not (ROOT / "products" / "guides-pdf" / f"{k}.pdf").exists())

    if stale or missing:
        print("Printables are out of date:\n", file=sys.stderr)
        for k in stale:
            print(f"  {k} — source, print scale or fonts changed since the PDF was rendered",
                  file=sys.stderr)
        for k in missing:
            print(f"  {k} — PDF missing", file=sys.stderr)
        print("\nRun:  python3 .github/scripts/render_all_pdfs.py", file=sys.stderr)
        print("then commit the regenerated PDFs.", file=sys.stderr)
        return 1

    print(f"{len(now)} printables are current.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

