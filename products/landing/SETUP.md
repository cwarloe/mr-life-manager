# Landing Page — Setup

**Status:** Live on GitHub Pages, MailerLite wired on both pages (account
`2635985`, form `00ZwEr`). Custom domain **mrlifemanager.com** declared via the
`CNAME` file in this directory — **DNS records still need adding at the
registrar**, see below. Parent-facing variant at `/index-parents.html` uses the
same form.

`index.html` is the main page; `index-parents.html` is the parent-facing variant.
Both are static — no build step, no dependencies.

---

## Email provider: MailerLite

**ESP:** MailerLite  
**Account ID:** `2635985`  
**Embedded form ID:** `00ZwEr`

Both pages load MailerLite Universal once (script after `</style>`) and embed the
same form in the hero and closing signup sections via:

```html
<div class="ml-embedded" data-form="00ZwEr"></div>
```

Surrounding section copy is unchanged. Guide cards no longer link out — the
guides are the signup incentive.

## Then: the delivery sequence

Signing up has to actually deliver the three guides. Set up in MailerLite:

1. **Immediate** — the three guides (PDF exports of the checklist HTML files)
2. **Day 3** — one genuinely useful thing, no ask
3. **Day 7** — one more, and an invitation to reply and tell you what they're
   stuck on ← **this is the research channel**, and the most valuable email in
   the sequence

Keep the sequence teaching, not selling
([product-ladder.md](../../docs/business/product-ladder.md) rung 0: a free asset
that's really a sales pitch poisons everything above it).

## Remaining before launch

- [x] **PDF exports** — print each checklist HTML to PDF for the email attachments
- [x] **Deploy** — host the static page (Netlify, Cloudflare Pages, GitHub Pages,
      or Vercel) and point a domain at it
- [ ] Confirm both embedded forms submit successfully on phone and desktop
- [ ] Confirm the MailerLite welcome/automation sends all three guides, schedules
      the day-3/day-7 messages, honors unsubscribe, and routes replies correctly

## Guides on the page

The three guide cards describe the free assets but **do not link** to open
previews. Readers get the guides by signing up.

## Domain: mrlifemanager.com

The `CNAME` file in this directory tells GitHub Pages the custom domain. It has
to sit **inside the published directory** (`products/landing/`) because that's
what the deploy workflow uploads.

### DNS records to add at your registrar

**Apex — `mrlifemanager.com`** → four A records, all with host `@`:

```
185.199.108.153
185.199.109.153
185.199.110.153
185.199.111.153
```

Add the AAAA records too if your registrar supports IPv6:

```
2606:50c0:8000::153
2606:50c0:8001::153
2606:50c0:8002::153
2606:50c0:8003::153
```

**`www.mrlifemanager.com`** → one CNAME record:

```
host: www     value: cwarloe.github.io
```

> **Confirm these against the repo's own Settings → Pages screen.** After the
> CNAME file deploys, GitHub shows the exact records it expects for your domain
> right there — that's the authoritative list, and it beats any list written
> down elsewhere.

### After DNS propagates

1. **Settings → Pages** — the custom domain should show as verified. Propagation
   is usually minutes, occasionally a few hours.
2. **Tick "Enforce HTTPS."** It only becomes available once the certificate is
   issued, which can take another hour or so after verification. Don't skip it —
   a signup form on plain HTTP is a bad look and some browsers will say so.
3. Load both pages and submit a test address through the MailerLite form. Confirm
   it lands in the list **and** that the automation fires.

## Hosting

Static file. Netlify, Cloudflare Pages, GitHub Pages, or Vercel — all free at
this scale, all take a drag-and-drop or a repo connection.

You'll want a domain. Check availability alongside the trademark search that
[ADR-013](../../planning/decisions.md#adr-013--licensing-revised-free-to-use-never-free-to-sell)
made a prerequisite.

## Still missing

- [ ] **DNS records at the registrar** — the CNAME file alone does nothing until
      the domain points here. See *Domain* above.
- [ ] **Tick "Enforce HTTPS"** once the certificate is issued.
- [ ] **Confirm the guide PDFs are attached in MailerLite.** No PDFs are
      committed to this repo, so the day-0 email has nothing to send unless
      they're already uploaded on the MailerLite side. Verify by subscribing a
      test address and checking what actually arrives.
- [ ] Contact address in [PERMISSIONS.md](../../PERMISSIONS.md) and in the footer
- [ ] A photo of Dave, if he's willing — the Dave section carries the page and
      currently has no face
- [ ] Privacy note near the signup, once there's a real list
- [x] A parent-facing variant (`index-parents.html`), per the Phase 2 channel test in
      [roadmap.md](../../planning/roadmap.md)

## Copy decisions worth knowing

**The hero doesn't say "first apartment."** Per
[ADR-010](../../planning/decisions.md#adr-010--beachhead-keep-the-audience-change-the-payer),
the content serves first-timers but the marketing addresses anyone who was never
taught this. The specifics in the subhead (sheets, leases, cleaning products) do
the work of naming the audience without narrowing it to twenty-two-year-olds.

**Dave's quote is the hero of the page, not the headline.** The competitive
research found "nobody taught you this" is already used by the category's
winners — so the frame can't be the differentiator. Dave can. Nobody else has a
real person who says the thing is obvious and means it.

**The domains section shows the scope, with the covered ones marked.** Scope is
the actual differentiator: every competitor is single-domain. Showing thirteen
and highlighting seven is honest about where the material currently is.

**"Order isn't the point"** exists because hospitality is the destination
([principles.md](../../docs/vision/principles.md) §7), and no competitor ends
there. Everyone else stops at *clean*.
