# MailerLite — operating specification

**Account:** `2635985` · **Embedded form:** `00ZwEr`
**Status reported by owner 2026-09-22:** four automations are active. Each
sequence sends one PDF link in email 1 —
[`The Week`](https://mrlifemanager.com/print/the-week.pdf) — followed by two
smaller emails and then stops. The entry-page action sheet is available before
signup and is never promised by email.

This file describes the intended live state. The repository can verify the
public pages and PDF, but it cannot inspect MailerLite's private automation
state. If the account and this file disagree, pause broad distribution until the
account has been brought back to this specification.

## Routing

The same form is embedded after the completed action on all four pages. Page
code sends the tag under both `fields[guide]` and `guide` because MailerLite's
rendered field naming has varied.

| Entry page | `guide` value | Group | Sequence source |
|---|---|---|---|
| `/first-night.html` | `first-night` | `entry-first-night` | [`first-night-sequence.md`](first-night-sequence.md) |
| `/guests.html` | `guests` | `entry-guests` | [`guests-sequence.md`](guests-sequence.md) |
| `/underwater.html` | `underwater` | `entry-underwater` | [`underwater-sequence.md`](underwater-sequence.md) |
| `/one-room.html` | `one-room` | `entry-one-room` | [`one-room-sequence.md`](one-room-sequence.md) |
| missing or unknown | anything else | `entry-unknown` | none; investigate |

`entry-unknown` is an alarm. It should stay empty.

## Sequence invariant

Each automation triggers when a subscriber joins its matching group:

| Email | Timing | Purpose |
|---|---|---|
| 1 | Immediately | Link `The Week`; add one entry-specific action |
| 2 | Three days later | Ask less than email 1 |
| 3 | Four days later | One easy reply question, then stop |

Settings for all four:

- Allow re-entry: **off**
- Resend to unopens: **off**
- Stop on reply: **on**, if the plan supports it
- Sender: **Charles**, from an address that accepts replies
- No fourth email, promotion, win-back, or behavior-based branch

The copy files are the source of truth. The withdrawn
[`welcome-sequence.md`](welcome-sequence.md) must never be reactivated.

## Delivery promise

The website gives the immediate task and print option before signup. Email 1
delivers only:

`https://mrlifemanager.com/print/the-week.pdf`

It does not promise or deliver a second PDF. This distinction implements
[ADR-015](../../../planning/decisions.md#adr-015--the-win-comes-before-the-email):
the reader has already acted; email supplies the reusable maintenance system.

## Operational verification

The public-site monitor verifies that all four pages load, contain the correct
form and route tag, and that `The Week` resolves as a PDF. A controlled external
account check is still the only way to prove private MailerLite behavior:

- each tag reaches its matching group;
- `entry-unknown` remains empty;
- email 1 arrives and its single PDF link works;
- replies reach the monitored inbox;
- unsubscribe and the required footer work;
- email 2 and email 3 follow their delays; and
- nothing arrives after email 3.

Record the date and result in
[`planning/operations.md`](../../../planning/operations.md) when that
account-level check is performed. Remove test subscribers afterward so the
operating numbers remain honest.

## Domain state

Direct DNS checks on 2026-09-22 found MailerLite domain verification, SPF for
MailerLite and Zoho, and MailerLite DKIM selectors. No DMARC record resolved.
DMARC is the remaining authentication task; begin in monitoring mode and do not
enforce quarantine or rejection until both MailerLite and Zoho alignment have
been confirmed.
