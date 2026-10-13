# Social media strategy

**Status:** Proposal for Charles, 2026-10-13. None of the planned handles is
claimed yet. The planned handles are @mrlifemanager on TikTok, X and YouTube,
and @mr.lifemanager on Instagram and Facebook. ADR-010, ADR-015 and ADR-016 are
under review, so the buyer is treated as open, and each place this strategy
depends on that decision is marked **[depends on buyer]**. Principle numbers
refer to [principles.md](../vision/principles.md). No external platform figures
are used.

## What social media is for

Social media puts a moment in front of the person who is in it. The business
we are really in (PR #86) is the practical stuff nobody showed you, at the
moment it hurts. The moments model runs: a moment, a free task on an entry
page, the weekly habit by email, and then the next moment. Social media covers
only the first step. A post succeeds when someone finishes the task on the
matching entry page, not when they follow the account (principle 11:
completion is what converts).

The voice is ADR-011's apprentice: Dave's methods, passed on by someone who
learned them the hard way, with no hype, shaming or drill sergeant.

## Platform pick: YouTube Shorts first, with the same video on TikTok

Start with one short vertical video a week. Post it on YouTube as a Short, and
post the same file on TikTok.

**Why YouTube Shorts:**
- People look for help there when the moment arrives, so a video titled
  "Someone's coming over in an hour" can be found by the person who needs it.
- [target-audiences.md](../vision/target-audiences.md) lists YouTube and
  search among the places Tyler finds help.
- A short video shows the task actually being done: the sink emptied, the bin
  taken out, the lamp switched on.

**Why TikTok second:** target-audiences.md says Maya discovers through TikTok,
and posting the same file costs almost nothing extra (principle 9, simple
enough to keep).

**What the others wait for:**
- **Instagram Reels** waits until two platforms have run steadily for eight
  weeks, because a third inbox is real work.
- **Facebook** waits for the buyer decision. It is the likely place for
  parents and gift buyers, which is ADR-010's open question **[depends on
  buyer]**.
- **X** has no planned role. Claim the handle only to protect the name.

## Content pillars, tied to the moments

Each pillar is one moment and one entry page.

| Pillar | Entry page | Example post |
|---|---|---|
| Your first night in a new place | `/first-night.html` | Photographing every room before the first box comes in, and why it protects the deposit |
| Someone is coming over | `/guests.html` | The first three of the six steps, in order, about fifteen minutes |
| The week got away from you | `/underwater.html` | The kitchen reset that comes first, about fifteen minutes |
| A room you stopped using | `/one-room.html` | Dave's three piles for one zone of a garage or closet |

A fifth pillar, **why it works**, carries one of Dave's reasons in under a
minute: why an empty sink changes how a kitchen reads, for example. It still
points to the matching entry page (principle 10: teach the why, then the what).

## Formats and cadence

- **Format:** a vertical video of 30 to 60 seconds that shows one task, start
  to finish, with on-screen text naming the moment. A short caption names the
  entry page.
- **Cadence:** one new video a week, posted to YouTube Shorts and TikTok. That
  is four videos a month.
- **Replies:** one fifteen-minute session for answering comments, twice a week.

**In a bad week, cut in this order:**
1. The second reply session.
2. The new video. Repost an older one instead and say so in the caption.
3. Replies, for that week only.

No streak is kept (principle 4: systems beat motivation, so the plan has to
survive the worst week).

## From post to finished task

Each post has one next step: do this task now, and the rest of the list is on
the page.
- **Links:** the profile link and the video description (where the platform
  allows a link; check this at setup) point to the matching entry page with a
  source tag. For example, `/guests.html?from=yt` or `/guests.html?from=tt`.
  The entry pages already carry the `from` tag through to the finished-task
  page (`products/landing/assets/entry.js`), so a finish can be traced back to
  its post.
- **One task:** each post points to one entry page.
- **No signup ask:** posts never ask for an email address. The email ask
  happens only after the task is finished, on the page.
- **No other offers:** posts never mention First Place or any paid product
  until Charles re-decides the buyer and the paid step **[depends on buyer]**.

## We will never

- post rage bait, or hooks like "you're doing it wrong"
- post before-and-after shots that shame a person or a home, or call someone's
  place disgusting
- suggest someone is lonely, failing or behind because of their home
  (principle 8: dignity, not shame)
- use fake urgency or scarcity: no countdowns, "last chance" or "only today"
- use engagement bait, such as "comment YES," "tag a friend who needs this" or
  follow-for-part-two cliffhangers
- reward sharing, referrals or follows
- buy followers, views or comments, or use engagement groups
- invent Dave quotes, or put Dave on screen without his agreement (ADR-011)
- post faith content in this product channel
  ([brand-positioning.md](brand-positioning.md))

## What we measure

These measures reflect completion, not popularity:
1. **Entry-page visits** by source tag (`yt`, `tt`).
2. **Finished-task page reaches** by source tag.
3. **Email signups after finishing**, by source tag.
4. **Saves, and "I did it" replies**, counted by hand.

Followers and views are noted monthly for context; no decision rests on
them.

**This depends on analytics.** The site has no visitor analytics yet
([SETUP.md](../../products/landing/SETUP.md) lists it as open). Until Charles
approves a tool, only measure 4 can be read.

## First 30 days

1. **Week 1:** Charles makes decisions 1 to 3 below. The first four videos
   are made, one per entry page, before anything is posted.
2. **Week 2:** the guests video is posted on both platforms, and comments are
   answered.
3. **Week 3:** the first-night and underwater videos are posted. Note which
   words people repeat back in comments, and compare them with the
   entry-page headlines.
4. **Week 4:** the one-room video is posted. Review visits, finishes and
   replies by source tag, then Charles makes decision 4.

## Decisions for Charles

1. **Handles.** Claim all five planned handles to protect the name, or only
   YouTube and TikTok for now.
2. **Analytics.** Approve one privacy-first analytics tool for the site.
   Without it, completion by source cannot be measured.
3. **Who appears on camera.** The options:
   - **Hands only:** the apprentice's hands doing the task, with no face. This
     is the lowest effort and keeps attention on the task.
   - **The apprentice's face:** more trust, more effort.
   - **Dave on camera:** only with his agreement (ADR-011 says recording him is
     under consideration). He is the source of the methods, not a presenter.

   ADR-015's "no video, no face" rule was written for entry pages and is under
   review. Social video needs its own answer. The recommendation is hands
   only, with Dave named as the source in captions.
4. **Continue after 30 days**, judged on finishes and replies, not followers.
5. **The buyer and the paid step** (ADR-010, ADR-015, ADR-016). These decide
   whether Facebook is added and whether a post may ever mention First Place.
