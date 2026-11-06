# Customer profile: the student and the parent who buys for them

**Written:** 2026-11-05, in answer to the Bronco Entrepreneur Challenge 2026 judges.
**Status:** Draft for Charles. Docs only.

## Read this first: what we know and what we don't

- **No customer interviews have been done yet.** The repo has an interview
  script ([customer-interview-script.md](../research/interviews/customer-interview-script.md))
  and a first-reader test ([first-reader-test.md](../research/interviews/first-reader-test.md)),
  but no notes or results from either. Nothing in this file comes from a
  conversation with a customer.
- Every line below is labeled:
  - **Evidence** means a source we can point to (published research, a
    competitor's sales signal, or the judges' feedback).
  - **Assumption** means our best guess. The
    [willingness-to-pay plan](willingness-to-pay-plan.md) is how we test it.
- **The parent-as-buyer decision is on hold.** ADR-010 ("keep the audience,
  change the payer") is under review. Charles put it on hold on 2026-10-03.
  This file describes the parent as a possible buyer. It does not decide that
  the parent is the buyer.

---

## Profile 1: Tyler, the student or first-time renter

This is the person who **uses** the checklists.

| | Detail | Label |
|---|---|---|
| **Age** | About 18–25 | Assumption, from [target-audiences.md](../vision/target-audiences.md) |
| **Situation** | Moving out for the first time: dorm, first apartment, or first place after graduation | Assumption |
| **Money** | Limited budget; may still get help from parents | Assumption |
| **What they believe** | "I should already know this." Feels embarrassed to ask | Evidence: [customer-problems.md](../research/customer-problems.md), pattern 5 (desk research, not interviews) |
| **How they look for help** | Search, short videos, asking friends; rarely buys a course | Evidence: low course numbers for "adulting" courses (see [competitor-scan.md](competitor-scan.md)) |
| **What they will not tolerate** | Being lectured or made to feel behind | Assumption, matches judges' praise of the no-shame voice |

**The moment.** A specific night: people are coming over, the room nobody uses
needs clearing, or the whole place needs doing and they don't know where to
start. Also the first week in a new place. (Assumption.)

**What Tyler is buying.** Mostly nothing. Tyler gets the free checklist. The
value to Tyler is "I knew what to do first, and I did it." Tyler is the best
user and probably a weak direct buyer. (Evidence: Society of Grownups and the
small "adulting" course numbers in the competitor scan. Assumption for Tyler
himself.)

**Where to reach Tyler honestly**
- Campus orientation and move-in week materials (needs a school partner)
- Resident assistant (RA) programs that already run life-skills sessions
- QR flyers in places students wait: coffee shops, laundromats, campus boards
  (see the away-from-home design in PR #108: the scan saves the steps for later)
- Short videos on Reels, Shorts and TikTok, using the three moment hooks
- Friends sharing a checklist that worked

---

## Profile 2: the parent buying a gift

Judge 3 suggested this person: "a first-apartment guide makes a good graduation
or move-out gift."

| | Detail | Label |
|---|---|---|
| **Age** | About 45–60 | Assumption |
| **Situation** | Child is graduating, leaving for college, or moving into a first apartment | Assumption |
| **Money** | More to spend than the student; already buying move-in items | Assumption; Target and IKEA aim their checklists at this shopping trip (Evidence that the trip exists) |
| **What they believe** | "I didn't teach them all of this, and I want them to be okay." | Assumption |
| **What they want to avoid** | A gift that feels like a criticism of their child | Assumption, and important: the gift must not shame the student |
| **How they buy** | Graduation gifts, move-in shopping lists, parent Facebook groups | Assumption |

**The moment.** Graduation season (May–June) and move-in season (August).
Also the week before a child signs a first lease. (Assumption.)

**What the parent is buying.** Peace of mind, and a gift that says "I believe
you can do this" and not "you can't do this." A printed or boxed version of
the first-apartment checklist is one possible form. (Assumption; the site has a
parents page, `products/landing/index-parents.html`, but no paid gift product
exists today.)

**Where to reach the parent honestly**
- Parent Facebook groups for a specific college or graduating class (only where
  the group allows it, and only with Charles's OK)
- Graduation gift guides and move-in shopping lists
- Parent orientation sessions at colleges (needs a school partner)
- The parents homepage, linked from the student pages ("send this to someone
  who's moving out")

---

## How the two connect

The student uses it and the parent may pay for it. The content stays the same;
only the framing changes. Copy for parents must never describe the student as
a problem. That rule comes from our no-shame principle and applies no matter
how ADR-010 is decided.

## What would change this profile

- Interviews in which students say they have paid for help of this kind
  (would make Tyler a buyer)
- Parents who say they would not give a guide like this as a gift (would weaken
  Profile 2)
- A price test result (see the plan)
