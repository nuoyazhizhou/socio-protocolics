> **Translation record**
> - Chinese source: `README.md` (sha256 `44d301bd525015a8ecc7b948f1ecdbe010762dee5450bd4fb333723836ed6d1d`, 11958 bytes, 2026-11-09)
> - Chinese version / release tag: `v11.2-r20261106` (theoretical version remains v11.2)
> - Translation version: `en-v0.1`
> - Translation date: 2026-11-09
> - Check status: checked sentence by sentence against the Chinese source for claim status, negative guardrails and numbering; machine and glossary checks only; no independent professional native-speaker review
> - Pending sync: none at present; to be recorded item by item if the Chinese source is updated
> - Status: complete translation
> - Authority: the Chinese SSOT is authoritative; this translation does not constitute a separate set of definitions (C2)

# Socio-Protocolics · 社会系统协议学

> **An open cross-disciplinary research programme using distributed-systems, protocol-stack and multi-agent concepts to organise and examine questions of social coordination, institutional change and governance cost.**

**English** | **[简体中文](../README.md)** &nbsp;|&nbsp; **[Online Documentation (EN)](https://nuoyazhizhou.github.io/socio-protocolics/en/)** · **[中文在线阅读网站](https://nuoyazhizhou.github.io/socio-protocolics/)**  
Project repository: [nuoyazhizhou/socio-protocolics](https://github.com/nuoyazhizhou/socio-protocolics) | Release tag: **v11.2-r20261106** (see the [Revision Record](REVISION_RECORD.md); the unified theoretical version of the whitepaper remains v11.2)

---

## What Does Socio-Protocolics Study?

Large-scale human coordination relies on language, contracts, organisational approvals, legal enforcement and public rules. Institutional economics, historical sociology and political science—such as Mancur Olson on institutional sclerosis, Joseph Tainter on diminishing returns to complexity, Kydland and Prescott on dynamic inconsistency, North and Weingast on credible commitment, Charles Tilly on state formation, James C. Scott on state legibility, F. A. Hayek on distributed information, and Zeynep Tufekci on networked mobilisation—have built rich explanatory accounts, yet their conceptual interfaces often remain fragmented across disciplines. Meanwhile, distributed computing, operating systems and network engineering have developed a precise analytical vocabulary for high-concurrency coordination, privilege boundaries, fault recovery and legacy-system migration.

**Socio-Protocolics** aligns these systems-engineering primitives with mainstream social-science questions in a **Dual-Track Unified Monograph** (`L1 Vernacular layer` in plain systems-engineering language + `L2 Theoretical Spec` as a Multi-Agent Object Model), organising modelling, comparative case analysis and falsifiable testing around six core groups of questions:

1. **Channel Capacity & Semantic Boundary (Group I)**: How do forms of expression and naming rules shape comprehension cost and coordination diffusion? Why do foundational language reforms—such as Hu Shi's written-vernacular Chinese movement (Hu Shi was a leading advocate of replacing classical literary Chinese with written vernacular Chinese in modern China)—lower reading and transmission barriers, whereas other standards stop at formal adoption on paper?
2. **Intermediary Parasitism & Compatibility Decay (Group II)**: Does organisational or institutional middleware provide a genuine translation, authentication and coordination service, or has it evolved into an exclusive gate for non-productive rent extraction? When two approval steps are deleted, does the coordination work really get lighter?
3. **Intertemporal Finality & Expectation Credibility (Group III)**: How do contract enforcement, breach recovery and record durability shape intertemporal finality, and in turn alter agents' expectations and long-term irreversible investments?
4. **Privilege Ring Isolation & Split-Brain Contagion (Group IV)**: How can rule executors themselves be constrained through clear authority boundaries (the Ring-0/Ring-3 privilege-boundary analogy), independent review and remedy? How do resource cutoffs, conflicting multi-headed commands (split-brain) and exit barriers reshape strategic equilibria?
5. **Transport Topology & Task Feedback (Group V)**: Why does large-scale informational mobilisation not automatically translate into sustained governance capacity? How do acknowledgement receipts (ACK), resource resupply and error-correction loops fit together?
6. **Debt Accounting & Evolutionary Selection (Group VI)**: Faced with heavy historical institutional baggage (technical debt), how should the net migration burden of a full rewrite be compared against an incremental Strangler Fig bypass? Under finite budgets, when do parallel multi-branch userland trials and mature-feedback screening outperform a single top-down design?

### Framework Structure and Epistemic Boundaries

- **Three-tier modelling navigation (`3 → 6 → 19`)**: Built on **5 primitive objects** (`O1: Agent`, `O2: Protocol`, `O3: Expectation & Trust`, `O4: Middleware — intermediary interpretation layer`, `O5: Resource & Energy — physical hard constraints`), **3 first-order postulates (P1–P3)** organise **six core proposition groups (I–VI)** and **19 numbered SP-RFC items (001—019, where 003 is a semantic propagation application, 007 is a cross-group normative rule, and 019 is the Chapter 8 cross-group tooling and research norm, with 2 non-numbered materials retained)**. Tier arrows denote modelling dependency and clause attribution; they do not imply that all propositions have been strictly proved from the three postulates.
- **An open research programme, not proven universal laws**: This is a research programme open to revision and counterexample testing. Engineering analogies help compress expression and formulate questions; they do not substitute for mathematical proof or assert social isomorphism. Citations of established physical results, formal conditional propositions, empirical mechanism hypotheses, accounting definitions and normative rules each require their own evidence. The Chapter 8 measurement indicators and reference code constitute **a conceptual formalisation and reference architecture, plus a future empirical research agenda**; they do not claim completed social measurement or predictive capability.
- **Current review progress**: The [online reading site](https://nuoyazhizhou.github.io/socio-protocolics/en/) is generated from the same public Markdown and offers chapter-by-chapter reading, full-text search and formula rendering. The whitepaper is now in chapter-by-chapter review and incremental revision: each round focuses on specific questions within a single chapter, reading the relevant main text, definitions and evidence cards as needed, with discussion conclusions and actual edits recorded separately. The current chapter, open questions and next item are collected in [Chapter Review Progress](ROADMAP.md#chapter-review); installing the chunking tool or passing the automated checks does not establish that a chapter has been reviewed.

**Search Keywords**: `Socio-Protocolics` · `社会系统协议学` · `Protocol Governance` · `Institutional Analysis & Institutional Change` · `Distributed Systems` · `Multi-Agent Systems` · `Middleware Rent-Seeking & Administrative Burden` · `Credible Commitment` · `Technical Debt & Incremental Migration`

---

## Where to Start

### Quick Entry by Reading Goal

- **Start with concrete case essays (no theory prerequisite)**: Read [How to Evaluate Hu Shi's Work: Whether the Work Is Good, and What It Changed](articles/hu-shih/how_to_evaluate_hu_shis_works.md) or [Delete Two Approval Steps, and Did the Work Really Get Lighter?](articles/intermediary/two_approvals_removed.md).
- **Run the Multi-Agent Simulation Sandbox (Socio-Engine)**: Read the [Sandbox Architecture & QuickStart](../socio_engine/README_EN.md) and [Universal Scenario Prompt Template](../socio_engine/docs/UNIVERSAL_SCENARIO_PROMPT_TEMPLATE.md) to replicate Ming Dynasty Huizhou tax games and Hai Rui's breakthrough experiments.
- **10-minute core concept overview**: Browse the [Core Concepts CheatSheet](CHEATSHEET.md) and the [3→6→19 Theme and Case Index](framework_and_case_index.md).
- **Read the whitepaper systematically**: Visit the [Online Reading Site (EN)](https://nuoyazhizhou.github.io/socio-protocolics/en/), or jump straight to [Whitepaper v11.2 (Chapter 1)](whitepaper/chapter-01.md) (with the Chinese SSOT remaining the sole canonical source).
- **Spot errors, critique or pick up an open question**: Explore [Open Questions and Research Designs](research/README.md) or [How to Contribute](CONTRIBUTING.md) (endorsing the overall framework is not a condition of participation).

### Complete Navigation Table

| Category | What you want to see | Entry point |
| --- | --- | --- |
| **Cases & Evidence** | A concrete article open to criticism | [How to Evaluate Hu Shi's Work: Whether the Work Is Good, and What It Changed](articles/hu-shih/how_to_evaluate_hu_shis_works.md) |
| **Cases & Evidence** | The article's sources and evidence boundaries | [Sources for the Hu Shi article](articles/hu-shih/source_notes.md) |
| **Cases & Evidence** | A second theme beyond language reform | [Delete Two Approval Steps, and Did the Work Really Get Lighter?](articles/intermediary/two_approvals_removed.md) |
| **Cases & Evidence** | Check the evidence boundaries of the core cases | [Sources and Boundaries of the Core Cases](case_sources_and_boundaries.md) |
| **Whitepaper & CheatSheet** | Understand the overall framework | [Whitepaper v11.2, phased English translation (Chapter 1)](whitepaper/chapter-01.md) |
| **Whitepaper & CheatSheet** | A quick concept lookup | [Core Concepts CheatSheet](CHEATSHEET.md) |
| **Whitepaper & CheatSheet** | Which postulates and SP-RFCs an article cites, and what other themes lack | [3→6→19 Theme and Case Index](framework_and_case_index.md) |
| **Whitepaper & CheatSheet** | Read or edit a single chapter of the whitepaper | [Reading, Previewing and Replacing by Tag](CHUNK_READING_GUIDE.md) |
| **Open Research** | A small question to take up | [Open Questions and Research Designs](research/README.md) |
| **Open Research** | Whether the engineering claims actually hold up | [OP-001: Comparison Draft of an Engineering Checklist and an Ordinary Process Checklist](research/OP-001/question_card.md) |
| **Open Research** | Accreditation access and organisational autonomy | [OP-002: When Access Absorbs, and When It Protects Independent Inquiry](research/OP-002/question_card.md) |
| **Open Research** | Review an agent-collaboration experiment | [PR-001: Access Cost and Collaboration Scale (Design Draft)](research/PR-001_agent_collaboration_scale.md) |
| **Open Research** | Continue case studies across the six proposition groups | [Implementation Plan and First Tasks for Groups I—VI](research/topic_plan/README.md) |
| **Open Research** | How success and failure are compared | [Case Selection and Comparison Method](research/case_selection_and_comparison_method.md) |
| **Simulation & Sandbox** | Run the Multi-Agent Historical & Institutional Sandbox (Socio-Engine) | [Architecture & Quickstart](../socio_engine/README_EN.md) · [User Guide](../socio_engine/USER_GUIDE.md) |
| **Simulation & Sandbox** | Universal Scenario Prompt Template (Song / Tang / Rome) | [Scenario Prompt Template](../socio_engine/docs/UNIVERSAL_SCENARIO_PROMPT_TEMPLATE.md) |
| **Simulation & Sandbox** | Ming Dynasty Huizhou Tax Archival Baseline | [Historical Baseline](../socio_engine/docs/HISTORICAL_BASELINE.md) |
| **Review & Participation** | Join this round of chapter-by-chapter review | [Chapter Order and Current Progress](ROADMAP.md#chapter-review) · [How to Give Chapter Feedback](CONTRIBUTING.md#chapter-feedback) |
| **Review & Participation** | Report an error or submit a revision | [How to Contribute](CONTRIBUTING.md) |
| **Review & Participation** | The sequence of work and current gaps | [Project Roadmap](ROADMAP.md) |

## Simulation Sandbox & Experimental Tool · Socio-Engine

The theory is not merely a set of whitepaper texts; this project implements an open-source, reproducible **Multi-Agent Historical & Social Systems Protocol Sandbox (Socio-Engine)** to simulate historical institutional transitions and micro/macro games:

- **Dual-Layer Architecture**: The physical foundation is built with native Rust (`socio_core`), strictly enforcing double-entry conservation (silver, grain, land), four-tier privilege ring isolation (Ring-0 to Ring-3), and Petgraph topological blast-radius analysis. The cognitive layer uses Python Agent-as-Data to orchestrate LLM agents (DeepSeek / Claude / GPT) pursuing private utilities $U_i$ and survival limits.
- **Ming Dynasty Huizhou Historical Experiments**: Grounded in authentic tax registers from the *Shexian County Gazettes* and *The Book of Silk* (1573–1577), multiple converged trials have been executed (including standard bureaucrat games, Hai Rui's moral purge triggering clerk strikes, and Hai Rui's institutional breakthrough via "Dis-intermediation" replacing old clerks with students, alongside an anonymized empire ablation study).
- **Universal Scenario Extension**: Provides a self-contained axiomatic meta-prompt allowing researchers to compile new historical reforms (e.g. Northern Song Wang Anshi's Green Sprouts Law, Tang Dynasty Two-Tax Law, Ancient Rome Price Edict) into runnable multi-agent sandboxes.

👉 **Navigation & Getting Started**:
- [Architecture & Quickstart (socio_engine/README_EN.md)](../socio_engine/README_EN.md) ｜ [Chinese Documentation (socio_engine/README.md)](../socio_engine/README.md)
- [User Configuration & API Key Guide (socio_engine/USER_GUIDE.md)](../socio_engine/USER_GUIDE.md)
- [Universal Scenario Prompt Template (socio_engine/docs/UNIVERSAL_SCENARIO_PROMPT_TEMPLATE.md)](../socio_engine/docs/UNIVERSAL_SCENARIO_PROMPT_TEMPLATE.md)
- [Ming Dynasty Huizhou Historical Archival Baseline (socio_engine/docs/HISTORICAL_BASELINE.md)](../socio_engine/docs/HISTORICAL_BASELINE.md)

## How Cases Feed Back into Theory

Each case distinguishes four things: what the external material says, which concepts this article borrows, which assumptions it adds, and which observations would force us to revise. The attention an article receives does not imply verification of the framework; counterexamples, null gains and better existing explanations should all enter the revision record.

The [Open Research Library](research/README.md) welcomes independent researchers who choose their own materials and methods to support, refute or narrow specific sub-claims. The authors provide checkable questions and starting points for sources; findings are written back, according to the evidence, into candidate hypotheses and the whitepaper clauses that need revision; participation does not require endorsing the overall framework.

The Hu Shi case first raises questions of comprehension cost, formal adoption and sample diffusion; these remain local explanations awaiting comparison, and on this basis no postulate or any of the six core proposition groups has been declared corroborated. [Correspondence between the Case and the Whitepaper](articles/hu-shih/source_notes.md#correspondence-with-the-whitepaper) lists the specific boundaries.

The intermediary theme already has a conceptual sample chapter (pending reconstruction with a real case), single-item registration materials from Zhejiang, partial cross-checks of foreign studies, and the OP-001 fictional problem set; it has not passed the real-case acceptance stage (T3). The unified requirements are set out in [Case-Driven Writing and Proposition Testing](CASE_DRIVEN_TESTING.md). The article distinguishes where the work goes, the service provided and the approval gate; OP-001 asks directly whether the engineering representation reduces misinterpretation relative to an ordinary cost checklist. No effect data from this project exist for either, nor has this been used to corroborate all the mechanisms of the second core proposition group.

Later work will bring together Chinese and foreign cases of adoption, obstruction and withdrawal, first distinguishing formal entry, actual adoption, comprehension effects and switching costs, and only then comparing mechanisms. All original documents addressed to readers are written in Chinese first, and an English counterpart is produced for each one in turn; both languages keep the same set of cases. [Bilingual and Writing Conventions](BILINGUAL_CONVENTIONS.md) govern version synchronisation and how articles are linked.

## Directory Layout

```text
社会系统协议学白皮书.md             Canonical text, original path retained
核心概念速查手册_CheatSheet.md      Concept entry point, original path retained
articles/                          Public cases, sources and brief revision notes
research/                          Open questions and material specifications
docs/                              Framework index, writing conventions and publication rules
en/                                English entry points, phased chapter translations, case and research counterparts
socio_engine/                      Multi-Agent Simulation Sandbox (Rust physical kernel + Python cognitive layer)
tools/                             Content checks, public-file check, site builder and history-free export
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
