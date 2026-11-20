---
id: ana1/limits
title: Limits of sequences
lecture: 3
prerequisites: [ana1/sequences]
exam_weight: 3
sources: ["L03 slides 12-18"]
status: draft
---

# Limits of sequences (*Grenzwert einer Folge*)

## In one sentence

A sequence has limit *a* if its terms eventually stay as close to *a* as you like.

## Intuition

Pick any tolerance band around *a*, however thin. From some point on, every term lies inside it. Early terms don't matter; only the tail does.

## Definition

(aₙ) converges to *a* if for every ε > 0 there is an N such that |aₙ − a| < ε for all n ≥ N.

## Example

aₙ = 1/n → 0. Given ε, choose N > 1/ε. Then for n ≥ N: |1/n − 0| = 1/n ≤ 1/N < ε.

## Common mistakes

- Choosing N before ε. N may depend on ε, never the other way round.
- Thinking a limit must be reached. 1/n never equals 0.

## Connections

- Builds on [Sequences](sequences.md).
- Needed for continuity and series.

## Recall questions

1. State the ε-N definition of a limit.
   <details><summary>Answer</summary>For every ε > 0 there is an N with |aₙ − a| < ε for all n ≥ N.</details>
2. Why does the limit of (1/n) exist even though no term equals it?
   <details><summary>Answer</summary>The definition only asks that the terms get and stay arbitrarily close, not that they reach it.</details>
3. Does changing the first 1,000 terms change the limit?
   <details><summary>Answer</summary>No. Only the tail matters: take N larger than 1,000.</details>
