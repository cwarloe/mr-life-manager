#!/usr/bin/env python3
"""Fail-closed, offline quality contract for the published first-win journeys.

This checks source structure and analytics event *definitions*, not live users,
network services, or whether somebody physically finished a household task.
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from html.parser import HTMLParser
from pathlib import Path

from site_catalog import ENTRY_ROUTES, PUBLISHED_ENTRY_ROUTES


ROOT = Path(__file__).resolve().parents[2]
LANDING = ROOT / "products" / "landing"
ENTRY_JS = LANDING / "assets" / "entry.js"

# Existing Umami event names are a contract, not proposed new instrumentation.
# A new event/payload key requires deliberate review of interpretation/privacy.
EVENT_FIELDS: dict[str, frozenset[str]] = {
    "start-now": frozenset(),
    "not-right-now": frozenset(),
    "print": frozenset(),
    "reached-end": frozenset({"path"}),
    "finished": frozenset({"path"}),
    "time-picked": frozenset({"choice"}),
    "calendar-added": frozenset({"kind"}),
    "shared-with-checker": frozenset(),
    "came-back": frozenset({"moved", "step"}),
    "started-from-reminder": frozenset({"moved"}),
    "rescheduled": frozenset({"where", "moved"}),
    "stopped-at-limit": frozenset({"step"}),
    "let-go": frozenset(),
}
OPTIONAL_EVENT_FIELDS = {"rescheduled": frozenset({"step"})}
ALLOWED_FIELDS = frozenset({"path", "choice", "kind", "moved", "step", "where"})
COMMON_FIELDS = frozenset({"page", "from", "look"})
CALL = re.compile(r"\btrack\(\s*(['\"])([a-z0-9-]+)\1\s*(?:,\s*\{([^{}]*)\})?\s*\)", re.S)
CALL_SITE = re.compile(r"(?<![\w$.])track\s*\(")
FUNCTION_DEFINITION = re.compile(r"\bfunction\s+$")
DIRECT_UMAMI = re.compile(r"\bumami\.track\s*\(")
FIELD = re.compile(r"(?:^|,)\s*([a-zA-Z_$][\w$]*)\s*:")


class StepText(HTMLParser):
    """Extract actual step headings/actions without executing scripts."""

    def __init__(self) -> None:
        super().__init__(convert_charrefs=True)
        self.steps: list[dict[str, str]] = []
        self.current: dict[str, list[str]] | None = None
        self.capture = ""

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        classes = set((dict(attrs).get("class") or "").split())
        if tag == "li" and "step" in classes:
            self.current = {"heading": [], "action": []}
        elif self.current is not None and tag == "h2":
            self.capture = "heading"
        elif self.current is not None and tag == "p" and "do" in classes:
            self.capture = "action"

    def handle_data(self, data: str) -> None:
        if self.current is not None and self.capture:
            self.current[self.capture].append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag in ("h2", "p"):
            self.capture = ""
        elif tag == "li" and self.current is not None:
            self.steps.append({key: " ".join(" ".join(parts).split())
                               for key, parts in self.current.items()})
            self.current = None
            self.capture = ""


def check_events(js: str) -> tuple[dict[str, list[str]], list[str]]:
    problems: list[str] = []
    seen: dict[str, list[str]] = {}
    parsed_calls = list(CALL.finditer(js))
    parsed_starts = {match.start() for match in parsed_calls}
    for site in CALL_SITE.finditer(js):
        # This simple scanner intentionally accepts only literal event names
        # and flat payloads. Otherwise nested objects or computed names can
        # bypass the approved event-key contract without being inspected.
        before = js[max(0, site.start() - 24):site.start()]
        if FUNCTION_DEFINITION.search(before):
            continue
        if site.start() not in parsed_starts:
            problems.append("entry.js: unreviewed analytics track() call shape; "
                            "use a literal event name and flat payload")
    # The single approved direct Umami call is inside the track() adapter.
    # Extra direct calls would bypass payload/event review entirely.
    if len(DIRECT_UMAMI.findall(js)) != 1:
        problems.append("entry.js: direct Umami tracking bypasses the reviewed track() adapter")

    for match in parsed_calls:
        name = match.group(2)
        fields = set(FIELD.findall(match.group(3) or ""))
        seen.setdefault(name, []).append(",".join(sorted(fields)))
        if name not in EVENT_FIELDS:
            problems.append(f"entry.js: unexpected analytics event {name!r}; review its purpose and privacy")
            continue
        unexpected = fields - (EVENT_FIELDS[name] | OPTIONAL_EVENT_FIELDS.get(name, frozenset()))
        if unexpected:
            problems.append(f"entry.js: {name} has unreviewed payload keys {sorted(unexpected)}")
        missing = EVENT_FIELDS[name] - fields
        if missing:
            problems.append(f"entry.js: {name} is missing event keys {sorted(missing)}")

    for name in sorted(EVENT_FIELDS.keys() - seen.keys()):
        problems.append(f"entry.js: missing event {name!r}; measurement would drift")
    for marker in ("data.page = guide || location.pathname", "data.from = fromTag", "data.look = root.getAttribute('data-look')"):
        if marker not in js:
            problems.append(f"entry.js: missing common event attribution {marker!r}")
    if "^[a-z0-9-]{1,40}$" not in js:
        problems.append("entry.js: source attribution validation is missing")
    return seen, problems


def check_route(slug: str, page: str, completion: str, html: str,
                *, in_public_picker: bool) -> tuple[dict[str, object], list[str]]:
    problems: list[str] = []
    parser = StepText()
    parser.feed(html)
    steps = parser.steps

    # Six is the present product contract, not a recommended universal length.
    # A deliberate redesign should change this guard together with its QA cases.
    if len(steps) != 6:
        problems.append(f"{page}: {len(steps)} action steps; current published contract is 6")
    for i, step in enumerate(steps, 1):
        for field in ("heading", "action"):
            if not step[field]:
                problems.append(f"{page}: step {i} has no {field}")
    headings = [s["heading"] for s in steps if s["heading"]]
    if len(set(headings)) != len(headings):
        problems.append(f"{page}: duplicate step headings obscure the progression")

    if f'data-guide="{slug}"' not in html:
        problems.append(f"{page}: route identity mismatch")
    if f'data-completion-url="/{completion}"' not in html:
        problems.append(f"{page}: completion path mismatch")
    if 'class="go-do"' not in html or 'class="steps"' not in html:
        problems.append(f"{page}: no complete start-to-action structure")

    return {
        "slug": slug,
        "entry": page,
        "completion": completion,
        "placement": "public-picker" if in_public_picker else "direct-link-only",
        "step_count": len(steps),
        "first_action": steps[0]["heading"] if steps else None,
        "last_action": steps[-1]["heading"] if steps else None,
        "deferred_path": 'data-defer="on"' in html,
    }, problems


def audit(root: Path = ROOT) -> tuple[dict[str, object], list[str]]:
    landing = root / "products" / "landing"
    problems: list[str] = []
    routes: list[dict[str, object]] = []
    public = {route.slug for route in ENTRY_ROUTES}

    for route in PUBLISHED_ENTRY_ROUTES:
        path = landing / route.page
        try:
            source = path.read_text(encoding="utf-8")
        except OSError:
            problems.append(f"{route.page}: missing source")
            continue
        summary, errors = check_route(route.slug, route.page, route.completion_page,
                                      source, in_public_picker=route.slug in public)
        routes.append(summary)
        problems.extend(errors)

    try:
        js = (landing / "assets" / "entry.js").read_text(encoding="utf-8")
    except OSError:
        events, errors = {}, ["entry.js: missing analytics source"]
    else:
        events, errors = check_events(js)
    problems.extend(errors)
    report: dict[str, object] = {
        "schema_version": 1,
        "status": "PASS" if not problems else "FAIL",
        "routes": routes,
        "events": sorted(events),
        "allowed_payload_keys": sorted(ALLOWED_FIELDS | COMMON_FIELDS),
        "measurement_limit": (
            "Static checks prove source contracts only. Umami events and finished-page "
            "visits are directional self-reports, not proof of physical task completion "
            "or a user-level conversion rate. No real visitor data was accessed."
        ),
        "problems": problems,
    }
    return report, problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, help="Optional reviewer-readable JSON artifact")
    args = parser.parse_args()
    report, problems = audit()
    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        args.out.write_text(json.dumps(report, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    if problems:
        for problem in problems:
            print(f"- {problem}", file=sys.stderr)
        return 1
    print(f"Journey contract: {len(report['routes'])} published tasks, "
          f"{len(report['events'])} defined analytics events; source QA PASS")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
