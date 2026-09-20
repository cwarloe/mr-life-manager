# Operator prompt — wire the MailerLite sequences

Paste everything between the rules into an agent that has browser access and is
signed in to MailerLite. Written to be run, not interpreted.

**Source of truth:** [`MAILERLITE-SETUP.md`](MAILERLITE-SETUP.md),
[`guests-sequence.md`](guests-sequence.md),
[`first-night-sequence.md`](first-night-sequence.md). The copy is duplicated in
the prompt for the agent's convenience — **if it ever disagrees with those files,
those files win.**

---

You are configuring email automation in MailerLite for a small publishing project
called Mr. Life Manager. Work carefully. Several steps fail silently, so verify
each one before moving on.

## Context you need

The website has two pages. Each has an embedded MailerLite form (account
`2635985`, form `00ZwEr`). When someone signs up, the page attaches a hidden
field recording which page they came from:

| Page | Hidden field value |
|---|---|
| `https://mrlifemanager.com/first-night.html` | `first-night` |
| `https://mrlifemanager.com/guests.html` | `guests` |

That value is the only thing deciding which of two email sequences a person
receives. Everything you build depends on it arriving correctly.

## Your tasks, in order

### 0. Authenticate the sending domain

Settings → Domains. Authenticate `mrlifemanager.com` and report the exact SPF and
DKIM records MailerLite asks for, so the owner can add them to DNS.

**Do not skip this and do not work around it.** If the domain is already verified,
say so and continue.

Also report whether email automations are available on the current plan. If they
are not, **stop and report that** — do not build anything else.

### 1. Create the custom field

Subscribers → Fields. Create a **Text** field with the key `guide`.

Then report **the exact key MailerLite assigned**, verbatim. It may differ from
what you typed.

### 2. Report the form's real field naming — this is the critical check

Open `https://mrlifemanager.com/guests.html` in the browser, find the embedded
signup form, and inspect the email input element.

**Report the exact `name` attribute**, character for character. It will be
something like `fields[email]` or `email`.

This matters because the pages guess at the convention. If the guess is wrong,
signups keep working and every one arrives untagged, which means **nobody gets any
email at all** and nothing appears broken. Report what you find; do not try to fix
the website.

### 3. Create three groups

- `entry-first-night`
- `entry-guests`
- `entry-unknown`

### 4. Route signups by the `guide` field

Configure routing so that:

```
guide = "first-night"  → add to entry-first-night
guide = "guests"       → add to entry-guests
anything else or empty → add to entry-unknown
```

`entry-unknown` is deliberate. It is an alarm: it should stay empty forever, and
anything landing in it means the tagging is broken.

### 5. Build two automations

Each triggers on **subscriber joins group** and sends three emails.

**Settings for both, all mandatory:**

- Allow re-entry: **OFF**
- Resend to unopeners: **OFF** — this is on by default in some accounts and must
  be disabled
- Stop automation on reply: **ON**, if the plan offers it
- Sender name: **Charles**
- Sender address: a real inbox that a person reads

**Timing for both:** email 1 immediately, email 2 three days after email 1,
email 3 four days after email 2.

Use the copy below **exactly as written**. Do not rewrite, shorten, improve,
add greetings, add sign-offs, or add postscripts. Do not add an offer, a product,
a discount, or a link to anything not listed. Plain text formatting; no stock
images, no banners, no hero graphics.

---

#### Automation A — group `entry-guests`

**Email 1 — immediately. Subject: `Here's the printable`**

```
The page you just used, as one sheet you can keep. Stick it inside a cabinet door and you'll never have to find it again.

https://mrlifemanager.com/print/guests-when-someone-is-coming-over.pdf

Now the part that means you don't need it.

Dave's version is ten minutes, before bed:

1. Empty the sink. Completely.
2. Wipe the counters and the table.
3. Walk one lap and put back anything that isn't where it lives.

That's the whole system. There's no week two.

It works because none of it is cleaning. It's just not letting today's mess turn into next month's project — which is the only reason tonight was ever necessary.

— Charles
```

**Email 2 — 3 days later. Subject: `The shorter version`**

