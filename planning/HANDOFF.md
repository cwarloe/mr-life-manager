# Handoff — mr-life-manager

You are continuing work on **mr-life-manager**, Charles Warloe's business that
teaches the practical systems of adulthood, derived from his friend Dave
Webster's real teaching documents. Repo lives at `/home/user/mr-life-manager`
(note: the shell may open in a different repo — `cd` in first). Push to
`main` after the checks pass (Charles, 2026-10-26: "you can push to main. I
trust you. we can always revert."). Deploys run via GitHub Actions when changes
land on `main`.

## Read these before doing anything

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

## Open threads (nothing is blocking)

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
