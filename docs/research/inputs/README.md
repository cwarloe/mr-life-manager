# Research Inputs

External research reports, verbatim.

## Why this folder exists

Same principle as [`source-material/`](../../../source-material/): **inputs and
interpretation are different artifacts, and mixing them destroys both.**

- **Inputs** (this folder) are what an outside source actually said, unedited.
  Their value is that they can be checked.
- **Findings** (`docs/research/*.md`) are our synthesis — what we believe, at what
  confidence, and what we're doing about it.

If a report gets edited to match our conclusions, we lose the ability to ask the
most useful question available: *did the source actually support this, or did we
drift?*

## Rules

1. **Store verbatim.** Including citations, hedges, and errors. Fix nothing.
2. **Always record provenance:** who or what produced it, when, by what method,
   and what was asked. A finding without provenance can't be weighted.
3. **Never cite an input as fact in a derived doc** without stating its
   confidence and whether we independently verified it. See the standard set in
   [`competitor-notes.md`](../competitor-notes.md).
4. **Annotate in separate, marked blocks** if commentary is needed:

   > **[Note, 2026-09-05]:** Citations [1] and [3] do not support this claim.

5. **One file per input**, named `YYYY-MM-DD-short-description.md`.
6. **Run the acceptance test before filing anything.**
   [research-prompts.md](../research-prompts.md) § Acceptance test — spot-check
   five citations, and discard the whole report if any one fails.

## Index

| File | Source | Date | Synthesized into |
|---|---|---|---|
| [2026-09-05-brand-name-research-summary.md](2026-09-05-brand-name-research-summary.md) | AI research assistant, web search | 2026-09-05 | [brand-name-scan.md](../brand-name-scan.md) — name closed 2026-09-23; full report abandoned (summary was sufficient) |
| [2026-09-05-competitive-landscape-claude-opus-5.md](2026-09-05-competitive-landscape-claude-opus-5.md) | Claude Opus 5 (high effort), web research, Prompt 2 | 2026-09-05 | [competitor-notes.md § Findings](../competitor-notes.md#findings) |
| [2026-09-05-competitive-landscape-adult-life-systems.md](2026-09-05-competitive-landscape-adult-life-systems.md) | AI research pass (model not recorded), Prompt 2 | 2026-09-05 | [competitor-notes.md § Findings](../competitor-notes.md#findings) |
| [2026-09-06-competitive-landscape.md](2026-09-06-competitive-landscape.md) | AI research pass (model not recorded), Prompt 2 | 2026-09-06 | [competitor-notes.md § Findings](../competitor-notes.md#findings) |
