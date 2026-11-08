> **Translation record**
> - Chinese source: `AGENTS.md` (sha256 `3fd935d6fbb3dbebe134b54d7109a635f650b2f7263e03bf1cf97543ab7adc62`, 16871 bytes, 2026-11-08)
> - Chinese version / release tag: `v11.2-r20261106` (theoretical version remains v11.2)
> - Translation version: `en-v0.1`
> - Translation date: 2026-11-08
> - Check status: checked sentence by sentence against the Chinese source for claim status, negative guardrails and numbering; machine and glossary checks only; no independent professional native-speaker review
> - Pending sync: none at present; to be recorded item by item if the Chinese source is updated
> - Status: complete translation
> - Authority: the Chinese SSOT is authoritative; this translation does not constitute a separate set of definitions (C2)

# Agent Rules for the Systems Architect and Academic Editor of Socio-Protocolics (Sole Directory-Level Authority)

This page is an English translation only. The Chinese AGENTS.md in the repository root is the sole authoritative set of agent rules.

## I. Design Philosophy and System Positioning

This directory is the main repository of the **authoritative archival project for Socio-Protocolics**.

Its theoretical form is a **Dual-Track Unified Monograph: L1 engineer's plain-language vernacular + L2 multi-agent protocol formal specification**.

* **Unified release version**: v11.2 (Orthogonal Axiomatic Foundation Edition)
* **Single Source of Truth (SSOT)**: [Whitepaper v11.2, the sole canonical text](../社会系统协议学白皮书.md)
* **L1 cognitive cache CheatSheet**: [Core Concepts CheatSheet](../核心概念速查手册_CheatSheet.md)
* **Internal unabridged edition**: `社会系统协议学白皮书_内部未删节版.md`, maintained only on the maintainer's local machine and not part of the public repository — not included in public Git tracking or distribution.
* **Pointer distribution entry**: [socio_protocolics_whitepaper.md](../socio_protocolics_whitepaper.md)

**Read on demand, edit locally**: the whitepaper is divided into blocks by paired `SP:BEGIN`/`SP:END` comments for `chapter-01` through `chapter-08` and `appendix`. First use `python tools/whitepaper_blocks.py list` to locate a block, then use `read ID` to read only the body text the task requires; related O/P items, cross-chapter interfaces and generated cards are read as dependencies require, and the full text is not repeatedly output by default. For small edits, prefer changing paragraphs; whole-block replacement is preview-only by default, and is written only after an explicit `--write` and a check of the original block's SHA-256; the tags, existing anchors and content outside the blocks are preserved. See [Reading, Previewing and Replacing by Tag](../docs/白皮书分块读取与编辑.md) for details. Tags are not a new definition source, and a local read must not be used to omit conditions that affect the conclusion.

**Chapter-by-chapter discussion and revision**: this round's order, status and open questions are recorded together in [Chapter Review Progress](../ROADMAP.md#chapter-review), rather than keeping a separate progress copy in each of the four entry files. Each round first reads back the current item and existing conclusions in that table, then reads the target block and any necessary dependencies; by default it focuses on one subsection or a small number of disputed points, discussing the original text, the question, optional changes and their costs, and does not re-review the whole book by default.

When the user asks only for discussion or evaluation, the main text is not changed automatically; once a modification, revision or implementation is explicitly requested, it is completed within the already-authorised scope without asking for permission again. Each round distinguishes among retaining, rewording, splitting, moving to candidate research, holding pending material, and declining, together with the reasons; a decision to retain may be made even without new evidence, and the theory is not forcibly changed merely to show progress. When executing, update the master source and the affected generated cards, CheatSheet, source notes and purpose branches incrementally; synchronise the internal edition according to the shared conventions and the actual changes, without overwriting private annotations chapter by chapter. Full conversations and working drafts remain local; the public progress record carries only concise conclusions, gaps and the next item. Passing the automated checks records only that the designated checks passed, and does not present a finished discussion as the theory having been substantiated.

---

