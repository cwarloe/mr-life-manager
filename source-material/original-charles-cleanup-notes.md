# Original Cleanup & Household Notes

> **⚠️ PLACEHOLDER — the actual source material has not been added yet.**
>
> This file is a container waiting for content. Nothing below is a
> reconstruction, paraphrase, or guess at what the original notes contain,
> because inventing source material would defeat the entire purpose of keeping
> source material.

---

## ⚠️ Provenance question, opened 2026-09-08

[ADR-011](../planning/decisions.md#adr-011--mr-life-manager-is-a-real-person-dave-webster)
establishes that **Mr. Life Manager is Dave Webster**, a real person, and that
the founder's role is the apprentice who learned from him.

That makes this file's name and contents an open question:

- Are these notes **the founder's own**?
- Are they **Dave's**, in his words?
- Are they **the founder's record of Dave's teaching** — which is a third thing,
  and the most likely?

**It matters, for three reasons.** Attribution has to be accurate. Dave's own
words are primary source material of a different order than notes about him. And
under [ADR-012](../planning/decisions.md#adr-012--licensing-permission-is-the-marketing),
which asks others to credit their sources, this project should be scrupulous
about crediting its own.

**Do not rename or reorganize this file until that is answered.** If material
from both people ends up here, keep it in **separate files** with distinct
headers — never merged.

## What goes in this file

The original household cleaning and organization notes that started this project
— the practical guidance written before there was a business concept, a brand
name, or a framework.

## Why it's kept separate

**Source material and derived work are different kinds of artifact, and mixing
them destroys both.**

- **Source material is evidence.** It records what was actually thought, in the
  words it was actually thought in. Its value comes entirely from being
  unedited.
- **Derived work is interpretation.** The frameworks in
  [`frameworks/`](../frameworks/) are abstractions built *from* the source. They
  can and should be revised freely.

If the original gets edited to match the framework, the framework can no longer
be checked against anything. The chain of reasoning becomes circular, and you
lose the ability to ask the most useful question available: *did we get the
abstraction right, or did we lose something in the generalization?*

Original notes also tend to contain specifics — an exact product, a particular
trick, a phrasing that lands — that get smoothed away in the process of making
something general. Those specifics are frequently the most valuable content in
the whole repository.

## Rules for this folder

1. **Add source material verbatim.** Typos, tangents, incomplete thoughts and
   all. Fix nothing.
2. **Never edit source material to match a framework.** If the framework and the
   source disagree, that's a finding worth examining, not an error to correct.
3. **Derived work lives elsewhere** — in `frameworks/`, `content/`, or `docs/`.
4. **Annotate in a separate block**, clearly marked, if commentary is needed:

   ```markdown
   > **[Note, 2026-09-05]:** This became the "everything has a place" framework.
   ```

5. **Date and label everything.** When was it written, in what context, for whom.
6. **One file per distinct source.** Don't merge separate documents into one.

## How to add the notes

1. Paste the original text into this file, or add a new file in this directory
   if the material is substantial enough to stand alone.
2. Add the header block below.
3. Commit with a message like `Add original household cleanup notes`.
4. **Then** — separately — trace which frameworks derive from which parts, and
   note anything in the original that hasn't yet made it into the derived work.

## Header template

```markdown
# [Title]

**Written:** [date or approximate period]
**Context:** [why it was written, who it was for]
**Format:** [notes, list, letter, outline, transcript...]
**Status:** Verbatim — do not edit

---

[original text]
```

---

## Source material index

| File | Description | Date written | Added |
|---|---|---|---|
| *(none yet)* | | | |

---

## When the notes are added, look for

A short checklist for the pass that should follow the import:

- [ ] **Cadences and frequencies.** "How often should I…" is the single
      highest-demand content in this category
      ([customer-problems.md](../docs/research/customer-problems.md)). Original
      notes usually contain real ones.
- [ ] **Specific products, tools, and techniques** — the concrete details that
      generalization tends to erase.
- [ ] **Phrasing worth keeping.** Original voice is almost always better than
      rewritten voice.
- [ ] **Sequences.** What order things were done in, and why.
- [ ] **Anything the frameworks missed.** Ideas in the source that didn't make it
      into [`frameworks/`](../frameworks/) — these are the most interesting
      finds, and the reason for doing the pass at all.
- [ ] **Anything the frameworks got wrong.** Places where the abstraction drifted
      from what was actually meant.

## Related

- [`frameworks/`](../frameworks/) — the derived conceptual models
- [`content/`](../content/) — teaching content built from both
- [`planning/decisions.md`](../planning/decisions.md) — why things were decided
