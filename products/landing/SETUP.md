# Landing Page — Setup

**Status:** MailerLite wired on both pages (account `2635985`, form `00ZwEr`). Copy and
design done. PDF exports and main deploy are done. Parent-facing variant is live at
`/index-parents.html` (same MailerLite form as `index.html`).

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
- [ ] Confirm the MailerLite welcome/automation actually sends the three guides

## Guides on the page

The three guide cards describe the free assets but **do not link** to open
previews. Readers get the guides by signing up.

## Hosting

Static file. Netlify, Cloudflare Pages, GitHub Pages, or Vercel — all free at
this scale, all take a drag-and-drop or a repo connection.

You'll want a domain. Check availability alongside the trademark search that
[ADR-013](../../planning/decisions.md#adr-013--licensing-revised-free-to-use-never-free-to-sell)
made a prerequisite.

## Still missing

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
