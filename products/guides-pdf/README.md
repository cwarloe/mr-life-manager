# Guide PDFs

Print-ready exports of the free-tier guides. **These are what MailerLite
attaches to the day-0 welcome email.**

| File | Pages | Source |
|---|---|---|
| `first-apartment-checklist.pdf` | 7 | [source](../checklists/first-apartment/first-apartment-checklist.html) |
| `how-often-should-i.pdf` | 9 | [source](../checklists/how-often/how-often-should-i.html) |
| `cleaning-supply-starter-list.pdf` | 6 | [source](../checklists/cleaning-supplies/cleaning-supply-starter-list.html) |
| `household-agreement.pdf` | 7 | [source](../worksheets/household-agreement/household-agreement.html) |
| `laundry-solved.pdf` | 6 | [source](../checklists/laundry/laundry-solved.html) |
| `ten-meals.pdf` | 6 | [source](../checklists/ten-meals/ten-meals.html) |

Only the first three go in the day-0 email. The household agreement, laundry and
ten-meals guides are later assets — good candidates for the day-3 and day-7
emails, or for a second signup incentive once the list is running.

## Regenerating

**The HTML is the source. Never edit a PDF.** After changing any guide, re-export:

```bash
chrome --headless --disable-gpu --no-sandbox --no-pdf-header-footer \
  --print-to-pdf="products/guides-pdf/NAME.pdf" \
  --virtual-time-budget=8000 \
  "file://$PWD/path/to/guide.html"
```

`--no-pdf-header-footer` removes the browser's default URL and date chrome.
`--virtual-time-budget` gives the Google Fonts request time to land — without it
the export falls back to system fonts and looks wrong.

Each guide's print stylesheet already drops it to black-on-white and holds
sections together across page breaks, so the PDF is genuinely print-ready rather
than a screenshot of a web page.
