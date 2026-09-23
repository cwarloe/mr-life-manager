# Landing Page — Setup

**Status (2026-09-21):** The public site is live at
[https://mrlifemanager.com](https://mrlifemanager.com). HTTPS is on. HTTP
redirects. `www` redirects to the apex.

The homepage is a **router**. It does not capture email. Signup lives on the
entry pages, after the action
([ADR-015](../../planning/decisions.md#adr-015--the-win-comes-before-the-email)).

| URL | What |
|---|---|
| `/` | Router — pick the pain that is true today |
| `/first-night.html` | Entry page + signup |
| `/guests.html` | Entry page + signup |
| `/underwater.html` | Entry page + signup |
| `/one-room.html` | Entry page + signup |
| `/index-parents.html` | Parent page — send them a door, no form |
| `/guides/` | Archive of the free guides |
| `/guides/<slug>.html` | Each guide |
| `/print/` | Index of print-ready PDFs |
| `/print/<slug>.pdf` | A specific printable |
| `/finished-<door>.html` | No-index completion destination for each entry page |
| `/first-place.html` | No-charge reservation for the planned $39 founding offer |
| `/privacy.html` | What an email is used for |

`index.html` is the main page. `index-parents.html` is the parent-facing
variant. It does **not** collect email. A parent forwards a door.

The site is assembled by `.github/scripts/build_site.py`. It copies everything
in this folder except `SETUP.md` and subdirectories (`briefs/`, `emails/`),
publishes the guides from `products/`, and copies PDFs from
`products/guides-pdf/` to `/print/`.

```bash
python3 .github/scripts/build_site.py   # writes _site/ (gitignored)
```

## MailerLite

**ESP:** MailerLite  
**Account ID:** `2635985`  
**Embedded form ID:** `00ZwEr`

The form is embedded on all four entry pages and their four completion pages.
Do not put it back on the homepage or the *First Place* founding-offer page. The
completion pages reuse the originating door tag, so the reader receives the
same three-email sequence whether they signed up in reading mode or immediately
after finishing in doing mode.

The intended account state is documented in
[`emails/MAILERLITE-SETUP.md`](emails/MAILERLITE-SETUP.md). Do **not** wire
[`emails/welcome-sequence.md`](emails/welcome-sequence.md) — that draft is
withdrawn. Live copy is in the four entry-specific sequence files.

The owner reported all four automations active on 2026-09-22. Each sends one PDF
link in email 1 — `/print/the-week.pdf` — not a copy of the action page. The
action and its print option have already been delivered before signup.

The founding-offer page uses a prefilled email to `hello@mrlifemanager.com`.
That keeps the demand test live without a fifth automation or a risk that a
reservation receives an unrelated free sequence. Treat each sent message as a
reservation, not revenue.

The repository's live-site monitor proves that the public pages, route tags,
form containers and PDF are present. Private MailerLite routing and delivery
still require a controlled account-level test; record the last result in
[`planning/operations.md`](../../planning/operations.md).

## Domain

DNS already points at GitHub Pages (`185.199.108–111.153`). The `CNAME` file
in this directory must stay in the published root.

If the certificate or HTTPS checkbox ever falls off: Settings → Pages →
confirm `mrlifemanager.com` → Enforce HTTPS.

## External operating items

- [ ] Record a four-page MailerLite delivery test and footer/unsubscribe check
- [x] Confirm SPF/DKIM and MailerLite domain verification (DNS checked 2026-09-22)
- [ ] Add DMARC in monitoring mode, then verify MailerLite and Zoho alignment
- [ ] Add privacy-first visitor analytics and Search Console verification
- [ ] A photo of Dave, if he's willing
- [ ] USPTO / name check
