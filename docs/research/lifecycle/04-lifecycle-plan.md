# Lifecycle 04: the plan, from a QR code to a customer who tells a friend

**Status:** Proposal, 2026-10-26. Nothing here is live and nothing here is
decided. Every item that needs Charles is marked **Decision** and collected at
the end.
**Author:** lifecycle-strategist.
**Built on:** [01, acquisition and first win](01-acquisition-and-first-win.md) ·
[02, emails and first purchase](02-emails-and-first-purchase.md) ·
[03, retention, upsells and referrals](03-retention-upsells-referrals.md) ·
[Vivid Vision 2029](../../vision/vivid-vision-2029.md) (draft) ·
[deferred-win architecture](../../../planning/deferred-win-architecture.md) ·
[operations](../../../planning/operations.md) ·
[email sequences](../../../products/landing/emails/) ·
[niche strategy](../../business/niche-strategy.md).
**Governing decisions:** ADR-009, ADR-013, ADR-014, ADR-020 and ADR-021 are
Accepted. ADR-010, ADR-015 and ADR-016 are **under review**; this plan stays
inside their current rules (win before email, shrinking sequences that end)
and flags every place it would need them changed.

**Labels.** **Evidence** is what a named source reports, with its confidence
(High, Medium, Low) as graded in research files 01–03 unless I note a change.
**Inference** is my reasoning from evidence. **Opinion** is a judgment call with
no evidence behind it. Nearly all of the design below is inference or opinion;
the evidence constrains it but does not prove it.

---

## 0. The plan on one page

| Stage | What the plan does | Main evidence |
|---|---|---|
| Flier or link → first win | Put fliers where the task happens and in the hands of insiders; match the flier's words to the page; keep "Start now" primary; let the checker share carry a tag and a calendar invite for the friend. | Point-of-decision prompts; person beats print; message match; planning-later licensing |
| Emails | Keep the three-email, shrinking, ending shape on all five routes. Wire the office route. No offer in any sequence. Replies are where the next step happens. | Reminder research flattens after a few contacts; tailoring helps a little |
| First purchase | Help taking action, not more content: a short **start call** at the reader's chosen time. Free pilot first, then a fixed price in the $9–19 band, charged only when the call happens. | Telephone coaching raised adherence; guided beats unguided for people who are stuck; price does not create use |
| Staying a customer | No subscription. Each new transition is a new free win; paid help is per use. A few dated return points the reader opts into. "Graduating" means the week runs without us. | Gym non-use; fresh-start dates; stepped care |
| Referrals | No reward to the referrer. Make sharing one tap, task-and-time framed, and credited to the sender. Insiders and partners are the main channel. | Gershon, Cryder & John 2020; Verlegh et al. 2013; Chapman & Reshadi 2025 |
| Measurement | One north-star count (first checklists finished) plus a guardrail for every growth idea, mapped to Umami events. | Small numbers: counts and replies over rates |

**The single biggest conflict:** the Vivid Vision says people pay gladly for
*help taking action* (automated help and coaching). ADR-020 defines the paid
tier as *deeper $9–19 guides*. This plan proposes help-taking-action as the
first paid offer and flags that Charles has to decide it (section 3.5).

---

## 1. From QR code or link to first win

### 1.1 What the evidence says, briefly

