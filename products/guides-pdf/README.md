# Guide PDFs

Print-ready exports of the free-tier guides. **These are what MailerLite
attaches to the day-0 welcome email.**

| File | Pages | Source |
|---|---|---|
| `first-apartment-checklist.pdf` | 7 | [source](../checklists/first-apartment/first-apartment-checklist.html) |
| `how-often-should-i.pdf` | 9 | [source](../checklists/how-often/how-often-should-i.html) |
| `cleaning-supply-starter-list.pdf` | 5 | [source](../checklists/cleaning-supplies/cleaning-supply-starter-list.html) |
| `household-agreement.pdf` | 7 | [source](../worksheets/household-agreement/household-agreement.html) |

The household agreement isn't in the day-0 email — it's a later asset. Exported
here so it's ready.

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
