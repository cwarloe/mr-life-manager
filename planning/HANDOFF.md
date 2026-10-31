# Handoff — mr-life-manager

You are continuing work on **mr-life-manager**, Charles Warloe's business that
teaches the practical systems of adulthood, derived from his friend Dave
Webster's real teaching documents. Repo lives at `/home/user/mr-life-manager`
(note: the shell may open in a different repo — `cd` in first). Push to
`main` after the checks pass (Charles, 2026-10-26: "you can push to main. I
trust you. we can always revert."). Deploys run via GitHub Actions when changes
land on `main`.

## Read these before doing anything

**Current publication scope, 2026-10-27:** Charles selected five active
entrances, in this order: first-night, guests, dinner, underwater, one-room.
Other task pages (including office), the organizing comparison, and reference
guides/PDFs are paused. Their source remains intact; old HTML URLs redirect to
the homepage. Only The Week and partner pilot handout stay published as PDFs,
to preserve active delivery promises. The homepage, parent page, partner page,
and guide index all point to the five. `ACTIVE_ENTRY_SLUGS` and the reference
publication flag control what ships; build checks reject paused content and
picker drift. Older entries below describe previous publication states.

**2026-10-31:** office is published again as a direct-link page
(`DIRECT_LINK_SLUGS` in `site_catalog.py`): live at `/office.html`, not in
pickers or the sitemap, so the link that office already has works. Time copy
before the start button is one plain line ("Give it about an hour. Longer if
the sink is full."), not a disclaimer (Charles: "stop being defensive").

**Audience landing pages, 2026-10-31:** the main page stays; each QR audience
gets its own landing page at `/for/<audience>.html` in its own look, and the
look carries through the checklist, calendar return and finish page (Charles
chose "carry it through"). First one: `/for/early-career.html`, `pro` look.
Students (Comic Panel) and military (Mission Board) are next candidates. How
to add one: [`products/landing/audiences/README.md`](../products/landing/audiences/README.md).

- `CLAUDE.md` — the working agreement. The two rules that matter most:
  (1) You make changes and push to `main` once checks pass; a
  bot does everything downstream (MailerLite, any live account). Don't hand
  Charles manual steps or a chore list; that's what the bot is for. End with a short plain-prose note for
  the bot. (2) Keep replies short by default.
- `content/README.md` — house style: depth rule, US English, email voice
  (full sentences, not clipped AI fragments), printables ≠ web pages, how to
  refer to Dave (first name, "decades," not his last name; not on task pages,
  only after the win).
- `planning/decisions.md` — the ADRs. ADR-014 completion converts; ADR-015 the
  win comes before the email ask; ADR-016 the follow-up sequence shrinks
  unconditionally; ADR-017 Kitchen That Works is free, folded into Six Meals;
  ADR-018 six meals taken off the old paid flagship; ADR-019
  Laundry, Solved and the roommate kit are free only (no $9 tier for now).
  ADR-020 win before wallet is **Accepted (2026-10-15)** (retires the $39
  flagship; house-in-order system is the flagship).
  **ADR-010, ADR-015 and ADR-016 are under review as of 2026-10-03**
  (buyers, revenue model and marketing strategy being reworked); don't build
  new work on them until they're re-decided.
- `source-material/INVENTORY.md` — every known Dave document and its state.
  Everything under `source-material/` is **verbatim, never edited, not even for
  spelling.** Interpretation goes in separate analysis files.

## Unlisted live review section, 2026-10-28

Charles requested viewing the revised paused material live outside the standard
workflow. `/preview/` now indexes twenty review choices: seven short tasks,
four organizing drafts plus their comparison, and eight reference guides.
Guide pages link to `/preview/print/` copies of the eight current saved PDFs.
The full twelve-step Markdown checklist is rendered to HTML; the three longer
variants remain on the synchronized comparison page with separate anchor links.

`preview_site.py` builds from retained sources, adds draft/back-to-index chrome,
noindex metadata and no sitemap entries. It removes forms/MailerLite, and uses
a generated execution-script copy with production tracking/signup code removed.
Completion pages and calendar return URLs stay inside `/preview/`; ordinary
paused URLs and five normal choices are unchanged. Preview PDF crawling is
excluded in robots.txt. `check_preview_site.py`, called by the normal built-site
checker, guards inventory, noindex, local links, source PDF equality, tracking
isolation and absence of links from the standard site. Workflow path filters
include the new modules. Browser review covers320/375px, all seven task flows,
calendar/resume, one-page printing, twelve full-reset and24variant checkboxes,
three-page comparison printing and reference layouts. This is unlisted public
review, not reader validation or approval to promote the drafts.

## Paused drafts revised, 2026-10-28

Charles authorized improving the paused material for later use while keeping
it unpublished. All 20 audited source surfaces now have design revisions:
seven paused entries, the comparison and four organizing drafts, and eight
reference guides/worksheets. The [readiness index](../docs/research/paused-checklist-readiness.md)
links each source and explains the changes, checks, and remaining real-user
validation. The multi-drawer reset retains its full meal-tool win; recipe and
reference procedures have concrete prerequisites and truthful outcomes.
Eight retained reference PDFs are regenerated with updated scales and hashes.
No active-entry source, verbatim source material, email sequence, publication
flag, The Week PDF or partner PDF was changed. Paused URLs remain redirects;
these are prepared for pilot review, not measured or approved for reactivation.

## Audit follow-through, 2026-10-28

Charles authorized revisions to the five active checklists and asked the audit
agent to review paused material as well. The
[active revision brief](../products/landing/briefs/active-checklist-revisions.md)
records the shipped changes. The pages keep six steps and full outcomes; they
state supplies, clarify variable work, and use explicitly untested calendar
planning blocks instead of narrow finish-time claims. Homepage, parent and
partner blurbs no longer repeat the old timing or partial-finish promises;
the shared Done screen asks the reader to check the complete task.

The [paused audit](../docs/research/paused-checklist-completion-audit.md) covers
seven paused entries, the organizing comparison, the full reset and its three
variants (including drawers), and eight reference guides/worksheets. It does
not revise or reactivate those products. Current publication remains five.
Source/PDF freshness, mobile task flow, completion, calendar and one-page print
checks pass; these are technical checks, not observed household completion.
No participants were contacted, and no email-account changes were made.
The next evidence step remains real-user full-task pilots from the audit.

## Completion audit, 2026-10-28

Charles requested an agent review of cognitive load, time, and actual completion.
The [sourced audit](../docs/research/checklist-completion-audit.md) combines an
independent agent review with research and a route-by-route task analysis.
Dinner is the strongest pilot candidate; first-night and guests are conditional;
underwater and one-room need revision before their broad fixed-time promises
are defensible. None has measured completion evidence from this audit. Keep the
full outcomes: clarify prerequisites/workload and calibrate timing through
observed full-task sessions rather than counting partial tasks as finished.
The audit includes proposed corrections and an exploratory pilot protocol.
Public pages, calendar durations and analytics were not changed by the audit;
these remain open implementation work. No participants were contacted.

## Finish-line copy, 2026-10-28

Each of the five active entry pages now states a concrete result before the
start/calendar choice. Charles approved making the win clear, but rejected
shorter finish lines for these tasks. Keep the full six steps; do not pitch
completing only the first one or two as the finished job. Existing time blocks
remain estimates (first night about an hour, guests 35 minutes, reset 40 minutes,
one zone about two hours); dinner has no completion-time promise. The room
promise is one fully finished zone, not the whole room. The task instructions,
calendar flow, signup delivery, and publication scope are unchanged. Copy is
an experiment, not evidence of improved completion.

## Where things stand

The funnel is: one pain → one entry page → one action → one win → then the
email ask. The entry pages in `site_catalog.py` are live and CI-complete
(`first-night`, `guests`, `one-room`, `underwater`, and `office`), each with a
phone "doing mode" (one step per screen, Next/Back, `Why?` toggles) and a real
one-page printable. `office` (added 2026-10-06) is a deliberate one-off
(Charles, 2026-10-08): keep it direct-link only; do not add it to the homepage,
parents, or partners pickers. Nine printables render to PDF from HTML via
headless Chromium with brand fonts embedded (`.github/scripts/render_all_pdfs.py`).
Four MailerLite email sequences are active per owner confirmation on 2026-09-22;
the office sequence is drafted, but its MailerLite group and automation are not
set up yet. Each sequence sends one PDF link in email 1: `/print/the-week.pdf`.
The entry-page action sheet is available before signup, so email doesn't
promise it.

CI scripts enforce the invariants — run them before committing:
- Public origin + the entry routes live in
  `.github/scripts/site_catalog.py` — import from there; don't hardcode the
  doors in new checks
- `python3 .github/scripts/validate_repo.py` (HTML + internal links)
- `python3 .github/scripts/check_entry_pages.py` (each page has doing-mode,
  mode buttons, print rules, a signup tag, AND a matching `<tag>-sequence.md`)
- `python3 .github/scripts/check_pdfs_fresh.py` (PDF source hash unchanged)
- `python3 .github/scripts/build_site.py` (assemble `_site/`)
- `python3 .github/scripts/check_built_site.py` (generated metadata, routes and
  offer invariants; run after the build)

**Added 2026-10-26** — read these before touching the entry pages:

- **"Not right now" flow** on all five task pages
  ([ADR-021](decisions.md#adr-021--when-the-reader-cant-act-yet-ask-for-a-when),
  [architecture](deferred-win-architecture.md)): the box above the buttons states
  the time and place; "Not right now" picks an exact time and makes a calendar
  invite; the invite returns the reader to the step they left; two moves, then
  "start now or let it go." All in the shared `assets/entry.js`, opted in per page
  with `data-defer`.
- **Task pages don't mention Dave**
  ([content rules](../content/README.md#referring-to-dave)). He is introduced
  after the win: completion page and emails.
- **Analytics:** Umami event tracking is coded and off until a website ID is
  set (see the "Waiting on the bot" list in [operations.md](operations.md)).
- **Dave's principles engine** ([frameworks/dave-principles.md](../frameworks/dave-principles.md))
  is how new pages are built from his method.
- **What the bot needs to do** is listed in one place: the top of
  [operations.md](operations.md#waiting-on-the-bot).

Production monitoring runs automatically after Pages deploys and every Monday
through `.github/workflows/check-live-site.yml`. It checks public pages and the
single promised PDF without submitting the MailerLite form.

**Added 2026-10-27 — intervention template.** Charles reviewed and approved the
Drive transcript for use. The [2014 analysis](../source-material/2014-01-15-analysis.md)
now has timestamped observations and exact short quotes, without claiming a
completed transformation or a validated service. The
[session template](../content/intervention-template.md) supplies blank forms and
a partial worked example. The [principles engine](../frameworks/dave-principles.md)
now includes the video as evidence, four-category sorting as a valid application,
and the return-visit qualification to a one-session reset. The transcript itself
is unchanged. Charles's own retrospective and results from a new session remain
to be captured; the template's prompts are ours. No MailerLite update is needed.

## Open threads (nothing is blocking)

**Added 2026-10-27 — guide-derived felt-pain entrances.** Six new six-step
pages cover clean laundry piles, a simple bean-wrap dinner, a suitable cleaner
for one kitchen surface, a useful sitting spot, a kitchen ready for breakfast,
and one shared dishes agreement. The
[coverage brief](../products/landing/briefs/felt-pain-guides.md) maps the full
guide library to new or existing entrances. Each new route uses doing mode,
Letter printing, a calendar option, and a no-signup completion page with no
longer-checklist links. The homepage groups eleven choices by immediate need;
office stays direct-link. Longer guides and PDFs are preserved. No new
MailerLite setup or live-account work is needed. Reader appeal, completion,
and lasting outcomes remain untested.

**Updated 2026-10-27 — dinner links and calendar.** Charles asked to de-link
the longer checklists for now. The dinner page and its completion page no
longer link to them; all longer draft files remain intact. Dinner now opts into
the shared “Not right now” calendar flow, reserving ten minutes to start and
preserving source attribution and mid-task resume steps. Completion ends at
the win, without an email signup or next-step offer. The route catalog now
declares `email_signup` explicitly rather than inferring it from a next URL.

**Added 2026-10-27 — dinner entry point.** Charles chose “Dinner's ready.
There's nowhere to eat.” The six-step page at `/dinner.html` is linked from
the homepage and parent/partner pages. It makes the table and needed seats
usable; the temporary basket is explicitly unfinished. Its completion page
offers the longer table checklist directly, without collecting email or
promising a new sequence. The route catalog supports this explicit direct-next
path, while existing email routes keep their signup requirements. The three
eight-step drafts and twelve-step guide remain unchanged. Browser checks cover
mobile navigation, completion, source attribution, and the next-step link;
print scale is tuned to one Letter page. Reader outcomes remain untested.

**Added 2026-10-27 — three organizing checklist drafts.** Charles asked to
compare the same method in three spaces. The public
[comparison page](../products/landing/organizing-ideas.html), at
`/organizing-ideas.html`, contains eight-step versions for kitchen junk drawers,
a household cupboard or closet where things disappear, and a dining table
blocked by clutter. Each has an observable daily-life finish. The
[shared brief](../products/checklists/reset-your-space/versions/brief.md) records
source evidence and adaptations; the Markdown copies sit beside it. These are
direct-link comparison drafts, not three registered entry pages or homepage
choices. No winner or completion-time claim has been established. No new
MailerLite setup is needed for this comparison page.

1. **Roommate-agreement material.** Searched Gmail 2026-09-22. Four documents
   found, none Dave's, all in `.doc/.docx` attachments the Gmail connector can
   list but not download (see `source-material/INVENTORY.md`). Best two: the
   2024 Boise roommate agreement (thread `18fd06c6c2a00d54` — Charles adapted
   Chad Morgan's versions; forwarded 2025 as "the template," but **recipient
   unconfirmed** / not Dave's known address; **contents never read**, so nothing
   in the repo is built from it) and Micah Stroh's 2011 "tenant house rules"
   behavior policy (thread `1315e9526d510865`). To use either, Charles must "Add
   to Drive" from Gmail, then the Drive connector can read the text. Don't turn
   this into a chore list — offer it once. Note: there's already a
   `household-agreement` printable in the repo.
2. **The "mail thing."** Searched thoroughly — subject, phrases, Dave's
   addresses. Nothing. Dave's "earlier papers on mail" (referenced in the 2009
   weekly schedule) remains unfound. Treat as a dead end unless Charles locates
   a file.
3. **`Do it now.jpg`** (2023 attachment) still unretrieved — Drive can read
   JPEGs if he adds it.
4. ~~The `underwater` and `one-room` email copy is unreviewed.~~ **Reviewed
   2026-09-21** (PR #10) and reported active 2026-09-22. Reader validation
   remains open.

Business operations, trigger gates, account continuity and the last external
funnel check live in [`operations.md`](operations.md). Monthly evidence lives in
[`monthly-scorecard.md`](monthly-scorecard.md); do not create a parallel tracker.

## The workflow

Do the work, run the CI scripts, commit on a branch, and open a PR. **Do not
merge to `main` without Charles.** End your reply with a 2–3 line note telling
the bot what changed and what (if anything) to update in MailerLite. Commit
trailer to use:

    Co-Authored-By: <model name> <noreply@anthropic.com>
    Claude-Session: <session url>
