#!/usr/bin/env python3
"""Render HTML to PDF with brand fonts embedded (offline @font-face, not CDN).

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
CHROME_CANDIDATES = (
    "/opt/pw-browsers/chromium-1194/chrome-linux/chrome",
    "/usr/bin/google-chrome",
    "/usr/bin/google-chrome-stable",
    "/usr/bin/chromium",
    "/usr/bin/chromium-browser",
)

GF_LINK = re.compile(
    r'<link[^>]+fonts\.(?:googleapis|gstatic)\.com[^>]*>\s*', re.I)
# Local (non-CDN) stylesheet links — relative or same-origin path.
LOCAL_CSS_LINK = re.compile(
    r'<link\b[^>]*\brel=["\']stylesheet["\'][^>]*\bhref=["\']([^"\']+)["\'][^>]*>\s*'
    r'|'
    r'<link\b[^>]*\bhref=["\']([^"\']+)["\'][^>]*\brel=["\']stylesheet["\'][^>]*>\s*',
    re.I,
)


def find_chrome() -> str:
    for candidate in CHROME_CANDIDATES:
        if Path(candidate).exists() or shutil.which(candidate):
            return candidate
    which = shutil.which("google-chrome") or shutil.which("chromium")
    if which:
        return which
    sys.exit("chrome not found (tried " + ", ".join(CHROME_CANDIDATES) + ")")


def is_remote(href: str) -> bool:
    return href.startswith(("http://", "https://", "//", "data:"))


def inline_local_stylesheets(html: str, src: Path) -> tuple[str, int]:
    """Replace local <link rel=stylesheet> with <style>…</style> so tempfile print works."""
    count = 0

    def repl(match: re.Match) -> str:
        nonlocal count
        href = match.group(1) or match.group(2)
        if not href or is_remote(href):
            return match.group(0)
        css_path = (src.parent / href).resolve()
        try:
            css_path.relative_to(ROOT)
        except ValueError:
            sys.exit(f"{src}: stylesheet escapes repository: {href}")
        if not css_path.is_file():
            sys.exit(f"{src}: missing stylesheet {href} ({css_path})")
        count += 1
        return "<style>\n" + css_path.read_text() + "\n</style>\n"

    return LOCAL_CSS_LINK.sub(repl, html), count


def linked_local_stylesheets(src: Path) -> list[Path]:
    """Return local stylesheet paths referenced by src (for freshness hashing)."""
    html = src.read_text()
    out: list[Path] = []
    for match in LOCAL_CSS_LINK.finditer(html):
        href = match.group(1) or match.group(2)
        if not href or is_remote(href):
            continue
        css_path = (src.parent / href).resolve()
        if css_path.is_file():
            out.append(css_path)
    return out


def render(src: Path, out: Path, zoom: float = 1.0) -> None:
    html = src.read_text()
    if not FONT_CSS.exists():
        sys.exit(f"missing {FONT_CSS} — fonts cannot be embedded")

    html, n_css = inline_local_stylesheets(html, src)
    style = "<style>\n" + FONT_CSS.read_text() + "\n</style>"
    if zoom != 1.0:
        # Chrome honours zoom in print and it scales pt units too, which a
        # root font-size override does not. Used by tune_print_scale.py.
        style += f"<style>@media print{{body{{zoom:{zoom}}}}}</style>"
    html, n = GF_LINK.subn("", html)
    if "</head>" not in html:
        sys.exit(f"{src}: no </head>")
    html = html.replace("</head>", style + "\n</head>", 1)

    chrome = find_chrome()
    out.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory() as tmp:
        staged = Path(tmp) / src.name
        staged.write_text(html)
        subprocess.run(
            [chrome, "--headless", "--disable-gpu", "--no-sandbox",
             "--no-pdf-header-footer", f"--print-to-pdf={out}", str(staged)],
            check=True, capture_output=True)
    # Assert brand faces landed (Chrome can silently fall back without CDN).
    blob = out.read_bytes()
    missing = [f for f in (b"Archivo", b"SourceSerif4") if f not in blob]
    if missing:
        sys.exit(f"{out.name}: brand fonts missing from output "
                 f"({', '.join(m.decode() for m in missing)}) — refusing to ship it")

    try:
        shown = out.relative_to(ROOT)
    except ValueError:
        shown = out
    print(f"{shown}  ({n} CDN link(s) replaced, {n_css} local CSS inlined, "
          f"{out.stat().st_size // 1024}KB)")


def main() -> int:
    if len(sys.argv) not in (3, 4):
        sys.exit(__doc__)
    find_chrome()  # fail fast
    zoom = float(sys.argv[3]) if len(sys.argv) > 3 else 1.0
    render(Path(sys.argv[1]).resolve(), Path(sys.argv[2]).resolve(), zoom)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
