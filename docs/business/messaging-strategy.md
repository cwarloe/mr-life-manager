# Messaging strategy

**Status:** Draft for Charles's review, 2026-09-29. Written to be argued with.
Nothing here has met a reader; like
[ADR-015](../../planning/decisions.md#adr-015--the-win-comes-before-the-email),
it is a hypothesis. Word budgets are working judgments, not measurements.

**Why this exists.** Piecemeal fixes swung the copy from clipped ("Six things,
in order.") to over-corrected full sentences, then back to "just enough words to
be clear on the first read." A single blanket rule keeps losing because the
reader is doing different things at different moments. **Two ideas carry this
document.** First, every line has to carry the information the reader doesn't
have yet (see *Communication principles*). Second, every moment has its own word
budget for carrying it (§1). A step heading can be three words. A tear tab
can't, because it has to make sense in a pocket two days later.

Sources: [principles](../vision/principles.md),
[brand-positioning](brand-positioning.md),
[target-audiences](../vision/target-audiences.md), ADR-010/014/015/016,
[customer-problems](../research/customer-problems.md), live copy on `main`
(2ca2775), and the PR #54 flyer. The MailerLite form heading, success message and
confirmation email live in the account, not the repo, so they are quoted as
reported.

**Who we're talking to.** Per ADR-010, the marketing addresses **Dana**, the
overwhelmed adult already running a household. The content still serves
**Tyler** (`/first-night.html`). Dana "has tried apps, planners… nothing stuck
because it was all too elaborate," so padded copy reads to her as one more
elaborate system. Tyler "won't ask his parents," so any whiff of *should have
known* loses him.

---

## Communication principles

This is a checklist to run over any line, not a rulebook.

1. **Name the thing, every time.** Say "a one-page weekly cleaning plan." Never
   say "the page," "it," or an internal name the reader hasn't learned yet.
2. **Say the action, then what they get.** One message does one job.
3. **Promise only what's true and useful to the reader.** Don't announce
   internal rules, like the sequence stopping. A reply starts a real
   conversation, and more will come later.
4. **Write for what the reader knows at that moment,** not for what the team
   knows.
5. **Test each line by asking what it tells them.** If the answer is nothing,
   cut it. If they'd have to guess, add words.

**Why the edits have yo-yoed.** The copy was written from inside the team's
context: we know what "the page," "The Week," and "Dave's week" refer to, and
the reader doesn't. When a line read wrong, it got fixed by changing its length.
Clipped lines were padded into full sentences, and long lines were trimmed back
to fragments. But the problem was never length. It was missing content. A line
that says "the page" fails at four words and would still fail at fourteen,
because the reader doesn't know which page. The fix is to add the missing noun or fact,
and then let the word budget decide how much else fits.

---

## 1. The journey, moment by moment

| Moment | Reader is thinking | Job of the copy | Budget |
|---|---|---|---|
| **Flyer, walking past** | "Is this for me?" | Name the situation in their words | Headline ≤ 6 words; ≤ ~25 words readable from six feet |
| **Flyer, deciding to scan** | "What do I get? What's the catch?" | Say what's behind the QR, and that it's free | Caption ≤ 15 |
| **Tear tab** | *(days later)* "What was this?" | Stand alone | ≤ 12, with a subject and a verb |
| **Landing, first screen** | "Right place? How long?" | Echo the situation, give the time, start | H1 ≤ 12; ≤ 50 before step 1 |
| **Mid-task** | "What next? Is this enough?" | Instruct; the *why* is optional | Heading 2–7 (clipped is fine); instruction ≤ 40; why ≤ 60 |
| **Finish** | "Am I done? Did that count?" | Close the loop; say that what they did counts | ≤ 25 |
| **Signup ask** | "What arrives, how often, can I leave?" | Name the thing they'll get and what else will arrive | Heading ≤ 8; subtext ≤ 35 |
| **Success message** | "Did it work? What now?" | What happened, plus the one next action | ≤ 15 |
| **Confirmation email** | "Is this legit? Why click?" | Recognizable sender, one button | Subject ≤ 8; body ≤ 50 |
| **Email 1** | "Is this what I asked for?" | Name the plan, link it, give one action | ≤ 130 |
| **Email 2** | "Do I have to read this?" | Less than email 1 | ≤ 90 |
| **Email 3** | "Oh, it's them." | One question | ≤ 50 |

**The rule behind the table: clip only where the context supplies the missing
words.** Mid-task, the page supplies them: the reader is in the kitchen, so
"Empty the sink." is complete. At first contact (the flyer, a tab, a subject
line, a form heading) nothing supplies them, so the line needs a subject and a
verb. Charles's "happy medium" rule is right. It just belongs to moments, not to
the whole site.

**Against current copy:**
- **First screens are over budget.** All four entry pages run 98–122 words
  before step 1, against a budget of about 50.
- **Email 2 reads longer than email 1.** In the guests sequence it is 126 words
  against email 1's 110. The *ask* shrinks, as ADR-016 requires, but the reading
  load grows, and a skimmer notices that first.

---

## 2. Voice: four candidates

Each voice renders the same three lines: **flyer headline / signup heading /
success message.**

**A. Plain friend who's been there (the apprentice).** What brand-positioning
already specifies: "a competent older sibling or a good RA." First person,
admits what it didn't know, credits Dave.
- *Someone coming over? Here's where to start.* / *Want a weekly cleaning plan
  that keeps it this way?* / *Sent. Check your inbox for your weekly cleaning
  plan.*
- **Strengths:** fits ADR-011's apprentice structure, is the least shaming
  voice, and is sustainable.
- **Risks:** it drifts into chattiness (it wrote the 100-word intros), and it
  sounds like every warm competitor.

**B. Calm coach.** Reassuring and forward-looking; talks to feelings.
- *Guests on the way? You've got this.* / *Keep the momentum going.* / *You're
  all set. Your next step is waiting.*
- **Strengths:** warm.
- **Risks:** ADR-015 rules out "personality hype." It sells a feeling, while the
  brand's gap is competence. Dana heard this voice from every app she quit.

**C. Dry honest-ad (*Crazy People*).** Tells you the true, slightly unflattering
thing, and wins trust by doing it.
- *Having people over? Step one is the trash.* / *A one-page cleaning plan by
  email. Not a newsletter.* / *Sent. One cleaning plan, no daily emails.*
- **Strengths:** the most trustworthy voice where readers expect a trick
  (signup, frequency, unsubscribe).
- **Risks:** irony. "Clever, ironic" is a brand Don't, and a joke at the place
  is one step from a joke at the person.

**D. Practical checklist.** Labels, numbers, imperatives; no persona.
- *Guests coming? 6 steps, 35 min.* / *Email me the weekly cleaning plan (PDF).*
  / *Sent: 1 PDF. Check your inbox.*
- **Strengths:** fastest to scan, and ideal mid-task.
- **Risks:** cold, and exactly the clipped register Charles objected to at first
  contact. Nobody replies to a checklist, and replies are ADR-016's only signal.

**Judgment: A is the voice. Borrow D's register inside the steps and C's candor
(not its jokes) wherever we make a promise. Reject B.** This follows from the
budget table:
- Mid-task, the reader wants D.
- Signup is a trust decision. C's plain honesty about what will arrive earns
  it.
- A carries the relationship that makes replying to email 3 feel natural. The
  budgets are what keep A from getting chatty.

---

## 3. Diagnosis of the current copy

**What works. Keep it:**
- **The why-paragraphs mid-task.** "An empty sink makes a kitchen read as clean
  even if you touch nothing else." Specific, true, and it teaches. This is the
  product.
- **Ordering by consequence.** Stopping early is always the right place to
  stop, so the structure does the reassuring.
- **Honest limits.** "This is a trick and you're going to have to deal with
  it."
- **Emails 2 and 3.** "That's my fault for leading with it" and "Which room do
  you avoid?"

**Cryptic:**
- *"Ready to start? The steps are below either way. These just clear everything
  else out of the way."* It's UI talking about itself, and it never says what
  "these" are.
- *"Do not turn the win into a new list."* (all four finished pages). An
  abstraction delivered as an order.
- *"Those are the doors open so far."* (index). "Doors" is our internal word.
- **"The Week"** (see §4).

**Padded:**
- **First screens.** Two paragraphs of reassurance where one sentence would do.
- **Index picker descriptions.** 15–20 words each, for a choice made in
  seconds.
- **"That's the whole ___."** It appears about ten times across the index and
  entry pages (method, point, job, reason, list…). Once is emphasis; ten times
  is a tic.

**Off-brand or untrue:**
- **"Newsletter / Signup for news and special offers!"** Every part is wrong:
  - There is no newsletter. What actually arrives is one plan and two short
    follow-ups.
  - There are no offers. guests-sequence.md: "No paid offer appears anywhere in
    this sequence, deliberately."
  - "Signup" is a noun; the verb is "sign up."
  - It carries the only exclamation mark on the site.

  It sits at the moment of trust, which makes it the most important fix in the
  funnel.
- **"Check your inbox — your 3 guides are on the way."** This is false. Email 1
  delivers one PDF ("It does not promise or deliver a second PDF," per
  MAILERLITE-SETUP), and it contradicts ADR-014 in the one sentence every
  subscriber reads. **A correctness bug, not a taste question.**
- **The default MailerLite confirmation email** (if double opt-in is on; that
  can't be checked from the repo). Generic, in someone else's voice, arriving
  when the reader has the least reason to trust us.
- **Assumed context in the signup copy.** "Dave's week on one page," the line
  announcing that the two follow-ups are the last emails, and "One PDF link in
  the first email. No pack of downloads." A cold reader doesn't know who Dave is
  or what the week is. Announcing an end is an internal rule, and it overstates,
  since a reply starts a conversation. It works against the ongoing
  relationship we actually want.
- **"Disaster"** (the guests page H1). It works as a search query and fails
  everywhere else (§6, §7).
- **Commanding register.** ADR-015 says "plain, not commanding." Yet
  underwater.html says "Do not…" five times, and the finished pages end on an
  order. Where doc and copy disagree, the doc wins.

**Patterns that read as machine-written:**
- **Two- and three-beat heading fragments.** "Bin out. Window open." "Make the
  bed. Properly." "Open the mail. Two minutes. Then sit down." "Start one load of
  laundry. Or don't." About 10 of the 26 step headings. Any one is fine mid-task;
  the uniformity is the tell.
- **"Not X. Y." antithesis.** "Not out of indifference. Out of invisibility."
  "Not laziness — an unmade decision." "That's not a discipline problem" appears
  on two pages, and "This is not a character problem" on a third.
- **Aphorism pairs.** "Tonight is a floor. Tomorrow is a direction." "Systems buy
  you margin. Margin is what lets you say come over." "The order is yours. The
  finishing isn't."
- **Triplets.** The index hero is three verbless fragments in a row.
- **Coined labels the reader never agreed to.** "Put a floor under it" ("floor"
  appears seven times on underwater.html), "the cheap column," "the crisis
  version," "One thing finished," "the win."
- **Intensifiers and dashes.** "Genuinely," "actually," "the single most," and
  about 50 em-dashes across the index and the four entry pages.

None of these is banned. The fix is a ceiling: **one aphorism and one coined
label per page.**

---

## 4. The naming problem: "The Week"

A cold reader can't tell what "The Week" is, and it is also the name of an
established news magazine. It only works once someone has explained it, which is
the definition of a weak name. "Dave"
doesn't help a cold reader either: on a flyer or in a subject line, "Dave's"
raises "who's Dave?" before it earns anything.

**Brainstorm:**
- *Ten Minutes a Night*
- *The One-Page Week*
- *Dave's Week*
- *The Weekly Reset*
- *The Cabinet-Door Page*
- *Ten a Night, One a Day*
- *The Keep-It-Ready Week*
- *Nothing to Rescue*

**Judgment: in copy, don't use a name at all. Describe it: "a one-page weekly
cleaning plan"** (principle 1). A name only helps once the reader has learned
it, and nobody gets far enough into this funnel to learn one. On the PDF itself,
title it "Ten Minutes a Night" with the subhead "A one-page weekly cleaning
plan: ten minutes a night and one job a day."
- It names the benefit, and the benefit is also the first action.
- It is what the page itself calls "the part that matters."
- It survives email 2's shrink, since "just empty the sink" is a smaller ten
  minutes.
- The reader is already holding it, so the title can be a name there.

Runner-up: "The One-Page Week" (it names the format, not the benefit). Keep the
`the-week.pdf` URL; renaming it would break four live automations.

---

## 5. The copy test

Anyone can apply this to any line.

1. **First-read clarity.** Could someone who arrived five seconds ago say what
   this is?
2. **Subject present.** At first contact, is there a *who* or *what* and a verb?
   Mid-task headings are exempt.
3. **The reader's own next step.** Do they know what *they* do next, in their
   words, not ours?
4. **One offer.** Exactly one thing to act on (principle #11).
5. **No shame.** About the place and the system, never the person. No "should."
6. **No urgency.** No invented deadlines or "act now." A true time ("about
   thirty-five minutes") is fine.
7. **Within budget** for its moment (§1).
8. **True.** Every promise matches what is delivered. "3 guides" fails here,
   whatever else it passes.

---

## 6. Proposed rewrites

**Signup heading (MailerLite form). Pick: remove it.** Every page already has
its own heading right above the embed, so the form's heading is a second,
conflicting one. If MailerLite requires a heading, use *Get a one-page weekly
cleaning plan*. The page heading, "Want the week written down?", fails
principle 1 in its own right, because "the week" is our word. Consider *Want a
weekly cleaning plan to print?*

**Under the email box (pick):** *We'll email you a one-page weekly cleaning plan
to print, plus two short follow-ups over the next week.* It names the thing,
says what else will arrive, and promises nothing we'd have to retract when a
reply turns into a conversation.

**Success message (pick, for double opt-in):** *Almost done. Check your inbox
and click Confirm, and we'll send your weekly cleaning plan.* It gives the
action first, then what they get, and it replaces "3 guides." If double opt-in
turns out to be off, the same principles give: *Done. Your one-page weekly
cleaning plan is on its way to your inbox.*

**Confirmation email (pick).** Sender: **Mr. Life Manager**, with no personal
signature. This is a system step, and a person signing it would be pretending
otherwise. The personal "— Charles" signature starts at email 1.
- **Subject:** *Confirm your email to get your weekly cleaning plan*
- **Body:** *Click the button below to confirm your email address. Then we'll
  send you a one-page weekly cleaning plan to print. If you didn't sign up, you
  can ignore this email.*
- **Button:** *Confirm my email*

**Email 1 subject, all four sequences.** Change *Here's the thing worth
printing* to ***Your one-page weekly cleaning plan.*** The old subject is all
vague nouns ("the thing"), and it names nothing the reader asked for.

**Other lines in `products/landing/emails/*-sequence.md` flagged under the
principles.** These are suggestions only, and none has been edited.
- **Email 1 openers:**
  - *"Here's what I'd print instead."* (first-night, guests)
  - *"You won't need that page again if this works."* (guests)
  - *"a copy of that page"* (first-night)

  "That page" means the entry page, which the reader may not connect. Name
  the plan instead: *"Here's a one-page weekly cleaning plan to print
  instead."*
- **"The thing" as a noun:**
  - *"It's the thing that means nobody ever has to do tonight again."*
    (guests)
  - *"Here's the thing that keeps it there."* (underwater, which also carries
    the coined *"You put a floor under the week tonight"*)
- ***"It's one page, and it's Dave's whole system."*** (all four) "System"
  for what? Try *"It's Dave's whole weekly cleaning routine on one page."*
  The entry page has introduced Dave by this point, so the name is fine.
- ***"Here's what stops the next one filling up"*** and ***"the ten minutes
  is where things go"*** (one-room). "The next one" and "the ten minutes"
  both assume the reader is holding the plan.
- **Email 2 subjects:**
  - *"The shorter version"* (guests, underwater): the shorter version of
    what?
  - *"Smaller than a box"* (first-night): cryptic.
  - *"The next one is smaller than you think"* (one-room): what next one?

  Name the content: *"If ten minutes a night is too much"*, *"Unpack one
  drawer"*, *"Your next zone: one shelf."*
- ***"So here's the version that fits anywhere"*** (guests, underwater). The
  version of what? The next line already says it, so cut this one.
- **Email 3:**
  - Subject *"One question"* (all four) tells them nothing. Use the question
    itself as the subject, e.g. *"Which room do you avoid?"* (guests,
    underwater) or *"What's still in a box?"* (first-night).
  - *"There's nothing attached to this one"* describes our email instead of
    telling the reader anything. Cut it.

**Guests page H1**
- (a) Keep *…and your place is a disaster.*
- (b) *Someone's coming over and the place is a mess.*
- (c) *…and the place isn't ready.*

**Pick: (b).** It's the word people say out loud, it's about the place rather
than the person, and the page's own meta description already uses it. (c) is a
euphemism, and euphemisms read as marketing.

**Flyer (PR #54)**
- (a) Keep *Having people over?* with the new caption.
- (b) *Someone coming over? Start here.*
- (c) *People coming over, and the place isn't ready?*

**Pick: (a).** Three words, no shame, and the caption now carries the
explanation. The risk is that it reads as party planning, so test it against
(c).

**Finished pages.** Keep *That counts.* Replace *Do not turn the win into a new
list.* with *That's enough for today.*

---

## 7. Where this disagrees

**With the docs**
- **Principle 3 vs ADR-016.** "More will come later" is true in spirit: a reply
  starts a real conversation. But ADR-016 and MAILERLITE-SETUP still say the
  sequence ends after email 3, "silence means stop," and there is "no fourth
  email." Copy must not promise ongoing email until someone decides what
  "later" is. Flagged, not resolved.
- **"Nobody taught you."** Brand-positioning finds that frame occupied and "not
  the differentiator," yet still recommends *"The life skills nobody thought to
  teach you"* as the primary tagline, and the index closes on *"Nobody expected
  you to have known this."* Flagged, not resolved.
- **ADR-010 vs target-audiences.** ADR-010 aims the marketing at Dana. The
  target-audiences prioritization table still says "Build the MVP for Tyler."
  Flagged.
- **ADR-015's "my place is a disaster."** Right as a query, wrong as the H1 that
  every surface lands on. Principle #8 should outrank a working title.
- **The index fails principle #11's offer filter.** It makes four asks:
  - the picker
  - the $39 First Place link, which carries PR #48's open $9-vs-$39 flag
  - the pilot page
  - "tell me which one you need"

**With Charles's recent calls**
- **The rule itself.** "Complete phrases" and "happy medium" answer the wrong
  question. The swing will continue until the rule is attached to moments (§1).
- **No time word on the flyer.** Agreed, but the mismatch then moves to
  guests.html, which is written for the day of the visit ("stop when they
  knock"). Fix it there with one line: *Coming later this week? Do these on the
  day.*
- **Keeping the support line.** Acceptable, but it's the one flyer line over the
  glance budget. If anything goes after testing, it goes first.
- **Dave's apostrophe.** "Everything has it's place" is verbatim from 2009, but
  a cold reader sees a typo, not fidelity. Print "its" and keep the original in
  `source-material/`.
- **No sharing asks.** Agreed. The license footer is not an ask.

---

## What this doesn't settle

- **Every budget and pick is a hypothesis.** The cheapest real test is the
  flyer: tabs taken, and `?from=flyer-guests` visits per wording.
- **Whether double opt-in is on** has to be checked in the MailerLite account.
- **Nothing here changes a live page.** Each rewrite would be its own small PR,
  approved by Charles.
