# The Deferred Win — reading somewhere you can't act

**Status:** Problem framing and research, 2026-10-26. No solution chosen yet.
**Decision recorded:** [ADR-021](../../planning/decisions.md#adr-021--when-the-reader-cant-act-yet-ask-for-a-when)

---

## The problem

Feedback from users, plus the QR-code plan (cafés, bookstores, campuses): people
will often read a page **somewhere they can't act on it**. Every page assumes
the reader is standing where the task is. A QR code puts them somewhere else.

Experienced readers (25–30 and up) make it worse, not better. They've read the
blogs and the posts, and they know the drill: read it, agree with it, file it
under "someday." That's the opposite of what this site is for.

**As a site problem:**

> The site turns reading into action only when the reader is already in the
> space. For readers who arrive somewhere else, it has no way to carry the
> intention from *here* to *there*. Reading becomes agreement, and agreement
> becomes "someday."

**As a job story:**

> **When** I come across a page that names a problem I really have, but I'm
> somewhere I can't act on it,
> **I want** to commit to a specific time to do it, with as little effort as
> possible right now,
> **so I can** actually do it when I'm back in the space, instead of agreeing
> with it and forgetting it.

**Success:** the reader leaves with a specific *when*; at that time the page
comes back to them, already on step one; they finish it. Completion stays the
measure, not reminders sent or links clicked.

## Charles's decisions (2026-10-26)

- **Asking for a way to reach them at the right time is part of the win, not an
  ask before it.** They are signing up to get the task back when they can do it,
  not for a newsletter. See ADR-021.
- **No snoozing forever.** Rescheduling is capped, then it ends.
- **Reading alone is not success.** Every page needs a path from "read it" to
  "did it."

## How this connects to Dave

Dave's documents run in five stages: decide, prepare, reset, place, maintain
([principles](../../frameworks/dave-principles.md)). **The first two stages
can be done anywhere. The last three need the space.** At the QR moment, "do it
now" can't mean the reset. It can mean *decide now* (principle 1: do I really
want this?) and *set the date* (principle 23: set a date and have someone check
you). The office page's first step, "Put two hours on your calendar," is
already doable from a café.

---

## Research

### What works

