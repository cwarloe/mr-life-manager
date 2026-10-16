# Referral QR Placement

**Status:** Proposed 2026-09-28. Not adopted; nothing here is live.
**Scope:** Where a "send this to someone" link or QR code may appear.

Governed by [principle 11](../vision/principles.md) and
[commerce-rules.md](commerce-rules.md). Where this page conflicts with either,
they win.

**Today:** one QR source.
[`generate_share_assets.py`](../../.github/scripts/generate_share_assets.py)
prints four into `/print/partner-pilot.pdf`, each encoding
`https://mrlifemanager.com/partners.html?from=` plus `parent`, `mentor`,
`church` or `campus`. No other printable, page, or email carries one.

## Rule

A referral appears only where the reader has no open ask left, and it pays
nothing: no rewards, credits, or discounts. It must stay "defensible if no
commission existed" ([commerce-rules.md](commerce-rules.md)). The wording
offers and never nudges (principle 8, *Dignity, not shame*).

## Placements, ranked

1. **Printable footers.** A small QR to `https://mrlifemanager.com/` beside
   the existing "Free to copy and share" credit on The Week and the free
   guides. The sheet's action is already on paper, so the footer competes
   with nothing. Principle 11. Nightly Audit Engineer.
2. **After the signup is sent.** One line in the form's success message:
   "Know someone starting out? Send them the page you just used." A plain
   link. Principle 11: the one ask is already answered. Mailer Bot.
3. **Email footer.** One static line, "Free to share: mrlifemanager.com," with
   no QR, since the reader is already on a screen. Principle 9, *Simple enough
   to actually keep*. Mailer Bot.

**Not here:** entry pages, the completion page before signup, the *First
Place* page, email bodies.

## Conflicts / open questions

- [`the-week.html`](../../products/print/the-week.html): "No links, no
  navigation, nothing that assumes a screen." A QR assumes a phone.
- The pilot handout has no "with credit" line, unlike the other printables.
- [`check_built_site.py`](../../.github/scripts/check_built_site.py) fails a
  completion page containing `navigator.share`, so placement 2 stays a plain
  link.

Charles approves each placement before anyone implements it.
