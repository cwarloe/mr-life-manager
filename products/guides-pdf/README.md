# Guide PDFs

Print-ready exports, published at `/print/`. Every entry sequence links one of
them — `the-week.pdf` — in email 1 (see [SETUP.md](../landing/SETUP.md#mailerlite));
the rest are archive, per
[ADR-015](../../planning/decisions.md#adr-015--the-win-comes-before-the-email).

| File | Pages | Source |
|---|---|---|
| `the-week.pdf` | 1 | [source](../print/the-week.html) |
| `first-apartment-checklist.pdf` | 4 | [source](../checklists/first-apartment/first-apartment-checklist.html) |
| `how-often-should-i.pdf` | 3 | [source](../checklists/how-often/how-often-should-i.html) |
| `cleaning-supply-starter-list.pdf` | 3 | [source](../checklists/cleaning-supplies/cleaning-supply-starter-list.html) |
| `what-is-this-room-for.pdf` | 2 | [source](../checklists/room-for/what-is-this-room-for.html) |
| `the-light-is-the-problem.pdf` | 2 | [source](../checklists/light/the-light-is-the-problem.html) |
| `laundry-solved.pdf` | 4 | [source](../checklists/laundry/laundry-solved.html) |
| `ten-meals.pdf` | 4 | [source](../checklists/ten-meals/ten-meals.html) |
| `household-agreement.pdf` | 5 | [source](../worksheets/household-agreement/household-agreement.html) |
| `partner-pilot.pdf` | 4 | [generator](../../.github/scripts/generate_share_assets.py) |

Entry pages have no PDF: the reader prints them from the page itself.

## Regenerating

**The HTML is the source. Never edit a PDF.** After changing any guide:

```bash
python3 .github/scripts/render_all_pdfs.py
```

It embeds the brand fonts, so the render doesn't depend on Google Fonts, and
records source hashes that
[`check_pdfs_fresh.py`](../../.github/scripts/check_pdfs_fresh.py) uses to fail CI
when a PDF falls behind its HTML.
