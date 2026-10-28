#!/usr/bin/env python3
"""Assert every entry page has required scripts, print styles, and signup wiring."""
import sys
from pathlib import Path

from site_catalog import (
    ALL_ENTRY_ROUTES,
    ENTRY_CSS_MARKERS,
    ENTRY_JS_MARKERS,
    ENTRY_ROUTES,
    MAILERLITE_FORM_ATTR,
    MAILERLITE_JS_URL,
)

ROOT = Path(__file__).resolve().parents[2]
LANDING = ROOT / "products" / "landing"
EMAILS = LANDING / "emails"
ENTRY_JS = LANDING / "assets" / "entry.js"
ENTRY_CSS = LANDING / "assets" / "entry.css"

REQUIRED = [
    ("shared entry stylesheet", 'href="/assets/entry.css"'),
    ("shared entry script", 'src="/assets/entry.js"'),
    ("mode buttons", 'class="go-do"'),
    ("print scale", "body{zoom:"),
]

EMAIL_REQUIRED = [
    ("MailerLite form", MAILERLITE_FORM_ATTR),
    ("MailerLite CDN", MAILERLITE_JS_URL),
    ("one-PDF promise", "one thing worth printing: the week on one page"),
]


def main() -> int:
    problems = []

    if not ENTRY_JS.is_file():
        problems.append(f"missing shared script: {ENTRY_JS.relative_to(ROOT)}")
    else:
        js = ENTRY_JS.read_text()
        for label, needle in ENTRY_JS_MARKERS:
            if needle not in js:
                problems.append(f"entry.js: missing {label}")

    if not ENTRY_CSS.is_file():
        problems.append(f"missing shared stylesheet: {ENTRY_CSS.relative_to(ROOT)}")
    else:
        css = ENTRY_CSS.read_text()
        for label, needle in ENTRY_CSS_MARKERS:
            if needle not in css:
                problems.append(f"entry.css: missing {label}")

    catalog_pages = []
    for route in ENTRY_ROUTES:
        path = LANDING / route.page
        if not path.is_file():
            problems.append(f"missing ENTRY_ROUTES page: {route.page}")
            continue
        catalog_pages.append(path)
        s = path.read_text()
        required = REQUIRED + EMAIL_REQUIRED if route.collects_email else REQUIRED
        for label, needle in required:
            if needle not in s:
                problems.append(f"{path.name}: missing {label}")

        if 'data-defer="on"' in s:
            for label, needle in (("'Not right now' button", 'class="go-later"'),
                                  ("appointment length", 'data-minutes="'),
                                  ("calendar title", 'data-task="')):
                if needle not in s:
                    problems.append(f"{path.name}: data-defer is on but missing {label}")

        expected_completion = f"/{route.completion_page}"
        completion_attr = f'data-completion-url="{expected_completion}"'
        if completion_attr not in s:
            problems.append(
                f"{path.name}: missing data-completion-url for {route.completion_page}"
            )

        if f'data-guide="{route.slug}"' not in s:
            problems.append(f'{path.name}: missing data-guide="{route.slug}"')
        seq = EMAILS / f"{route.slug}-sequence.md"
        if route.collects_email and not seq.is_file():
            problems.append(f"{path.name}: {seq.name} does not exist")
        if not route.collects_email:
            if 'class="ml-embedded"' in s:
                problems.append(f"{path.name}: direct-next route must not collect email")
            if route.next_url:
                target = ROOT / "products" / "landing" / route.next_url.lstrip("/").split("#", 1)[0]
                if not target.is_file() or not route.next_title or not route.next_description:
                    problems.append(f"{path.name}: direct next step must have an existing target and descriptive copy")

    # Warn on unexpected steps pages outside the catalog (orphan HTML).
    expected_names = {route.page for route in ALL_ENTRY_ROUTES}
    for path in sorted(LANDING.glob("*.html")):
        if path.name in expected_names:
            continue
        if 'class="steps"' in path.read_text():
            problems.append(
                f'{path.name}: has class="steps" but is not in ENTRY_ROUTES'
            )

    # Pre-build: completion template must keep the MailerLite CDN URL.
    finished_tmpl = LANDING / "templates" / "finished.html"
    if not finished_tmpl.is_file():
        problems.append(
            f"missing completion template: {finished_tmpl.relative_to(ROOT)}"
        )
    elif MAILERLITE_JS_URL not in finished_tmpl.read_text():
        problems.append(
            f"{finished_tmpl.relative_to(ROOT)}: missing MailerLite CDN "
            f"({MAILERLITE_JS_URL})"
        )

    if problems:
        print("Entry pages are incomplete:\n", file=sys.stderr)
        for x in problems:
            print(f"  {x}", file=sys.stderr)
        print("\nSee content/README.md — \"Building a new entry page\".",
              file=sys.stderr)
        return 1

    print(f"{len(catalog_pages)} entry pages complete: "
          f"{', '.join(p.stem for p in catalog_pages)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
