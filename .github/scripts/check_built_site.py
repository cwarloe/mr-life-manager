#!/usr/bin/env python3
"""Verify generated-site metadata, routing and public offer invariants."""

from __future__ import annotations

import re
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urlsplit
from check_preview_site import check_preview_site

from guide_inventory import LEGACY_GUIDE_SLUGS, PAUSED_GUIDE_SLUGS, PUBLISHED_PDF_NAMES, PDF_TITLES
from site_catalog import (
    ENTRY_ROUTES,
    PAUSED_LANDING_PAGES,
    ORIGIN,
    MAILERLITE_FORM_ATTR,
    MAILERLITE_JS_URL,
    PARTNERS_BUILT_MARKERS,
    PRIVACY_BUILT_MARKERS,
    UMAMI_SCRIPT_URL,
    UMAMI_WEBSITE_ID,
    public_url as catalog_public_url,
    required_share_images,
)

ROOT = Path(__file__).resolve().parents[2]
OUT = ROOT / "_site"


class PublicLinks(HTMLParser):
    def __init__(self) -> None:
        super().__init__()
        self.picks: list[str] = []
        self.links: list[str] = []

    def handle_starttag(self, tag, attrs):
        if tag != "a":
            return
        attrs = dict(attrs)
        href = attrs.get("href", "")
        parsed = urlsplit(href)
        if parsed.netloc and parsed.netloc != urlsplit(ORIGIN).netloc:
            return
        self.links.append(parsed.path)
        if "pick" in attrs.get("class", "").split():
            self.picks.append(parsed.path)


def public_url(path: Path) -> str:
    return catalog_public_url(path, OUT)


