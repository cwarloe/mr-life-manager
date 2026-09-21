# Handoff — doing-mode layout and print density

**Repo:** `github.com/cwarloe/mr-life-manager` · branch `main`
**Files:** `products/landing/guests.html` and `products/landing/first-night.html`
(identical structure — fix both, keep them consistent)

---

## Context

These two pages have two modes. **Reading mode** is the default and persuades
someone to start. **Doing mode** is entered by a button and shows one step at a
time, full screen, with the explanatory text hidden. Printing always produces a
one-page action sheet with no explanatory text at all.

That all works. Two layout problems remain.

## Problem 1 — the Next button falls below the fold

In doing mode, `.step.current` is `min-height:calc(100dvh - 11rem)` with its
content vertically centered. `.nav` (Back / Next step / "3 of 6" / exit link)
sits *after* it in flow, so on a phone the button is pushed off-screen and needs
a scroll — while a large band of empty space sits above it inside the card.

**Wanted:** the Next button is always visible without scrolling, pinned at the
bottom of the viewport. The step content uses the space that's currently wasted,
and the type gets bigger as a result — this is a document read at arm's length
with wet hands.

**Constraints:**
- `100vh` is wrong on mobile browsers (toolbars). `100dvh` is already used, keep
  that approach and keep the `@supports not (height:100dvh)` fallback.
- Respect the safe area on notched phones: `env(safe-area-inset-bottom)`.
- Must degrade sanely on desktop, where the viewport is short and wide.
- Card content should scroll internally if a step is genuinely too tall, rather
  than pushing the button away.

A fixed/sticky footer for `.nav` plus a flex column layout on the card is the
obvious approach, but use your judgement.

## Problem 2 — the printed sheet wastes most of the page

The print stylesheet (second `@media print` block in each file) shrinks
everything to guarantee one page: `body{font-size:10pt}`, step headings at
`11.5pt`, `.do` at `9.5pt`. The result is one page of small type with a large
empty area at the bottom.

**Wanted:** fill the sheet. Type as large as fits while staying on **one page**.
Roughly: step headings in the mid-to-high teens (pt), body around 11–13pt,
generous spacing between steps.

**Constraints:**
- **Must remain exactly one printed page** for both files. This is the hard
  constraint — verify, don't assume.
- `@page{size:Letter}` stays. US audience.
- The explanatory text (`.why`), the `Why?` buttons, `.nav`, `.done`, `.fork`,
  the brand story and the signup must stay hidden in print. Do not reintroduce
  them. There is history here: an earlier `-webkit-line-clamp` rule on `.why`
  silently re-enabled `display` and leaked the explanations into the PDF.
- All steps must print, not just the current one — `.step{display:block
  !important}` exists for that reason.
- Header, the framing block, the safety note and the closing block stay.

## Do not change

- The reading-mode page. Only doing mode and print.
- Any wording. Layout and CSS only.
- The two-mode JavaScript behavior (which step is current, Back/Next, the `Why?`
  toggles, the exit links).

## Verify before you commit

```bash
python3 .github/scripts/validate_repo.py       # HTML + internal links
python3 .github/scripts/render_pdf.py products/landing/guests.html /tmp/g.pdf
python3 .github/scripts/render_pdf.py products/landing/first-night.html /tmp/f.pdf
```

Then confirm, for **both** PDFs:

1. Exactly one page.
2. None of the explanatory text is present. For `guests.html`, the strings
   `Smell is what people register`, `Why this is first` and `This is a trick`
   must all be absent from the PDF bytes.
3. Type is visibly larger than before and the sheet is reasonably full.

Also check doing mode at a narrow viewport (≈390×670) with the Next button
visible without scrolling, on the first step and the longest step.

`render_pdf.py` embeds the brand fonts and refuses to write a PDF without them,
so a font failure will surface as an error rather than silently.

## Commit

Small, focused commits. Push to `main` — the site deploys automatically via
GitHub Actions. No other systems need touching.
