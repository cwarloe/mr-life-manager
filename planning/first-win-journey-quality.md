# First-win journey: standard work and measurement contract

**Scope:** internal production control for the existing free checklists. This is
not a request to change customer copy, gather personal data, or add analytics.

## What leaves the production line

One published checklist, from the visitor's choice through a practical action
and an explicit finish-page acknowledgement. The five public-picker checklists
and direct-link office page share the same six-step structure, source script,
and finish-page pattern. `site_catalog.py` owns the route inventory; paused
pages are outside this release check.

| Gate | Inspect | Stop for |
| --- | --- | --- |
| Action structure | A six-step sequence with readable headings and nonempty actions | Missing/duplicate steps or an action that is empty |
| Route integrity | Source guide identity and intended finish page | Completion points to another person's checklist |
| Measurement consistency | Existing 13 Umami event names and the payload for each event | Renamed event, unreviewed parameter, dropped stage |
| Site integration | Existing `check_entry_pages.py` and `check_built_site.py` | Broken public route, mailer wiring, PDF, metadata or privacy notice |
| Behavioral review | Existing `tests/test_campaign_flows.py` browser tests, run by the `mobile-journey` CI job | A visitor can't proceed, schedule, resume or finish |

`python3 .github/scripts/check_journey_quality.py --out artifacts/journey-quality.json`
records a small, deterministic *traveler*: each published route, first and
last action, number of steps, direct-link/public-picker placement, completion
destination, deferred-scheduling mode, and approved analytics event names.
It contains **no live visitor records**. CI attaches that JSON even when a
subsequent test fails, allowing another agent to identify the exact contract
that was checked. Unit tests deliberately introduce broken steps, routes,
missing events and unreviewed payload fields to prove the gate rejects them.

## What the numbers mean

The current Umami implementation records `start-now`, `not-right-now`,
`time-picked`, `calendar-added`, `came-back`, `started-from-reminder`,
`reached-end`, and `finished`, among other specific events. The primary
outcome proxy is the **count of `finished` events**, grouped by checklist
and approved source tag. `reached-end` is an earlier stage; it is not a win.

- An explicit `finished` visit is a **self-report**, not independent proof of a
  physically completed task. A visitor can leave without acknowledging a win.
- Same-period event counts are not a deduplicated user cohort. A person can
  start twice, come back tomorrow, or use another device; an apparent
  `finished / start-now` ratio is therefore **not** an observed conversion rate.
- Page views, source tags and finish counts can help diagnose friction, but
  do not fabricate a baseline when Umami results have not been retrieved.
  **Live outcome data has not been inspected for this control.**
- `from`, `page` and `look` are constrained attribution dimensions, not a
  visitor identity. New payload fields require privacy and interpretation
  review. The static gate is useful drift detection, not a full JavaScript
  data-flow or security analysis.

## Small, sustainable improvement cycle

1. **Observe:** use the existing monthly scorecard and real reader feedback.
   Start with the current five public paths; do not widen the content catalog.
2. **Diagnose:** distinguish no traffic, no start, lost progress, no explicit
   finish, and confusing physical actions. Preserve a reproducible example.
3. **Correct:** change the smallest applicable source and add a regression
   test for that specific failure. Retain earlier corrections.
4. **Verify:** run the offline gate, repository/site validation, and browser
   journey tests if the actual interaction changed.
5. **Release:** ordinary internal engineering can merge after green CI.
   Marketing decisions, new data collection, paid offers, customer outreach,
   and changes to established public content remain separate decisions.

The operating goal is **completed useful actions per owner-hour**, with
minimal review burden. A broken CI contract or repeated support issue is a
reason to stop and investigate; a green static gate is **not** permission to
claim a demonstrated learning or business outcome.

Related: [operations and scorecard](operations.md),
[`CLAUDE.md`](../CLAUDE.md),
[`tests/test_campaign_flows.py`](../tests/test_campaign_flows.py),
and [open reminder concept PR #108](https://github.com/cwarloe/mr-life-manager/pull/108)
(owner review required; not changed by this initiative).

## Automated mobile regression check

The `mobile-journey` job in `validate-content.yml` builds the local site and
runs `tests/test_campaign_flows.py` using the pinned Playwright dependency in
`tests/requirements-browser.txt`. It runs on pull requests and relevant main
pushes, including browser-test and dependency-file changes. The browser
context blocks requests outside its local server; there are no signups,
calendar-account saves or live-customer records involved.

The browser suite verifies the accepted commitment-first entrances, one
start-time picker, near-term and future-day choices, rejection of missing/past
times, removal of stale calendar links after edits, calendar contents and
return URLs, reminder/current-step resume, all six steps, mobile overflow,
one-page print output, completion routing for every published task, and full
checklist access when JavaScript is unavailable. The existing offline gate remains a fast separate
check. A passing browser run verifies interaction behavior, not physical work
or Instagram's calendar integration.

For a local run, install `tests/requirements-browser.txt` in a virtual
environment, install its Chromium with `python -m playwright install chromium`,
build with `python3 .github/scripts/build_site.py`, and run
`python tests/test_campaign_flows.py -v`. `CAMPAIGN_BROWSER` can select an
existing Chromium executable; otherwise the tests prefer their pinned
Playwright browser when no explicit executable is selected.
