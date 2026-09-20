# First Reader Test — the entry pages

**Different job from the [customer interview script](customer-interview-script.md).**
That one asks whether the problems are real. This one asks whether **a page makes
a specific thing get done.**

**Status:** written 2026-09-20, before any reader has seen anything.

---

## What is being tested

Exactly one thing, because
[ADR-014](../../../planning/decisions.md#adr-014--completion-is-what-converts)
says so:

> **Did something get done, and where did they stop?**

Not whether they liked it. Not whether it's clear, useful, well-written or nicely
designed. Every one of those produces a polite answer that predicts nothing, and
the readers available right now are **friends of the founder**, which makes the
politeness problem about as bad as it gets.

---

## The setup

**Send it when the situation is real.** A page for "someone's coming over in
ninety minutes" tells you nothing when it's read on a calm Tuesday afternoon.
Wait for the actual moment — someone moving, someone hosting — and send the link
then. One real use beats ten reviews.

**Send the link and nothing else.** No "let me know what you think," no context,
no apology, no "I've been working on this." Ideally:

> *Thought of you — you're moving Saturday, right? mrlifemanager.com/first-night.html*

That's the whole message. Anything more coaches them.

**Don't watch.** Being watched turns a user into a performer: they'll read more
carefully than they would, and they'll do steps they'd otherwise skip, to be
polite. Send it cold and ask afterwards.

**Never explain a step.** If they message asking what something means, that is the
single most valuable signal you'll get all week. **Write down the exact wording of
their question** and then answer it. The question is the finding; the answer is
just politeness.

---

## Decide these before you send, not after

Otherwise whatever happens gets rationalised into a success.

| Page | Pass | Fail |
|---|---|---|
| **Someone's coming over** | They did **two or more steps** during an actual pre-guest panic | They read it, said something nice, and did nothing |
| **Your first night** | **They took the photos.** That's the one worth money and the one they'd never have thought of | They skipped step 1 |
| **Either** | They forwarded it to someone without being asked | They had to be prompted to respond at all |

**Writing these down now is the point.** A test whose criteria are set afterwards
isn't a test.

---

## What to ask, afterwards

Four questions. All are about the past, none has a wrong answer, and none
mentions quality.

1. **"Where did you stop?"**
   The most useful question on the page. Everyone stops somewhere; saying so costs
   them nothing. The stopping point is the design problem.

2. **"What would you have done if that page didn't exist?"**
   The one that actually matters. We're not competing with nothing — we're
   competing with *panic-cleaning in a random order* and *googling it*. If their
   answer is "about the same thing, probably," the page isn't earning its
   existence, however much they liked it.

3. **"Was there anywhere you nearly stopped and didn't?"**
   Finds the friction that got survived. Next reader won't survive it.

4. **"What did you skip?"**
   Skipping is information. A step everyone skips is either in the wrong place or
   shouldn't be there.

Then, if it's genuinely true: **"If it's worth sending to someone, send it."**
Whether they do is worth more than every answer above combined, because it's
behaviour rather than opinion. Don't chase it, don't follow up on it, just notice.

---

## What not to ask

- *"Was that helpful?"* — produces "yeah, really helpful" from everyone, always
- *"What did you think?"* — invites a critique of the writing, which is not the test
- *"Would you pay for this?"* — predicts nothing; only a real transaction does
- *"Any feedback?"* — puts them in reviewer mode, where they invent suggestions to
  seem useful
- Anything mentioning design, wording, or layout unless they raise it first

---

## The honest limits

**One or two readers is a smoke test, not evidence.** It can tell you something is
obviously broken. It cannot tell you the thing works, and it cannot tell you
anything at all about conversion.

Things it genuinely can't answer, no matter how well it goes:

- Whether a stranger who arrived by search behaves like a friend who got a text
- Whether anyone gives an email address after the win
- Whether anyone pays for anything
- Whether the shrinking sequence reduces unsubscribes — nothing is configured yet

**Resist the pull to conclude more than this supports.** Everything decided on
2026-09-20 is reasoning, not evidence, and one enthusiastic friend does not
change that.

---

## What to do with what you get

Write it down the same day, verbatim where possible, in
[`docs/research/inputs/`](../inputs/) with the date. Their words, not a summary —
the [source-material rule](../../../source-material/INVENTORY.md) applies here
too: **capture first, interpret separately.**

Then look for the one thing that would change what gets built next. Not a list of
improvements — the one thing. If nothing would change, say so plainly rather than
manufacturing a finding.
