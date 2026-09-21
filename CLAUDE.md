# Working agreement

## Division of labor

**Claude makes the changes and pushes to GitHub. A bot does everything
downstream.** The bot handles MailerLite, verification, and anything that
touches a live account.

So:

- **Do the work, commit it, push it.** GitHub Actions deploys the site on push
  to `main`.
- **End with a short prompt for the bot** — a few lines, plain prose, saying
  what changed and what to update. Not a checklist, not a runbook.
- **Never hand Charles manual steps.** No "open this in a browser," no "send
  yourself a test signup," no "inspect this element and tell me what it says."
  If something genuinely can't be verified from here, either remove the
  uncertainty in code or let the bot find out.

The failure mode to avoid: turning a finished piece of work into a list of
chores for him. He has a bot precisely so that doesn't happen.

## How to communicate

- **Concise.** He skims long replies. Half the length is usually right.
- **One question at a time, and only when the answer changes what gets built.**
  Stacked questions are worse than a wrong assumption stated out loud.
- **Prefer eliminating a question to asking it.** When the page had to guess at
  MailerLite's field naming, the right fix was sending both names, not asking
  him to go look.
- **Push back plainly** when something's wrong, then do the work. He wants a
  peer, not agreement.
- **Say what's untested.** Most decisions here are reasoning, not evidence, and
  should be labelled that way.

## Standing rules already written down

Don't re-derive these — read them:

- [`content/README.md`](content/README.md) — depth rule, US English, email
  voice (full sentences, never clipped fragments), how printables differ from
  web pages, how to refer to Dave
- [`planning/decisions.md`](planning/decisions.md) — the ADRs. ADR-014
  (completion converts), ADR-015 (the win comes before the email), ADR-016
  (the sequence shrinks unconditionally) govern most product decisions
- [`docs/business/commerce-rules.md`](docs/business/commerce-rules.md) —
  affiliate and pricing rules
- [`source-material/`](source-material/INVENTORY.md) — Dave's original
  documents. **Verbatim, never edited**, not even for spelling

## Mechanics

- `python3 .github/scripts/build_site.py` — assemble `_site/`
- `python3 .github/scripts/validate_repo.py` — HTML + internal links; run before
  committing
- `python3 .github/scripts/render_all_pdfs.py` — regenerate printables with the
  brand fonts embedded; it refuses to write a PDF missing them
- Entry-page action sheets are **not** committed as PDFs. They print from each
  page's own stylesheet, so the sheet can't drift from the page.
