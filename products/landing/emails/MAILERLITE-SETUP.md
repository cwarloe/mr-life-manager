# MailerLite — wiring the two sequences

**Account:** `2635985` · **Form:** `00ZwEr` (embedded on both entry pages)
**Written 2026-09-20.** Nothing below is configured yet.

> **Handing this to an agent instead?**
> [`MAILERLITE-AGENT-PROMPT.md`](MAILERLITE-AGENT-PROMPT.md) is the same job
> written as a runnable prompt, with the email copy embedded so nothing gets
> improvised. This file stays the source of truth if the two disagree.

Both entry pages already inject a hidden field on submit:

| Page | Hidden field |
|---|---|
| `/first-night.html` | `guide` = `first-night` |
| `/guests.html` | `guide` = `guests` |

That field is the only thing that decides which sequence someone gets. Everything
else follows from it.

---

## 0. Authenticate the sending domain — do this first

**Settings → Domains → Authenticate.** Add the SPF and DKIM records MailerLite
gives you to the DNS for `mrlifemanager.com`, in the same place the site's A
records live.

This is the step people skip, and skipping it is why a sequence that works
perfectly ends up in spam. Nothing below matters if the mail doesn't arrive.
Allow up to a day for DNS, and don't send anything real until MailerLite shows
the domain verified.

Also confirm automations are available on the plan you're on before building
them — that varies, and it's better to find out now than after writing them in.

## 1. Create the custom field

**Subscribers → Fields → Create field.** Type **Text**, key `guide`.

**A mismatch here fails silently** — signups keep working, they just all arrive
with no `guide` value and therefore no sequence. That is the single most likely
way this setup breaks, and it breaks quietly.

> **Known risk, handled in the page code.** MailerLite names its embedded-form
> inputs `fields[email]`, not `email`. The first version of the entry pages
> appended a hidden input called `guide`, which MailerLite would most likely have
> discarded. Both pages now **read the naming convention off the rendered form**
> and match it — `fields[guide]` where the form uses `fields[…]`, `guide` where
> it doesn't, and both if it can't tell. This has **not been verified against a
> live form**, so step 1 of the test below is the one that matters.

## 2. Two groups

`entry-first-night` and `entry-guests`. Groups, not segments — automations trigger
more reliably on group join.

## 3. Two automations

Each one: **trigger = subscriber joins group**, then three emails.

| | Delay | Subject |
|---|---|---|
| 1 | immediately | Here's the printable |
| 2 | 3 days after previous | *first-night:* Smaller than a box · *guests:* The shorter version |
| 3 | 4 days after previous | One question |

Copy is in [`first-night-sequence.md`](first-night-sequence.md) and
[`guests-sequence.md`](guests-sequence.md). Paste it as written — the wording is
load-bearing, not decorative.

**Settings that matter:**

- **Allow re-entry: OFF.** Nobody should get the same sequence twice.
- **Resend to unopens: OFF.** It's on by default in some accounts and it
  directly violates [ADR-016](../../../planning/decisions.md#adr-016--the-sequence-shrinks-unconditionally)
  — it re-asks for the same thing, which is the one move the whole sequence is
  designed not to make.
- **Stop on reply** if the plan offers it. A reply means a conversation, not
  another scheduled email.
- **Sender:** Charles, from a real address that accepts replies. The emails are
  signed by a person and email 3 says *"it's me reading them, not a system."*
  That has to be true.

## 4. Routing on the `guide` field

Simplest reliable arrangement — a condition on the form submission, or an
automation on the main form that sorts and stops:

```
if guide = "first-night"  → add to group entry-first-night
if guide = "guests"       → add to group entry-guests
else                      → add to group entry-unknown
```

**Keep `entry-unknown`.** It should stay empty. If it fills up, the hidden field
isn't arriving, and that's the failure mode to watch for.

## 5. The printable links

Linked, not attached — better deliverability and it can be corrected after
sending without re-sending.

| Sequence | URL |
|---|---|
| first-night | `https://mrlifemanager.com/print/first-night.pdf` |
| guests | `https://mrlifemanager.com/print/guests-when-someone-is-coming-over.pdf` |

Published by the build from `products/guides-pdf/`. **Open both in a browser
before sending anything** — a dead link in email 1 kills the sequence at the only
moment the reader is paying attention.

---

## Test it before it's real

Subscribe yourself from **both** pages, using two addresses, and confirm:

- [ ] Each one lands in the right group, with `guide` populated
- [ ] `entry-unknown` is empty
- [ ] Email 1 arrives within a few minutes and the printable link opens
- [ ] The subject lines are right and the sender name is a person
- [ ] Unsubscribe works and the footer address is correct
- [ ] Replying reaches a real inbox someone reads
- [ ] Email 2 arrives on day 3 and **asks for less than email 1** — if it reads
      like a nudge, it's wrong
- [ ] Nothing arrives after email 3

Then remove both test addresses so they don't pollute the first real numbers.

---

## What not to turn on

- **Re-engagement / win-back campaigns.** "We miss you", "you haven't opened in a
  while" — both reference behaviour we agreed never to reference, and both
  manufacture the exact shame this brand exists to remove.
- **Open tracking as a decision input.** It can stay on for curiosity, but Apple
  Mail Privacy Protection pre-fetches images, so a share of recorded opens never
  happened. **Nothing branches on it.**
- **Anything after email 3.** Silence means stop. If there's a reason to write
  again later, it's a new decision, not an automation that was left running.
