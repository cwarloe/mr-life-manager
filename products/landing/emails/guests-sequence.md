# Sequence — "Someone's coming over" (Draft 4)

**Entry:** [`/guests.html`](../guests.html). Tagged `guide=guests` on the form.
**Status:** Active in MailerLite per owner 2026-09-22. Reader validation remains open.
**Governed by** [ADR-016](../../../planning/decisions.md#adr-016--the-sequence-shrinks-unconditionally)
and [ADR-015](../../../planning/decisions.md#adr-015--the-win-comes-before-the-email).

**Replaces** the withdrawn site-wide Draft 3 welcome sequence for this entry
only — see [ADR-016](../../../planning/decisions.md#adr-016--the-sequence-shrinks-unconditionally).
Per-entry sequences (not one site-wide welcome) per [ADR-015](../../../planning/decisions.md#adr-015--the-win-comes-before-the-email).

---

## The shape

| | When | Ask | Size |
|---|---|---|---|
| 1 | Immediate | The Week (one page), plus one named action | ~10 min |
| 2 | Day 3 | The same thing, smaller | ~4 min |
| 3 | Day 7 | Nothing. One question. | one word |
| — | After | **Stop.** | — |

It shrinks **unconditionally** — nobody is branched on opens, clicks, or any
guess about whether they did it. A **reply** or a **purchase** takes someone out
of the sequence and into a conversation. Nothing else does.

---

## Footer — all three emails (draft, pending approval)

One static line in the footer of emails 1, 2 and 3: below the sign-off, in the
footer area with MailerLite's unsubscribe text. It is not body copy. Plain text,
no QR code, no button.

> Free to share: mrlifemanager.com

Not live until Charles approves. The MailerLite edit is in
[MAILERLITE-SETUP.md](MAILERLITE-SETUP.md) under *Referral lines*.

---

## Email 1 — immediate

**Subject:** Here's the thing worth printing

> You already did the hard part tonight, so I'm not going to send you a copy of it. You won't need that page again if this works.
>
> Here's what I'd print instead.
>
> https://mrlifemanager.com/print/the-week.pdf
>
> It's one page, and it's Dave's whole system. The top of it is the ten minutes you do before bed — empty the sink, wipe the counters, walk one lap and put things back. Underneath that there's one job for each day of the week, and two days with nothing on them at all.
>
> Print it and stick it inside a cabinet door. It's the thing that means nobody ever has to do tonight again.
>
> — Charles

*Link (not attach): <https://mrlifemanager.com/print/the-week.pdf>*

---

## Email 2 — day 3

**Subject:** The shorter version

> I think ten minutes a night is the right answer, but I also think it's more than most people can start with. That's my fault for leading with it.
>
> So here's the version that fits anywhere.
>
> Just empty the sink before you go to bed. That's it.
>
> It takes about four minutes most nights. You can skip the counters and skip the lap around the room. Just do the sink.
>
> It's the one that does the most work. A kitchen with an empty sink looks under control even if you haven't touched anything else, and walking into that in the morning changes how the whole day starts.
>
> Some nights it won't happen, and that's fine. This isn't a streak and there's nothing to reset.
>
> — Charles

---

## Email 3 — day 7

**Subject:** One question

> There's nothing attached to this one.
>
> I'm trying to figure out what to write next, and the most useful thing anyone has told me so far came out of a question like this one.
>
> Which room do you avoid?
>
> One word is a complete answer. Just hit reply. It's me reading these, not a system.
>
> — Charles

Then the sequence ends. **Silence means stop.**

---

## The rules this is built on

- **It shrinks unconditionally.** Every email asks less than the last, for
  everyone. We never infer behaviour, so we can never imply we know someone
  failed.
- **No question with a wrong answer.** "Which room do you avoid?" has none.
  Draft 3's *"Done / Started, didn't finish / Haven't yet"* had two.
- **Never reference what they did or didn't do.** Not once in three emails.
- **When something didn't land, it's ours out loud.** Email 2 opens with
  *"that's my fault for leading with it"* rather than asking why they stopped.
- **No streaks, no progress language, no "still haven't…".** Email 2 says so
  explicitly: *"It isn't a streak, and nothing resets."*
- **Silence means stop.** Carried from Draft 3, which got this part right.

## What happens on a reply

A reply is a person, so a person answers — not an autoresponder and not a
sequence. Read it, answer the actual question, and if there's a guide that fits,
send **one**. If there isn't, say so and answer anyway. At this volume this is
genuinely doable and it's the only real research we have.

---

## Still open

1. ~~**The printable.**~~ Done — Email 1 links
   <https://mrlifemanager.com/print/the-week.pdf>. Open it before sending.
2. **No paid offer appears anywhere in this sequence**, deliberately. ADR-015
   says the paid step is smaller and in the same domain; that product ($9, the
   maintenance version) **does not exist yet**. Inserting a placeholder offer
   would break the shrinking rule and sell something we can't deliver. The
   natural insertion point is after email 3, once there's something real.
3. ~~**MailerLite automation.**~~ **Done** 2026-09-22 (Active per owner). Live
   ops spec: [MAILERLITE-SETUP.md](MAILERLITE-SETUP.md). Keep
   "resend to unopens" off — it violates ADR-016.

Homepage is the pain router to four entry doors (ADR-016); this file is the
guests door only.
