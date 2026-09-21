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
| `/index-parents.html` | Parent page — send them a door, no form |
| `/guides/` | Archive of the free guides |
| `/guides/<slug>.html` | Each guide |
| `/print/` | Index of print-ready PDFs |
| `/print/<slug>.pdf` | A specific printable |
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

The form is embedded on `/first-night.html` and `/guests.html` only. Do not
put it back on the homepage.

Wiring the sequences is a separate job. Follow
[`emails/MAILERLITE-SETUP.md`](emails/MAILERLITE-SETUP.md). Do **not** wire
[`emails/welcome-sequence.md`](emails/welcome-sequence.md) — that draft is
withdrawn. Live copy is `first-night-sequence.md` and `guests-sequence.md`.

A signup is not proven until a test address from each entry page receives the
printable for **that** page and nothing else.

## Domain

DNS already points at GitHub Pages (`185.199.108–111.153`). The `CNAME` file
in this directory must stay in the published root.

If the certificate or HTTPS checkbox ever falls off: Settings → Pages →
confirm `mrlifemanager.com` → Enforce HTTPS.

## Still missing

- [ ] Confirm a test signup on first-night and on guests
- [ ] Confirm SPF/DKIM for the sending domain
- [ ] A photo of Dave, if he's willing
- [ ] USPTO / name check
