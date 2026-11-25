# Social media strategy

**Status:** Proposal for Charles, revised 2026-10-13. Chief of Staff is claiming
the planned accounts; this doc assumes they exist. ADR-010, ADR-015 and ADR-016
are under review, so the buyer is treated as open. Each place that depends on
it is marked **[depends on buyer]**. Principle numbers refer to
[principles.md](../vision/principles.md).

## The goal

Our posts are not trying to win attention or watch time. A post succeeds when
someone stops scrolling and, right then on their phone, opens the matching
entry-page checklist and does the first step. Each post is a short on-ramp to a
phone action. It gives nothing to binge, belongs to no series designed to keep
people on the platform, and ends with a clear handoff to the checklist link.

This follows from the business we are really in (PR #86): the practical stuff
nobody showed you, at the moment it hurts. It also follows the moments model,
in which a moment leads to a free task on an entry page, then the weekly habit
by email, then the next moment. Social media serves only the first step.
Principle 11 (completion is what converts) is the test for every post: did
someone start the task?

The voice is ADR-011's apprentice: Dave's methods, passed on by someone who
learned them the hard way, with no hype, shaming or drill sergeant.

## Link friction decides the platform

Because the goal is a tap to the checklist, the deciding question is how many
taps stand between the post and the entry page. Checked 2026-10-13:

- **YouTube Shorts.** URLs in Shorts descriptions and comments are not
  clickable ([YouTube Help](https://support.google.com/youtube/answer/13748639)).
  The "related video" link on a Short can only point to another YouTube video
  ([YouTube Help](https://support.google.com/youtube/answer/14075157)). The
  only tappable route to our site is the channel profile link, so a viewer
  taps the channel name, then the link: two taps, plus finding it.
- **TikTok.** A website link in the profile needs at least 1,000 followers or
  a Verified Business Account. This was reported from TikTok's help article
  ([Linkero, read 2026-08-19](https://linke.ro/blog/tiktok-link-in-bio-not-showing)).
  TikTok's own business page says a Verified Business Account can also attach
  a destination link to individual videos ("organic conversion anchors";
  [TikTok Business Help](https://ads.tiktok.com/resources/help/article/about-business-registration?lang=en)).
  I didn't confirm whether that is available to an account like ours.

**The pick changes: TikTok first, as a Verified Business Account, with
YouTube Shorts second and only if the TikTok link works.** TikTok is the only
one of the two that can put a tappable link on the post itself. Without
business verification it has no website link at all until 1,000 followers, and
then it is worse than YouTube. So the first decision for Charles is whether to
apply for business verification **[depends on buyer]**, because verification
asks for business details.

Instagram, Facebook and X wait. Their link rules were not checked, and adding
a platform before the first one works breaks principle 9 (simple enough to
keep).

## The handoff, spoken and on screen

Every post ends the same way, in about five seconds:
- **Spoken:** "The whole list is at mrlifemanager.com/guests. Open it now and
  do step one."
- **On screen:** the short address in large type for the last three seconds.
- **Tappable:** the link on the video or in the profile, tagged by platform,
  for example `/guests.html?from=tt` or `/guests.html?from=yt`.

The entry pages already pass the `from` tag through to the finished-task page
(`products/landing/assets/entry.js`). A typed address such as
`mrlifemanager.com/guests` already loads, but it arrives without a tag, so
those visits can't be traced to a post.

**A site change to consider later:** today the checklist opens in full-page
view, and the reader taps "Just the steps" to enter doing mode. Letting a
tagged link open straight into doing mode, at step one, would remove one more
tap. It would be a separate change for Charles to approve.

## What a post is

- **Length:** 15 to 30 seconds. One moment, one task, shown being done, then
  the handoff.
- **Content:** the first step only. The video shows step one being done and
  says that steps two to six are on the page. For guests, that's the bin out
  and the window open.
- **Nothing to binge:** no "part two," no numbered series, no cliffhanger, no
  "follow for more."
- **Captions:** they name the moment in the reader's words, such as
  "Someone's coming over in an hour."
- **No signup ask:** posts never ask for an email address; the page asks after
  the task. Posts never mention First Place **[depends on buyer]**.

## Pillars, one per entry page

| Moment | Entry page | Step one shown |
|---|---|---|
| First night in a new place | `/first-night.html` | Photograph every room before the first box comes in |
| Someone is coming over | `/guests.html` | Take the bin out and open a window |
| The week got away from you | `/underwater.html` | Reset the kitchen |
| A room you stopped using | `/one-room.html` | Answer Dave's one question before touching anything |

## Cadence one person can keep

- One new post a week, on TikTok first.
- One fifteen-minute session a week for answering comments, pointing each
  question to the matching page.

**In a bad week, cut in this order:** first the reply session, then the new
post (repost an older one). No streak is kept (principle 4).

## We will never

- design posts to keep people scrolling or bingeing
- post rage bait, or hooks like "you're doing it wrong"
- post before-and-after shots that shame a person or a home
- suggest someone is lonely, failing or behind because of their home
  (principle 8)
- use fake urgency or scarcity
- use engagement bait ("comment YES," "tag a friend," "follow for part two")
- reward sharing, referrals or follows
- buy followers, views or comments
- invent Dave quotes, or show Dave without his agreement (ADR-011)
- post faith content in this channel
  ([brand-positioning.md](brand-positioning.md))

## How we judge success

Success counts only people who started or finished the task:
1. **Checklist opens** by `from` tag.
2. **First-step reaches:** taps on "Just the steps" or "Next step" for those
   visits.
3. **Finished-task page reaches** by `from` tag.
4. **"I did it" replies**, counted by hand.

Views, watch time and follows are recorded only as diagnostics. A post with
many views and no checklist opens has failed.

**This depends on analytics.** The site has no visitor analytics yet
([SETUP.md](../../products/landing/SETUP.md) lists it as open). Measures 1 and
3 need a privacy-first page counter. Measure 2 also needs an event on the
step buttons. Until Charles approves one, only measure 4 can be read.

## First 30 days

1. **Week 1:** Charles makes decisions 1 to 3 below. Four posts are made, one
   per entry page.
2. **Week 2:** the guests post goes up. Check that the link works on a phone
   that isn't logged in.
3. **Week 3:** the first-night and underwater posts go up.
4. **Week 4:** the one-room post goes up. Review checklist opens, first-step
   reaches and finishes by tag, then Charles makes decision 4.

## Decisions for Charles

1. **TikTok business verification**, which is the only route to a tappable
   link on the post. If it's declined, YouTube Shorts with the profile link
   becomes the pick **[depends on buyer]**.
2. **Analytics:** approve one privacy-first page counter, plus an event on the
   step buttons.
3. **Who appears on camera:**
   - hands only (recommended), with Dave named in captions
   - the apprentice's face
   - Dave, only with his agreement (ADR-011)

   ADR-015's "no video, no face" rule was written for entry pages and is under
   review.
4. **Continue after 30 days**, judged on checklist opens and finishes, not
   views.
5. **Later:** whether a tagged link should open straight into doing mode.
