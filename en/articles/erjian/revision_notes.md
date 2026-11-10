> **Translation record**
> - Chinese source: `articles/erjian/修订说明.md` (sha256 `65866251b18283a73503c8dfad7d08b61b0c1f9bb5a88f892f9aee3d30a0d755`, `4156` bytes, 2026-11-10)
> - Chinese version / release tag: `v0.1` (theoretical version remains v11.2)
> - Translation version: `en-v0.1`
> - Translation date: 2026-11-10
> - Check status: checked sentence by sentence against the Chinese source for claim status, negative guardrails and numbering; machine and glossary checks only; no independent professional native-speaker review
> - Pending sync: synchronized in public-files.json and mkdocs.yml
> - Status: complete translation
> - Authority: the Chinese SSOT is authoritative; this translation does not constitute a separate set of definitions (C2)

# Second-Round Simplification & Script Reform Topic: Revision Notes

Version: v0.1 | Date: 2026-11-10 | Complete English translation of `articles/erjian/修订说明.md`.

This document records the evolution of [*Why Did First-Round Simplified Characters Succeed While Second-Round Simplification Was Halted? — "Hash Collisions" and Disambiguation Cost Shifting in Chinese Character Reform*](why_second_round_simplification_was_halted.md) from evidence-card screening and drafting to substantive audit and bilingual synchronization.

---

## v0.1: Project Registration, Drafting, and Boundary Audit Based on the CN-S2 Evidence Card (2026-11-10)

1. **Strict Alignment with the `CN-S2` Evidentiary Baseline**:
   - Re-read and upgraded the [CN-S2 Evidence Starting-Point Card v0.5](../../research/cases/CN-S2_evidence_starting_point.md) and the [Group I Topic Plan](../../research/topic_plan/I_channel_capacity_and_semantic_boundary.md) prior to drafting, anchoring this topic as a **reverse-test case against the over-strong extrapolation of [SP-RFC-001](../../whitepaper/chapter-02.md#sp-rfc-001) ("fewer strokes / shorter symbols automatically lower comprehension cost")**, cross-linked with **[SP-RFC-017](../../whitepaper/chapter-07.md#sp-rfc-017)** installed-base migration cost accounting.
2. **Exclusion of Unverified Percentages and Pseudo-Precise Arithmetic (Audit Correction 1)**:
   - Enforced all screening decisions from the [CN-S2 Evidence Card](../../research/cases/CN-S2_evidence_starting_point.md), **completely excluding** unverified claims from outside secondary drafts—including alleged Second-Round recognition rates of *"83.5%/91.3% vs. 46.4%/66.9%,"* average stroke counts of *"13.1 → 6.9,"* the *"16x morpheme loss amplification (3,500 → 56,008),"* and the claim that *"merging two characters always loses 1 bit that can never be recovered"*;
   - Built the narrative strictly on verified official administrative transcriptions (`S1`: `Jingzhengfa [1986] No. 107` forwarding `Guofa [1986] No. 64` and the State Language Commission submission), Unicode technical standards (`UAX #38 §3.7.1 & §3.4`), the psycholinguistic megastudy (`R1`: Tsang et al., 2023/2024), and Korean/Vietnamese archival preservation records (`K1/V1`).
3. **Incorporating the 1956 First-Round Simplification Counter-Example and Context Tiers (Audit Correction 2)**:
   - Refused to mythologize the 1956 First-Round Simplification as "zero many-to-one merges or 100% lossless/reversible"; directly addressed why 1956 merges (`后/後`, `发/發/髮`) operated stably in prose;
   - Introduced a three-tier contextual gradient (**context-rich sentences & fixed disyllabic compounds vs. zero-context short fields [names/indexes/headers] vs. cross-generational single-record inversion**) alongside **marginal collision density** and **installed-base lock-in (1956 cold-start vs. 1977–1986 dictionary and fixed-mask ROM chip lock-in)** to explain the divergent outcomes.
4. **Explicit Demarcation of Engineering Analogies and Surname Illustrations (Audit Correction 3)**:
   - Placed an explicit boundary note beside the first appearance of "Hash Collision," defining it as an **engineering analogy for disambiguation cost shifting under many-to-one mapping ($f(A)=f(B)=X$)** rather than mathematical isomorphism to cryptographic hash tables;
   - Bounded surname examples (*Dai* 代/戴, *Fu* 付/傅, *Xiao* 肖/萧) strictly as **conditional structural illustrations of restricted-context fields**, stating explicitly that they do not substitute for per-person household register audits or prove that all modern bearers of those spellings resulted from the 1977 draft.
5. **Addition of the *Three-Category Mapping Catalog of the 1977 Draft & Official 1986 Collision Rollbacks Appendix* (Audit Enhancement 4)**:
   - Based on the full public transcriptions of the 1977-12-20 *Second Chinese Character Simplification Scheme (Draft)* (`S2`) and the 1986-10-10 *Explanatory Note on Re-Publishing the "General Table of Simplified Characters"* (`S3`), added the **[Appendix: Three-Category Mapping Catalog from Source to Target](why_second_round_simplification_was_halted.md#erjian-mapping-appendix)** at the end of the essay;
   - Strictly distinguished **Table 1 (immediate trial use in Dec 1977)** from **Table 2 (discussion draft)**, documenting exact table locations and structural effects across **Table A: Cross-Semantic Many-to-One Homophone Merges ($f(A)=f(B)=X$)**, **Table B: Newly Coined Outlines & Component Replacements ($f(A)=A'$)**, and **Table C: Official 1986 Collision Rollbacks (`叠/覆/像/啰/瞭`)**.
6. **Theory Write-Back Verdict**:
   - Because Whitepaper v11.2 provisions `SP-RFC-001`, `SP-RFC-007`, `SP-RFC-012/014`, and `SP-RFC-017` already distinguish physical symbol length, semantic disambiguation overhead, and migration switching costs, **no edits to the Whitepaper main text are required in this round**.