## II. Fatal Red Lines and Meta-Principles (Touching Them Damages the Theoretical Foundation; Remember Them Permanently)

1. **The three-tier orthogonal pyramid must never be conflated**:
   * Strictly observe [Layer 0: the 3 first-order postulates] → [Layer 1: the 6 core proposition groups] → [Layer 2: the 19 SP-RFC items numbered continuously 001—019];
   * Do not extend the coverage of existing clauses by adding new phenomena; any merge must check the objects, premises and results. 003 is a semantic application, 007 is a cross-group normative rule, and 019 is the Chapter 8 cross-group tooling/research norm; the former v11.1 numbers 006/010 are retained as non-numbered materials and are not claimed to have been demonstrated by another model. Old numbers are interpreted by version, and old and new numbers sharing the same value must not be mixed.
   * The six groups respectively identify citations of established physical results, conditional propositions, mechanism hypotheses or accounting definitions; they must not be collectively called proven universal laws. Group VI is uniformly named "Debt Accounting & Evolutionary Selection".
   * Postulates and normative clauses (RFCs) must never be conflated under the single name of axioms; "orthogonal" denotes orthogonal as a division of responsibilities, and formal independence requires separate proof; the tier arrows denote modelling dependency and navigation, and cannot substitute for additional assumptions, a complete proof or empirical testing; a group-level summary cannot serve as the proof of its own sub-clauses;
   * Objective physical descriptive laws must never be conflated with the architect's subjective precepts (`SP-RFC-007` must be strictly marked as a normative operational rule and must not be listed alongside objective laws).
2. **Tautological formulas and circular argument are strictly forbidden**:
   * Postulate P1 defines finite physical energy, irreversible time and the abnormal-state priority boundary; it must not embed RFC-017's concrete net-present-value accounting formula;
   * Proposition Group VI and RFC-017 handle the full accounting of technical debt and the refactoring/migration cost model; tautological circular argument of the form $A \implies A$ is absolutely excluded.
3. **Maintain alignment with the cross-disciplinary academic radar and the unified meta-compiler positioning**:
   * In `§1.6` and elsewhere, maintain in-depth term mapping with the classics of social science (Olson's institutional sclerosis, Tainter's diminishing returns to complexity, Kydland–Prescott time inconsistency, North–Weingast credible commitment, Tilly's bandit economics, Scott's state legibility, Hayek's distributed prices, Tufekci's network mobilisation);
   * At the same time firmly maintain the meta-theoretical research programme and unified modelling language of the "unified meta-compiler for computing systems engineering": map cross-disciplinary mechanisms onto comparable interfaces and draw on industrial-grade reference implementations; do not claim that industrial operating scale demonstrates social isomorphism, and do not claim that the formalisation and empirical validation of all social experience has been completed. Incremental contributions must undergo testing for predictive gain relative to existing explanations.
4. **SP-POSTULATE-1, RFC-017 & RFC-018 constrain the theory itself (against the Happy Path and the top-designer illusion)**:
   * Reject analysing only the ideal path (Happy Path); test both the normal state and the abnormal state, and prioritise low-frequency, high-loss events. The "99% exception path" (Exception Path) is a non-empirical cautionary phrase, not a count of paths, a runtime share or an incident rate;
   * Do not fall into the utopian frenzy of a "Happy Path simulator"; **a destructive wholesale rewrite of the whitepaper from scratch is strictly forbidden (the Netscape 6 trap)**. Theoretical evolution follows an incremental Strangler Fig bypass (Strangler Fig Pattern);
   * **Dispel the "top-designer illusion" (the essence is evolution, not a deity)**: maintain multi-branch trials in userland (Ring-3) and PDCA evolutionary screening. $K\gg1$ and $\Delta t\to0$ are retained as engineering slogans encouraging diversity and timely feedback; an executable model must satisfy a finite budget, branch independence and $T_{\text{latency}}\le\Delta t<T_{\text{environment}}$, and does not imply infinite concurrency, zero feedback latency or the inevitable failure of a single branch. The architect acts as gatekeeper of the evolutionary racecourse and Bazaar Maintainer & Merge Architect; the mainline may be autonomous or an industry standard, and the state authorisation interface is used only for goals such as compulsory state enforcement.
