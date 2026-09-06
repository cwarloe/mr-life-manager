# Research Prompts

Reusable prompts for the research this project keeps needing, plus how to assign
them and how to decide whether the result is trustworthy.

**Why these exist.** The first external research pass
([brand-name-scan.md](brand-name-scan.md)) came back with sound reasoning built
on weak retrieval: it never opened a trademark database, searched the wrong
product category, and attached several citations to claims they did not support.
The reasoning was fine. The sourcing was not. These prompts are written to make
that specific failure visible instead of invisible.

**Two jobs, two prompts.** The original request conflated a name/trademark check
with a competitive landscape survey. Those have different authoritative sources,
different methods, and different definitions of done. Run them separately.

---

## Assignment guide

| Job | Assign to | Effort | Why |
|---|---|---|---|
| **Trademark search** | **Yourself** | ~10 min | USPTO's public search is free and authoritative. An LLM adds a lossy layer over a database you can query directly — and that layer is exactly what failed. |
| Domain / handle / book-title check | Mid-tier model, or yourself | Low | Lookup, not judgment. |
| **Competitor landscape** (Prompt 2) | **Top-tier reasoning model with genuine deep-research browsing** | Highest | Long-horizon, many-source, and the key question — reading *absence* correctly — is real judgment. |
| Audience reaction to the name | **Nobody. Go ask people.** | — | See [What not to assign](#what-not-to-assign-to-a-model). |

**The thing to select for is retrieval, not intelligence.** Raising reasoning
effort improves synthesis; it does not improve source fidelity. A high-effort
model with weak retrieval produces a *more elegantly argued* fabrication. Pick
the tool that actually opens pages, then turn the effort up.

---

## Prompt 1 — Name and trademark scan

Run the trademark portion yourself. Use this for the rest, or to double-check.

```text
You are doing a preliminary name-availability scan for a brand name. This is
research, not advice, and it will be checked against your sources.

BRAND: "Mr. Life Manager"
BUSINESS: A content and curriculum business — ebooks, checklists, worksheets,
and courses teaching practical household and life-management systems to
first-time independent adults. It is NOT a software product, NOT an app, and
NOT a professional-organizing service. Judge relevance by that category.

SEARCH THESE, AND SAY WHICH ONES YOU ACTUALLY REACHED:
1. USPTO trademark database (tmsearch.uspto.gov) — search "life manager",
   "mr life manager", "life management", and "Mr. Man". Report live marks,
   dead marks, owners, filing dates, and international classes. This is the
   authoritative source for the trademark question; everything else is
   secondary.
2. Domain registrars — availability of mrlifemanager.com and close variants.
3. Social handle availability on Instagram, TikTok, YouTube, X.
4. Book publishing — Amazon and Google Books, for titles or author brands
   using this or a close name.
5. General web — any operating business using this name in ANY category.

RULES, IN PRIORITY ORDER:
- Every factual claim needs an inline URL and the date you checked it. A claim
  without a checkable source must be labeled INFERENCE, not fact.
- Each citation must actually support the specific sentence it is attached to.
  Do not attach a source to a claim it does not establish.
- If you could not access a source, say so plainly in a "Sources I could not
  reach" section. Do not substitute an adjacent source and present it as
  equivalent. An incomplete scan clearly labeled is far more useful than a
  complete-looking one.
- Do not cite results that merely share a word with the brand unless you
  explain the relevance. ("MR" is also an abbreviation for pharmaceutical
  medical representatives; that is a homonym, not a competitor.)
- Distinguish "I found no evidence of X" from "X does not exist." Say which
  you mean, every time.
- Do not describe or evaluate the business's own materials. Only outside
  sources.

OUTPUT:
- A findings table: claim | source URL | date checked | confidence
  (high/medium/low) | why that confidence
- Trademark section: live marks that could conflict, their classes and owners,
  and whether the relevant classes (printed matter, educational services,
  downloadable publications) are crowded or clear
- Distinctiveness assessment: which part of the mark, if any, is protectable
- A "Sources I could not reach" section
- Three to five specific questions worth taking to a trademark attorney

Do not recommend a rename. Do not propose alternative names. Report what you
found and how confident you are.
```

**Load-bearing lines:** the "Sources I could not reach" section and the
fact/inference split. Without them, gaps get filled with adjacent-looking
sources and the citation count disguises what was never checked.

---

## Prompt 2 — Competitor landscape

This is the real gap. Phases A–D of [competitor-notes.md](competitor-notes.md)
remain unresearched, and the name scan was never going to answer them.

```text
You are mapping the competitive landscape for a content and curriculum
business. Accuracy matters more than coverage: a short report of verified
findings beats a long one containing guesses.

THE BUSINESS: Teaches practical adult-life systems — home, food, money, time,
maintenance, paperwork, hospitality — to people who were never explicitly
taught them. Primary audience: first-time independent adults (first apartment,
leaving home, newly married). Products are ebooks, checklists, worksheets, and
courses. Entry-point topic is household cleaning and organization, but that is
not the whole scope.

RESEARCH THESE CATEGORIES. Find 3-5 real, currently-operating examples in each:
1. Cleaning and home-care content creators
2. Home organization and decluttering methods and brands
3. "Adulting" and life-skills content aimed at 18-25 year olds  <- HIGHEST PRIORITY
4. Personal finance education for young adults  <- study the business model
5. Homemaking and home-economics content
6. Institutional life-skills programs: university residence life and first-year
   experience, military transition assistance, church young-adult ministry,
   foster-care aging-out and reentry programs
7. Home maintenance and DIY, especially anything aimed at RENTERS
8. ADHD and executive-function coaching
9. Notion template and printable/planner sellers in the household space

FOR EACH EXAMPLE, REPORT:
- What they sell, to whom, at what observed price, and how they are discovered
- Business model: ad/sponsorship-supported content, or actual products?
- Any visible volume signal: review counts, "X students enrolled", bestseller
  rank — and say plainly if there is none
- What they do well, and what their reviews complain about
- Source URL and date checked, for every one

THEN ANSWER FOUR QUESTIONS DIRECTLY:
1. Does anyone teach practical systems across MULTIPLE life domains, or is
   everyone single-domain?
2. Does anyone target first-time independent adults specifically?
3. Does anyone position around "nobody taught you this" rather than
   aspiration or shame?
4. Where you find no one doing something — is that an opening, or a graveyard?
   Actively look for abandoned attempts: dead blogs, discontinued products,
   courses that stopped enrolling, brands that pivoted away. An empty category
   is sometimes empty because nobody would pay. Report what you find either
   way, and say which explanation the evidence supports.

RULES:
- Never invent a company, a price, an audience size, or a revenue figure. If
  you cannot verify a number, write "not found" rather than estimating.
- Separate OBSERVED (you saw it on a page) from INFERRED (you concluded it).
  Label every claim as one or the other.
- List categories where you found nothing credible, and say so.
- Quote actual customer language from reviews and forums verbatim where you
  find it — exact phrasing is more valuable to me than your paraphrase.
```

**Question 4 is the one most people leave out**, and it's the one most likely to
save a year. An empty category is not automatically an opportunity.

---

## What not to assign to a model

**The name's gender perception.** No model can say how a 22-year-old woman reacts
to "Mr." It can only confirm the risk exists — which two independent passes have
now done. Answering it takes ~15 real conversations. Assigning it to a model
produces more confident text and zero new information.

**Whether people will pay.** A model will describe the market as attractive. It
has no idea. Only past spending and real conversations answer this.

**Anything in [customer-problems.md](customer-problems.md) marked for
validation.** Those need humans, by design.

---

## Choosing a tool

Model names and version numbers go stale faster than this document will be
updated, so use the test rather than a recommendation:

> Give the candidate a narrow question with a verifiable answer that requires
> opening a page — e.g. *"What does the pricing page for [specific product] list
> today, and what is the URL?"* Then check it.
>
> Right number and a resolving URL → it is reading. Hedging, paraphrase, or a
> plausible-but-wrong figure → it is writing from memory behind a search layer.
> Do not give that one your research.

Prefer a **deep-research mode** over a search-grounded chat mode. They are often
the same underlying model with very different retrieval behavior, and that
difference is the whole ballgame here.

---

## Acceptance test

Apply this to every report before any of it enters the repo.

**1. Spot-check five citations at random.** Open them. Does each support the
sentence it is attached to?

> **If any one fails, discard the entire report.** Do not salvage the parts that
> look right. A broken citation apparatus means the citations you did *not* check
> are equally unreliable — which was exactly the situation with the first scan.

**2. Run it twice, on two different tools, and diff.** Verified facts appear in
both. Fabrications rarely survive — two systems seldom invent the same company at
the same price. Disagreements mark precisely where to look, and they are cheap to
check.

**3. Confirm the honesty sections exist.** If there is no "could not reach" or
"found nothing credible" section, the report is claiming complete coverage.
Assume it is wrong and send it back.

**4. Check the category.** Are the examples from *this* business's category —
content and curriculum — or from an adjacent one that merely shares vocabulary?

---

## Where results go

1. Full report, verbatim, into [`inputs/`](inputs/) with provenance. Never edit it.
2. Synthesis into a derived file — findings, confidence ratings, **limitations**,
   and what changed as a result. Model: [brand-name-scan.md](brand-name-scan.md).
3. Verified competitor entries into [competitor-notes.md](competitor-notes.md),
   using the recording format already defined there.
4. Confirmed problems marked ✅ in [customer-problems.md](customer-problems.md).
5. Anything that changes a decision → an ADR update in
   [decisions.md](../../planning/decisions.md).
