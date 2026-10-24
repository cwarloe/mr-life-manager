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
