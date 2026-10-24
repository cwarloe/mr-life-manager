# Save for later: a reminder for readers who can't act yet

**Status:** Proposal, 2026-10-23. Docs only. Nothing is built, sent or published.
**Owner:** MLM Growth Steward. **Decision:** Charles.

## The problem

Most visitors from social media open an entry page (guests, underwater,
first-night, one-room, office) on a phone while they are away from home. They
read the steps, feel that they have made progress, and close the page. They
have done nothing. Principle 11 calls this the worst outcome: the feeling of
progress replaces the action that the feeling should have started.

These readers can't act right now. The page should help them choose a time to
do the steps at home, so reading on the bus does not count as doing.

## Marketing for people who are not home

**Added 2026-10-23 from Charles's direction.** For QR flyers (coffee shops,
community boards) and for social video, we assume the reader is **not home**.
The ad makes them want the checklist. The site then holds the steps back on
purpose until the reader is home and ready, and checks that they are ready
before it shows the steps. The delay is there to help the reader finish. It is
not a gate: the steps page always stays one tap away, and email is never
required.

### 1. The video and flyer script (about 18 seconds)

No steps appear in the ad. The ad sells the moment and the reminder.

| Time | On screen (and spoken) |
|---|---|
| 0–3 s | **Do you want to get your home in order?** |
| 3–7 s | **People are coming over tonight, and the house isn't ready.** |
| 7–11 s | **There's a room in your house that nobody uses anymore.** |
| 11–15 s | **The whole house needs doing, and you don't know where to start.** |
| 15–18 s | **Not home yet? Scan this, pick yours, and we'll remind you when you're home.** |

- The flyer prints the same five lines, with the QR code next to the last line.
  The QR code opens `mrlifemanager.com/start?from=flyer`.
- On video, the last frame shows the QR code and the profile link. The profile
  link opens `/start?from=social`.
- The three moments match three existing pages: guests, one-room and underwater.
- We use "isn't ready," never "mess," which follows the site wording rule.

### 2. The landing flow for `?from=flyer` and `?from=social`

**Screen 1: "What's going on right now?"** There are three buttons, one for each
moment in the ad:
- People are coming over tonight.
- There's a room nobody uses anymore.
- The whole house needs doing.

**Screen 2: the reminder choice, not the steps.**
> **When will you be home?** Pick a time, and your calendar will remind you with
> the checklist.
- Buttons: **Tonight at 7** · **Tomorrow at 9 am** · **Saturday at 10 am**.
  Each one opens a Google Calendar link or downloads an `.ics` file.
- A small link below: **I'm home now. Show me the steps.**

**The guests exception.** Guests are coming *tonight*, so a reminder tomorrow is
no use. The guests choice offers **In 1 hour** · **At 5 pm**, and also
**I'm home now. Show me the steps.**

**Screen 3: the readiness check.** The calendar event links to the page with
`?from=reminder`. Before the steps, the page asks:
> **Are you home with about [time for that checklist]?**
- **Yes, show me the steps** opens the checklist at step one.
- **Not yet** opens screen 2 again, so the reader can pick a new time.

Use the checklist's own time: about 35 minutes for guests, about 40 minutes for
underwater, and the one-room page's stated time for one-room.

**What stays the same:** visitors without `?from=flyer`, `?from=social` or
`?from=reminder` (search, direct, shared links) go straight to the page as
today. The plain entry-page URLs always show the steps.

### 3. Mechanisms compared

| Mechanism | Works on iPhone? | Data we hold | Cost | Verdict |
|---|---|---|---|---|
| **Calendar link / `.ics`** | Yes | None | About a day to build, no service | **Pick** |
| Email reminder | Yes | Email address | New field, group, automation | Charles's decision (see below) |
| Web push | Only after "Add to Home Screen" | Push token | Service worker, permission prompt | No. Most iPhone readers can't get it |
| SMS | Yes | Phone number | Paid service, TCPA consent, 10DLC registration | No. Too much cost and data |