5. **Break the "Hu Shi Paradox" and defend the engineering compression primitives**:
   * Do not strip out accessible computer-engineering terms (TCP/UDP, Ring-0/3, memory isolation, compiler) in order to court the scholastic school;
   * Hold to "scholarship as the load-bearing wall, plain language as the interior finish", and refuse to degenerate into obscure, dry scholastic jargon.
6. **Tone Compartmentalization**:
   * [Normative clauses / Normative Spec]: keep the cool, objective, restrained, clinical-diagnostic language of systems science and distributed control.
   * [Annotations & Case Studies]: fully retain the pungent, sharp, satirical critical edge and vivid historical slices.
7. **Falsifiability Boundary Up Front**:
   * Conditional propositions state their assumptions, quantifiers and derivations; empirical mechanism hypotheses state operationalisable rejection conditions, comparison objects and error requirements; accounting definitions state units, scope and items that cannot be mixed in the accounting; normative rules state objectives, rights and costs. The identical holding of a definition must not be treated as empirical verification, nor may a normative choice be passed off as a physical theorem.
8. **Epistemological caution, Socio-Radar methodological modesty and the empirical-boundary red line (strictly guarding against pseudo-certainty)**:
   * Socio-Radar must never be advertised as "an operating system that can already measure society" (guarding against charges of false precision); it is strictly anchored as **a conceptual formalisation and reference architecture, plus a future empirical research agenda**;
   * Indicators for which reproducible measurement materials and methods are not provided must not be labelled measured results; hypothetical indicator values in historical cases must be marked as "illustrative worked examples showing the calculation logic", and no predictive power may be claimed on that basis. Sourced historical records, the author's interpretations and simulated values are labelled separately; when the sample size is insufficient, extrapolation is restricted, and small-sample observations are not uniformly relabelled as simulations;
   * Engineering analogies must never be equated directly with mathematical proof; all borrowed terms must undergo equivalent testing of comprehension cost, definitional stability and predictive gain;
   * The automated verification gate checks only the directory, numbering, textual completeness and reference algorithm implementations; it does not mean that empirical validation of external physical reality has been completed.
9. **Real cases first, reverse testing and theoretical write-back (binding on all authors and agents)**:
   * Case articles test, support, refute or narrow specific sub-claims with real-world evidence, and check the gain relative to existing explanations; the whitepaper must not first be assumed correct and stories then sought to corroborate it, and reach or case count must not substitute for theoretical evidence.
   * Before drafting, the topic plan must register the target sub-claim, its position in the master source and its epistemic status, the real main case and its evidence chain, real counter-material or a sourced competing explanation, the observations that would change the verdict, and the gaps; continuations and translations must read back and update that card. Where a historical outcome is already known, state its retrospective character explicitly and do not present it as an ex ante prediction.
   * At least one real main case must be developed with its objects, period, actors, rules/decisions, key processes and checkable results, with key facts carrying original sources and locations; at least one piece of real counter-material, opposing observations in the same case, or a sourced competing explanation must be checked. Hypothetical counterexamples cannot substitute for retrieval and checking. When material is insufficient, continue the evidence work or record the reason for changing the case; do not fabricate motives, dialogue, data or outcomes.
   * Fictional scenarios serve only as explicitly labelled leads, and simulated numbers only demonstrate the accounting; neither may carry real-world conclusions. A text consisting mainly of conceptual explanation, fictional worked examples or scattered name-checks of real material must be labelled a "conceptual sample chapter, pending reconstruction with a real case", and does not count as an article that has completed case testing.
   * An engineering mapping states what is retained and what is lost, and whether an ordinary explanation already covers it. Formal propositions, empirical hypotheses, accounting definitions and normative objectives are adjudicated separately; an unsatisfied premise is an application boundary and does not automatically overturn a formal derivation. Partial support, rejecting a specific empirical prediction, narrowing the application, the sufficiency of an existing explanation, or insufficient evidence are all permitted; favourable and unfavourable results must not both be written up as the same proposition having been substantiated.
   * Each article supplies a "claim–supporting/opposing evidence–competing explanation–verdict–proposed revision location" receipt. Where the theory changes, update the SSOT and derived drafts incrementally and run regression; where evidence is insufficient, state plainly that the theory is not revised for now, do not change the theory merely to produce a revision, and do not edit only the audit report. Templates and stage acceptance are governed by [Case-Driven Writing and Proposition Testing](../docs/案例驱动写作与命题检验.md). This rule also binds new topics, continuations of existing drafts, revisions and translations.

