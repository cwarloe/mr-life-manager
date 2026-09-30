#!/usr/bin/env python3
"""Regenerate printable PDFs with embedded brand fonts.

Entry pages are not rendered here — the reader's browser prints them from the page stylesheet.
"""
import json
import subprocess
import sys
from pathlib import Path

from guide_inventory import SHEETS

ROOT = Path(__file__).resolve().parents[2]
RENDER = ROOT / ".github" / "scripts" / "render_pdf.py"
OUT = ROOT / "products" / "guides-pdf"


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
    sys.path.insert(0, str(ROOT / ".github" / "scripts"))
    from check_pdfs_fresh import source_digest  # noqa: E402
    manifest = {stem: source_digest(ROOT / src)
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
