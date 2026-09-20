# Sequence — "Someone's coming over" (Draft 4)

**Entry:** [`/guests.html`](../guests.html). Tagged `guide=guests` on the form.
**Status:** Drafted 2026-09-20. Not sent. Not reviewed by a reader.
**Governed by** [ADR-016](../../../planning/decisions.md#adr-016--the-sequence-shrinks-unconditionally)
and [ADR-015](../../../planning/decisions.md#adr-015--the-win-comes-before-the-email).

**Replaces** the withdrawn [Draft 3](welcome-sequence.md) for this entry only.
Under ADR-015 sequences are per-entry, not one welcome sequence for the site.

---

## The shape

| | When | Ask | Size |
|---|---|---|---|
| 1 | Immediate | The printable, plus one named action | ~10 min |
| 2 | Day 3 | The same thing, smaller | ~4 min |
| 3 | Day 7 | Nothing. One question. | one word |
| — | After | **Stop.** | — |

It shrinks **unconditionally** — nobody is branched on opens, clicks, or any
guess about whether they did it. A **reply** or a **purchase** takes someone out
of the sequence and into a conversation. Nothing else does.

---

## Email 1 — immediate

**Subject:** Here's the printable

> The page you just used, as one sheet you can keep. Stick it inside a cabinet
> door and you'll never have to find it again.
>
> Now the part that means you don't need it.
>
> Dave's version is ten minutes, before bed:
>
> **1. Empty the sink. Completely.**
> **2. Wipe the counters and the table.**
> **3. Walk one lap and put back anything that isn't where it lives.**
>
> That's the whole system. There's no week two.
>
> It works because none of it is cleaning. It's just not letting today's mess
> turn into next month's project — which is the only reason tonight was ever
> necessary.
>
> — Charles

*Link (not attach): <https://mrlifemanager.com/print/guests-when-someone-is-coming-over.pdf>*

---

## Email 2 — day 3

**Subject:** The shorter version

> Ten minutes a night is the right answer, and for a lot of people it's too much
> to start with. That's my fault for leading with it.
>
> So here's the version that fits anywhere:
>
> **Empty the sink before bed. That's all.**
>
> Four minutes, most nights. Skip the counters. Skip the lap around the room.
> Just the sink.
>
> It's the one that does the most work, because a kitchen with an empty sink
> reads as under control even when nothing else has been touched — and walking
> into that in the morning changes how the day starts.
>
> Some nights it won't happen. That's fine. It isn't a streak, and nothing
> resets.
>
> — Charles

---

## Email 3 — day 7

**Subject:** One question

> Nothing attached to this one.
>
> I'm working out what to write next, and the most useful thing anyone has told
> me came from a question like this one:
>
> **Which room do you avoid?**
>
> One word is a complete answer. Hit reply — it's me reading them, not a system.
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

## Not built — do not send until these are closed

1. **The printable.** Email 1 promises it. Generated as
   [`products/guides-pdf/guests-when-someone-is-coming-over.pdf`](../../guides-pdf/)
   — **published** at <https://mrlifemanager.com/print/guests-when-someone-is-coming-over.pdf> by the build. Open it before sending.
2. **No paid offer appears anywhere in this sequence**, deliberately. ADR-015
   says the paid step is smaller and in the same domain; that product ($9, the
   maintenance version) **does not exist yet**. Inserting a placeholder offer
   would break the shrinking rule and sell something we can't deliver. The
   natural insertion point is after email 3, once there's something real.
3. **MailerLite:** a group or automation keyed on `guide=guests`, three emails at
   0 / 3 / 7 days, no re-entry, and no "resend to unopens" — that last one is a
   standard feature and it directly violates ADR-016.

## Resolved 2026-09-20 — the main page is a router

The landing page previously captured email directly and offered a three-way
picker whose three paths had no sequence once Draft 3 was withdrawn — collecting
addresses with nothing to send them.

**Both email forms have been removed from the main page.** It now explains what
this is and routes to entry pages; every entry page carries its own action and
its own signup, and no entry page ships without a sequence.

**Consequence, stated plainly: there is one door.** `/guests.html`. The page says
so rather than pretending otherwise, and invites people to name the one they
needed — which is both honest and the cheapest research available on what to
build next.