**Email reminder needs an exception to ADR-020.** ADR-020 puts the email ask
after the win, and the MailerLite specification says the checklist is never
promised by email. An exception for away-from-home scans only is **Charles's
decision**. If he approves it, the hand-off to Mailer Bot would be:

- New form, separate from `00ZwEr`, shown only on screen 2 for
  `?from=flyer|social`, as an alternative to the calendar buttons (still one
  offer on the screen: "remind me").
- Fields: `email`, `guide` (`guests` | `one-room` | `underwater`),
  `remind_at` (date and time, in the reader's local time zone, from the button
  they picked).
- Group: `reminder-<guide>`. It does **not** join the entry sequence groups.
- Automation: wait until `remind_at`, then send one email: subject "Your
  [checklist name] is ready when you are." The body has one link to
  `/<guide>.html?from=reminder`. Then it stops. No follow-up, no re-entry,
  resend to unopens off.
- Consent text under the field: "We'll send one email at the time you picked,
  with the link to your checklist. Nothing else unless you sign up later."
- After the email, the subscriber is deleted, or kept only if they later sign up
  through the normal form after finishing.

### 4. Why this fits the principles

- **Principle 11, completion converts:** reading the steps on a bus feels like
  progress and isn't. Holding them until the reader is home protects the
  feeling that should drive the action. It is one offer on each screen.
- **Principle 8, dignity:** "Not home yet?" and "Not yet" describe the situation.
  They never judge the reader.
- **No squeeze:** there is no countdown and no "don't miss out," and email is
  never required. "I'm home now. Show me the steps." is always on screen, and
  the plain page URL always shows the steps. The delay is offered for the
  reader's success, and the reader can always skip it.
- **Principle 9, simple:** three screens and three times, with no account.

### 5. Measurement

Track these five numbers for each moment and each source (`flyer`, `social`):

1. **Scans or visits** to `/start` with `?from=flyer` or `?from=social`
2. **Reminders saved:** calendar buttons tapped
3. **Reminder returns:** visits with `?from=reminder`
4. **Readiness yes:** "Yes, show me the steps" tapped
5. **Completions:** the last step checked. **This is the number that matters.**

Also track "I'm home now" taps and "Not yet" reschedules. A high "Not yet"
rate means the reminder times are wrong. Use a separate QR code for each flyer
location (`?from=flyer-<place>`) to see which locations work.

## What already exists, and what limits the design

- Each entry page opens with "Ready to start?" and two buttons: "Just the
  steps" and "Print it." The steps are on the page with nothing to sign up for.
- The one MailerLite form (`00ZwEr`) appears only **after** the reader
  finishes the steps (ADR-020, win before wallet). Email 1 sends *The Week*,
  and the specification says the entry-page steps are **never promised by
  email** (`products/landing/emails/MAILERLITE-SETUP.md`).
- Each sequence is three emails and then nothing more. There is no
  behavior-based branch (ADR-016, under review since 2026-10-03).
- Principle 11: offer one thing at a time, pace delivery behind action, and
  measure completion, not downloads.

## Options

### A. "Add a reminder to my calendar" (no email needed)

One button opens a small choice: **Tonight at 7**, **Tomorrow morning**, or
**Saturday morning**. The reader taps one and gets either a Google Calendar link
or an `.ics` file (Apple and Outlook calendars). The event is called
"Underwater checklist: 40 minutes". Its description has the first step and the
page link with `?from=reminder`.

- **Good:** no email address, no account and no list. The reminder appears at
  home time, in an app the reader already trusts. The site never holds anything
  about the reader.
- **Costs:** a small script on each page (about 40 lines, no third-party
  service). Building an `.ics` file in the browser needs no server.
- **Limits:** we can't confirm the event was saved. We only see whether the
  reminder link was opened (`?from=reminder`).

### B. "Email me this checklist tonight"

The reader types an email address, and the checklist arrives at 7 pm their time.

- **Good:** familiar, and the reader can open it easily.
- **Costs:** it conflicts with three existing rules. It puts the email ask
  before the win (ADR-020). It promises the entry-page steps by email, which the
  MailerLite specification forbids. It also needs a new form field, a new group
  and a new timed automation. In practice the reader joins the mailing list to
  get a reminder, which is a small squeeze.

