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

### 3. Mechanisms compared, and the pick

**Revised 2026-10-23 per Charles.** Screen 2 offers **one choice: "Remind me
when I'm home."** The reader picks a time, then picks how to be reminded:
**Add to my calendar** or **Email me the checklist at that time**. Both deliver
the same thing at the same time, so this is one offer with two ways to receive it.

| Mechanism | Timing | Data we hold | Cost | Verdict |
|---|---|---|---|---|
| **Calendar link / `.ics`** | Good, in the reader's own calendar | None | About a day to build | **Offered** |
| **Timed email** | Good, arrives at the chosen time | Email address, until sent | Separate MailerLite group and automation | **Offered** (pending Charles's approval of the spec below) |
| SMS | Best: texts are read within minutes | Phone number, the most personal data | About 1–2 cents per text, plus US 10DLC brand and campaign registration (fees and weeks of review) and TCPA written consent | **Defer** until reminder usage is proven |
| Web push | Poor on iPhone: works only after "Add to Home Screen" | Push token | Service worker and permission prompt | No |

**SMS, honestly:** it has the best timing of any option. It is deferred, not
rejected. Revisit it once calendar and email reminders show that people save
reminders and come back to finish. If returns are high but email open rates are
low, SMS is the next test.

**ADR-020 fits.** ADR-020 is about list signup before the win. A timed email
that sends one checklist at a time the reader chose is a delivery, not a
signup. It stays separate from the newsletter and entry sequences. See the
clarifying note proposed in `planning/adr-020-win-before-wallet.md`.

#### Hand-off to Mailer Bot: PENDING CHARLES'S APPROVAL. Do not build yet.

- **Form:** a new embedded form `reminder`, separate from `00ZwEr`. It is shown
  only on screen 2 after the reader taps "Email me the checklist at that time."
- **Fields:**
  - `email` (required)
  - `moment`: `guests` | `one-room` | `underwater`
  - `remind_at`: date and time in ISO 8601 with the reader's UTC offset, set by
    the time button. The reader never types it.
- **Group:** `reminder-<moment>`. **Not** `entry-*`, and not any newsletter
  group.
- **Automation (one per group):** trigger when a subscriber joins the group →
  wait until the date in `remind_at` → send one email → remove the subscriber
  from the group. Re-entry on (a reader can set a new reminder). Resend to
  unopens off. No second email.
- **Email copy draft:**
  - From: Mr. Life Manager. No signature.
  - Subject: **Your [guests / one-room / fresh-start] checklist is ready when you are**
  - Body: "You asked us to send this now. When you're home and have about
    [35 / NN / 40] minutes, open the checklist and start at step one.
    [Open the checklist] → `/<moment>.html?from=reminder`
    This is the only email we'll send for this reminder."
  - Footer: the standard MailerLite unsubscribe link and address.
- **Consent line under the field:** "We'll send one email at the time you
  picked, with the link to your checklist. We won't add you to any list unless
  you sign up later."
- **Data:** after the email is sent, delete the subscriber unless they are also
  in an `entry-*` group because they signed up through the normal form.
- **Never:** add reminder subscribers to the entry sequences, a newsletter or
  any promotion.

### 4. Why this fits the principles

- **Principle 11, completion converts:** reading the steps on a bus feels like
  progress and isn't. Holding them until the reader is home protects the
  feeling that should drive the action. It is one offer on each screen.
- **Principle 8, dignity:** "Not home yet?" and "Not yet" describe the situation.
  They never judge the reader.
- **No squeeze:** there is no countdown and no "don't miss out," and email is
  optional, never required. "I'm home now. Show me the steps." is always on screen, and
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

## The pick (revised 2026-10-23)

**Superseded:** the earlier pick was calendar only. The current pick is in
"Marketing for people who are not home," section 3: one choice, "Remind me
when I'm home," delivered by calendar or by a single timed email. The pick
serves principle 11 (one offer, paced behind readiness), principle 8 (no
judgment), principle 9 (simple) and principle 4 (a system does the
remembering). SMS is deferred.

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

The calendar option needs nothing. The timed email option needs the new
`reminder-<moment>` groups and automation in the hand-off above, **pending
Charles's approval**. The entry sequences and form `00ZwEr` don't change.

## Conflicts found

- ADR-020: resolved by Charles's clarification that a timed delivery is not a
  list signup. A clarifying note is proposed in the ADR file (docs only).
- `MAILERLITE-SETUP.md` says the checklist is "never promised by email." That
  line covers the entry sequences. It needs a matching note once the reminder
  group is approved.
- ADR-016 is under review. This proposal doesn't depend on how it ends.
- The measurement depends on Charles's open decision about an analytics tool.

## Next step, if approved

Build the button on one page (underwater, the most-shared), on its own branch
and pull request, and measure for two weeks before adding it to the other four
pages.