---

## III. Quick Reference: Five Foundational Primitives, Three First-Order Postulates and Six Core Proposition Groups

* **O1: Agent** (an adaptive game unit with a private objective function $U_i$ and discount factor $\beta_i$)
* **O2: Protocol** (a cross-node rule set $\mathcal{P} = \langle \Sigma, \mathcal{S}, \delta, \mathcal{R} \rangle$)
* **O3: Expectation** (the subjective probability distribution $\mu_{i,t}(A)=\Pr_i(S_{t+1}\in A\mid\mathcal I_{i,t},\mathcal P_t)$ of agent $i$ under information set $\mathcal I_{i,t}$ and protocol $\mathcal P_t$; different agents' beliefs may differ. For an integrable function $f$, the expected value is $\mathbb E_i[f(S_{t+1})]=\int f(s)\,d\mu_{i,t}(s)$; the expected value is not to be taken as the distribution.)
* **O4: Middleware** (a structure between terminal Agents that performs translation, authentication, routing, supervision or coordination; its net contribution must be compared with feasible alternative mechanisms. Only the subclass exhibiting exclusive control and non-productive rent extraction is subject to rent-seeking compatibility-layer analysis)
* **O5: Resource** (the resource feasibility domain and constraint set $\Omega$ bounded by available energy, land, physical channel capacity and irreversible time; thermodynamic laws constrain resource conversion, and the laws themselves are not treated as disposable resources)

* **SP-POSTULATE-1 (The Finite World & Non-Zero Impedance Postulate)**: finite energy and cognitive bandwidth; information-transmission dissipation; physical channel capacity and social semantic bridging are kept separate, and the latter must be calibrated independently; the "99% exception path" is a non-empirical cautionary phrase; the normal state and the abnormal state are assessed separately; boundary conditions come first.
* **SP-POSTULATE-2 (The Agent Autonomy Postulate)**: an Agent possesses independent utility and freedom of strategic deviation; it is not a mechanical executor or a logic gate.
* **SP-POSTULATE-3 (The Expectation-Induced Equilibrium Postulate)**: a protocol influences incentives and action by reshaping agents' beliefs and cannot be driven mechanically by force; the existence and uniqueness of a Nash equilibrium, and the convergence of update dynamics, must each be argued in a specified model.

* **6 Core Proposition Groups**:
  1. Proposition Group I: Channel Capacity & Semantic Boundary (RFC-001, 002, 003: semantic propagation application)
  2. Proposition Group II: Intermediary Parasitism & Compatibility Decay (RFC-004, 005, 006; cross-group rule entry: RFC-007)
  3. Proposition Group III: Intertemporal Finality & Expectation Credibility (RFC-008, 009, 010)
  4. Proposition Group IV: Privilege Ring Isolation & Split-Brain Contagion (RFC-011, 012, 013, 014, 015)
  5. Proposition Group V: Transport Topology & Task Feedback (RFC-016)
  6. Proposition Group VI: Debt Accounting & Evolutionary Selection (RFC-017, 018)

* **Cross-group tooling/research norm**: RFC-019 is located in Chapter 8 and is not counted among Group VI's deductive clauses; the normative status of both 007 and 019 must be stated separately, with their objectives, costs and verification methods.
* **Non-numbered materials**: the candidate process diagram at the end of Group II's chapter, and the consumption and policy application note at the end of Group III's chapter. The former v11.1 number entries are retained, and valid content is not deleted because a number was retired.

---

## IV. Automated Quality Gate (Verification Gate)

After modifying the whitepaper, the CheatSheet or these rules, the repository's own [verify_all.py](../tools/verify_all.py) must be run. Python 3.10+ is required; on the first run, install the [reference-engine dependencies](../tools/requirements.txt) first:

```powershell
python -m pip install -r tools/requirements.txt
python tools/verify_all.py
python tools/test_whitepaper_blocks.py
python tools/check_public.py
# When modifying the clause-directory checks, also run the negative structural regression:
python tools/test_verify_structure.py
```

The default gate checks the public whitepaper, the CheatSheet and these rules, and does not require reading internal material. The script locates repository files relative to its own position; when run from another directory, the correct path to the script must be given. The default report explicitly lists "internal edition and cross-version comparison not checked", and must not claim that a four-document regression has been completed.

The gate also includes a **same-version anchor reachability check**: every internal link in the version being checked must find its corresponding anchor within that same version, anchor ids must not be duplicated, and "case-level anchors" are not permitted (this book provides only section-level anchors; a case such as `案例 3.7-B` is merely a running-text label and does not carry its own anchor). It judges only whether an anchor exists, not whether the content pointed to supports the claim; nor does it check external URL liveness, cross-file links, or heading anchors auto-generated after rendering. After changing an anchor or a link, the gate must be re-run, and "all checks green" must not be read as "links are reachable".

**Cross-file links (of the form `文件.md#锚点`) are outside the scope of verify_all**; the site must be rebuilt first and then checked with [check_site.py](../tools/check_site.py); site dependencies are listed in [requirements-site.txt](../tools/requirements-site.txt). If the site dependencies are not installed, or the site build output is older than the body text, **"cross-file anchors not checked" must be reported plainly**, and link reachability must not be claimed on the grounds that the regular gate is all green. Such cross-file anchors exist in the CheatSheet, these rules, README and ROADMAP, so this check must be re-run especially after changing body text or subsection headings.

When the maintainer modifies the local internal edition or the shared conventions, the internal edition must also be specified explicitly:

```powershell
python tools/verify_all.py --internal ".local/内部资料/社会系统协议学白皮书_内部未删节版.md"
```

`--internal` relative paths are resolved from the repository root, and absolute paths are also accepted; if the specified file is missing or unreadable, the run fails rather than skipping silently. This mode adds structural and reference-code checks for the internal edition, plus a word-for-word comparison of §1.5 and §1.6 in the two texts, and does not mean the other chapters are identical in full. The internal edition is still not for public distribution.

Ensure that the 19 effective SP-RFC items, the version-number comparison, the three first-order postulates, the attribution of the six core proposition groups, the cross-disciplinary academic radar markers and the reference-code cases listed by the gate all pass; report the actual mode, checked items, unchecked items and failed items. Passing indicates only that these structural, textual and reference-implementation checks passed, and does not mean that full-text semantic consistency, mathematical proof or external empirical validation has been completed. Missing dependencies or missing files must be reported as a failure, and cannot be replaced by a public-scope check.

## V. Public Directory and Local Materials

* Public files use `public-files.json` as their per-file manifest; the whitepaper and the CheatSheet retain their original paths. New cases go in `articles/`, and open questions in `research/`.
* The internal edition, conversations, discussions, working drafts, reviews and audit evidence remain local; real files are not deleted and are not entered into the public index; public revision summaries do not reproduce original internal material.
* `.gitignore` cannot erase existing history; ceasing to track a file must not be described as history cleanup being complete; public export uses `tools/export_public.py` and does not copy the old `.git`.
* The publication-scope check is `python tools/check_public.py`, run separately from the content regression gate above; when exporting without a Git snapshot, use `python tools/check_public.py --snapshot` to check the file scope, and do not claim that the Git index has been checked.
