# Landing Page — Setup

**Status:** Draft 1, 2026-09-09. Copy and design done. **Not connected to anything.**

`index.html` is the page. It's static — no build step, no dependencies.

---

## The one thing you have to do: pick an email provider

The page has **two identical signup forms** (hero and footer). Both have an empty
`action=""` marked with a comment block. Paste your provider's form endpoint into
both and the page works.

Candidates, all with free tiers at this size:

| | Notes |
|---|---|
| **Buttondown** | Simplest. Plain-text, writer-first, cheap. Good fit for the voice. |
| **ConvertKit / Kit** | Best automation for a free-guide-then-sequence funnel. Heavier. |
| **Beehiiv** | Strong growth tooling; more publication-shaped than list-shaped. |
| **MailerLite** | Generous free tier, decent automation. |

**Recommendation: Buttondown or Kit.** Buttondown if you want to start writing
this week; Kit if you know you want the delivery sequence automated from day one.

Whichever you pick, the only change to this file is the `action` URL — the field
is already named `email_address`, which most providers accept. Check your
provider's expected field name and adjust if it differs.

## Then: the delivery sequence

Signing up has to actually deliver the three guides. Set up:

1. **Immediate** — the three guides (PDF exports of the checklist HTML files)
2. **Day 3** — one genuinely useful thing, no ask
3. **Day 7** — one more, and an invitation to reply and tell you what they're
   stuck on ← **this is the research channel**, and the most valuable email in
   the sequence

Keep the sequence teaching, not selling
([product-ladder.md](../../docs/business/product-ladder.md) rung 0: a free asset
that's really a sales pitch poisons everything above it).

## Guides: preview vs. production

The three guide cards currently link to the published artifact previews, so the
page can be clicked through end to end. **In production they shouldn't link
anywhere** — the guides are what you get *for* signing up. Either remove the
hrefs or point them at a post-signup delivery page.

Print each checklist HTML to PDF for the email attachments.

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
- [ ] A parent-facing variant, per the Phase 2 channel test in
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
