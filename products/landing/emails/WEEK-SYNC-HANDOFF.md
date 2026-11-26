# MailerLite handoff: revised weekly checklist emails

Prepared November 26, 2026. This file preserves the owner's authorized handoff;
it does not mean an account bot has been launched or the private account has
been updated. The revised PDF was published at its existing URL. Current saved
MailerLite copy and automation status have not been inspected in this task.
Use the current sequence files, not copies pasted into an older chat.

## Prompt for the account operator

Update the existing Mr. Life Manager email sequences in MailerLite to match
the latest files under `products/landing/emails/` in `cwarloe/mr-life-manager`:

- [guests-sequence.md](guests-sequence.md)
- [underwater-sequence.md](underwater-sequence.md)
- [first-night-sequence.md](first-night-sequence.md)
- [one-room-sequence.md](one-room-sequence.md)
- [office-sequence.md](office-sequence.md), preserving its current activation
  status. If the office automation does not exist, report that; this copy-sync
  task does not authorize creating or activating it.

The revisions align the emails with the updated weekly checklist: maintain
areas already reset, plan remaining work, avoid universal ten-minute routine
and four-minute sink promises, and describe the sheet as an adaptation of
Dave's weekly schedule. The source files define the exact replacement text.

Preserve existing routing tags, automation triggers, subjects, email timing,
subscriber positions and activation status. Keep Email 1's one PDF link:
https://mrlifemanager.com/print/the-week.pdf

Check the saved copy and link using MailerLite's preview. Do not send a
broadcast, restart subscribers, add recipients or activate a paused sequence.
If safe editing requires pausing or altering subscriber positions, report the
specific limitation before making that account change. Mark a sequence updated
only after verifying what was saved, not merely after opening the editor.

Report each sequence as updated, already matching, absent or blocked, with the
verification date. Record confirmed results in
[planning/operations.md](../../../planning/operations.md). Until an operator
provides that evidence, account synchronization remains unverified.

## Supporting references

- [Operating specification](MAILERLITE-SETUP.md) for routing and cadence.
- [Source-based weekly review](../../print/the-week-review.md) for what changed
  and its connection to Dave's original documents.

These files describe repo intent and available copy. They do not establish
private MailerLite delivery behavior or authorize new campaign content.
