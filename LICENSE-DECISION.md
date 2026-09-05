# License Decision (Open — Not Yet Made)

**Status:** Undecided. No `LICENSE` file has been added on purpose.

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

## Recommendation

Hold at **Option A (no license)** while the repo is a concept sandbox. Move to
**Option D** the moment the first real product exists — but only after answering
whether `products/` belongs in public at all.

**This is not legal advice.** Before licensing or trademarking anything with
commercial value, talk to an attorney.

Record the outcome as an ADR in [`planning/decisions.md`](planning/decisions.md).
