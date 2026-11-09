> **Translation record**
> - Chinese source: `README.md` (sha256 `e16332aa5ea69c3da96faff8f2de6776f4ff295c475b37595c3017c112cd5a95`, 6341 bytes, 2026-11-07)
> - Chinese version / release tag: `v11.2-r20261106` (theoretical version remains v11.2)
> - Translation version: `en-v0.1`
> - Translation date: 2026-11-07
> - Check status: checked sentence by sentence against the Chinese source for claim status, negative guardrails and numbering; machine and glossary checks only; no independent professional native-speaker review
> - Pending sync: none at present; to be recorded item by item if the Chinese source is updated
> - Status: complete translation
> - Authority: the Chinese SSOT is authoritative; this translation does not constitute a separate set of definitions (C2)

# Socio-Protocolics

Project repository: [nuoyazhizhou/socio-protocolics](https://github.com/nuoyazhizhou/socio-protocolics).

Release tag: **v11.2-r20261106**; see the [Revision Record](REVISION_RECORD.md). The [online reading site](https://nuoyazhizhou.github.io/socio-protocolics/) is generated from the same public Markdown and offers chapter-by-chapter reading, search and formula rendering; the unified whitepaper version remains v11.2.

The framework uses engineering concepts—protocols, interfaces, middleware, migration and feedback—to organise questions about social coordination. This repository holds the whitepaper, case articles written for a general readership, and open research questions ready to be taken up and tested.

This is a research programme open to revision: engineering analogies help formulate questions, whereas historical explanations, mathematical propositions and empirical effects each require their own evidence.

The whitepaper is now in chapter-by-chapter review and incremental revision. Each round focuses on specific questions within a single chapter, reading the relevant main text, definitions and evidence cards as needed; the conclusions of a discussion and the actual edits are recorded separately. The current chapter, open questions and next item are collected in [Chapter Review Progress](ROADMAP.md#chapter-review); installing the chunking tool or passing the automated checks does not establish that a chapter has been reviewed.

## Where to Start

| What you want to see | Entry point |
|---|---|
| A concrete article open to criticism | [How to Evaluate Hu Shi's Work: Whether the Work Is Good, and What It Changed](articles/hu-shih/how_to_evaluate_hu_shis_works.md) |
| The article's sources and evidence boundaries | [Sources for the Hu Shi article](articles/hu-shih/source_notes.md) |
| A second theme beyond language reform | [Delete Two Approval Steps, and Did the Work Really Get Lighter?](articles/intermediary/two_approvals_removed.md) |
| Whether the engineering claims actually hold up | [OP-001: Comparison Draft of an Engineering Checklist and an Ordinary Process Checklist](research/OP-001/question_card.md) |
| Accreditation access and organisational autonomy | [OP-002: When Access Absorbs, and When It Protects Independent Inquiry](research/OP-002/question_card.md) |
| A small question to take up | [Open Questions and Research Designs](research/README.md) |
| Review an agent-collaboration experiment | [PR-001: Access Cost and Collaboration Scale (Design Draft)](research/PR-001_agent_collaboration_scale.md) |
| Check the evidence boundaries of the core cases | [Sources and Boundaries of the Core Cases](case_sources_and_boundaries.md) |
| Understand the overall framework | [Whitepaper v11.2, the sole canonical text](whitepaper/chapter-01.md) |
| Read or edit a single chapter of the whitepaper | [Reading, Previewing and Replacing by Tag](CHUNK_READING_GUIDE.md) |
| Join this round of chapter-by-chapter review | [Chapter Order and Current Progress](ROADMAP.md#chapter-review) · [How to Give Chapter Feedback](CONTRIBUTING.md#chapter-feedback) |
| A quick concept lookup | [Core Concepts CheatSheet](CHEATSHEET.md) |
| Report an error or submit a revision | [How to Contribute](CONTRIBUTING.md) |
| The sequence of work and current gaps | [Project Roadmap](ROADMAP.md) |
| Which postulates and SP-RFCs an article cites, and what other themes lack | [3→6→19 Theme and Case Index](framework_and_case_index.md) |
| Continue case studies across the six proposition groups | [Implementation Plan and First Tasks for Groups I—VI](research/topic_plan/README.md) |
| How success and failure are compared | [Case Selection and Comparison Method](research/case_selection_and_comparison_method.md) |

## How Cases Feed Back into Theory

Each case distinguishes four things: what the external material says, which concepts this article borrows, which assumptions it adds, and which observations would force us to revise. The attention an article receives does not imply verification of the framework; counterexamples, null gains and better existing explanations should all enter the revision record.

The [Open Research Library](research/README.md) welcomes independent researchers who choose their own materials and methods to support, refute or narrow specific sub-claims. The authors provide checkable questions and starting points for sources; findings are written back, according to the evidence, into candidate hypotheses and the whitepaper clauses that need revision; participation does not require endorsing the overall framework.

The Hu Shi case—Hu Shi was a leading advocate of written vernacular Chinese in modern China—first raises questions of comprehension cost, formal adoption and sample diffusion; these remain local explanations awaiting comparison, and on this basis no postulate or any of the six core proposition groups has been declared corroborated. [Correspondence between the Case and the Whitepaper](articles/hu-shih/source_notes.md#correspondence-with-the-whitepaper) lists the specific boundaries.

The intermediary theme already has a conceptual sample chapter (pending reconstruction with a real case), single-item registration materials from Zhejiang, partial cross-checks of foreign studies, and the OP-001 fictional problem set; it has not passed the real-case acceptance stage (T3). The unified requirements are set out in [Case-Driven Writing and Proposition Testing](CASE_DRIVEN_TESTING.md). The article distinguishes where the work goes, the service provided and the approval gate; OP-001 asks directly whether the engineering representation reduces misinterpretation relative to an ordinary cost checklist. No effect data from this project exist for either, nor has this been used to corroborate all the mechanisms of the second core proposition group.

Later work will bring together Chinese and foreign cases of adoption, obstruction and withdrawal, first distinguishing formal entry, actual adoption, comprehension effects and switching costs, and only then comparing mechanisms. All original documents addressed to readers are written in Chinese first, and an English counterpart is produced for each one in turn; both languages keep the same set of cases. [Bilingual and Writing Conventions](BILINGUAL_CONVENTIONS.md) govern version synchronisation and how articles are linked.

## Directory Layout

```text
社会系统协议学白皮书.md             Canonical text, original path retained
核心概念速查手册_CheatSheet.md      Concept entry point, original path retained
articles/                          Public cases, sources and brief revision notes
research/                          Open questions and material specifications
docs/                              Directory and publication conventions
tools/                             Content checks, public-file check, history-free export
public-files.json                  Explicit per-file public manifest
```

Local working materials are not part of the public directory. Python 3.10+ is required; after installing the reference-engine dependencies for the first time, run two kinds of checks:

```powershell
python -m pip install -r tools/requirements.txt
python tools/verify_all.py
python tools/check_public.py
```

`verify_all.py` checks the designated structure, text boundaries and reference code of the public documents; by default it does not read the internal edition. The maintainer's procedure for checking the internal edition is described in [AGENTS.md](AGENTS.md#iv-automated-quality-gate-verification-gate). To obtain a file bundle without the old Git history, run `python tools/export_public.py`. For the exact boundaries see [Publication and Directory Conventions](PUBLICATION_CONVENTIONS.md). These checks do not substitute for checking the literature, mathematical proof or empirical validation.

No unified open licence has been declared for this repository. The contents may be read publicly and suggestions submitted; redistribution, adaptation and the scope of contribution licensing remain to be determined by the author, and hosting on GitHub does not by itself confer an MIT or CC BY licence.
