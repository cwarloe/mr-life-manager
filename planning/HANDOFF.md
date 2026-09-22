# Handoff — mr-life-manager

You are continuing work on **mr-life-manager**, Charles Warloe's business that
teaches the practical systems of adulthood, derived from his friend Dave
Webster's real teaching documents. Repo lives at `/home/user/mr-life-manager`
(note: the shell may open in a different repo — `cd` in first). Branch: `main`,
pushes deploy via GitHub Actions.

## Read these before doing anything

- `CLAUDE.md` — the working agreement. The two rules that matter most:
  (1) You make changes and push; a bot does everything downstream (MailerLite,
  any live account). Never hand Charles manual steps or a chore list. End with
  a short plain-prose note for the bot. (2) Keep replies short by default.
- `content/README.md` — house style: depth rule, US English, email voice
  (full sentences, never clipped AI fragments), printables ≠ web pages, how to
  refer to Dave (first name, "decades," never his last name, mentioned only
  after the win).
- `planning/decisions.md` — the ADRs. ADR-014 completion converts; ADR-015 the
  win comes before the email ask; ADR-016 the follow-up sequence shrinks
  unconditionally.
- `source-material/INVENTORY.md` — every known Dave document and its state.
  Everything under `source-material/` is **verbatim, never edited, not even for
  spelling.** Interpretation goes in separate analysis files.

## Where things stand

The funnel is: one pain → one entry page → one action → one win → then the
email ask. Four entry pages are live and CI-complete (`first-night`, `guests`,
`one-room`, `underwater`), each with a phone "doing mode" (one step per screen,
Next/Back, `Why?` toggles) and a real one-page printable. Nine printables
render to PDF from HTML via headless Chromium with brand fonts embedded
(`.github/scripts/render_all_pdfs.py`). Four MailerLite email sequences are
active per owner confirmation on 2026-09-22. Each sends one PDF link in email 1:
`/print/the-week.pdf`. The entry-page action sheet is available before signup
and is never promised by email.

CI scripts enforce the invariants — run them before committing:
- `python3 .github/scripts/validate_repo.py` (HTML + internal links)
- `python3 .github/scripts/check_entry_pages.py` (each page has doing-mode,
  mode buttons, print rules, a signup tag, AND a matching `<tag>-sequence.md`)
- `python3 .github/scripts/check_pdfs_fresh.py` (PDF source hash unchanged)
- `python3 .github/scripts/build_site.py` (assemble `_site/`)
- `python3 .github/scripts/check_built_site.py` (generated metadata, routes and
  offer invariants; run after the build)

Production monitoring runs automatically after Pages deploys and every Monday
through `.github/workflows/check-live-site.yml`. It checks public pages and the
single promised PDF without submitting the MailerLite form.

## Open threads (nothing is blocking)

1. **Roommate-agreement material.** Searched Gmail 2026-09-22. Four documents
   found, none Dave's, all in `.doc/.docx` attachments the Gmail connector can
   list but not download. Best two: Charles's own 2024 Boise roommate agreement
   (thread `18fd06c6c2a00d54`, he calls it "the template") and Micah Stroh's
   2011 "tenant house rules" behavior policy (thread `1315e9526d510865`). To use
   either, Charles must "Add to Drive" from Gmail, then the Drive connector can
   read the text (same path used for Dave's four guides). Don't turn this into a
   chore list — offer it once. Note: there's already a `household-agreement`
   printable in the repo.
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

Do the work, run the CI scripts, commit, push to `main`. End your reply with a
2–3 line note telling the bot what changed and what (if anything) to update in
MailerLite. Commit trailer to use:

    Co-Authored-By: Claude Opus 4.8 <noreply@anthropic.com>
    Claude-Session: <session url>
