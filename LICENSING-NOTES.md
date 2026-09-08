# License Decision (Open — Not Yet Made)

**Status:** Undecided. No `LICENSE` file has been added on purpose.

> **On this file's name:** it is deliberately *not* called `LICENSE-DECISION.md`.
> GitHub scans for files whose names begin with `LICENSE`, and it was picking
> this one up and tagging the repository as licensed "Other" — implying a license
> exists when the entire point is that none does yet. Keep the `LICENSE` prefix
> free until there is a real license to put there.

Under U.S. copyright law, content without a license is "all rights reserved" by
default. That is the current, deliberate state: the material here is protected,
and nobody has permission to reuse it. That is a fine holding position for a
commercial product concept, but it should be a choice, not an accident.

## Why this is genuinely a decision, not a formality

This repository is unusual: it mixes three different kinds of material that may
deserve different treatment.

1. **Commercial product content** (ebooks, courses, toolkits) — the thing
   customers pay for.
2. **Frameworks and vocabulary** ("Everything Has a Place," "Preventative vs.
   Crisis") — ideas that spread only if people are allowed to use them.
3. **Planning and business documents** — internal, and arguably shouldn't be
   public at all long-term.

A single license for all three is probably the wrong answer.

## Options and their real implications

### Option A — All rights reserved (no license file)

- **What it means:** No one may copy, adapt, or redistribute anything here.
- **Upside:** Maximum protection for paid products. Simplest.
- **Downside:** The repository is public but legally inert — people can read it
  and nothing else. Also blocks well-meaning contributors and quotation.
- **Best if:** The public repo exists mainly for transparency and portfolio.

### Option B — Creative Commons BY-NC-SA 4.0 (content) 

- **What it means:** Anyone may share and adapt for **non-commercial** use with
  attribution, and derivatives must carry the same license.
- **Upside:** Frameworks spread. Churches, campus ministries, RA programs, and
  student groups can legally use the material — which is exactly the kind of
  distribution this concept wants.
- **Downside:** "Non-commercial" is famously vague and hard to enforce. It also
  makes some paid licensing conversations awkward, because a prospect may ask
  why they should pay for something they can use free.
- **Best if:** Reach and ministry-style distribution matter more than tight
  commercial control.

### Option C — CC BY-NC-ND 4.0 (no derivatives)

- Same as B, but no adaptations allowed — share verbatim only.
- **Upside:** Protects the integrity of the material and the brand voice.
- **Downside:** Kills the most valuable use case (a college adapting a checklist
  for its own orientation program).

### Option D — Split license (recommended shape, not yet adopted)

- `frameworks/` and `docs/vision/` → **CC BY 4.0** or **CC BY-SA 4.0**
  (spreadable ideas, attribution required)
- `content/` and `products/` → **all rights reserved** (the commercial core)
- `docs/business/` and `planning/` → all rights reserved, and consider moving
  to a private repo entirely
- **Upside:** Ideas travel, products stay protected.
- **Downside:** More complexity; requires per-directory `LICENSE` files and a
  clear note in the README so nobody guesses wrong.

### Option E — Trademark, not copyright, as the real moat

Worth naming explicitly: for a brand like this, the durable protection is
probably the **name and identity** ("Mr. Life Manager"), not the text. Copyright
protects a specific expression, not the idea of teaching adults to run a home.
Anyone can write their own first-apartment checklist. Nobody else should be able
to call theirs Mr. Life Manager.

## What has to be true before deciding

- [ ] Is `products/` going to live in this public repo at all, or only in a
      private build repo? (This is the biggest fork in the road.)
- [ ] Do we want colleges, churches, and military transition programs to be able
      to use material for free, or should that always be a paid license?
- [ ] Is a name/trademark search worth doing before publicizing the brand?
- [ ] Do we want outside contributors? (If yes, a CLA or license is required.)

## Decision (2026-09-08)

**Settled by [ADR-013](planning/decisions.md#adr-013--licensing-revised-free-to-use-never-free-to-sell).**

> **Free to use. Never free to sell. The brand travels with it.**

| Use | Allowed? |
|---|---|
| A person uses it to run their own home | **Yes** |
| A church, ministry, or RA program teaches from it | **Yes** |
| Someone adapts a checklist for their own program | **Yes**, with credit, same terms |
| Someone sells it, or a product built on it | **No** — come and ask |
| Someone strips the branding and reissues it | **No**, under any circumstances |

**Instrument: CC BY-NC-SA 4.0** for `frameworks/` and the free tier. Paid
products stay all rights reserved. The **name** remains the primary protected
asset.

- **BY** — attribution, so the brand travels with every copy. This alone already
  forbids rebranding: stripping the name violates the licence.
- **NC** — nobody sells it, or a product built on it, rebranded or not.
- **SA** — adaptations carry the same terms, so nobody adapts it and then locks
  their version down.

**Why not fully permissive.** An earlier version of this decision
([ADR-012](planning/decisions.md#adr-012--licensing-permission-is-the-marketing),
now superseded) allowed commercial reuse under CC BY. The point of giving the
material away is **reach**, and free use by people and programs achieves that.
Free *commercial* reuse just donates the business to whoever moves fastest.

**The real cost, stated plainly.** "Non-commercial" is famously vague. Is a
church charging $10 for printed workbooks commercial? A university charging
tuition? A nonprofit with a paid facilitator? The line is genuinely unclear.

**The mitigation makes the cost useful.** CC licences are **non-exclusive**, so
this can be dual-licensed. Public terms are BY-NC-SA; anyone outside them comes
and asks. Ambiguity becomes an **inbound qualification mechanism** — every
awkward edge case is an institution identifying itself as a potential customer.
Say yes generously; just say it deliberately.

**What this makes urgent.** If the name is the asset, the trademark is no longer
optional. The free USPTO search is a prerequisite — more so since
[ADR-011](planning/decisions.md#adr-011--mr-life-manager-is-a-real-person-dave-webster)
tied the brand to a real person.

**Written:** [PERMISSIONS.md](PERMISSIONS.md) — the plain-language version for
people who need to know what they can do and are not lawyers. It answers the
awkward middle cases explicitly (a church covering copying costs, a university
course, a grant-funded workshop) by inviting the question rather than pretending
the line is clear.

**Still not legal advice.** Talk to an attorney before registering a trademark or
publishing a license file — especially given ADR-011.

**This is not legal advice.** Before licensing or trademarking anything with
commercial value, talk to an attorney.

Record the outcome as an ADR in [`planning/decisions.md`](planning/decisions.md).
