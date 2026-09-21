# Sequence — "Your first night" (Draft 1)

**Entry:** [`/first-night.html`](../first-night.html). Tagged `guide=first-night`.
**Status:** Drafted 2026-09-20. Not sent. Not reviewed by a reader.
**Governed by** [ADR-016](../../../planning/decisions.md#adr-016--the-sequence-shrinks-unconditionally)
and [ADR-015](../../../planning/decisions.md#adr-015--the-win-comes-before-the-email).

---

## The shape

| | When | Ask | Size |
|---|---|---|---|
| 1 | Immediate | The printable, plus one named action | one box |
| 2 | Day 3 | The same thing, smaller | one drawer |
| 3 | Day 7 | Nothing. One question. | one word |
| — | After | **Stop.** | — |

Shrinks unconditionally. Nobody is branched on opens or clicks. A **reply** or a
**purchase** moves someone out of it; nothing else does.

---

## Email 1 — immediate

**Subject:** Here's the printable

> Here's a one-page version of the guide you just used. Print it out and keep it somewhere you'll find it again. The part about the breaker box and the water shutoff is the kind of thing you look up maybe twice in ten years, and both times you need it in a hurry.
>
> https://mrlifemanager.com/print/first-night.pdf
>
> Now, about tomorrow.
>
> Your instinct will be to empty every box and then figure out where things go. Try it the other way around.
>
> Take one box. Before anything comes out of it, decide where each thing is going to live. Then put it there.
>
> Not "somewhere for now." I mean the place it's actually going to live.
>
> One box done that way beats six boxes emptied onto the floor, because six boxes on the floor is just the same job again with more steps.
>
> Right now this costs you nothing extra, because you're already holding everything for the first time anyway.
>
> — Charles

*Link (not attach): <https://mrlifemanager.com/print/first-night.pdf>*

---

## Email 2 — day 3

**Subject:** Smaller than a box

> A whole box is probably more than most people have in them during week one, when you're also working and eating badly and still finding the light switches. That's on me for starting there.
>
> So here's a smaller one.
>
> Just do one drawer. Pick the kitchen one you've already opened four times looking for something.
>
> Take everything out, decide what actually belongs in it, put that back, and find homes for the rest. It takes about ten minutes.
>
> That's the drawer you'll open a thousand times this year, so it's the best ten minutes you can spend anywhere in the place. And unlike the boxes, it's finished the moment you close it.
>
> There's no schedule attached to any of this. Some weeks nothing gets unpacked, and that's normal. It isn't a failure.
>
> — Charles

---

## Email 3 — day 7

**Subject:** One question

> There's nothing attached to this one.
>
> I'm trying to figure out what to write next, and the most useful thing anyone has told me so far came out of a question like this one.
>
> What's still in a box?
>
> One word is a complete answer. Just hit reply. It's me reading these, not a system.
>
> — Charles

Then it ends. **Silence means stop.**

---

## Why these three actions

Email 1 is [everything-has-a-place](../../../frameworks/everything-has-a-place.md)
delivered at the one moment in a person's life when it's free. Nothing has a home
yet, so assigning one costs nothing extra — the thing is already in your hand. Six
months later the same decision costs a weekend. The entry page sets this up; the
email is where it's actually used.

Email 2 shrinks to a drawer because a box is a *session* and a drawer is a *task*.
The kitchen drawer specifically, because it's the one with the highest open-count
per year in any home.

Email 3 asks nothing and gives nothing. "What's still in a box?" has no wrong
answer — everyone has something in a box, including people who moved in years ago,
which is the quiet point of the question.

---

## Not built — do not send until these are closed

1. ~~**The printable.**~~ Done — published by the build at
   <https://mrlifemanager.com/print/first-night.pdf>. Open it before sending.
2. **No paid offer.** Deliberate — the $9 product doesn't exist. Insertion point
   is after email 3.
3. **MailerLite:** automation keyed on `guide=first-night`, 0 / 3 / 7 days, no
   re-entry, and **"resend to unopens" must stay off** — it's a standard feature
   and it directly violates ADR-016.

## Factual claims to verify before sending

The entry page makes two claims that go slightly beyond taught-not-looked-up, and
both should be checked against the [depth rule](../../../content/README.md) and
against reality before this is promoted:

- **Move-in photographs as deposit evidence.** True and widely advised, but the
  legal weight varies by jurisdiction. The page states it as practical advice
  rather than law, which is the right register — worth a second read to be sure
  it stays there.
- **Smoke alarms being the landlord's legal obligation.** True in most US states
  and in the UK, but not universally, and the page says "in most places" rather
  than asserting it flatly. Keep that hedge.
