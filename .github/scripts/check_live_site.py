#!/usr/bin/env python3
"""Smoke-test the production site without submitting forms or collecting data."""

from __future__ import annotations

import sys
import time
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen

from site_catalog import (
    ENTRY_ROUTES,
    FIRST_PLACE_LIVE_MARKERS,
    MAILERLITE_FORM_ATTR,
    MAILERLITE_JS_URL,
    ORIGIN,
    PARTNERS_LIVE_MARKERS,
    PRIVACY_LIVE_MARKERS,
    required_share_images,
)


def _entry_pages() -> dict[str, tuple[str, ...]]:
    pages: dict[str, tuple[str, ...]] = {
        "/": ("Run your home without carrying all of it in your head",),
    }
    for route in ENTRY_ROUTES:
        pages[f"/{route.page}"] = (
            MAILERLITE_FORM_ATTR,
            f'data-guide="{route.slug}"',
            'src="/assets/entry.js"',
            "Dave's week on one page",
        )
    for route in ENTRY_ROUTES:
        pages[f"/{route.completion_page}"] = (
            MAILERLITE_FORM_ATTR,
            MAILERLITE_JS_URL,
            f'data-guide="{route.slug}"',
            'src="/assets/entry.js"',
            "ml-fallback",
            "One thing finished",
        )
    pages["/first-place.html"] = FIRST_PLACE_LIVE_MARKERS
    pages["/partners.html"] = PARTNERS_LIVE_MARKERS
    pages["/privacy.html"] = PRIVACY_LIVE_MARKERS
    return pages


PAGES = _entry_pages()
# Live check expects home + entry doors + privacy (subset of sitemap_core_urls).
SITEMAP_URLS = (
    f"{ORIGIN}/",
    *(f"{ORIGIN}/{route.page}" for route in ENTRY_ROUTES),
    f"{ORIGIN}/privacy.html",
)


def fetch(url: str) -> tuple[str, str, bytes]:
    request = Request(url, headers={"User-Agent": "mr-life-manager-healthcheck/1.0"})
    with urlopen(request, timeout=20) as response:
        return response.geturl(), response.headers.get_content_type(), response.read()


def _expect_pdf(url: str, problems: list[str]) -> None:
    try:
        final, content_type, body = fetch(url)
        if final != url:
            problems.append(f"{url}: unexpected final URL {final}")
        if content_type != "application/pdf" or not body.startswith(b"%PDF-"):
            problems.append(f"{url}: response is not a PDF")
    except (HTTPError, URLError, TimeoutError) as exc:
        problems.append(f"{url}: {exc}")


def run_once() -> list[str]:
    problems: list[str] = []
    for path, markers in PAGES.items():
        url = ORIGIN + path
        try:
            final, content_type, body = fetch(url)
        except (HTTPError, URLError, TimeoutError) as exc:
            problems.append(f"{url}: {exc}")
            continue
        if not final.startswith(ORIGIN):
            problems.append(f"{url}: redirected outside canonical domain to {final}")
        if content_type != "text/html":
            problems.append(f"{url}: content type {content_type}, expected text/html")
        text = body.decode("utf-8", errors="replace")
        for marker in markers:
            if marker not in text:
                problems.append(f"{url}: missing {marker}")
        if 'rel="canonical"' not in text:
            problems.append(f"{url}: missing canonical metadata")
        if path != "/privacy.html" and 'href="/privacy.html"' not in text:
            problems.append(f"{url}: missing privacy link")

    _expect_pdf(ORIGIN + "/print/the-week.pdf", problems)
    _expect_pdf(ORIGIN + "/print/partner-pilot.pdf", problems)

    for share_name in required_share_images():
        share_url = ORIGIN + f"/assets/share/{share_name}"
        try:
            final, content_type, body = fetch(share_url)
            if final != share_url:
                problems.append(f"{share_url}: unexpected final URL {final}")
            if content_type != "image/png" or not body.startswith(b"\x89PNG\r\n\x1a\n"):
                problems.append(f"{share_url}: response is not a PNG")
        except (HTTPError, URLError, TimeoutError) as exc:
            problems.append(f"{share_url}: {exc}")

    sitemap_url = ORIGIN + "/sitemap.xml"
    try:
        final, content_type, body = fetch(sitemap_url)
        if final != sitemap_url:
            problems.append(f"{sitemap_url}: unexpected final URL {final}")
        if content_type not in {"application/xml", "text/xml"}:
            problems.append(f"{sitemap_url}: content type {content_type}, expected XML")
        sitemap = body.decode("utf-8", errors="replace")
        if "finished-" in sitemap:
            problems.append(f"{sitemap_url}: completion pages must stay out of search")
        for loc in SITEMAP_URLS:
            if loc not in sitemap:
                problems.append(f"{sitemap_url}: missing {loc}")
    except (HTTPError, URLError, TimeoutError) as exc:
        problems.append(f"{sitemap_url}: {exc}")

    robots_url = ORIGIN + "/robots.txt"
    try:
        final, _, body = fetch(robots_url)
        robots = body.decode("utf-8", errors="replace")
        if sitemap_url not in robots:
            problems.append(f"{robots_url}: missing Sitemap line for {sitemap_url}")
    except (HTTPError, URLError, TimeoutError) as exc:
        problems.append(f"{robots_url}: {exc}")

    for start in ("http://mrlifemanager.com/", "https://www.mrlifemanager.com/"):
        try:
            final, _, _ = fetch(start)
            if final != ORIGIN + "/":
                problems.append(f"{start}: ended at {final}, expected {ORIGIN}/")
        except (HTTPError, URLError, TimeoutError) as exc:
            problems.append(f"{start}: {exc}")
    return problems


def main() -> int:
    problems: list[str] = []
    for attempt in range(3):
        problems = run_once()
        if not problems:
            print(
                f"Production smoke test passed: {len(PAGES)} pages, "
                f"{len(ENTRY_ROUTES)} routes, one partner path, one founding offer, "
                "two PDFs, share images, sitemap, robots and canonical redirects."
            )
            return 0
        if attempt < 2:
            time.sleep(10)
    print("Production smoke test failed:", file=sys.stderr)
    for problem in problems:
        print(f"- {problem}", file=sys.stderr)
    return 1


if __name__ == "__main__":
    raise SystemExit(main())