- **Evidence (Medium):** passive poster scanning is rare: 37 unique scanners
  from ten campus spots over two weeks
  ([Geisler et al. 2024](https://arxiv.org/html/2407.16230v1)). Distrust is the
  main reason people don't scan (77% of non-scanners in the same study).
- **Evidence (High):** a person asking beats print by a wide margin. In
  get-out-the-vote experiments, canvassing raised turnout about 8.7 points and
  a mailing about 0.5 ([Green & Gerber via SSIR](https://ssir.org/articles/entry/getting_out_the_vote_is_tougher_than_you_think)).
  Influence runs through close ties ([Bond et al. 2012](https://sparq.stanford.edu/sites/g/files/sbiybj19021/files/media/file/bond_et_al._2012_-_a_61-million-person_experiment_in_social_influence_political_mobilization.pdf)).
- **Evidence (Medium):** a QR flier handed over by staff got 17% participation
  against 91% for an in-person ask, but reached people who disclosed more
  privately ([Beatty et al. 2024](https://formative.jmir.org/2024/1/e48823)).
- **Evidence (High):** prompts at the point of decision work (stair signs: about
  a 50% relative rise in stair use)
  ([Community Guide](https://www.thecommunityguide.org/findings/physical-activity-point-decision-prompts-encourage-use-stairs)).
- **Evidence (Medium):** pages that match the ad convert better (Hoover: 34.8%
  vs 25.0%) ([NextAfter](https://www.nextafter.com/experiments/increasing-landing-page-congruence-affects-cost-subscriber/)).
- **Evidence (Medium, upgraded from file 03's caution):** merely planning to make
  progress later can lead to present choices against the goal. I read the
  abstract of [Fishbach & Dhar 2005](https://academic.oup.com/jcr/article-abstract/32/3/370/1787396)
  on 2026-10-26 and it says this ("merely planning to make goal progress in the
  future may facilitate incongruent choice of immediate action"). Files 01 and
  02 rate it Medium–High and High; file 03 said not to use it until the paper
  was read. The abstract confirms the finding; it is four lab studies, so I
  rate it **Medium** for our setting.
- **Evidence (High):** plan-making helps one-off acts and not habits
  ([Carrera et al. 2018](https://www.nber.org/papers/w24959)).

**Inference:** fliers are a support for insiders, not a channel on their own.
The flier's job is to earn the scan with a specific, trustworthy promise. The
page's job is to make "Start now" the easy default, with "Not right now" as an
honest fallback that does not pull people away from starting.

### 1.2 Fliers

| Do | Why | Label |
|---|---|---|
| **Headline = the page's headline**, in the reader's words, with a time: "Your kitchen back in forty minutes." | Message match; specific benefit; tailoring helps a little | Inference from Medium/High evidence |
| **Print the plain address** (mrlifemanager.com/underwater) beside the code, large enough to read from a step away. | Distrust is the scan barrier; QR plus URL beat URL alone in mail surveys ([Marlar & Schreiner 2024](https://www.ebsco.com/articles/history/80704703-d01e-5451-8a27-dcd3702e24e0/the-use-of-qr-codes-to-encourage-participation-in-mail-push-to-web-surveys-an-evaluation-of-experiments-from-2015-and-2022)) | Inference; the trust fix is untested |
| **One problem per flier, sparse layout.** No brand story, no Dave. | Overwhelmed readers are put off by complexity ([Okazaki et al. 2019](https://ideas.repec.org/a/eee/jbrese/v99y2019icp498-506.html)); task pages never mention Dave | Inference |
| **Place them where the task happens:** laundry rooms, dorm halls, apartment mailrooms, move-in tables, the inside of a utility closet door. Cafés are the weakest spot. | Point-of-decision prompts | Inference from High evidence |
| **Every code gets its own tag**, `?from=qr-<place>-<page>`, as the architecture already specifies. | Lets places be compared ([Southampton trial](https://eprints.soton.ac.uk/348567)) | Already decided |
| **Hand them over when possible.** A flier given by a person who says one sentence beats one pinned to a board. | Person beats print | Inference from High evidence |

**What to test (small, honest tests).** At single-digit scans per spot, no A/B
test will reach significance for months (file 01, implication 4). Judge on
completions per spot and on replies, not on scans.

1. **Placement:** the same flier at a point-of-action spot and at a café, with
   two tags. Compare `finished` counts per tag over eight weeks.
2. **Wording next to the code:** "Scan to start" versus a time ("Scan: forty
   minutes tonight"). No published controlled test exists (file 01, Low), so
   this is cheap curiosity, not a priority.

### 1.3 Partner handoff

Partners are the strongest channel the evidence supports and the ones the vision
names: ministries, schools and colleges, the service academies (starting with
the Air Force Academy through Dave), landlords and mentoring organizations.

- **A one-sentence handoff, with a time.** The vision's Chris story is the
  model: "Saturday at 10. I'll check on you." That sentence does three proven
  things at once: a personal ask, a specific time, and a respected checker.
  **Evidence:** reporting progress to someone raises goal attainment
  (d = 0.40, 138 studies; [Harkin et al. 2016](https://www.apa.org/news/press/releases/2015/10/progress-goals.aspx), High);
  telling a goal to someone you respect raised performance
  ([Klein et al. 2019](https://news.osu.edu/share-your-goals--but-be-careful-whom-you-tell/), Medium).
  **Inference:** the partner handout should print that sentence as a script.
- **A tag per partner**, `from=partner-<org>-<page>`, with no personal names,
  so the partner can be told how many finished.
- **The partner pilot stays as it is:** five people, three numbers back (tried,
  finished, where anyone stopped). It already avoids a progress report on
  individuals, which protects the shame-sensitive reader.
- **No institutional branding** without explicit agreement (niche strategy,
  caution 2). "For new lieutenants," not "USAFA edition."
- **Time handoffs to fresh starts and transitions:** semester start, move-in
  week, graduation and PCS season (about 65% of DoD household moves fall between
  May 15 and Sept. 30; [Joint Base Charleston](https://www.jbcharleston.jb.mil/News/Article/233776/peak-move-season-get-ready), Medium).

### 1.4 The first screen

The live pages already do most of this. Keep:

- The headline names the reader's situation, matching the flier.
- The fork sits high, with time and place stated before "Start now."
- No menus, no Dave, no links out.

Change or check:

| Item | Proposal | Label |
|---|---|---|
| **"Start now" stays visually primary;** "Not right now" stays secondary. | Guard against the planning-later licensing effect. Never style them as equals. | Inference from Medium evidence |
| **First step is quick and sure** on every page. | Early progress that feels fast reduces drop-off; slow early progress raises it ([Villar et al. 2013](https://research.google/pubs/where-am-i-a-meta-analysis-of-experiments-on-the-effects-of-progress-indicators-for-web-surveys/), High). Audit each page's step 1. | Inference |
| **Reading level check** (5th–7th grade) on each entry page. | Plain pages correlated with higher conversion ([Unbounce via MarketingProfs](https://marketingprofs.com/charts/2024/52374/landing-page-conversion-benchmarks), Medium, correlational) | Inference |
| **Credit real progress on return** from a reminder: "You already picked the zone." | Endowed progress, honestly applied ([Nunes & Drèze 2006](https://knowledge.wharton.upenn.edu/podcast/knowledge-at-wharton-podcast/the-lowdown-on-customer-loyalty-programs-which-are-the-most-effective-and-why/), High). Never a fake head start. | Inference |
| **The checker share carries a tag and a calendar invite for the friend.** See section 5.2. | The vision names this exact mechanic. | Opinion, untested |

**Keep the appointment flow for one-off tasks only.** Do not extend the "pick a
time" logic to the nightly ten minutes and expect the same effect (Carrera).

---

## 2. An email flow for every entry route

### 2.1 Rules every flow keeps

These are the current rules (ADR-016, under review). The plan keeps all of them.

1. Three emails: day 0, day 3, day 7. Each asks less than the one before.
2. Never branch on opens or clicks. Only a reply or a purchase changes the path.
3. Never ask a question with a wrong answer; never refer to what the reader did
   or didn't do.
4. **Silence means stop.** No fourth email, promotion or win-back.
5. **No paid offer inside any sequence.** (This is a choice in this plan, not
   only a rule; see 3.4 for why.)

**Evidence for the shape:** reminders raise response up to about three or four
contacts, then flatten ([Menon & Muraleedharan 2020](https://pmc.ncbi.nlm.nih.gov/articles/PMC7398086/),
Medium–High); one well-timed, specific reminder does most of the work
([Karlan et al. 2016](https://www.nber.org/papers/w16205), High). **No study
says when a post-win sequence should end** (file 02). Stopping at three is a
values decision consistent with the evidence, and should be labeled that way.

**Evidence for per-route emails:** tailoring helps behavior change a little
(r = 0.074 across 57 studies; [Noar et al. 2007](https://pubmed.ncbi.nlm.nih.gov/17592961/), High).
Our routes tailor on a situation the reader chose, which is the honest version.

### 2.2 The five task routes

The live copy is good and should stay. The outline below records each route's
purpose and asks, and the one or two changes proposed.

| Route | Purpose | Email 1 (day 0) asks | Email 2 (day 3) asks | Email 3 (day 7) asks | Stops | Proposed change |
|---|---|---|---|---|---|---|
| **First night** | Turn a one-time moment into homes for things | Print The Week; unpack one box by deciding homes first | One kitchen drawer, ten minutes | "What's still in a box?" | After email 3, or on reply | None to copy. Reply handling: answer, and if a room comes up, send the one matching free page. |
| **Guests** | Move from crisis cleaning to the nightly ten minutes | Print The Week; stick it inside a cabinet door | Just the sink, four minutes | "Which room do you avoid?" | Same | Reply handling: the answer names the next free win (one-room or underwater page). Offer to set a time for it. |
| **Underwater** | Keep the reset without shame | Print The Week; the two empty days are the point | Just the sink | "Which room do you avoid?" | Same | Same as guests. No copy change. |
| **One room** | Make the next zone feel small | Print The Week; the ten minutes is where things go | One shelf, twenty minutes, same three piles | "What was the hardest thing to let go of?" | Same | None. |
| **Office** | Keep a cleared desk clear | Print The Week; the last ten minutes before leaving | One drawer, twenty minutes | "What's the one thing that keeps landing on your desk?" | Same | **Wire it, or remove the form.** See below. |

**The office route is breaking a promise today.** The shared completion page
tells every reader who signs up, "Two shorter emails follow it." The office
page carries the same form, but its `entry-office` group and automation don't
exist ([operations.md](../../../planning/operations.md#waiting-on-the-bot)), so
an office signup gets nothing, or lands in `entry-unknown`. **Proposal:** wire
`entry-office` from the existing [office-sequence.md](../../../products/landing/emails/office-sequence.md).
It costs the bot one setup and Charles nothing. The alternative is to hide the
form on the office pages. **Decision.**

### 2.3 Routes before the win, and around the win

| Route | Is it a sequence? | Shape | Stops |
|---|---|---|---|
| **Appointment holders** ("Not right now," ADR-021) | **No. A reminder, not marketing.** | Today: the calendar invite is the reminder; nothing is emailed. Phase 2 (if built): one confirmation with the time and the return link, one reminder at the time, at most two moves. Delivers only the task. No The Week, no offer. | After the appointment, after the second move, or on "let it go." If they later finish and sign up on the completion page, they enter their route's three emails like anyone else. |
| **The checker** (the friend who was sent the appointment) | **No.** We never get their address. | The share text and the friend's calendar invite are the whole flow (section 5.2). | Nothing to stop. |
| **Parents** (`/index-parents.html`) | **No, for now.** | The page already says "Do not sign up for them. Forward the page." Keep that. Add the same "send it with a time" mechanic the checker uses, worded so it doesn't read as a judgment. | n/a |
| **Partners** (`/partners.html`) | **A human flow of three touches,** drafted by the bot, sent by Charles. | (1) On a pilot request: the handout, tagged links, the one-sentence handoff script. (2) About two weeks later: "Three numbers when you have them: how many tried, how many finished, where anyone stopped." (3) A thank-you with what we changed because of their answer. | After touch 3. Reopen at the next term or PCS season **only if the partner says yes** in touch 3. |

**Why no parent email flow.** **Evidence (High):** self-improvement gifts hurt
recipients' feelings and drew more negative reviews in five experiments
([Chapman & Reshadi 2025](https://business.fiu.edu/news/2025/new-fiu-research-some-holiday-gifts-can-backfire-leading-to-hurt-feelings-bad-reviews.html)).
**Evidence (High):** 59% of parents of 18–34-year-olds gave financial help last
year ([Pew 2024](https://www.pewresearch.org/social-trends/2024/01/25/financial-help-and-independence-in-young-adulthood/)),
so parents are a real payer, but nothing found shows them repeat-buying life
skills. **Inference:** a parent flow has more risk than value until ADR-010
(parents as payers, under review) is re-decided. **Decision** if Charles wants
parents as payers.

### 2.4 Flows that need a decision because they would stretch ADR-016

| Proposed flow | What it is | Conflict |
|---|---|---|
| **Return dates** (section 4.3) | A separate, explicit opt-in: "Want one email at the start of spring and before move-in season?" At most three a year, one task each. Ends after twelve months unless renewed. | ADR-016 and MAILERLITE-SETUP forbid a fourth email. This is a different group the reader chose, but it is more email. **Decision.** |
| **Buyer flow** (after a paid start call) | Confirmation with the time and how to prepare; the call; one question afterward; stop. | ADR-016 already allows "a purchase moves someone to a different sequence." No conflict if it shrinks and ends. |

---

## 3. From first win to first purchase

### 3.1 What the vision asks for

The vision says people "gladly pay for help taking action: automated help that
starts with the calendar reminder and goes further, and coaching, either over
the phone or recorded," and refuses any subscription people pay for and don't
use. The year-one guess is about $1,000 from 50–100 paying customers.

**Inference from the vision's own numbers:** $1,000 across 50–100 customers is
$10–20 each, which is one purchase per person inside the $9–19 band. That is a
plan built on a single first purchase, not a ladder of repeat buys. It also
matches the realistic base rate: the median Gumroad creator made **$70** in
2020 ([Gumroad report via Silicon Florist](https://siliconflorist.com/2021/01/12/what-happened-in-the-gumroad-creator-community-in-2020/), Medium).

### 3.2 What the evidence says about the first purchase

- **Evidence (High):** price screens in likelier users but does not make anyone
  use what they bought ([Cohen & Dupas 2010](https://www.povertyactionlab.org/evaluation/free-distribution-or-cost-sharing-evidence-malaria-prevention-experiment-kenya);
  [Ashraf, Berry & Shapiro 2010](https://www.povertyactionlab.org/evaluation/can-higher-prices-stimulate-product-use-evidence-randomized-experiment-zambia)).
  A paid guide is no more likely to be finished than a free one.
- **Evidence (High):** guided help beats unguided mainly for people who are
  struggling ([Karyotaki et al. 2021](https://www.healio.com/news/psychiatry/20210120/guided-internetbased-cbt-more-effective-for-depression-than-unguided-form));
  stepped care works moderately ([van Straten et al. 2015](https://www.cambridge.org/core/journals/psychological-medicine/article/abs/stepped-care-treatment-delivery-for-depression-a-systematic-review-and-metaanalysis/451FCB6B909825F5142A1E845F8651E2), Medium–High).
  The guide's profession didn't seem to matter
  ([Musiat et al. 2021](https://www.cambridge.org/core/journals/psychological-medicine/article/abs/impact-of-guidance-on-intervention-adherence-in-computerised-interventions-for-mental-health-problems-a-metaanalysis/02990B48E8FEB565569640C54BF8E9F1), Medium–High).
- **New evidence (Medium; clinical, small):** in a 101-person trial, telephone
  coaching raised adherence to a self-help web program over self-directed use:
  more days logged in, longer use, more lessons. The coaching was one call of
  about 44 minutes, then about eight calls averaging 9 minutes. Most people in
  both arms still dropped out by week 12
  ([Mohr et al. 2013, PLOS ONE](https://pmc.ncbi.nlm.nih.gov/articles/PMC3749146/),
  read 2026-10-26). **Inference:** short calls are the right unit. They help
  people start and keep going; they do not guarantee finishing.
- **Evidence (Medium, a model, not a trial):** a coach helps when seen as
  trustworthy, benevolent and expert, with clear, process-focused expectations
  ([Mohr, Cuijpers & Lehman 2011](https://pmc.ncbi.nlm.nih.gov/articles/PMC3221353)).
  This is what Dave did for Charles.
- **Evidence (Medium):** a sales pitch tacked onto good service lowered intent
  to buy ([Söderlund 2013](https://www.emeraldinsight.com/insight/content/doi/10.1108/MSQ-03-2013-0045/full/html)).
  Progress can license stopping (Fishbach & Dhar, above), and effort dips right
  after a reward ([Kivetz et al. 2006](https://business.columbia.edu/faculty/research/goal-gradient-hypothesis-resurrected-purchase-acceleration-illusionary-goal), High).
- **Evidence (High):** pay-what-you-want drew *fewer* buyers than a fixed price
  ([Gneezy et al. 2012](https://pmc.ncbi.nlm.nih.gov/articles/PMC3358869)).
- **Evidence (High):** $9–19 matches what comparable creators charge today: KC
  Davis $4.99–14.99, Dana K. White $15 with a 30-day refund
  ([Struggle Care](https://www.strugglecare.com/);
  [Dana K. White](https://dana-k-white.teachable.com/courses/258319)).
- **Market context (Low–Medium):** human help elsewhere runs about $40–250 an
  hour (organizers, virtual sessions, ADHD coaches; file 03, section 2.2).

### 3.3 The proposed first paid offer: a start call

**What it is (opinion, built on the evidence above).** The reader picks the
next task and a time. At that time, Charles (or, later, a trained helper) calls
for about fifteen minutes. They do step one together on the phone. The reader
finishes alone, then sends one word: "done" or "stuck." If stuck, there is one
short follow-up call. That is the whole product.

**Why this and not a guide first.**

| Reason | Label |
|---|---|
| It is exactly the vision's "help taking action." A guide is more to read. | Opinion (the vision is Charles's own words) |
| It is Dave's actual method: he sent the checklist and walked Charles through it. | Inference from the deferred-win architecture |
| It targets the people the free page didn't move, which is where guidance helps most. | Inference from High evidence |
| It needs almost no building: a payment link, a booking link, a phone. An automated check-in (step 3) needs a backend and texting consent. | Inference |
| Price can't create use, so the paid thing must itself produce use. A call does; a PDF does not. | Inference from High evidence |

**Price and terms (to decide).**

- **Fixed price in the band, $19, charged only if the call happened.** Two ways:
  pay after the call with a link, or pay up front and get an automatic refund
  if the call never happened. Both carry out "If they're not using it, I don't
  want them paying for it." No evidence compares them. Pay-after is closer to
  the vision; pay-up-front is simpler to run. **Decision.**
- **No pay-what-you-want.** It loses shame-sensitive buyers (Gneezy et al.).
- **A plain refund promise** in any case, as comparable creators offer. Its
  effect on digital sales is unmeasured (file 02).
- **Arithmetic (inference):** 15 minutes for $19 is about $76 an hour, below
  market for human help. Fifty calls a year is about 13 hours of calls. That
  fits inside ten hours a week, with room. A weekly cap of four calls (one hour)
  keeps it inside the budget.
- **Scholarship (vision):** a few free calls a month for people who can't pay,
  funded from what comes in. Fits "what the money does." **Decision** on
  whether to start with it.

**What "recorded coaching" should be (opinion).** A short recorded walk-along:
a person doing step one of a page on camera, in real time, so the viewer works
alongside. Once made, it costs nothing to serve. Under ADR-020's principle
("we don't charge for what costs us nothing to make") it should be **free**,
not paid. No evidence tests recorded walk-alongs for household tasks.

### 3.4 How and when it is offered

| Where | When | How it reads | Label |
|---|---|---|---|
| **At the point of struggle, before any win:** the "Stop for now" screen after the second move, and the "let it go" screen | When cheaper help has visibly not worked | "Want a person to start it with you? I'll call at your time." | Inference: help at the moment of struggle reads as help, not a pitch (Söderlund; stepped care) |
| **In Charles's reply** to an email-3 answer | When the reader has written about something stuck | One sentence, only if their reply asks for help | Inference; matches the existing reply rule ("if there's a guide that fits, send one") |
| **On a quiet "next win" page** linked once from the completion page | Whenever the reader chooses to go | Pull, not push: the next free page for their route, and below it the start call | Inference |
| **Not** inside the three emails | | | Keeps the shrinking rule and avoids pitching right after a win |
| **Not** at the top of the completion page | | | Licensing and post-reward dip suggest the moment of success is when people feel done |

**Conflict with ADR-020 (flag, not resolved).** The first row offers help to
someone who **has not had a win yet**. ADR-020 says paid offers come only after
a free win. **Proposal:** help offered before a first win is **free** (the
start-call pilot, capped). The paid start call is offered only after a first
win, for the next task. That keeps "win before wallet" intact but costs Charles
time on people who may never pay. **Decision.**

**When (evidence is split).** Reciprocity favors soon after real value
([Falk 2007](https://iza.org/publications/dp/1148), High). Licensing and
post-reward dips favor later. Habit takes a median of 66 days
([Lally et al. 2010](https://bps.org.uk/research-digest/how-form-habit), High),
so a maintenance product can't be judged for weeks. **Inference:** offer the
start call for the *next* task, framed as a new goal, not as "more of the
same," and never on a timer.

> **Decided 2026-10-26 (Charles):** instead of a one-to-one start call, **one
> weekly group call that anyone can join**, from the start. If only one person
> shows up, it's still the group call. Everyone benefits from everyone's wins,
> setbacks and ideas. See [ADR-022](../../../planning/decisions.md#adr-022--price-follows-what-it-costs-us-to-deliver).
> Price for the weekly call is not yet set.

### 3.5 Conflicts this section raises

| # | Vision says | Current decision says | Status |
|---|---|---|---|
| C1 | People pay for help taking action (automated help, coaching) | ADR-020: paid tier is "deeper $9–19 guides per domain" | **Resolved 2026-10-26 by [ADR-022](../../../planning/decisions.md#adr-022--price-follows-what-it-costs-us-to-deliver):** both, at different levels. Price follows cost to deliver: guides cheap, group help next, one-to-one most expensive. |
| C2 | Coaching, by phone | ADR-020 sets no coaching price. The ladder's Rung 3 ($299–2,500) predates ADR-020 and was never re-decided. operations.md requires an agreement, cancellation policy, scheduling boundary and insurance review "before coaching." | **Open.** A $19 call fits the band; anything priced like market coaching contradicts it. |
| C3 | Recorded coaching as something people pay for | ADR-020: "we don't charge for what costs us nothing to make" | **Resolved 2026-10-26 by ADR-022:** a gray area, not automatically free; may go to frequent participants. Never a paid membership people don't use. |
| C4 | Help when stuck | ADR-020: no wallet before a win | **Conflict at the struggle point.** Proposal: pre-win help free. |
| C5 | No subscription people don't use | ADR-020: subscription only if action-gated | **Compatible; the vision is stricter.** See 4.4. |
| C6 | The ladder's health check: 2–5% free-to-paid in 90 days | That figure is borrowed from software freemium (file 02, Low for us) | **Replace with counts** (section 6). |

---

## 4. Staying a customer without a treadmill

### 4.1 The escalation ladder, with prices

Each step costs more to provide and is offered only after the step below it
didn't work. This is the existing ladder with the vision's offers placed on it.

| Step | Help | Price | Status / build |
|---|---|---|---|
| 0 | The page, in doing mode | Free forever | Live |
| 1 | An appointment: calendar invite (email reminder in Phase 2) | Free | Live (calendar) |
| 2 | A friend checks on you, with their own calendar invite | Free | Live as a share; invite proposed (5.2) |
| 2½ | A recorded walk-along for the page | Free (C3) | Proposed, later |
| 3 | An automated check-in at the time: "Are you starting? What's in the way?" | Paid per use, in the band, if it proves useful (vision: "automated help that goes further") | **Later.** Build only after start calls show what people say is in the way. |
| 4 | A person: the start call | Free pilot, then $19 per use (C2, C4) | Proposed first paid offer |

**Inference (from Kast et al. 2018):** cheap, regular feedback produced effects
similar to peer groups in Chile's savings trials
([J-PAL](https://www.povertyactionlab.org/media/file-research-paper/saving-more-groups-field-experimental-evidence-chile), High).
So step 3 may eventually do much of what step 4 does. **Opinion:** build the
human step first, learn from it what the bot should say, then automate. That is
cheaper at ten hours a week than building a bot no one has tested.

### 4.2 Retention without the gym model

- **Evidence (High):** gym members on flat contracts paid more per visit than a
  pass would have cost; the business earned from non-use
  ([DellaVigna & Malmendier 2006](https://eml.berkeley.edu/%7Eulrike/Papers/gym.pdf)).
  This is the vision's "gym that everyone joins in January."
- **Evidence (High):** self-improvement apps keep about 3–4% of users at 30 days
  ([Baumel et al. 2019](https://pmc.ncbi.nlm.nih.gov/articles/PMC6785720)).
- **Evidence (High):** fresh-start dates recur and are predictable
  ([Dai, Milkman & Riis 2014](https://faculty.wharton.upenn.edu/wp-content/uploads/2014/06/Dai_Fresh_Start_2014_Mgmt_Sci.pdf)).

**What "staying a customer" means in this plan (opinion, reconciling the
vision):** the vision wants "people using it all the time and taking action,"
and also a brand people need less over time. Both hold if *using it* means
**coming back at each new transition for a new free win**: a move, guests, a
new job, a new semester, a PCS move. It does not mean a daily habit app or a
content stream. Paid help is bought per use, when a task is hard, and never
charged when unused.

### 4.3 Return points the reader chooses

**Proposal (needs a decision, see 2.4):** an explicit opt-in on the completion
page or in email 1's footer, "Send me one email at the start of spring and
before move-in season." Rules:

- At most three dates a year, each tied to a fresh start or season (New Year,
  spring cleaning, late summer move-in or PCS).
  **Evidence (Medium):** 80% of Americans said they planned to spring clean in
  2024 ([ACI](https://www.businesswire.com/news/home/20240306966220/en/ACI-Survey-80-of-Americans-Now-Spring-Clean-Every-Year)).
- One task per email, linked to a free page with `from=email-return-<season>`.
- The start call may be mentioned once, below the task, never above it.
- **It ends after twelve months** unless the reader renews it with one click.

### 4.4 If a subscription is ever proposed

The vision is stricter than ADR-020. **Proposal:** no subscription at all until
per-use help has buyers. If one is ever built, it must be action-gated (ADR-020)
**and pause billing automatically in any month with no use**, the reverse of the
gym. No evidence was found on churn for action-gated or auto-pausing
memberships (file 03, a gap). **Decision** only if a subscription comes up.

### 4.5 What "graduating" looks like

**Evidence (Medium):** FlyLady members "graduate" off the emails once routines
stick ([Wikipedia](https://en.wikipedia.org/wiki/FlyLady)); WW Lifetime members
stay free as long as they check in at goal
([WW](https://weightwatchers.com/us/blog/weight-loss/lifetime-membership));
Hinge calls deletion success
([The Drum 2024](https://www.thedrum.com/news/2024/10/03/hinge-s-cmo-her-unconventional-kpi-dates-so-great-people-delete-the-app)).

**Proposal (opinion):** graduating means **The Week runs without us.** The
reader decides it, not us. We can't observe it and won't guess.

- The return-points email after about two months (the habit median) carries one
  line: "If the week is running on its own, you've graduated. Reply 'graduated'
  and I'll stop, or keep the seasonal emails."
- After a win, Dave may appear: a graduation page with his story, as the vision
  plans. Task pages still never mention him.
- A graduate is the best referrer: they are the person the vision's Jordan
  became, sending the page to roommates.
- **Opinion:** the next step for graduates who want it is the stewardship
  curriculum, which lives in Charles's separate project (ADR-009). Mention it
  only on the founder's own pages, never inside a product.

---

## 5. Referrals

### 5.1 What the evidence says

| Finding | Source | Confidence |
|---|---|---|
| Referred customers churned about 18% less and were worth 16–25% more (bank) | [Schmitt, Skiera & Van den Bulte 2011](https://faculty.wharton.upenn.edu/wp-content/uploads/2012/04/Schmitt-Skiera-vandenBulte-2011-Referral-Programs-Customer-Value.pdf) | High (one firm, paid program) |
| Referred customers refer more; reminding them they came through a friend raised referrals 20–27% | [Gershon & Jiang 2025](https://faculty.wharton.upenn.edu/wp-content/uploads/2020/06/gershon-jiang-2024-express-referral-contagion-downstream-benefits-of-customer-referrals.pdf) | High |
| Referring makes the referrer more loyal | [Garnefeld et al. 2013](https://csl.wpcarey.asu.edu/growing-existing-customers-revenue-streams-through-customer-referral-programs) | Medium–High |
| Friend-side rewards recruit more than sender rewards; senders refer about as much with no reward, but much less when anonymous: they want credit | [Gershon, Cryder & John 2020](https://source.washu.edu/2020/07/research-shows-how-businesses-can-win-more-customers-influence-your-friends/) | High |
| Paying the referrer makes friends suspect motives | [Verlegh et al. 2013](https://dare.uva.nl/id/553a0430-0ee6-4f93-bd73-f97db1105ca2) | High |
| Bigger rewards bring in less profitable customers | [Wolters, Schulze & Gedenk 2020](https://pubsonline.informs.org/doi/fpi/10.1287/mksc.2020.1242) | High |
| Self-improvement gifts hurt recipients | [Chapman & Reshadi 2025](https://business.fiu.edu/news/2025/new-fiu-research-some-holiday-gifts-can-backfire-leading-to-hurt-feelings-bad-reviews.html) | High |
| People share what makes them look good | [Berger 2014](https://faculty.wharton.upenn.edu/wp-content/uploads/2016/11/WOM-Annual-Rev-of-Psych.pdf) | High |
| Visible cues keep word of mouth going | [Berger & Schwartz 2011](https://faculty.wharton.upenn.edu/wp-content/uploads/2011/10/BzzAgent.pdf) | High |
| **No controlled study on asking right after a win** | file 03 | n/a |

### 5.2 The mechanics

There are two different moments, and the evidence says to keep them apart
(file 03, implication 4).

**A. The checker share (before the win, accountability).** Live today as "Send
it to someone who'll check on you." It sends the page address and a line of
text. Proposed changes:

1. **Tag the link** as `from=checker-<page>` (keeping any original `from=`),
   so a friend who opens it is counted. Today the shared link drops the tag
   (`location.origin + location.pathname`), so these referrals are invisible.
2. **Give the friend a calendar invite** for a few minutes after the reader's
   time: "Check on them about the kitchen." This is the vision's exact
   mechanic. Generated in the browser, like the reader's own invite; no data
   reaches us.
3. **Keep the text task-and-time specific** ("I've set aside Saturday at 10 to
   clear my desk. Check on me after?"), never identity-based. **Evidence
   (Medium):** announcing an identity goal can backfire
   ([Gollwitzer et al. 2009](https://stafforini.com/works/gollwitzer-2009-when-intentions-go/)).
4. **Suggest someone respected.** One line: "Someone whose opinion you care
   about." (Klein et al., Medium.)

**B. The post-win share (word of mouth).** Not on the completion page today.
Proposed:

1. **One quiet line under the email form** on the completion page: "Know
   someone with a room like this? Send them the page." Tagged
   `from=friend-<page>`. Worded so the sender looks helpful and the friend is
   not told they're a mess.
2. **"Do yours at the same time"** as the share's default text: an invitation
   to do the task together, not a gift. **Opinion, untested;** it sidesteps the
   self-improvement-gift problem by making the sender a participant.
3. **"Someone sent you this"** on the completion page when the arrival tag is
   `checker-` or `friend-`: "Someone sent you this. You could do the same for
   someone." Costs nothing; the closest test found raised referrals 20–27%
   (Gershon & Jiang). Inference.
4. **The printed sheet as a cue.** The share QR already sits on every
   printable. The Week on a cabinet door is the environmental cue Berger and
   Schwartz describe. No change needed.

**C. Insiders and partners.** The largest referral source, by the evidence,
is not a button. It is Dave at the Academy, a ministry leader, a landlord or a
mentor handing over a link with a sentence (section 1.3). **Inference:** the
weekly 45-minute growth block in operations.md should go mostly here.

### 5.3 The moment to ask

- **The checker:** at the moment the reader picks a time. Already live.
- **Post-win share:** on the completion page, below the email form, never above
  it. **Inference:** no study tests asking right after a win, but people share
  what makes them look good, and "I just did this" is a good look then.
- **Charles's reply:** when a reader writes back pleased, one sentence: "The
  page is free to pass on." Human, once.
- **Never** in the three emails as an ask of its own. It would make email 2 or
  3 ask more, not less.

### 5.4 Incentives: none to the referrer

**Proposal:** no reward, cash or otherwise, to the person who refers. The free
page is already a gift to the friend. This follows Verlegh et al., Jin & Huang
([IJRM 2014](https://ideas.repec.org/a/eee/ijrema/v31y2014i1p107-116.html)),
Wolters et al. and Dose et al. ([JAMS 2019](https://link.springer.com/article/10.1007/s11747-019-00635-z)).
It is also what a trust-based brand can afford.

**If a reward is ever wanted later (opinion):** give it to the friend, in kind,
and say so openly: for example, a referred friend's first start call is free.
Gershon, Cryder & John also tested a donation arm, but the research files don't
report its result, so a "your share funds a scholarship call" idea is
**untested**. **Decision** only if Charles wants a reward.

---

## 6. Measurement

### 6.1 The north star

**First checklists finished**, the number the vision watches most. Measured as
`finished` events, split by `path` (now / appointment) and by `from` tag.

**Limits (stated plainly):** Umami counts finishes, not people, and we keep no
profiles, so a second finish by the same person also counts. The completion page
proves the reader pressed "I finished," not that the kitchen is clean
(operations.md). It's directional, and it's still better than any email metric.

**Counts, not rates, for the first year.** At a few hundred visitors, a 2%
conversion is a handful of people. Record counts and read replies (file 02,
implication 2). Umami's free plan keeps six months of history, so the monthly
scorecard row must be written before data ages out.

### 6.2 A guardrail for every growth idea

Each idea gets a success number and a guardrail number that would show it is
hurting people. Umami events are from
[operations.md](../../../planning/operations.md#external-one-time-items).
**New** marks an event or tag this plan proposes.

| Growth idea | Success number | Guardrail: stop or rethink if… | Source |
|---|---|---|---|
| Fliers at point-of-action spots | `finished` per `qr-*` tag | Scans arrive but `finished` ÷ visits for that tag stays near zero after eight weeks (the flier attracts the wrong people or overpromises) | Umami page views and `finished` by `from` |
| Flier wording test | `start-now` per tag | Any wording that raises `not-right-now` but not `finished` | Umami |
| The fork ("Not right now") | `finished` with `path=appointment` | The share of `start-now` among fork choices falls, **or** total `finished` ÷ arrivals falls (planning later is replacing starting now) | `start-now`, `not-right-now`, `finished` |
| Appointment reminders | `started-from-reminder` ÷ `time-picked` | `stopped-at-limit` + `let-go` grow faster than `started-from-reminder` (the reminders are mostly producing endings) | Umami |
| Checker share with friend invite | `shared-with-checker`; arrivals and `finished` with `checker-*` tag (**new tag**) | Replies or partner reports that the share felt like nagging; `rescheduled` rises among shared appointments | Umami; replies |
| Post-win share line | **New** `shared-after-win`; `finished` with `friend-*` tag (**new**) | Email signups per `finished` fall after the line is added (the second ask is crowding out the first), or any reply says a share felt like a judgment | Umami; MailerLite signups; replies |
| Partner handoffs | `finished` per `partner-*` tag; partners' three numbers | A partner reports people felt checked up on; "where they stopped" clusters at one step (fix the page, not the partner) | Umami; partner replies |
| The three-email sequences (all routes, office included) | Replies per route | Unsubscribes above about 1% on any one email, or any spam complaint (Gmail's bulk threshold is 0.3%; we should be far below it) | MailerLite monthly review |
| Return-date emails (if approved) | `finished` with `email-return-*` tag | Unsubscribes or complaints above the sequence emails' rate; fewer than one in ten renew at twelve months (it isn't wanted) | MailerLite; Umami |
| Free start-call pilot | Pilot callers who report "done" | Charles's call time exceeds one hour a week; callers finish no more often than appointment-only readers | Charles's log; replies |
| Paid start call | Calls held and paid | **Any charge for a call that didn't happen** (target: zero); refund requests above one in ten; free `finished` falls after the offer appears on the next-win page | Payment records; Umami |
| Struggle-point offer | Calls booked from the "Stop for now" or "let it go" screens (**new** `help-offered`, `help-clicked`) | `let-go` rises after the offer appears (the offer is pushing people out rather than helping) | Umami |
| Referral volume overall (vision: about 100 in year one) | Arrivals tagged `checker-*` or `friend-*`, and the subset that finished | Referred arrivals finish less often than flier arrivals (the shares reach people who didn't want it) | Umami |
| Revenue (vision: about $1,000, 50–100 payers in year one) | Paying customers, count | Any paying customer with no use; revenue rising while `finished` falls | Payment records; Umami |

**Evidence for humility (High):** in a 61,000-person megastudy, experts
couldn't predict which nudges would work, and few effects lasted
([Milkman et al. 2021](https://mathematica.org/publications/megastudies-improve-the-impact-of-applied-behavioural-science)).
Our own completion data should outrank this plan.

---

## 7. What to build first

Sized for about ten hours a week of Charles's time, with Claude making the code
changes and the bot doing account work. Hours are Charles's, estimated.

| # | Item | Who does it | Charles's time | Needs a decision? |
|---|---|---|---|---|
| 1 | **Fix the office promise:** wire `entry-office`, or remove the form on office pages | Bot (MailerLite) | None | Yes, which one |
| 2 | **Tag shared links** (`checker-*`) and add the friend's calendar invite to the checker share | Claude (entry.js) | None | No |
| 3 | **Monthly scorecard from Umami:** finishes by path and tag, fork split, shares | Bot | 15 min a month to read it | No |
| 4 | **Flier and partner kit:** one flier per page with matching headline and plain address; a partner handout with the one-sentence handoff script; tags per place and partner | Claude drafts; bot generates tagged codes | 1–2 h a week handing them to two or three insiders (Dave first) | No |
| 5 | **Free start-call pilot,** ten people, offered at the struggle screens and in replies | Claude adds the offer line and events; Charles makes the calls | About 1 h a week, capped | Yes (C4) |
| 6 | **Post-win share line and "someone sent you this"** on completion pages | Claude | None | No |
| 7 | **First-sale gates** from operations.md: refund policy, checkout terms, entity, records; plus the coaching gates (agreement, cancellation, scheduling, insurance) | Charles, with the bot's help | A few hours once | Already required |
| 8 | **Paid start call,** $19, charged only when it happens, on the next-win page | Claude and bot | Within the 1 h call cap | Yes (C1, C2, price terms) |
| 9 | **Return-date opt-in** (spring, move-in or PCS season, New Year) | Claude and bot | None | Yes (ADR-016) |
| 10 | **Later:** automated check-in (step 3), recorded walk-alongs | Later | — | Yes, once calls show what people need |

**What not to build:** a subscription, a community, a referral reward, a parent
sequence, more guides before anyone has bought help, or any A/B test that needs
more traffic than we have.

---

## 8. Decisions Charles needs to make

1. **First paid offer:** help taking action (a start call) before deeper guides, against ADR-020's guide-first wording (C1)?
2. **Start-call price and terms:** $19, charged only if the call happened: pay after, or pay up front with automatic refund?
3. **Pre-win help:** keep help offered at the struggle point free, to honor "win before wallet" (C4)?
4. **Who makes the calls:** Charles alone, capped at one hour a week, until a helper or recording exists?
5. **Recorded coaching:** free once made, per ADR-020's "don't charge for what costs us nothing" (C3)?
6. **Coaching price band:** retire the old $299–2,500 Rung 3, or keep it parked (C2)?
7. **Office route:** wire `entry-office` or remove its form, since the completion page promises emails?
8. **Return-date opt-in:** allow a separate, chosen, at-most-three-a-year list despite ADR-016's "no fourth email"?
9. **Subscriptions:** none until per-use help sells, and if ever, action-gated and auto-paused when unused?
10. **Referral rewards:** none to the referrer; nothing to the friend unless you choose an in-kind gift later?
11. **Parents:** no parent email flow until ADR-010 is re-decided?
12. **Scholarship calls:** start a few free calls a month for people who can't pay from day one, or after revenue?
13. **Health check:** replace the 2–5% free-to-paid target with plain counts for year one?

---

## Notes on the research files

- **Fishbach & Dhar 2005:** the three files rate it differently. I read the
  abstract on 2026-10-26; it supports the claim as file 01 states it. Rated
  Medium here because it is lab work.
- **Prestwich et al. 2012 (partner-based plans):** file 03 links a White Rose
  record for it, but that record (eprint 10346) is a different, earlier study:
  86 students, decision balance sheet plus implementation intentions. The 2012
  paper's results remain unretrieved (*Health Psychology* 31(4), 486–495,
  doi 10.1037/a0027672). Nothing in this plan relies on it.
- **Ariely & Wertenbroch 2002** (self-imposed deadlines) was retracted in
  September 2026 and is not used. Shampanier, Mazar & Ariely 2007 (zero price)
  is not used either.
