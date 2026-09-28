#!/usr/bin/env python3
"""Assert every entry page has required scripts, print styles, and signup wiring."""
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
LANDING = ROOT / "products" / "landing"
EMAILS = LANDING / "emails"
ENTRY_JS = LANDING / "assets" / "entry.js"

REQUIRED = [
    ("shared entry script", 'src="/assets/entry.js"'),
    ("mode buttons", 'class="go-do"'),
    ("viewport-locked layout", "body.doing .steps{flex:1"),
    ("step numbering fix", "content:attr(data-n)"),
    ("print hides the reasoning", ".why,.why.open,.whybtn"),
    ("print forces all steps", ".step{display:block !important}"),
    ("Letter page size", "@page{size:Letter"),
    ("print scale", "body{zoom:"),
    ("MailerLite form", 'data-form="00ZwEr"'),
    ("one-PDF promise", "Dave's week on one page"),
    ("post-completion destination", 'data-completion-url="/finished-'),
    ("guide tag config", 'data-guide="'),
]

ENTRY_JS_REQUIRED = [
    ("doing-mode", "classList.add('doing')"),
    ("source attribution handoff", "new URLSearchParams(window.location.search).get('from')"),
    ("MailerLite dual-field tag", "fields[guide]"),
    ("MailerLite fallback", "ml-fallback"),
    ("guide VALUE wiring", "var VALUE = guide"),
]


def main() -> int:
    problems = []

    if not ENTRY_JS.is_file():
        problems.append(f"missing shared script: {ENTRY_JS.relative_to(ROOT)}")
    else:
        js = ENTRY_JS.read_text()
        for label, needle in ENTRY_JS_REQUIRED:
            if needle not in js:
                problems.append(f"entry.js: missing {label}")

    pages = sorted(p for p in LANDING.glob("*.html")
                   if 'class="steps"' in p.read_text())
    if not pages:
        print("no entry pages found — did the layout change?", file=sys.stderr)
        return 1

    for p in pages:
        s = p.read_text()
        for label, needle in REQUIRED:
            if needle not in s:
                problems.append(f"{p.name}: missing {label}")

        # A page that asks for an email must tag it, and that tag must have a
        # sequence to receive. Otherwise it collects addresses and sends nothing.
        if "ml-embedded" in s:
            m = re.search(r'data-guide="([a-z0-9-]+)"', s)
            if not m:
                problems.append(f"{p.name}: has a signup but does not tag it")
            else:
                seq = EMAILS / f"{m.group(1)}-sequence.md"
                if not seq.exists():
                    problems.append(
                        f"{p.name}: tags signups '{m.group(1)}' but "
                        f"{seq.name} does not exist")
            cm = re.search(r'data-completion-url="(/finished-[a-z0-9-]+\.html)"', s)
            if not cm:
                problems.append(f"{p.name}: missing data-completion-url")

    if problems:
        print("Entry pages are incomplete:\n", file=sys.stderr)
        for x in problems:
            print(f"  {x}", file=sys.stderr)
        print("\nSee content/README.md — \"Building a new entry page\".",
              file=sys.stderr)
        return 1

    print(f"{len(pages)} entry pages complete: "
          f"{', '.join(p.stem for p in pages)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
