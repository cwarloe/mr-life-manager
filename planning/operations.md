# Business Operations

The smallest operating system that keeps Mr. Life Manager trustworthy without
turning it into a full-time administrative job.

**Operating constraint:** maximize useful outcomes and revenue per owner-hour,
not the number of products, platforms, or channels.

## Waiting on the bot

**One list of everything that needs a live account.** Each item links to its
full steps. Remove an item when it's done; add one when a change needs account
work.

| Item | Status | Steps |
|---|---|---|
| **Office page emails** | **To do (approved by Charles 2026-10-26)** | Create group `entry-office` in MailerLite and set up the 3-email automation matching [`office-sequence.md`](../products/landing/emails/office-sequence.md). Rule: trigger on group join, immediate email 1, day 3 email 2, day 7 email 3. |
| **Google Search Console** | Not verified | Needs Charles's Google login: verify the domain and submit `/sitemap.xml`. See [External one-time items](#external-one-time-items). |
| **QR codes for fliers** | When fliers are made | Each printed code gets its own tag, `?from=qr-<place>-<page>`. Format and examples in the [deferred-win architecture](deferred-win-architecture.md#comparing-pages-and-places). A code aimed at an audience points to its landing page, e.g. `mrlifemanager.com/career?from=qr-<place>` (also `/students`, `/military`; see [audience pages](../products/landing/audiences/README.md)). Record each posted code in the [audience tracker](../docs/business/audience-tracker.md). |

Nothing else needs a live account right now. MailerLite does **not** need
changes for the "Not right now" flow, the new underwater headline, or the
removal of Dave's name from the task pages: the web addresses, tags and email
copy are unchanged.

## Current operating state

| System | Current use | Source of truth |
|---|---|---|
| GitHub Pages | Public website and PDFs | Repository `main` and deployment workflow |
| Cloudflare | DNS for `mrlifemanager.com` | Private account; do not store credentials here |
| Zoho | `hello@mrlifemanager.com` mailbox | Private account |
| MailerLite | One form, four route groups, four three-email automations; the office door's `entry-office` group and automation are not created yet | [`MAILERLITE-SETUP.md`](../products/landing/emails/MAILERLITE-SETUP.md) |
| GitHub Actions | Build, validation, deployment and public-site monitoring | [`.github/workflows/`](../.github/workflows/) |

**Email state reported by owner 2026-09-22:** all four automations are active.
Email 1 contains one PDF link, [`The Week`](https://mrlifemanager.com/print/the-week.pdf).
The entry-page action and print option happen before signup.

**Office door (added 2026-10-06):** deliberate one-off (Charles, 2026-10-08) —
direct-link only. Its `entry-office` group and automation are not created yet,
so it has not had a route test. For a one-off, ask Charles whether a MailerLite
group is wanted before wiring one.

**Last private account-level funnel test:** 2026-09-22 — **pass** for all four entry routes (confirm → correct `entry-*` group → Email 1 with [`The Week`](https://mrlifemanager.com/print/the-week.pdf)). Test subscribers removed. Guests/first-night verified earlier the same week; underwater/one-room completed on this date.

**Completion measurement:** each entry page now ends at a distinct
`/finished-*.html` page after the reader explicitly chooses “I finished.” Count
those page visits as a directional completion measure. They prove the reader
reached and acknowledged the end state, not that every physical action occurred.

**Paid-demand test:** none live. Per ADR-020 (Accepted) a paid guide is only
offered after a free win; no reservation or price page is running.

## The cadence

### Twice weekly — support block, 15 minutes

- Read replies to `hello@mrlifemanager.com`.
- Answer the person; do not turn one question into a new system.
- Record a repeated problem only after it appears at least twice.
- Handle deletion, unsubscribe or delivery problems first.

Support is handled in blocks, not continuously. No help desk is needed until the
inbox repeatedly exceeds the block.

### Weekly — growth block, 45 minutes

Choose **one** distribution experiment: one warm-network share, church or campus
contact, useful forum contribution, or short demonstration. Record the source
and the result in [`monthly-scorecard.md`](monthly-scorecard.md).

Use `/partners.html?from=church`, `/partners.html?from=campus`, or
`/partners.html?from=mentor` when one of those routes is the experiment. The
page asks for a five-person learning pilot, not an institutional purchase.

Do not build another product to avoid this block. If there are no visitors, the
problem is distribution. If there are visitors but no action or signup, the
problem is the page or offer.

### Monthly — operating review, 45 minutes

1. Complete one row in the scorecard.
2. Review MailerLite deliveries, bounces, unsubscribes, complaints and replies.
3. Review business expenses and save receipts outside this public repository.
4. Review support minutes. If administration exceeds 20% of available business
   time for two months, remove a channel, offer or recurring obligation.
5. Pull one item from P0/P1; do not add a second active item.

Open rates are not a decision metric. They are distorted by privacy prefetching,
and [ADR-016](decisions.md#adr-016--the-sequence-shrinks-unconditionally)
forbids branching on them.

## Trigger gates

These obligations stay dormant until their trigger occurs.

| Trigger | Activate then |
|---|---|
| Before broader email distribution | Recorded delivery test for every entry route; DMARC monitoring; valid postal footer; privacy text matches the live account |
| Before distributing the founding-offer page | Monitored `hello@` inbox; privacy text matches the live page; a simple count of unique reservation senders |
| Before the first sale | Checkout terms; refund policy; assumed-name/entity check; separate transaction records; tax and bookkeeping decision |
| After ten customers | FAQ from actual questions; three saved support replies; product version log |
| Before coaching | Written agreement, cancellation policy, scheduling boundary and insurance review |
| Before institutional sales | Contract and licensing review, W-9/invoicing process, accessibility check and one pilot case study |
| Before hiring help | Least-privilege access, contributor/IP agreement and a documented handoff |
| Before a membership | Proven recurring demand, support-capacity calculation, cancellation handling and content cadence |

No app, inventory, community, membership or custom institutional work is added
without its trigger. Custom work must be priced to cover its administrative
burden.

## Public funnel health

The scheduled live-site workflow checks:

- HTTPS and canonical redirects;
- the homepage, every entry page in `site_catalog.py` and the privacy page;
- the MailerLite form marker and page-specific `guide` value;
- the single promised PDF;
- required privacy and contact links; and
- `/sitemap.xml` and `/robots.txt` (sitemap lists the public doors; completion pages stay out).

That catches public breakage. It cannot see MailerLite's private groups or
delivered inbox messages. An account operator performs the controlled test of
every entry route and records only its date and pass/fail result here—never
test addresses.

## Incident response

| Symptom | First response |
|---|---|
| Site or PDF fails | Check the latest Pages deployment, then DNS. Roll forward with a corrected commit; do not edit generated `_site/`. |
| Form fails to render | Confirm MailerLite's universal script and form ID. The page's email fallback remains available. |
| Subscribers enter `entry-unknown` | Pause affected automations and repair `guide` routing before resuming distribution. |
| Wrong email or dead link is sent | Pause the automation, correct the source copy and MailerLite version, then run one controlled route test. |
| Deliverability drops | Pause broad sending; check SPF, DKIM, DMARC, complaint rate and sender alignment. |
| Account access is lost | Use the private recovery record; rotate affected credentials and review account activity. |

## Continuity and security

Maintain one **private** recovery record for the registrar, Cloudflare, GitHub,
Zoho and MailerLite. It should name the owner, renewal method, 2FA method,
recovery-code location and recovery email. Never commit credentials, recovery
codes, subscriber exports or signed agreements to this public repository.

Confirm domain auto-renewal and account recovery twice a year. Add a second
operator only when there is a real continuity need; do not share a password.

## External one-time items

These require an authenticated account or a human/legal decision and are not
repository work:

- DMARC monitoring TXT added 2026-09-22 (`p=none`, reports to `hello@`). Confirm
  Zoho and MailerLite alignment before enforcing quarantine or reject. SPF,
  MailerLite verification and DKIM were already resolved.
- Postal address in MailerLite footers confirmed 2026-09-22 (6621 West Holiday
  Drive, Boise).
- Privacy-first visitor analytics: **Umami Cloud, switched on 2026-10-26**
  (account under charles.warloe@gmail.com, Hobby plan). Replaces the earlier default, Cloudflare Web
  Analytics, which [does not record query strings](https://developers.cloudflare.com/web-analytics/faq/)
  (so it would drop the `from=` QR tags) and has no custom events (so it can't
  tell "start now" from "pick a time").
  - **Plan:** Hobby, free: 1 website, 100,000 events a month, 6 months of
    history ([pricing](https://umami.is/pricing), checked 2026-10-26). Record
    the monthly scorecard before data ages out.
  - **Commercial use is allowed.** Terms checked 2026-10-26: "for any lawful
    personal or business purpose, including commercial purposes" and "nothing in
    these Legal Terms restricts commercial use of the Services"
    ([terms](https://umami.is/terms)). An older version seen in search results
    said "personal, non-commercial use or internal business purpose"; recheck if
    the terms change.
  - **To switch it on (one step):** create the Umami Cloud account, add the
    site `mrlifemanager.com`, and paste its website ID into `UMAMI_WEBSITE_ID`
    in `.github/scripts/site_catalog.py`. The build then adds the script to
    every page and shows the analytics paragraph on the privacy page;
    `check_built_site.py` fails if those two ever disagree. Tracking only runs
    on `mrlifemanager.com`, not in tests or previews.
  - **Events sent** (no cookies, nothing personal; each carries `page` and the
    QR `from` tag): `start-now`, `not-right-now`, `time-picked` (choice),
    `calendar-added` (ics or google), `shared-with-checker`, `came-back` (moved,
    step), `started-from-reminder`, `rescheduled` (mid-task or on-return, step,
    moved), `stopped-at-limit`, `let-go`, `print`, `reached-end` (path),
    `finished` (path).
- Google Search Console: **not verified in the console** as of 2026-09-22.
  Public precheck **pass**: `/`, `/first-night.html`, `/guests.html`,
  `/underwater.html`, `/one-room.html`, and `/privacy.html` return HTTPS 200;
  `/sitemap.xml` is live and lists those URLs; `/robots.txt` points at the
  sitemap. Console verify + sitemap submit still need a Google login.
- Execute the Dave rights/compensation agreement outside this public repository.
- Complete the Idaho assumed-name/entity decisions before accepting payment
  under the brand. Owner closed the name-check for "Mr. Life Manager" 2026-09-23.
