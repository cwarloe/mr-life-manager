#!/usr/bin/env python3
"""Find the largest print scale each printable can take without gaining a page.

Print sizes were hand-tuned downward until everything fit, which guaranteed the
page count and left a lot of blank paper. This searches upward instead: the
biggest type that still fits the page budget it already has.

Writes products/guides-pdf/.print-scale.json, consumed by render_all_pdfs.py.
Run it after a layout change; it takes a couple of minutes.
"""
import json
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
RENDER = ROOT / ".github" / "scripts" / "render_pdf.py"
OUT = ROOT / "products" / "guides-pdf"
# Leave a little headroom: a sheet tuned to the exact limit flips to two pages
# on any future wording change.
SAFETY = 0.97


def pages(src: Path, zoom: float, tmp: Path) -> int:
    subprocess.run([sys.executable, str(RENDER), str(src), str(tmp), str(zoom)],
                   check=True, capture_output=True)
    d = tmp.read_bytes()
    return d.count(b"/Type /Page") - d.count(b"/Type /Pages")


def main() -> int:
    sys.path.insert(0, str(ROOT / ".github" / "scripts"))
    from render_all_pdfs import SHEETS

    scales = {}
    with tempfile.TemporaryDirectory() as td:
        tmp = Path(td) / "probe.pdf"
        for src, stem in SHEETS:
            s = ROOT / src
            if not s.exists():
                continue
            budget = pages(s, 1.0, tmp)
            lo, hi = 1.0, 2.2
            # widen only as far as it still fits
            while hi - lo > 0.02:
                mid = (lo + hi) / 2
                if pages(s, mid, tmp) <= budget:
                    lo = mid
                else:
                    hi = mid
            scale = round(lo * SAFETY, 2)
            scales[stem] = scale
            gain = int((scale - 1) * 100)
            print(f"  {stem:<32} {budget}pp  scale {scale:.2f}"
                  f"  ({gain:+d}% type)")

    (OUT / ".print-scale.json").write_text(
        json.dumps(scales, indent=2, sort_keys=True) + "\n")
    print(f"\nwrote {OUT.name}/.print-scale.json")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
