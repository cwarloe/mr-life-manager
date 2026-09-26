#!/usr/bin/env python3
"""Regenerate printable PDFs with embedded brand fonts.

Entry pages are not rendered here — the reader's browser prints them from the page stylesheet.
"""
import hashlib
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RENDER = ROOT / ".github" / "scripts" / "render_pdf.py"
OUT = ROOT / "products" / "guides-pdf"

# (source html, output stem)
SHEETS = [
    ("products/print/the-week.html", "the-week"),
    ("products/checklists/first-apartment/first-apartment-checklist.html", "first-apartment-checklist"),
    ("products/checklists/how-often/how-often-should-i.html", "how-often-should-i"),
    ("products/checklists/cleaning-supplies/cleaning-supply-starter-list.html", "cleaning-supply-starter-list"),
    ("products/checklists/room-for/what-is-this-room-for.html", "what-is-this-room-for"),
    ("products/checklists/light/the-light-is-the-problem.html", "the-light-is-the-problem"),
    ("products/checklists/laundry/laundry-solved.html", "laundry-solved"),
    ("products/checklists/ten-meals/ten-meals.html", "ten-meals"),
    ("products/worksheets/household-agreement/household-agreement.html", "household-agreement"),
]


def main() -> int:
    # Scales from tune_print_scale.py; under 5% gain is noise — skip the zoom rule.
    scale_file = OUT / ".print-scale.json"
    scales = json.loads(scale_file.read_text()) if scale_file.exists() else {}

    failed = []
    for src, stem in SHEETS:
        s = ROOT / src
        if not s.exists():
            failed.append(f"{src}: missing")
            continue
        zoom = scales.get(stem, 1.0)
        if zoom < 1.05:
            zoom = 1.0
        r = subprocess.run([sys.executable, str(RENDER), str(s),
                            str(OUT / f"{stem}.pdf"), str(zoom)],
                           capture_output=True, text=True)
        if r.returncode:
            failed.append(f"{stem}: {r.stderr.strip() or r.stdout.strip()}")
        else:
            print(r.stdout.strip())
    # Record what each PDF was rendered from, so check_pdfs_fresh.py can tell
    # when a source has moved on without the printable being regenerated.
    manifest = {stem: hashlib.sha256((ROOT / src).read_bytes()).hexdigest()[:16]
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