| Finding | Evidence | Confidence |
|---|---|---|
| **About half of intentions never become action.** The median share of people who intend to act but don't is about 47%. | [Sheeran & Webb 2016 review](https://eprints.whiterose.ac.uk/id/eprint/107519/3/The); physical-activity meta-analyses put it at 46–48% ([Rhodes & de Bruijn](https://www.researchgate.net/publication/236036780_How_big_is_the_physical_activity_intention-behaviour_gap_A_meta-analysis_using_the_action_control_framework)). | High that the gap is large; the exact figure varies by domain |
| **A specific "when and where" plan closes much of that gap.** Implementation intentions: a meta-analysis of 94 studies found a medium-to-large effect (d = 0.65). A later, larger analysis reportedly found smaller effects for behavior change; that figure is unverified. | [Gollwitzer & Sheeran 2006](https://howtostopprocrastinating.org/research/gollwitzer-2006-implementation-intentions/), *Adv. Exp. Soc. Psych.* 38, 69–119 | High for the effect; Medium for its size |
| **Date AND time matters; date alone doesn't.** In a randomized trial with 3,272 employees, writing down a date raised flu-shot uptake 1.5 points (not significant). Writing down a date *and time* raised it 4.2 points (significant). | [Milkman et al. 2011, *PNAS*](https://www.pnas.org/doi/pdf/10.1073/pnas.1103170108) | High |
| **Making a plan relieves the nagging feeling of an unfinished task.** Unfinished goals intruded on unrelated work; once people made a specific plan, the intrusions stopped. | [Masicampo & Baumeister 2011, *JPSP*](https://users.wfu.edu/masicaej/MasicampoBaumeister2011JPSP.pdf) | High |
| **One well-timed, specific reminder does the work; extra reminders add little.** Reminders raised savings goal attainment; specific content helped most; extra late reminders had no added effect. | [Karlan et al. 2016, *Management Science*](https://www.nber.org/papers/w16205) | High |
| **"It's reserved for you" framing works.** Of 19 text messages tested, the best framed the flu shot as already reserved for the patient. Reminders raised COVID booster uptake 21%; free rides added nothing beyond the reminder. | [Milkman et al. 2021, *PNAS*](https://www.pnas.org/doi/10.1073/pnas.2101165118); [Milkman et al. 2024, *Nature*](https://www.nature.com/articles/s41586-024-07591-x) | High |
| **Any reminder channel beats none; text and phone perform about the same.** Text reminders raised attendance about 14% over no reminder. Email has almost no direct evidence. | [Cochrane review](https://researchonline.lshtm.ac.uk/id/eprint/1386850/1/CD007458.pdf); [realist review 2016](https://www.tandfonline.com/doi/full/10.2147/PPA.S93046) | Medium–High |
| **Fresh starts motivate.** Goal-pursuit spikes after the start of a week, month, semester, a birthday or a holiday, and people see upcoming landmarks as good times to start. | [Dai, Milkman & Riis 2014, *Management Science*](https://faculty.wharton.upenn.edu/wp-content/uploads/2014/06/Dai_Fresh_Start_2014_Mgmt_Sci.pdf) | High |

### What others have done

| Who | Approach | Lesson for us |
|---|---|---|
| **FlyLady** (home cleaning) | 31 "baby steps," one a day, starting with "shine your sink," delivered by daily emails. Members "graduate" once routines stick and no longer need the emails. ([Wikipedia](https://en.wikipedia.org/wiki/FlyLady)) | A tiny first action and a scheduled return work. A daily email stream breaks our no-nagging rule. |
| **Duolingo** | Algorithmically timed daily reminders; success = a lesson finished within two hours of the notification. The system penalizes repeats to avoid fatigue. Reported lift: 0.5% daily active users. ([Yancey & Settles 2020](https://research.duolingo.com/papers/yancey.kdd20.pdf)) | Measures completion right after the reminder, which is the right measure. Heavy recurring nudges suit a habit app, not a one-time task. |
| **Read-later apps** (Pocket, Instapaper) | Save now, read later. | No credible data on how much saved material is never read; only anecdotes. Pocket shut down in 2025. "Save for later" without a time is the failure mode we're avoiding. |
| **Location reminders** ("when I get home") | Phone reminders that fire on arrival. | Researchers report they're still not very effective in practice, and a website can't create them. Not a priority. ([Wang & Pérez-Quiñones 2014](https://dl.acm.org/doi/10.1145/2638728.2641718)) |

### Don't cite

- **Self-imposed deadlines (Ariely & Wertenbroch 2002)** — widely quoted, but
  **retracted in September 2026** over data tampering, and a replication failed
  to reproduce it ([Retraction Watch](https://retractionwatch.com/2026/09/03/procrastination-study-duke-dan-ariely-psychological-science-data-colada-tampering-retraction/)).
- **"Starting a task makes you finish it" (Zeigarnik effect)** — the original
  finding is about memory, not completion, and the completion claims found are
  in blogs, not controlled trials. Plausible; unproven.

---

## What this means for the design

Not a solution yet; these are the requirements the research supports.

1. **Ask for a date and a time, not "later."** Date alone did nothing in the
   flu-shot trial.
2. **The appointment is itself a win at the café.** A specific plan relieves
   the nagging (Masicampo & Baumeister). The page can honestly say "that's
   decided" and mean it.
3. **Offer fresh-start times as defaults:** tonight, Saturday morning, Monday,
   the first of the month.
4. **One reminder, at the chosen time, specific and "reserved":** *"Your two
   hours for your desk are tonight at 7. Step one is ready."* It opens the page
   straight into step one.
5. **Let them move it a limited number of times, then end it** with the link
   and no further messages.
6. **Put the portable steps first.** Decide and prepare can happen anywhere.
   Every page should have something real to do from a phone in a café.
7. **Expect about half to still not do it.** That's the base rate, not failure.
   Measure completion, and compare against it.

## Technical constraints found

- **A calendar invite (`.ics` file)** can carry an exact date and time, needs
  no account or contact details, and works on a static site. The cheapest option
  with the strongest privacy.
- **MailerLite's date-based automation fires once a day at 4:00 AM UTC** and
  uses a date field (YYYY-MM-DD), per its
  [help docs](https://www.mailerlite.com/help/how-to-set-up-automation-triggers).
  So email can hit the right *day* but not, as far as we know, the right *time*.
  Whether a delay step can push it to an evening hour is unverified.
- **Text messages** need a provider, a small backend, and explicit consent under
  US texting rules. The evidence says text works about as well as a phone call,
  but it's the biggest build and the biggest ask.
