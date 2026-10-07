#!/usr/bin/env python3
"""Regenerate printable PDFs with embedded brand fonts.

Entry pages are not rendered here — the reader's browser prints them from the page stylesheet.
"""
import json
import subprocess
import sys
from pathlib import Path

from guide_inventory import SHEETS
from render_pdf import effective_zoom, print_scales, source_digest

ROOT = Path(__file__).resolve().parents[2]
RENDER = ROOT / ".github" / "scripts" / "render_pdf.py"
OUT = ROOT / "products" / "guides-pdf"


def main() -> int:
    scales = print_scales()

    failed = []
    for src, stem in SHEETS:
        s = ROOT / src
        if not s.exists():
            failed.append(f"{src}: missing")
            continue
        r = subprocess.run([sys.executable, str(RENDER), str(s),
                            str(OUT / f"{stem}.pdf"), str(effective_zoom(stem, scales))],
                           capture_output=True, text=True)
        if r.returncode:
            failed.append(f"{stem}: {r.stderr.strip() or r.stdout.strip()}")
        else:
            print(r.stdout.strip())
    # Record what each PDF was rendered from, so check_pdfs_fresh.py can tell
    # when a source has moved on without the printable being regenerated.
    manifest = {stem: source_digest(ROOT / src, effective_zoom(stem, scales))
                for src, stem in SHEETS if (ROOT / src).exists()}
    (OUT / ".sources.json").write_text(json.dumps(manifest, indent=2, sort_keys=True) + "\n")

    if failed:
        print("\nFAILED:", file=sys.stderr)
        for f in failed:
            print(f"  {f}", file=sys.stderr)
        return 1
    print(f"\n{len(SHEETS)} printables rendered.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
