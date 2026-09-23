# Business Operations

The smallest operating system that keeps Mr. Life Manager trustworthy without
turning it into a full-time administrative job.

**Operating constraint:** maximize useful outcomes and revenue per owner-hour,
not the number of products, platforms, or channels.

## Current operating state

| System | Current use | Source of truth |
|---|---|---|
| GitHub Pages | Public website and PDFs | Repository `main` and deployment workflow |
| Cloudflare | DNS for `mrlifemanager.com` | Private account; do not store credentials here |
| Zoho | `hello@mrlifemanager.com` mailbox | Private account |
| MailerLite | One form, four route groups, four three-email automations | [`MAILERLITE-SETUP.md`](../products/landing/emails/MAILERLITE-SETUP.md) |
| GitHub Actions | Build, validation, deployment and public-site monitoring | [`.github/workflows/`](../.github/workflows/) |

**Email state reported by owner 2026-09-22:** all four automations are active.
Email 1 contains one PDF link, [`The Week`](https://mrlifemanager.com/print/the-week.pdf).
The entry-page action and print option happen before signup.

**Last private account-level funnel test:** 2026-09-22 — **pass** for all four entry routes (confirm → correct `entry-*` group → Email 1 with [`The Week`](https://mrlifemanager.com/print/the-week.pdf)). Test subscribers removed. Guests/first-night verified earlier the same week; underwater/one-room completed on this date.

**Completion measurement:** each entry page now ends at a distinct
`/finished-*.html` page after the reader explicitly chooses “I finished.” Count
those page visits as a directional completion measure. They prove the reader
reached and acknowledged the end state, not that every physical action occurred.

**Paid-demand test:** `/first-place.html` names a planned $39 founding price and
collects no-charge reservations as prefilled emails to the monitored inbox. A
reservation is not a sale and must never be reported as revenue or paid demand.
The optional source label in the subject records the route that produced the
message; it is attribution, not identity tracking.

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
| Before broader email distribution | Recorded four-route delivery test; DMARC monitoring; valid postal footer; privacy text matches the live account |
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
- the homepage, four entry pages and privacy page;
- the MailerLite form marker and page-specific `guide` value;
- the single promised PDF; and
- required privacy and contact links.

That catches public breakage. It cannot see MailerLite's private groups or
delivered inbox messages. An account operator performs the controlled four-route
test and records only its date and pass/fail result here—never test addresses.

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
- Connect privacy-first visitor analytics, then update the privacy page to name
  the service actually used.
- Verify the domain in Google Search Console and submit `/sitemap.xml`.
- Execute the Dave rights/compensation agreement outside this public repository.
- Complete the name/trademark and Idaho assumed-name/entity decisions before
  accepting payment under the brand.
