# Deferred Win — proposed architecture

**Status:** Phase 1 **live on two pages**, 2026-10-26: [underwater](../products/landing/underwater.html)
and [one-room](../products/landing/one-room.html). Scope is **the first win only**.
**Problem and research:** [deferred-win.md](../docs/research/deferred-win.md) ·
**Decision:** [ADR-021](decisions.md#adr-021--when-the-reader-cant-act-yet-ask-for-a-when)

---

## The model: what Dave did, at scale

Charles could use Dave's checklists because Dave **sent them, told him they
existed, and walked him through them.** A page can't walk anyone through
anything. It can do the four things around the walkthrough:

1. **Name the exact problem** so the reader recognizes it as theirs.
2. **Get a decision**: do it now, or pick the exact time.
3. **Show up at that time** with the task ready on step one.
4. **Close every exit** between reading and doing.

The governing idea is Dave's own: [close the exits](../frameworks/remove-the-excuse.md),
applied to the reader instead of the garage. Every point where a reader can
drift away from action is an exit, and the design's job is to close it.

---

## The flow

```
  Arrive (QR, link, search)
        │
        ▼
  1. RECOGNIZE — headline names the exact situation
        │
        ▼
  2. THE FORK — "Are you where this happens right now?"
        │                              │
     Yes, I'm here                 Not right now
        │                              │
        │                              ▼
        │                    3. DO THE PORTABLE PART NOW
        │                       (decide + prepare: pick the zone,
        │                        name your excuses, check the exits)
        │                              │
        │                              ▼
        │                    4. SET THE APPOINTMENT
        │                       date AND time · fresh-start defaults
        │                       → calendar invite (default)
        │                       → email reminder (optional)
        │                       → "send to someone who'll check on you"
        │                              │
        │                              ▼
        │                       "That's decided."  ← the café win
        │                              │
        │                       … at the chosen time …
        │                              │
        │                    5. THE RETURN — reminder opens the page
        │                       straight into the steps, "reserved for you"
        │                              │
        │                    Can't now? → move it (limited times)
        │                              │      → then it ends
        ▼                              ▼
  6. THE STEPS (doing mode, one step per screen)
        │
        ▼
  7. FINISHED — completion page; then the existing "keep it" offer
```

---

## The exits, and how each one gets closed

| Exit (how a reader drifts away) | How it gets closed |
|---|---|
| **"Interesting, I'll come back to it."** | There is no "save for later." The only alternative to *now* is a **specific date and time**. Date alone barely works; date and time does. |
| **The experienced reader's habit:** read it, agree, move on | Name it on the page, in Dave's spirit: *"You've read things like this before. Reading it isn't doing it. Pick now or pick a time."* Dave's glazed eyes, said out loud. |
| **Nothing to do from the café** | Every page puts its **portable steps first**: decide and prepare work from a phone (choose the zone, block the time, list the excuses, check when the donation place is open). The reader leaves having done something real. |
| **Too much effort to schedule** | One tap on a default: **Tonight · Tomorrow evening · Saturday morning · Monday**. Fresh-start times as defaults. A custom time is a second tap. |
| **The reminder arrives and the page is gone** | The reminder links to the page **already in doing mode**, past the portable steps they finished. |
| **The reminder reads like spam** | Specific and reserved: *"Your two hours for your desk are tonight at 7. Step one is ready."* No branding, no other offers. |
| **"Not tonight" forever** | **Move it twice, at most.** The third time is honest: *"Either now, or let this one go."* Then nothing more is sent. |
| **Wandering off to other pages mid-task** | No menus or links to other guides inside the flow. One task until it's finished (already true of entry pages). |
| **Nobody notices if they skip it** | Dave's rule: *have someone check you.* Optional: send the appointment to a friend. Free, no data from us, and the first step toward human help. |

---

## Escalation: the same task, more help

Each step costs more to provide, so it's offered only after the step below it
hasn't worked. **Only steps 0–2 are in scope now.**

| Step | Help | Cost to us | Status |
|---|---|---|---|
| 0 | The page itself, doing mode | Nothing | Live |
| 1 | An appointment: calendar invite or email reminder | Nothing / very little | **Build now** |
| 2 | A friend checks on you (share the appointment) | Nothing | **Build now** |
| 3 | A bot checks in at the time: "Are you starting? What's in the way?" | Some | Later |
| 4 | A person walks you through it, live or on video (Dave's actual method) | Real time; paid | Later |

---

## Phase 1 — what to build first (no backend)

Works on the current static site and needs no new accounts.

1. **The fork**, after the framing on each entry page: "I'm there now" (existing
   doing mode) or "Not right now" (the appointment flow).
2. **Portable steps marked per page.** Each page flags which of its steps can be
   done away from the space. The appointment flow shows those first.
3. **Time picker** with the four defaults plus custom.
4. **Calendar invite**, generated in the browser:
   - `.ics` download (iPhone and most calendars)
   - Google Calendar link (Android)
   - The event carries the first step and the return link.
5. **Return link** that opens doing mode at the right step and counts moves
   (`?resume=…&moved=1`), so the move limit holds without a server.
6. **"Send to someone who'll check on you"**, using the phone's own share sheet.
7. **Measurement:** visits to the completion page tagged by which path the
   reader took (now vs. appointment), using the existing source tags. No
   cookies or profiles.

**Pilot on one page first** (office or underwater), compare completions, then
roll it to the rest.

### How Phase 1 was built

- Opt-in per page: `data-defer="on"`, `data-minutes`, `data-task` on `<html>`.
  Steps that can be done away from home carry `data-portable`.
- All behavior lives in the shared `assets/entry.js`; styles in `entry.css`.
  `check_entry_pages.py` fails if a page turns it on without the button or
  settings, or if the script loses the calendar invite or the move cap.
- Completion links carry `path=now` or `path=appointment`, alongside `from=`.
- The return link in the invite is `?resume=1`, plus `moved=N` after a move and
  the original `from=` tag.

### Comparing pages and places

The test is **which page gets traction in which places and populations**, not a
true A/B test: each page reaches different people with a different problem.

**Every printed QR code gets its own `from=` tag**, so places can be compared.
Format: `qr-<place>-<page>`, lowercase, hyphens, 40 characters at most, no
personal names. Examples:

- `https://mrlifemanager.com/underwater.html?from=qr-boise-cafe-underwater`
- `https://mrlifemanager.com/one-room.html?from=qr-bsu-board-one-room`

The tag rides through the calendar invite and reaches the completion page, so a
completion can be traced back to the flier that started it. **Note:** this only
works once visitor measurement is turned on, and only if that service keeps the
query string on page views. Check that when choosing it.

## Phase 2 — email reminder

MailerLite date field plus a date-based automation. **Known limit:** it fires
once a day at 4:00 AM UTC, so it hits the day, not the time. Needs testing
before it's offered: whether a delay step can land it in the evening, and
whether a resubmitted form can update the date (for "move it").

## Phase 3 and later

Text messages (needs a provider, a small backend, and explicit consent under US
texting rules), bot check-ins, and human walkthroughs. Not now.

---

## Open questions

1. **Which page pilots it?** Office (a known first audience) or underwater (the
   most common pain).
2. **Is two moves the right cap?** It's a judgment call with no research behind
   the number.
3. **How strongly to name the "reading isn't doing" habit** without sounding
   preachy to an experienced reader.
