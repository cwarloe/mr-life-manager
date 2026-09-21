#!/usr/bin/env python3
"""Render an HTML file to PDF with the brand fonts embedded.

The pages link Google Fonts, which keeps them light on the web. That is the
wrong dependency for a printable: if the CDN is slow, blocked, or the build runs
somewhere without egress, Chrome silently falls back to DejaVu and Liberation and
nobody notices until the PDF is already in someone's inbox. That is exactly what
happened to the first set.

So for PDFs we swap the <link> for base64 @font-face rules generated from the
same families, and the render is then deterministic and offline.

Usage:  render_pdf.py <source.html> <out.pdf>
"""
import re
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
FONT_CSS = ROOT / "products" / "print" / "fonts" / "embedded-fonts.css"
CHROME = "/opt/pw-browsers/chromium-1194/chrome-linux/chrome"

GF_LINK = re.compile(
    r'<link[^>]+fonts\.(?:googleapis|gstatic)\.com[^>]*>\s*', re.I)


def render(src: Path, out: Path) -> None:
    html = src.read_text()
    if not FONT_CSS.exists():
        sys.exit(f"missing {FONT_CSS} — fonts cannot be embedded")

    style = "<style>\n" + FONT_CSS.read_text() + "\n</style>"
    html, n = GF_LINK.subn("", html)
    if "</head>" not in html:
        sys.exit(f"{src}: no </head>")
    html = html.replace("</head>", style + "\n</head>", 1)

    out.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        staged = Path(tmp) / src.name
        staged.write_text(html)
        subprocess.run(
            [CHROME, "--headless", "--disable-gpu", "--no-sandbox",
             "--no-pdf-header-footer", f"--print-to-pdf={out}", str(staged)],
            check=True, capture_output=True)
    # The first set of printables shipped in DejaVu and Liberation because the
    # font CDN was unreachable and Chrome fell back without complaining. Assert
    # the brand faces actually made it in, so that can never happen quietly again.
    blob = out.read_bytes()
    missing = [f for f in (b"Archivo", b"SourceSerif4") if f not in blob]
    if missing:
        sys.exit(f"{out.name}: brand fonts missing from output "
                 f"({', '.join(m.decode() for m in missing)}) — refusing to ship it")

    try:
        shown = out.relative_to(ROOT)
    except ValueError:
        shown = out
    print(f"{shown}  ({n} CDN link(s) replaced, "
          f"{out.stat().st_size // 1024}KB)")


def main() -> int:
    if len(sys.argv) != 3:
        sys.exit(__doc__)
    if not shutil.which(CHROME) and not Path(CHROME).exists():
        sys.exit(f"chrome not found at {CHROME}")
    render(Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