def main() -> int:
    problems: list[str] = []
    pages = sorted(OUT.rglob("*.html"))
    if not pages:
        print("_site has no HTML; run build_site.py first", file=sys.stderr)
        return 1

    legacy_pages = {
        OUT / "guides" / f"{old}.html": f"/guides/{new}.html"
        for old, new in LEGACY_GUIDE_SLUGS.items()
    }
    legacy_pages.update({OUT / name: "/" for name in PAUSED_LANDING_PAGES})
    legacy_pages.update({OUT / "guides" / f"{slug}.html": "/" for slug in PAUSED_GUIDE_SLUGS})
    sitemap = (OUT / "sitemap.xml").read_text(encoding="utf-8")
    for path, target in legacy_pages.items():
        rel = path.relative_to(OUT)
        if not path.is_file():
            problems.append(f"missing legacy redirect: {rel} -> {target}")
            continue
        text = path.read_text(encoding="utf-8")
        target_path = OUT / target.lstrip("/")
        if target_path.is_dir():
            target_path = target_path / "index.html"
        if not target_path.is_file():
            problems.append(f"{rel}: redirect target {target} was not built")
        for marker in ('data-mlm-redirect="1"',
                       f'http-equiv="refresh" content="0; url={target}"',
                       f'<link rel="canonical" href="{ORIGIN}{target}">',
                       'name="robots" content="noindex"'):
            if marker not in text:
                problems.append(f"{rel}: missing {marker}")
        if public_url(path) in sitemap:
            problems.append(f"sitemap.xml: legacy redirect {rel} must stay out of search")
    for old, new in LEGACY_GUIDE_SLUGS.items():
        if (OUT / "print" / f"{new}.pdf").is_file() and not (OUT / "print" / f"{old}.pdf").is_file():
            problems.append(f"missing legacy PDF alias: print/{old}.pdf")

    published_pdfs = {path.name for path in (OUT / "print").glob("*.pdf")}
    expected_pdfs = PUBLISHED_PDF_NAMES | {
        f"{old}.pdf" for old, new in LEGACY_GUIDE_SLUGS.items()
        if f"{new}.pdf" in PUBLISHED_PDF_NAMES
    }
    if published_pdfs != expected_pdfs:
        problems.append(f"print/: published PDFs {sorted(published_pdfs)}, expected {sorted(expected_pdfs)}")

    expected_entries = [f"/{route.page}" for route in ENTRY_ROUTES]
    for filename, repeats in (("index.html", 1), ("index-parents.html", 2), ("partners.html", 1)):
        links = PublicLinks()
        links.feed((OUT / filename).read_text(encoding="utf-8"))
        if links.picks != expected_entries * repeats:
            problems.append(f"{filename}: public picker does not match the active checklist order")
    step_pages = {path.name for path in OUT.glob("*.html") if 'class="steps"' in path.read_text(encoding="utf-8")}
    if step_pages != {route.page for route in ENTRY_ROUTES}:
        problems.append("published task pages do not match the active entry catalog")
    paused_urls = {f"/{name}" for name in PAUSED_LANDING_PAGES}
    paused_urls.update(f"/guides/{slug}.html" for slug in PAUSED_GUIDE_SLUGS)
    paused_urls.update(f"/print/{name}" for name in PDF_TITLES if name not in expected_pdfs)
    for path in pages:
        links = PublicLinks()
        links.feed(path.read_text(encoding="utf-8"))
        if paused_urls.intersection(links.links):
            problems.append(f"{path.relative_to(OUT)}: links to paused checklist material")

    for path in pages:
        if path in legacy_pages:
            continue
        text = path.read_text(encoding="utf-8")
        rel = path.relative_to(OUT)
        expected = public_url(path)
        canonicals = re.findall(r'<link rel="canonical" href="([^"]+)">', text)
        if canonicals != [expected]:
            problems.append(f"{rel}: canonical {canonicals!r}, expected {expected}")
        if text.count('data-mlm-meta="1"') != 1:
            problems.append(f"{rel}: expected exactly one generated metadata block")
        for marker in ('rel="icon" href="/favicon.svg"', 'rel="manifest" href="/site.webmanifest"',
                       'property="og:title"', 'property="og:description"',
                       'property="og:url"', 'property="og:image"',
                       'name="twitter:card" content="summary_large_image"'):
            if marker not in text:
                problems.append(f"{rel}: missing {marker}")

    for route in ENTRY_ROUTES:
        tag = route.slug
        completion = route.completion_page
        completion_text = (OUT / completion).read_text(encoding="utf-8")
        markers = (f'data-guide="{tag}"', 'src="/assets/entry.js"', "One thing finished",
                   'name="robots" content="noindex,nofollow"')
        if route.collects_email:
            markers += (MAILERLITE_FORM_ATTR, MAILERLITE_JS_URL, "ml-fallback")
        else:
            if MAILERLITE_FORM_ATTR in completion_text or "ml-embedded" in completion_text:
                problems.append(f"{completion}: direct-next route must not collect email")
            if route.next_url:
                markers += (f'href="{route.next_url}"', route.next_title)
                next_path = OUT / route.next_url.lstrip("/").split("#", 1)[0]
                if not next_path.is_file():
                    problems.append(f"{completion}: next-step target does not exist")
            elif 'class="next-step"' in completion_text:
                problems.append(f"{completion}: unexpected next-step offer")
        for marker in markers:
            if marker not in completion_text:
                problems.append(f"{completion}: missing {marker}")
        # One ask after the win (principle 11): the signup is the only offer.
        for marker in ("/first-place.html", "navigator.share", "Where%20I%20stopped"):
            if marker in completion_text:
                problems.append(f"{completion}: must carry only the signup ask, found {marker}")

    # The $39 First Place offer was removed (ADR-020): no page may come back or link to it.
    if (OUT / "first-place.html").exists():
        problems.append("first-place.html: removed offer page is back in the build")
    for page in OUT.rglob("*.html"):
        if "/first-place.html" in page.read_text(encoding="utf-8"):
            problems.append(f"{page.relative_to(OUT)}: links to removed /first-place.html")

    partners = (OUT / "partners.html").read_text(encoding="utf-8")
    for marker in PARTNERS_BUILT_MARKERS:
        if marker not in partners:
            problems.append(f"partners.html: missing {marker}")

    privacy = (OUT / "privacy.html").read_text(encoding="utf-8")
    for marker in PRIVACY_BUILT_MARKERS:
        if marker not in privacy:
            problems.append(f"privacy.html: missing {marker}")

    for name in ("favicon.svg", "site.webmanifest", "robots.txt", "sitemap.xml",
                 "print/partner-pilot.pdf", "assets/entry.js", "assets/entry.css",
                 *(route.page for route in ENTRY_ROUTES)):
        if not (OUT / name).is_file():
            problems.append(f"missing generated public file: {name}")

    for share_name in required_share_images():
        rel = f"assets/share/{share_name}"
        if not (OUT / rel).is_file():
            problems.append(f"missing generated public file: {rel}")

    # Analytics: all-or-nothing, and the privacy page must match reality.
    privacy_text = (OUT / "privacy.html").read_text(encoding="utf-8")
    for path in pages:
        if path in legacy_pages:
            continue
        has = UMAMI_SCRIPT_URL in path.read_text(encoding="utf-8")
        expected_analytics = bool(UMAMI_WEBSITE_ID) and not path.is_relative_to(OUT / "preview")
        if expected_analytics != has:
            problems.append(f"{path.relative_to(OUT)}: analytics script "
                            f"{'missing' if UMAMI_WEBSITE_ID else 'present without an ID'}")
    if UMAMI_WEBSITE_ID and "Umami" not in privacy_text:
        problems.append("privacy.html: analytics is on but the page doesn't describe it")
    if not UMAMI_WEBSITE_ID and ("data-analytics-only" in privacy_text or "Umami" in privacy_text):
        problems.append("privacy.html: describes analytics that isn't running")

    if "finished-" in sitemap:
        problems.append("sitemap.xml: completion pages must stay out of search")

    check_preview_site(OUT, problems)
    if problems:
        print("Built-site validation failed:", file=sys.stderr)
        for problem in problems:
            print(f"- {problem}", file=sys.stderr)
        return 1

    print(f"Validated {len(pages) - len(legacy_pages)} generated pages, "
          f"{len(legacy_pages)} paused/legacy redirect(s), {len(ENTRY_ROUTES)} entry routes, "
          "and the partner path.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())