### C. Text message reminder

- **Good:** the most likely of all the options to be seen.
- **Costs:** a paid SMS service, a phone number, carrier consent rules (TCPA,
  10DLC registration) and the most personal data of any option. That is too
  much system for a reminder (principle 9).

### D. "Save to home screen" or bookmark

- **Good:** free, and nothing to build.
- **Costs:** nothing prompts the reader later, so this is the same as "I'll
  remember." Principle 4 says systems beat memory. It also has different steps
  on iPhone and Android.

## The pick: A, the calendar reminder

The calendar reminder is the only option that adds no email ask, no new data
and no rule conflict. The reminder arrives when the reader is home, which is the
point of the feature.

- **Principle 11, completion converts:** the reminder brings the reader back to
  do the steps, not to read more. It is one offer, and it replaces nothing.
- **Principle 8, dignity:** "Not home yet?" describes the situation. It does not
  judge the reader.
- **Principle 9, simple:** one button and three times. Nothing to maintain.
- **Principle 4, systems beat memory:** the calendar does the remembering.
- **ADR-020:** the email form stays where it is, after the win.

Option B should not be offered next to A. Two save options would break
"one offer at a time." If Charles still wants email, the only honest version
needs a decision to change the MailerLite specification, so it is not part of
this proposal.

## Where the reminder appears

- **Inside the existing "Ready to start?" block,** as a third choice under the
  two buttons, written as plain text so it doesn't compete with them:
  > **Not home yet?** Add the checklist to your calendar, and the steps will be
  > there when you get home.
- Show it to **all visitors.** It does not depend on `?from=social` or on
  detecting phones. Anyone at their desk ignores it, and it costs nothing.
- **Never mid-task.** It disappears once the reader taps "Just the steps" or
  checks off a step. It does not appear on completion pages or in printables.
- One line in the profile-link page and in video captions can say the same
  thing: "Save the checklist to your calendar for tonight."

### Copy

- Button: **Add the checklist to my calendar**
- Choices: **Tonight at 7** · **Tomorrow morning at 9** · **Saturday at 10**
- After tapping: "Your calendar has the checklist for [time]. The link opens
  this page at step one."
- Calendar event title: "[Checklist name]: [minutes] minutes"
- Calendar event description: "Start with step one: [step 1 heading].
  [page link]?from=reminder"

No countdowns, no "don't lose this," and no "you'll forget." The reminder is a
tool the reader chose.

## Measurement

The question: did readers who saved a reminder come back and finish?

1. Count `reminder_saved` events on each page, using the analytics tool Charles
   chooses (still an open decision).
2. Count visits with `?from=reminder`. Visits divided by saves gives the
   return rate.
3. Count completions (the last step checked) on `?from=reminder` visits.
   **This is the number that matters.**
4. Compare the completion rate for social visitors before and after the change.

Until an analytics tool is chosen, step 2 shows up in server or host logs as
`?from=reminder` visits.

## Privacy

- The calendar event is created on the reader's device. The site sends and
  stores nothing.
- The Google Calendar link sends the event text to Google only because the
  reader opens it in their own account.
- No email address, phone number or cookie is needed. Nothing to add to the
  privacy page except one line that the reminder link carries `?from=reminder`.

## MailerLite

**No changes are needed.** The pick uses no form, field, group or automation.
No hand-off to Mailer Bot is needed. If Charles chooses option B later, it would
need a new hand-off: a `remind_at` field, a new group and a timed automation,
plus an amendment to the MailerLite specification and ADR-020.

## Conflicts found

- Option B conflicts with ADR-020 and with the MailerLite specification line
  "the entry-page action sheet is available before signup and is never
  promised by email." This is why B is not the pick.
- ADR-016 is under review. This proposal does not depend on how that review
  ends.
- The measurement steps depend on Charles's open analytics-tool decision.

## Next step, if approved

Build the button on one page (underwater, the most-shared), on its own branch
and pull request, and measure for two weeks before adding it to the other four
pages.
