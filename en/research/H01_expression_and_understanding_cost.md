> **Translation record**
> - Chinese source: `research/H01_表达与理解成本.md` (sha256 `5ef7e19894b918c1ff89f0ba8cc20c14717a9bf9ae3a381e56bb29f706b2132f`, `3876` bytes, 2026-11-09)
> - Chinese version / release tag: `v11.2-r20261106` (theoretical version remains v11.2)
> - Translation version: `en-v0.1`
> - Translation date: 2026-11-09
> - Check status: checked sentence by sentence against the Chinese source for claim status, negative guardrails and numbering; machine and glossary checks only; no independent professional native-speaker review
> - Pending sync: pending registration in public-files.json / mkdocs.yml
> - Status: complete translation
> - Authority: the Chinese SSOT is authoritative; this translation does not constitute a separate set of definitions (C2)

# H01 | Does making expression explicit lower comprehension cost?

Status: design draft v0.3 (2026-10-23 added error-detection and task-distinction boundaries); not pre-registered, no participants recruited, no experimental results.

## Question and minimal task

When information content, mathematical background and task are kept as comparable as possible, does writing references and steps more explicitly raise the comprehension accuracy rate? What does the engineered term "decoding cost" add beyond ordinary explanations of language comprehension and cognitive load?

The first step makes material only: select a passage from the [preface to *Astronomical and Mathematical Essays* (《代微积拾级》)](https://zh.wikisource.org/wiki/代微積拾級/序), record the base text and paragraphs, list the propositions and references, then produce a candidate rewrite. Ask one reader who understands the relevant mathematics to check whether the rewrite is equivalent; if a disagreement appears, preserve the disagreement and do not begin an effect comparison. The goal of this trial is to submit a set of material within one to two weeks, not to establish the overall superiority of classical or vernacular Chinese.

## Input specification

Each piece of material is saved with: source link and version, original text, modern-punctuation treatment, symbol table, term glosses and their basis, proposition list, rewrite, added/removed information, and domain-check opinion. The original file is publicly readable, but the complete term explanations still need to be supplemented; one must not pretend that an equivalence question bank already exists.

## Later design and refutation

Fix the terms first, then consider a design of "old/modern symbols × compact/explicit expression". Versions must contain the same problem-solving information, and should match length, background cues and layout as closely as possible. When equivalence cannot be achieved, treat the added explanation as an independent factor, and do not attribute it all to grammar. Use grouping or order balancing to avoid the learning effect from having the same person read the hard version before the explained version.

Candidate metrics: comprehension-question accuracy, reading time, reference errors and subjective difficulty. The target population, sample size, minimum meaningful difference, interval estimation and exclusion rules must be fixed before formal testing; this card does not fabricate an already-locked threshold.

If the equivalence check fails, the original reading cue cannot serve as causal material; if, after controlling for background and extra explanation, the gain disappears or reverses, or only some class of readers benefits, the local explanation should be narrowed. "No significant difference" by itself does not establish equivalence; one should check whether the interval is sufficient to exclude the predetermined meaningful gain.

## Optional extension: can one detect that one's own comprehension was wrong?

If an error-detection study is conducted, list separately the ground truth, answer, confidence, whether the error was detected/corrected and the correction time, and compare under the same accuracy standard, without equating slower reading directly with net loss. Define in advance the denominator of the undetected-error rate (all items, answered-wrong items, etc. must not be mixed), the confidence threshold and the calibration method; ordinary glyph-recognition accuracy cannot directly substitute for semantic-comprehension or collaboration metrics.

This is a to-be-studied variable distilled from the [Second-Simplification clue review](./cases/CN-S2_evidence_starting_point.md); it is not an already-obtained Second-Simplification error-detection result. The surname stories have no per-person ground truth or change chain, and cannot serve as ready-made experimental samples. If the extension changes the original task or main result, a separate design version must be listed before the corresponding effect analysis, without switching metrics afterwards to chase significance; there are still no results at present.

## The Second-Simplification material's related task, not merged into the existing experiment

The Second-Simplification related task separately examines, after "distinct values that must be distinguished are mapped to the same glyph", whether correct recognition still holds under single-character, phrase and full-context conditions, and what information/time must be added to preserve accuracy. First verify the draft mapping and the ground truth of the task; variant merging and merging of different task values are kept separate. A phrase is not necessarily an effective remedy; items whose characters were not changed can serve as candidate comparison material, but the grouping and matching rules must be set separately.

This is independent material work for the [Second-Simplification table v0.3](./cases/CN-S2_evidence_starting_point.md); it is not mixed into the same treatment as *Astronomical and Mathematical Essays*, nor reported as an already-enlarged sample. If the existing context/fields are sufficient to preserve distinction with no added burden, this opposing observation must be preserved; net benefit is checked simultaneously across writing, recognition, error correction and affected populations, without predetermining an increase.

## What the author can provide

Entry to the original, a version-difference table, material layout and subsequent data-processing support; readers with expertise in linguistics and history of mathematics are needed to help check the content. Results are kept even if zero or negative. It tests only a local effect, and does not establish the postulates, the six core proposition groups or social isomorphism.