```
Ten minutes a night is the right answer, and for a lot of people it's too much to start with. That's my fault for leading with it.

So here's the version that fits anywhere:

Empty the sink before bed. That's all.

Four minutes, most nights. Skip the counters. Skip the lap around the room. Just the sink.

It's the one that does the most work, because a kitchen with an empty sink reads as under control even when nothing else has been touched — and walking into that in the morning changes how the day starts.

Some nights it won't happen. That's fine. It isn't a streak, and nothing resets.

— Charles
```

**Email 3 — 4 days later. Subject: `One question`**

```
Nothing attached to this one.

I'm working out what to write next, and the most useful thing anyone has told me came from a question like this one:

Which room do you avoid?

One word is a complete answer. Hit reply — it's me reading them, not a system.

— Charles
```

---

#### Automation B — group `entry-first-night`

**Email 1 — immediately. Subject: `Here's the printable`**

```
The page you just used, as one sheet. Worth keeping somewhere you'll find it again — the breaker box and water shutoff bit is the sort of thing you look up twice a decade and need urgently both times.

https://mrlifemanager.com/print/first-night.pdf

Now tomorrow.

The instinct is to empty every box and then work out where things go. Do it the other way round:

Take one box. Before anything comes out of it, decide where each thing is going to live. Then put it there.

Not "somewhere for now." Its actual place. One box done that way beats six boxes emptied onto the floor, because six boxes on the floor is just the same job again with more steps.

Right now that costs you nothing. Everything is still in your hands for the first time anyway.

— Charles
```

**Email 2 — 3 days later. Subject: `Smaller than a box`**

```
A whole box is more than most people have in them in week one of a new place, when you're also working and eating badly and still finding the light switches. That's on me for starting there.

So:

One drawer. The kitchen one you've already opened four times looking for something.

Take everything out, decide what belongs in it, put that back, and find homes for the rest. Ten minutes.

That drawer is the one you'll open a thousand times this year. It's the highest return on ten minutes anywhere in the place — and unlike the boxes, it's finished when you close it.

There's no schedule attached to this. Some weeks nothing gets unpacked. That's normal and it isn't a failure.

— Charles
```

**Email 3 — 4 days later. Subject: `One question`**

```
Nothing attached to this one.

I'm working out what to write next, and the most useful thing anyone's told me came from a question like this:

What's still in a box?

One word is a complete answer. Hit reply — it's me reading them, not a system.

— Charles
```

---

### 6. Verify both PDF links

Open both in the browser and confirm each loads a readable PDF:

- `https://mrlifemanager.com/print/guests-when-someone-is-coming-over.pdf`
- `https://mrlifemanager.com/print/first-night.pdf`

If either 404s, **report it and do not activate the automations.** A dead link in
email 1 wastes the only moment the reader is paying attention.

### 7. Test, then clean up

Sign up from **both** pages using two different test addresses. Confirm and
report each:

- [ ] Each landed in the correct group
- [ ] The `guide` field is populated, not empty
- [ ] `entry-unknown` is empty
- [ ] Email 1 arrived, and its PDF link opens
- [ ] Sender shows as a person, not a company
- [ ] Replying reaches a real inbox
- [ ] Unsubscribe works

Then delete both test subscribers so they don't pollute the first real numbers.

## Never do these

- **Never turn on re-engagement, win-back, or "we miss you" campaigns.** They
  reference the reader's behavior, which this project has decided never to do.
- **Never enable resend-to-unopeners.** It re-asks for the same thing. Every
  email in these sequences deliberately asks for *less* than the one before it.
- **Never add a fourth email**, a promotion, an upsell, or a "just checking in."
  The sequence ends at three. Silence is an acceptable answer from a reader.
- **Never edit the copy.** The wording is deliberate, including the parts that
  look like they need tightening.
- **Never branch on opens.** Apple Mail Privacy Protection pre-fetches images, so
  a share of recorded opens never happened.

## Stop and ask a human if

- Automations aren't available on the plan
- The `guide` field doesn't arrive populated in the test
- Either PDF link 404s
- MailerLite's interface doesn't match these steps closely enough to be confident
- Anything requires a payment, a plan change, or a DNS edit

## Report back

1. The SPF and DKIM records needed, verbatim
2. The exact `name` attribute of the form's email input
3. The exact key assigned to the `guide` field
4. The test checklist above, each item pass or fail
5. Anything you had to guess at

Do not mark the job complete unless every item in step 7 passed.
