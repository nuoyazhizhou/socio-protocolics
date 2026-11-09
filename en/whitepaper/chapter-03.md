> **Translation record**
> - Chinese source: `社会系统协议学白皮书.md`, block `chapter-03` — 369 lines, 46698 bytes, block sha256 `7933c32d20ed56c764071e6916af32d2058ef3fcd3172d409d379233154621b3`, taken as the content between the `<!-- SP:BEGIN chapter-03 -->` and `<!-- SP:END chapter-03 -->` markers and reported by `tools/whitepaper_blocks.py list`; whole-file sha256 `d5ffb73e3db73f8bb42a2ecb39871bf6c55eace8bb72111b63a2ee362134d9c8`, 338639 bytes, 2026-11-08
> - Chinese version / release tag: `v11.2-r20261106` (theoretical version remains v11.2)
> - Translation version: `en-v0.1-ch03`
> - Translation date: 2026-11-08
> - Check status: draft; C12 self-check run after write; independent read-only audit to follow; machine and glossary checks only; no independent professional native-speaker review
> - Pending sync: none at present; to be recorded item by item if the Chinese source is updated
> - Status: complete translation of this chapter block, including all 17 case-annotation entries (batch 4, 2026-11-09); nothing inside the block is omitted
> - Authority: the Chinese SSOT is authoritative; this translation does not constitute a separate set of definitions (C2)
> - Note on group name: the SSOT is internally inconsistent about Proposition Group II's name — the chapter title and table of contents (lines 35, 559) read "中介净贡献、复杂性与规范选择" (Intermediary Net Contribution, Complexity, and Normative Choice), while the overview tables (lines 274, 2420–2422) and the already-landed appendix / chapter-01 use "中介寄生与兼容层衰减" → "Proposition Group II: Intermediary Parasitism & Compatibility Decay". To keep the English edition internally consistent, this file follows the established landed form "Proposition Group II: Intermediary Parasitism & Compatibility Decay"; the SSOT's name inconsistency is flagged for the maintainer to reconcile.

**Scope and edition status.** This file is one block of a **phased** translation. As of batch 4 (2026-11-09), this file contains the complete chapter block, including the full case-annotation layer: the normative framework text, RFC 3.1–3.8, the §3.4 architect's conceptual-boundary statement, the comparison tables, the two ASCII diagrams, and all 17 case-annotation entries listed in the translation record are translated, and the Chinese master source remains authoritative (C2). The case-annotation sections retain the source's sharp register. Completeness of this block does not imply completeness of the edition, and this translation does not elevate any claim to established status. The block itself runs from the `<!-- SP:BEGIN chapter-03 -->` marker to the `<!-- SP:END chapter-03 -->` marker; the translation record, the chapter glossary and the two notes below precede that boundary and are not part of the translated text.

## Chapter Glossary — Chapter 3

| Chinese | English used in this file | Remark |
| :--- | :--- | :--- |
| 第二组核心命题：中介寄生与兼容层衰减 | Proposition Group II: Intermediary Parasitism & Compatibility Decay | group name, unique form in the whole book (SSOT title variant flagged) |
| 6 个核心命题组 | 6 Core Proposition Groups | H3-A landed |
| 19 项有效 SP-RFC | 19 Effective SP-RFC Items | title-case unique |
| 条件模型 | conditional model | claim identity |
| 条件性机制假说 | conditional mechanism hypothesis | claim identity |
| 条件判断与应用比较 | conditional judgment and application comparison | claim identity |
| 跨组规范守则 | cross-group normative rule | claim identity |
| 候选过程模式 | candidate process pattern | claim identity (non-numbered) |
| 串行兼容层 | serial compatibility layer | RFC-004 |
| 条件损耗率 | conditional loss rate | RFC-004 |
| 归一化保留率 | normalised retention rate | RFC-004 |
| 审批时延 | approval latency | RFC-006 |
| 任务生存期（TTL） | task lifetime (TTL) | RFC-006 |
| 任务期限 | mission deadline | RFC-006 |
| 保护收益 | protection benefit | RFC-006 |
| 可理解性 | understandability | RFC-007 |
| 规范守则 | normative rule | RFC-007 (locked title uses "Precepts"; "precept" where the source says 戒) |
| 极简人话戒 | The Plain Language Mandate | RFC-007 precept 1 |
| 斩断寻租戒 | The Proxy Bypass Mandate | RFC-007 precept 2 |
| 断然重构戒 | The Radical Refactoring Mandate | RFC-007 precept 3 |
| Ring-3 | Ring-3 | user-space sandbox, §3.4 |
| Code Smell | code smell | §3.4, §3.7.1 |
| Work-to-Rule | Work-to-Rule | §3.1 |
| Zero-Cost Abstraction | Zero-Cost Abstraction | §3.1 |
| Mētis / Repair Work | Mētis / Repair Work | §3.1 productive fault-tolerance buffer |
| Hard Fork | Hard Fork | §3.5 |
| WS-* | WS-* | §3.3-B, §3.6, §3.6.1, §3.7-D |
| 规范膨胀 | normative inflation / bloat | §3.2, §3.6.1 |
| 寄生 | parasitism | §3.2, §3.6.1, §3.7-D |
| BGP 路由劫持 | BGP Hijacking | §3.4 meta-annotation; the SSOT quotes the Chinese phrase here, while the locked glossary form is the source-provided proper name used in the Chapter 5 glossary and the appendix |
| 非幂等死锁 | non-idempotent deadlock | §3.4 meta-annotation |
| Ring-3 内存隔离 | Ring-3 memory isolation | §3.4 meta-annotation |
| O1–O5 | O1 Agent / O2 Protocol / O3 Expectation & Trust / O4 Middleware / O5 Resource & Physical Constraint | primitive-object codes |
| P1–P3 | P1 resource background / P2 agent autonomy / P3 expectation-induced equilibrium | assumption codes |

**Note on claim identities.** The claim-identity labels in this chapter (RFC 004: conditional model; RFC 005: conditional mechanism hypothesis; RFC 006: conditional judgment and application comparison; RFC 007: cross-group normative rule; the §3.8 candidate process pattern) are descriptive phrases at the grain of the source sentence (per R7 of the term ledger), not a taxonomy of claim identities. This translation keeps the five canonical claim identities — `postulate`, `conditional proposition`, `mechanism hypothesis`, `accounting definition`, `normative objective` — distinct, and renders the finer descriptive labels by reusing the locked class words. The labels are not upgraded into proven conclusions; the negation guardrails in the source (does not / cannot / has not) are preserved.

**Convention on link re-pointing.** Every in-page anchor that lives in another chapter (`#rfc-evidence-XXX`) is re-pointed to the Chinese source `../../社会系统协议学白皮书.md#…` so the build does not report a missing anchor; these resolve once the corresponding English chapter lands. Anchors that live in this file (`#chapter-3`, `#sp-rfc-004`…`#sp-rfc-007`, `#sec-3-1`…`#sec-3-8`, `#sec-3-7-1`, `#research-process-pattern`) remain same-page links.

---

<!-- SP:BEGIN chapter-03 -->
<a id="chapter-3"></a>

## Chapter 3: Proposition Group II — Intermediary Parasitism & Compatibility Decay

This chapter sets out four SP-RFCs (004–007) on intermediary net contribution, complexity and normative choice, then intellectual-history, software and risk-path cases; the cases do not automatically constitute clause verification.

<a id="sp-rfc-004"></a>
<a id="legacy-v11-1-sec-3-1"></a>
<a id="sec-3-1"></a>

<a id="legacy-v11-1-rfc-004"></a>
<a id="legacy-v11-0-rfc-003"></a>

### 3.1 SP-RFC-004 | Conditional Retention Rate of Serial Compatibility Layers

**Claim identity:** conditional model.
**Dependencies and additional conditions:** P1 background; the same traffic, serial conditional loss, and no added output or recovery path.
**Generation and evidence card:** [G004](../../社会系统协议学白皮书.md#rfc-evidence-004).

**Normative Spec (规范条文).**

> In a serial model where the same effective traffic passes through $n$ layers in sequence, with no added output and no recovery path, let $\lambda_i\in[0,1)$ be the conditional loss rate of layer $i$ relative to its input; the normalised retention rate is then:
> $$\eta_n=\prod_{i=1}^{n}(1-\lambda_i).$$
> If every layer has the constant loss $\lambda$, then $\eta_n=(1-\lambda)^n$; if there is only a uniform positive lower bound $\lambda_i\ge\lambda_{\min}>0$, then $\eta_n\le(1-\lambda_{\min})^n$. Mere per-layer positive loss is insufficient to guarantee exponential decay; actual performance also depends on productive contribution, compensation mechanisms, system margin, and task demand.

**Falsifiability Boundary and Counter-Example Cancellation (可证伪边界与反例对消判定).**

> **Low-net-cost abstraction layers and privileged rent-seeking compatibility layers must be accounted for separately:** Roman law, common-law precedent, the C standard library, and the Linux ABI may serve as comparison cases. Format adaptation, type checking, authentication, and caching may carry positive costs but higher net benefits; exclusive interpretive rights and mandatory skim may add non-productive costs. The number of layers alone does not determine net contribution; Zero-Cost Abstraction does not mean physical communication dissipates zero energy.

Moreover, one must distinguish the "privileged rent-setting that extracts non-productive rent (malign $\lambda_i$)" from the "informal coordination and tacit-knowledge daily repair (Mētis / Repair Work, productive fault-tolerance buffer) that grassroots actors provide to compensate for the incompleteness of formal protocols." If the buffering layers that actually perform exception-handling functions are cleared away without a feasible alternative mechanism, "work-to-rule" or degraded anomaly-recovery capacity may appear; this is a candidate applied-risk hypothesis, and does not presuppose that the two necessarily follow one another. Concrete applications must compare alternative mechanisms and specify observation windows and metrics such as anomaly handling and recovery performance.

> **Testing method:** pre-fix the throughput definition, boundaries, and observation window; independently measure each layer's conditional loss rate; then test the serial model's prediction error. If same-basis data persistently deviate from the pre-registered prediction interval and the deviation cannot be explained by measurement uncertainty, reject the model's applicability. When a parallel bypass, added output, or recovery path exists, a separate model must be built; one must not post-hoc rename every counter-example "good intermediary." $n\ge4$ by itself is not an attenuation or collapse threshold.

> 📊 **[Modern institutional-economics and econometric-empirical annotation · Case 3.1-A] (Olson's "institutional sclerosis", Tainter's diminishing returns to complexity, and village-level missing-expenditure evidence)**  
> *Classic monograph anchor*: the institutional economist Mancur Olson, in *The Rise and Decline of Nations* (1982), analysed the mechanism by which the accumulation of distributional coalitions and institutional sclerosis (Institutional Sclerosis) suppresses the vitality of economic growth; the historical anthropologist Joseph Tainter, in *The Collapse of Complex Societies* (1988), examined the diminishing marginal returns to investments in complexity; the connection to modern compliance burdens is this book's mechanism mapping. The two classics offer evolutionary-mechanism insight into organisations and systems facing rising maintenance costs, and must not be mechanically simplified into a universal quantitative law that all institutions inevitably proceed to absolute lock-in and collapse.  
> *Review of external empirical research*:  
> 1. **Village-level project expenditure gaps and audit effects**: Olken (2007, *Journal of Political Economy*) ran a randomised experiment on road projects in 608 Indonesian villages, measuring missing expenditure as the log difference between reported expenditure and an independent engineering cost estimate (interpreted in the paper as an approximate percentage), with a sample mean of about 24%; that absolute level is sensitive to measurement assumptions such as material wastage. Raising the probability of a government audit from about 4% to 100% reduced missing expenditure by about 8 percentage points. 608 is the total number of experimental villages; the effective samples for the specific indicators and regressions must be reported separately per Tables 3 and 4 of the original paper. The study supports that the audit mechanism can affect village-level resource leakage; it did not directly estimate the number of administrative transmission layers or each layer's loss coefficient; if a four-layer setting with 8% per layer is adopted, the resulting efficiency of about 71.6% is merely this book's hypothetical worked example. The 8% is a demonstrative value taken for each layer's conditional loss rate and is not obtained from Olken's audit-effect estimate.
> *Verification source*: [Olken (2007), Monitoring Corruption: Evidence from a Field Experiment in Indonesia](https://economics.mit.edu/sites/default/files/publications/Monitoring%20Corruption%20Evidence%20from%20a%20Field.pdf).
> 2. **Regulatory length, restrictiveness-word counts, and economic performance**: RegData uses counts of restrictive words in regulation as a proxy for regulatory scale; its version 4.0 covers 1970–2020. The Mercatus Center's 2020 release materials report that the 2019 CFR contained about 103 million words and 1.08 million restrictive words. Separately, per Dawson and Seater (2013, *Journal of Economic Growth*), model estimates based on the CFR length time series found regulatory accumulation to be associated with declines in output and total-factor-productivity growth. The two studies differ in period, indicators, and estimation objects; a restrictive-word count does not equal net social cost, nor does it directly test this book's middleware loss formula. Specific growth losses and monetary amounts must be listed separately once the final published-edition page numbers, estimating equations, and counterfactual definitions are provided.
> *Verification sources*: [QuantGov, The History of RegData](https://www.quantgov.org/history); [Mercatus Center, Quantifying Regulation in US States with State RegData 2.0](https://www.mercatus.org/research/data-visualizations/quantifying-regulation-us-states-state-regdata-20); [Dawson & Seater (2013), Federal regulation and aggregate economic growth](https://link.springer.com/article/10.1007/s10887-013-9088-y).

<a id="sp-rfc-005"></a>
<a id="legacy-v11-1-sec-3-2"></a>
<a id="sec-3-2"></a>

<a id="legacy-v11-1-rfc-005"></a>
<a id="legacy-v11-0-rfc-004"></a>
<a id="legacy-v11-0-rfc-014"></a>

### 3.2 SP-RFC-005 | Normative Complexity and Intermediary Rent-Seeking Feedback

**Claim identity:** conditional mechanism hypothesis.
**Dependencies and additional conditions:** P2/O4; exclusive rights, a dominant non-productive net payoff, and insufficient constraint.
**Generation and evidence card:** [G005](../../社会系统协议学白皮书.md#rfc-evidence-005).

**Normative Spec (规范条文).**

> **Epistemic identity: conditional mechanism hypothesis.** Within a pre-defined protocol operating period, if an intermediary holds exclusive access or interpretive rights, the payoff from non-productive rent net of penalty exceeds the payoff from productive services, and effective competition, exit, and independent error-correction are insufficient, then normative complexity and intermediary dependence may reinforce each other. One must separately verify the task necessity of each added clause, the compatibility and rights-protection benefit, the intermediary's actual authority and payoff, and then compare feasible alternative mechanisms.
> "Normative bloat" means the net burden added relative to a given task and necessary protection; it is not defined directly by length, terminology, or layer count; "parasitism" requires evidence of non-productive rent and is not determined by professional identity. Complexity accumulation, rent extraction, and task failure are different outcomes and must be measured separately; one must not infer from a bad outcome that the above conditions necessarily existed.
> **Institutionalised scenario (the qualified scenario for merged clauses):** the same mechanism may be tested within norms that have already attained formal status, but its authority, payoff, and constraint conditions must be re-confirmed. Institutionalisation, state adoption, or past opposition to the old order are not sufficient conditions for the mechanism to hold. Where materials show effective service, open interpretation, independent review, or internal repair, the judgment should be narrowed; no separate "entropy-inevitable-on-entry" law is introduced. General institutional-rigidity problems that do not meet this item's conditions are not automatically absorbed.
> **Comparison and rejection conditions:** pre-define the task, applicable period, authority/payoff conditions, alternative mechanisms, net burden, and independent outcomes; register the prediction range and error requirements; one must not explain everything with "may." When conditions are independently verified, estimation precision is sufficient, and comparison excludes the predetermined feedback/burden effect, reject the applied hypothesis; where materials or precision are insufficient, record as undetermined.

> 💻 **[Software–intellectual-history isomorphism annotation · Case 3.2-A] (The systemic recurrence from liberator to dragon)**  
> *The different paths of UNIX/GNU/Linux*: the FSF's [own historical record](https://www.fsf.org/history/) distinguishes the 1983 GNU announcement from the formal launch in 1984; the Linux 0.01 release notes record a source-code experiment with explicit limitations. On this basis this book compares licensing goals, experimental settings, and interface openness; it does not invert later legal disputes into the cause of these projects' early launches, nor take chronological priority as establishing the sole motive of the global developer migration.
> *Intellectual-history comparison leads (materials pending)*: doctrinal interpretation, church finance, university-theology censorship, and state authorisation should be studied separately by period and institution; this book does not fuse them into one millennium-invariant "middleman." Where interpretive rights are exclusive, payoffs are decoupled from verifiable services, and error-correction is obstructed, a closed-intermediary risk hypothesis may be posed; where materials show open debate, effective service, or internal reform, that interpretation must contract. This paragraph only locates the questions to be verified and is not registered as a completed historical-case test.
> **Systems reminder**: norms that once drove openness may themselves need revision; whether they close, whether they fail, and whether internal recovery is possible must be evidenced item by item. One cannot infer directly from "entry into the core" that purge or refactoring is necessary.

<a id="sp-rfc-006"></a>
<a id="legacy-v11-1-sec-3-4"></a>
<a id="sec-3-3"></a>

<a id="legacy-v11-1-rfc-007"></a>
<a id="legacy-v11-0-rfc-016"></a>

### 3.3 SP-RFC-006 | Approval Latency, Mission Deadline, and Protection Benefit

**Claim identity:** conditional judgment and application comparison.
**Dependencies and additional conditions:** given path, deadline, and protection goal; whether rent-seeking requires separate evidence.
**Generation and evidence card:** [G006](../../社会系统协议学白皮书.md#rfc-evidence-006).

**Normative Spec (规范条文).**

Facing frontier exploration or marginal technology, prudent review and compliance processes, even if entirely motivated by public-safety concern rather than rent-seeking, may still consume irreversible physical time; accelerating review or cancelling approval does not necessarily raise the system's overall net benefit. Therefore, this item preserves the independent analysis boundary of approval latency, deadline, and protection benefit, and does not directly fold it into the rent-seeking feedback model.
In concrete analysis, one must separately measure the compliance cost of lawful tasks, processing latency ($T_{\text{latency}}$), and the actual physical block rate of violations; when approval latency exceeds the task lifetime (TTL) and causes timeout, one must strictly distinguish four different consequences:
1. **Original planned path not completed on time** (Primary Path Delay);
2. **Low-cost alternative path available and bypass migration occurs** (Bypass Migration);
3. **Local exploration task fails** (Task-Level Failure);
4. **System-level organisational-governance failure** (Systemic Failure).
One must not equate an individual task delay or local bypass of an electronic fence directly with total organisational collapse or overall failure of the regulatory tool. Whether it constitutes empirical grounds for institutional restructuring or incremental-bypass design should compare, over the same task and observation period, the protection effect, compliance cost, processing latency, rights impact, and migration risk of the original rule and feasible alternatives. Even if the original rule has a protection benefit, if the alternative meets the pre-stated protection requirement, satisfies the rights constraint, and has a lower total cost, it can constitute grounds for improvement; "the original rule has no protection benefit" is not set as a necessary condition. When the protection effect is uncertain or incomparable, one should preserve the uncertainty and continue verification; one must not cancel necessary safeguards solely on the basis of latency.

*Citation convention for cases: Cases 3.3-A and 3.3-B in this section are located by this version's version number and case title; the same number does not guarantee the same materials across different-purpose drafts. Citations should state the version, title, and source together.*

> 📜 **[Technical-regulation history annotation · Case 3.3-A] (The UK Motor Car Act 1865 ("Red Flag Act") and regulatory impedance)**  
> *Historical citation*: [Sections 3 and 4 of the Motor Car Act 1865 as originally published](https://www.legislation.gov.uk/ukpga/Vict/28-29/83/pdfs/ukpga_18650083_en.pdf) stipulated that a non-horse-drawn motor vehicle on applicable roads carry at least three persons, one of whom walks at least 60 yards (about 55 metres) ahead of the vehicle carrying a red flag; the speed limit on ordinary highways was 4 mph, and 2 mph within cities, towns, or villages. What is reported here is the 1865 text; the subsequent evolution is not simplified into all vehicles having always been subject to the same rule.  
> *Systems analysis*: the crew, walking-flagman, and speed-limit requirements set locatable constraints on the road operation of the vehicles concerned; whether these requirements increased testing costs or slowed technological iteration, and by how much, is a to-be-tested mechanism question posed by this book — "significant impedance" or industrial consequences cannot be inferred from the statutory text alone. [Sections 1 and 4 and the Schedule of the 1896 Act](https://www.legislation.gov.uk/ukpga/Vict/59-60/36/pdfs/ukpga_18960036_en.pdf) exempted light locomotives as defined from the listed existing provisions and set a separate speed cap; this supports that the rules were adjusted, and does not prove the net benefit of the relaxation or the historical net harm of the earlier restrictions. Comparison must still include safety protection, implementation status, and feasible alternatives.

> 💻 **[Modern open-source penetration annotation · Case 3.3-B] (AI flight control and decentralised asymmetric penetration in the age of autonomous agents)**  
> *Technical boundary*: approval time and electronic-fence effectiveness must be verified separately by device, task, and applicable rules; one must not presuppose that all tasks require days of manual approval; classification rules, application-free paths, or long-term permits must also be included. Open-source flight-control and navigation solutions can change some technical dependencies, but regulatory failure overall cannot be asserted on that basis.
> 1. **AI-assisted code prototyping**: large language models can be used to generate or modify code prototypes for attitude control and waypoint cruising, but this book provides no reproducible evaluation of man-hours, accuracy, or stability, and one cannot claim from this that thresholds fall to zero or that a high-performance flight controller can be obtained in hours. Generated code and verified controllers must be distinguished; performance should be evaluated under specific device, task, and baseline conditions via simulation, hardware-in-the-loop, and applicable live-aircraft tests;
> 2. **Open-source flight control and hardware integration**: ArduPilot, PX4, and commercially available components and 3D-printing processes can serve as research instances of an open toolchain; control-board adaptation, sensors, actuators, power, and structural integration still carry costs. This book provides no complete bill of materials, adaptation records, or build man-hours; a single chip's quoted price and print time cannot be taken as evidence of whole-system cost or deployable performance;
> 3. **Bypass boundary**: techniques such as visual-inertial odometry (VIO) or optical flow can serve as examples for studying specific navigation dependencies; this book provides no data sufficient to prove that all radio countermeasures and electronic fences fail universally. Actual success rates should be measured by device, task, and threat model.
> *Systems irony*: administrative regulation that only adds form-filling burdens for the law-abiding while producing no corresponding safety benefit is of course worth questioning. But irony cannot substitute for the denominator: bypassing one protection does not mean the whole defence is zero, and approval friction does not mean every lawful enterprise is strangled.
> *Systems conclusion*: **if the approval latency for a designated task exceeds the mission deadline ($Latency_{\text{Audit}}>TTL_{\text{mission}}$), that path may fail to complete the task on time; application-free, long-term-permit, and alternative paths should be verified at the same time. Overall throughput, risk reduction, and malicious-bypass rates must be measured separately. Formal review cannot substitute for real security outcomes.**

> **Coupling boundary with `SP-RFC-005`:** high approval latency does not necessarily originate from rent-seeking (it may originate from risk aversion or insufficient assessment capacity). When the latency mismatch described in this item coexists with independent evidence that simultaneously satisfies SP-RFC-005's conditions of exclusive rights, dominant non-productive net payoff, and insufficient constraint, the two may be analysed jointly, reporting the latency consequence and the rent-setting evidence separately. A suspected improper payment to buy accelerated handling (Speed Money) or exclusive exemption can serve as a forensic clue for a specific mechanism; one must not judge rent-seeking solely on latency or fees. If one further claims that an intermediary "deliberately maintains" latency, intent must be evidenced separately and cannot be set as a necessary threshold for all rent-seeking judgments.

<a id="sp-rfc-007"></a>
<a id="legacy-v11-1-sec-3-5"></a>
<a id="sec-3-4"></a>

<a id="legacy-v11-1-rfc-008"></a>
<a id="legacy-v11-0-rfc-005"></a>

### 3.4 SP-RFC-007 | Architect's Understandability, Rights, and Migration Precepts

**Claim identity:** cross-group normative rule.
**Dependencies and additional conditions:** explicit design goals, rights, costs, and alternatives; not an objective law.
**Generation and evidence card:** [G007](../../社会系统协议学白皮书.md#rfc-evidence-007).

**Normative Spec (规范条文).**

When the design goal is to reduce unnecessary coordination cost, protect legitimate rights, and preserve error-correction capacity, the architect may adopt the following three normative engineering precepts. They are not universal commands automatically derived from physical constraints or equilibrium descriptions, nor do they guarantee that any system never collapses; the specific trade-off must disclose the affected parties, benefits and costs, alternatives, and remedy arrangements, and comply with SP-RFC-017's incremental-migration boundary.

1. **First precept: The Plain Language Mandate**  
   *If it is not necessary, do not add an API.*  
   Any legal clause, administrative regulation, or moral initiative should provide an explanation understandable to its target audience, and be tested by comprehension-accuracy, rights protection, and implementation effect. Professional complexity, syntactic layer count, or the use of intermediaries does not by itself constitute grounds for abolition; necessary exceptions and procedural safeguards should be retained.
2. **Second precept: The Proxy Bypass Mandate**  
   *Examine monopolistic interpretive rights and non-productive fees.*  
   Account separately for each intermediary's coordination, verification, and rights-protection payoff against its resource, exclusion, and rent-seeking costs; for those with net harm and feasible alternatives, open competition, bypass, or lawful restructuring. Where safety, protection of the vulnerable, and third-party externalities are involved, verify the alternative mechanism and retain independent remedy first; do not clear them across the board merely because they have a professional threshold.
3. **Third precept: The Radical Refactoring Mandate**  
   *When persistent smells appear, first verify the failure mechanism, then compare in-place repair against bypass refactoring.*  
   When code smells persist, first verify task failure, recovery capacity, rights impact, and migration net benefit. If in-place repair of the original architecture is ineffective or too costly, an alternative protocol may be incubated in an independent user-space sandbox (Ring-3); production traffic is incrementally diverted under SP-RFC-017 with rollback retained. The smell itself does not prove that continuing to patch necessarily accelerates deadlock.

> 💡 **【Architect's meta-annotation · conceptual-boundary statement】(engineering-concept borrowing, comprehension cost, and falsifiability testing)**  
> Addressing readers' prudent question of whether the whitepaper's own use of "non-idempotent deadlock," "Ring-3 memory isolation," and "BGP Hijacking" also fabricates jargon, this theory establishes a reciprocal testing principle:  
> 1. **Essential distinction between two kinds of textual feature:**  
>    - **Rent-Seeking Padding:** vague rhetoric piled up to evade responsibility or monopolise interpretive rights, which independent task testing proves increases comprehension or execution cost; this is a to-be-operationalised semantic classification and is not identical to the white-noise power of a Shannon physical channel. Whether something constitutes rent-seeking requires separate evidence of rights, payoff, and alternative mechanisms.  
>    - **Architectural Mapping Tokens:** borrow mature symbols from computer science that possess strict state-transition, boundary-condition, and exception-handling mechanisms, attempting to characterise specific dynamic mechanisms in social coordination.  
> 2. **Reciprocal testing and self-restraint:** all engineering terms introduced by this book enjoy no epistemological exemption whatsoever and must all undergo the same **comprehension-cost, definition-stability, and prediction-gain tests**. If readers and subsequent research prove that a given engineering analogy fails to provide incremental explanatory power beyond existing social-science concepts, or that its structure-preserving mapping breaks at real boundaries, that term should be judged invalid, redundant, and removed. All questions about conceptual clarity and validity are adjudicated rationally on the basis of their argument and empirical facts.

**Adversarial compliance and repair-space stress test:** the table below provides a verification interface for scenarios where the specification might be strategically circumvented; it is a to-be-executed adversarial design, not an empirical assertion that these behaviours have occurred. In implementation, first choose the threat model, sampling denominator, observation period, and affordable audit cost, balancing privacy and appeal; lower-cost independent verification methods may be compared, and not every organisation is required to mechanically add ten ledgers.

| RFC | Surface tick | Possible circumvention | Observable counter-evidence and independent verification |
| --- | --- | --- | --- |
| 005 | Announce cancellation of approval and fees, open interface | Actual verification and control transferred to affiliated consulting or certification vendors | Check actual refusal authority, affiliated ownership, contracts and end-to-end fees; compare net cost and success rate before and after reform for the same task |
| 006 | High on-time closure rate after acceptance | Non-acceptance, clock reset via supplementary filings, induced withdrawal, excluding failure denominator | Time from first attempt; include unregistered, withdrawn, overdue and appealed cases; also check risk-reduction effect — not only speed |
| 007 | Shorter text, lower PBR | Rights and exceptions hidden in appendices, everyday vocabulary keeps shifting blame | Blind-test the audience on subject, action, deadline and remedy; check proposition completeness, comprehension-accuracy and actual errors |
| 011 | Complete authority matrix and review seals | Shared administrator, normalised emergency escalation, or reviewer capture | Cross-check actual authority graph, escalation logs and external retention; when logs are produced by the supervised party, verify independently managed retention, event coverage and integrity records, and cross-check with authority-change and remedy materials; a checksum does not prove no omission or content truth; spot-check whether revocation and remedy decisions can actually be executed |
| 014 | Authorisation documents and seals present | Scope expansion, deadline drift, oral sub-delegation | Trace each execution back to subject, purpose, authority and deadline, and verify the authorisation document, sub-delegation and process version in force at execution; version change and revocation must be traceable, retaining legally protected information and audit-access boundaries; verify refusals and affected-party appeals |
| 015 | Signed voluntary consent, exit button provided | Data hard to migrate, basic services bundled, retaliation after exit | Include attempted-exit and non-joined parties; measure alternative availability, full migration cost and subsequent adverse consequences; do not take non-exit as proof of voluntariness |
| 016 | Receipts complete, high closed-loop rate | Execution and acceptance collude, ledgers or photos substituting for delivery | Randomly spot-check the true state of delivery across all closed tasks as the denominator; report reopened, lost-contact and unverifiable proportions |
| 017 | Accounting shows migration saves cost | Cost shifted to other parties, old repairs and recovery assets omitted | Fix the accounting boundary and cost-subject matrix; retain pre-migration repair records; re-check recovery time, risk and sensitivity |
| 018 | Many branches, fast PDCA, high success rate | Cloning homologous branches, hiding failures, short-term elimination or maintainer favouritism | Register all branches and budgets, identify common failures; retain mature-outcome, elimination and review records, disclose conflicts of interest |
| 019 | Claims manual review, calibrated and isolated authority | Tuning weights or deleting corpus to flatter conclusions, colour turned directly into penalty by a seal | Fix version, out-of-time samples and negative control; report omissions and false-positive/negative rates; check execution basis independent of radar output item by item |

Independent verification must also state the auditor's resources, appointment, and interest relations; merely writing "third party" into the name is insufficient. Frontline personnel may report mismatches and temporary repairs; their authority, reason, effect, period, and exit conditions should be recorded, and channels for review and protection from retaliation retained; the tacit knowledge required for error correction and non-productive privileges should be verified separately, and not every exception or circumvention pre-judged as malicious.

<a id="legacy-v11-1-sec-3-6"></a>
<a id="sec-3-5"></a>

### 3.5 Intermediary-Reconfiguration Cases in Intellectual History

**Authority-interface reconfiguration and access-threshold comparison matrix in intellectual history.**

*Comparison index: each row is not a completed record of monopoly overturn or reduced participation cost; the advocate's claims, organisational conditions, and actual influence are verified separately.*

| Historical node | Compared authority and practice interface | Advocate and interpretive framework | Change and coordination boundary to be compared |
| --- | --- | --- | --- |
| Ancient Greece | City-state rhetorical education and fee-charging private schools; does not presuppose the Sophists constituted an existing monopoly | Socrates<br>(dialectical questioning) | The maieutic question-and-answer conceptual test; one cannot thereby infer that fee-based teaching was overturned wholesale |
| Tang-dynasty East | Scriptures, commentaries, and exegetical learning; does not presuppose a single "salvation gateway" | Huineng of Chan (Sixth Patriarch)<br>Master Shandao (Pure Land) | Compare how sudden enlightenment and nianfo narration reconfigure learning requirements; lineage, precepts, and community still require investigation |
| 16th-century Europe | Papal sacramental and linguistic authority with reform controversy | Martin Luther<br>(Protestant Reformation) | Compare the shared-priesthood identity and the role of the vernacular Bible; does not mean abolishing teaching, pastoral office, or new creeds; denominational fork (Hard Fork) is analysed separately as an institutional question |
| Ming-dynasty East | Cheng-Zhu exegesis, state academy, and examination rules must be distinguished by period | Wang Yangming<br>(Yangming School) | Compare how "to extend one's innate knowledge" (zhi liangzhi) analogises the devolution of moral-judgment responsibility; public knowledge and institutional coordination still require external norms; the actual threshold change is verified separately |

<a id="legacy-v11-1-sec-3-6-1"></a>
<a id="sec-3-5-1"></a>

#### 3.5.1 Huineng of Chan and Pure Land: the "Zero-Intermediary and Single-Line Code" Interface Analogy

**Normative Spec (规范条文).**

This section uses practice interfaces such as "direct pointing at the mind" and "easy nianfo practice" to pose the research question of whether they reduce some translation burden compared with cumbersome commentary. Bypass is an analogy for authority-interface reconfiguration; the threshold and organisational effect must be compared by specific tradition; it does not assume that there are no lineage, community, or doctrinal conditions in reality.

> 📜 **[Intellectual-history annotation · Case 3.5.1-A] (Huineng of Chan's Bypass around complex doctrine)**  
> *Classical citation*: the *Platform Sutra of the Sixth Patriarch* (《六祖坛经》; the Dunhuang manuscript and the later Zongbao recension differ in wording; the Zongbao recension is the later, widely circulated version, recording his verse as “菩提本无树，明镜亦非台，本来无一物，何处惹尘埃” [Bodhi originally has no tree, the bright mirror is also no stand; originally there is not a single thing — where could dust alight?], while the early Dunhuang version records it as “佛性常清净，何处有尘埃” [Buddha-nature is ever pure — where could dust be?], among others). Huineng's sudden-enlightenment narrative emphasises pointing directly at one's own nature, and later Chan further distilled it into the path formula “教外别传、不立文字、直指人心、见性成佛” [a special transmission outside the teachings, not established on words, pointing directly at the mind, seeing one's nature and becoming Buddha].  
> *Version verification*: [CBETA Dunhuang text T2007, T48, p. 338a, lines 7—8](https://raw.githubusercontent.com/cbeta-org/xml-p5/master/T/T48/T48n2007.xml); [the Zongbao circulated recension T2008, T48, p. 349a, lines 7—8](https://raw.githubusercontent.com/cbeta-org/xml-p5/master/T/T48/T48n2008.xml). The sudden-enlightenment narrative and the lineage organisation must be explained separately; this paragraph does not establish a historical first.
> *Systems analysis*: this book uses Bypass as an analogy for the practice-interface reconfiguration in the sudden-enlightenment narrative; the texts allow posing the question of whether some of the commentary burden is reduced, but provide no measured values for participation thresholds or population-level effects. Lineage, precepts, and community must still be investigated separately; a real-world "zero intermediary" cannot be derived from the verse. Reducing one class of translation requirement also does not preclude the formation of new canons, lineages, or certification intermediaries; "bypass — regeneration of new intermediaries" should be tested as a competing mechanism against separate institutional materials, without presupposing that the total amount of intermediation declines.

> 📜 **[Intellectual-history annotation · Case 3.5.1-B] (Pure Land: name-holding nianfo that lowers the invocation threshold)**  
> *Classical citation*: Shandao's Commentary on the Contemplation Sutra (《观无量寿佛经疏》), scroll 4, discusses primary practice, supporting practices, and mixed practice, and calls exclusive invocation of Amitabha's name the “正定之业” [the practice of right samadhi], placing it in the doctrinal context of deep faith and the vow to transfer merit. See [CBETA T1753, T37, p. 272, column a, lines 28 to column b, line 13](https://raw.githubusercontent.com/cbeta-org/xml-p5/master/T/T37/T37n1753.xml). This case does not use this to assert a historical first for the easy path, nor interpret name-invocation as a single execution instruction detached from doctrinal conditions.
> *Systems analysis*: the learning requirements of name-invocation, contemplation, and other practices may be compared, posing a participation-cost hypothesis via the "lightweight invocation interface"; whether different strata participate more easily, and with what effect, still requires audience and institutional materials to test — doctrinal claims cannot substitute for social measurement.

<a id="legacy-v11-1-sec-3-6-2"></a>
<a id="sec-3-5-2"></a>

#### 3.5.2 Martin Luther and Wang Yangming: the Edge-Computing Analogy of Authority-Interface Reconfiguration

**Normative Spec (规范条文).**

When an authority interface is closed or translation cost is too high, one may compare an edge-computing path that devolves part of the judgment responsibility to the acting agent. "Justification by faith" and "to extend innate knowledge" are used in this book to pose mechanism analogies; they do not mean that all public facts can be self-verified by a local CPU with zero hops; empirical knowledge still requires external evidence, and the roles of teaching, pastoral office, lineage, and community must be investigated separately.

> 📜 **[Intellectual-history annotation · Case 3.5.2-A] (The critical analogy of "shredding the Pope's API" and the German Bible)**  
> *Text and editions*: [an English translation of the Ninety-five Theses](https://www.luther.de/en/95thesen.html), theses 21, 27, and 36 among others, discusses the relations among the indulgence promise, money, and repentance, and does not support summarising the Luther of 1517 as advocating the abolition of all church intermediaries. [the description of the Gruber Collection's 1522 New Testament](https://gruber.lstc.edu/luthers_bible/1522.php) and [the record of the 1534 complete German Bible](https://gruber.lstc.edu/luthers_bible/1534.php) support the corresponding publication milestones; this case does not rely on the "posting on the church door" detail, and universal literacy or a German standard set by one person cannot be inferred from the publication of the translation.
> *Systems analysis*: Luther advanced the "Priesthood of all believers", and this book uses it to analogise the reconfiguration of some authoritative intermediaries; the shared priesthood does not mean abolishing public preaching and the pastoral office. The relation between the diffusion of the German translation and literacy, education, and language integration must be tested against institutions, regions, and periods; universal literacy or an industrial leap cannot be derived directly from the publication of the translation.

> 📜 **[Intellectual-history annotation · Case 3.5.2-B] (Yangming's philosophy of mind: the analogy from cloud fetch to local CPU cache hit)**  
> *Locatable texts (paraphrase)*: [the *Chuanxilu* (《传习录》, Instructions for Practical Living), scroll 1, item 34](https://zh.wikisource.org/wiki/傳習錄/卷上#34) discusses mind and principle, good and evil; [scroll 2, "In Reply to Gu Dongqiao", item 139](https://zh.wikisource.org/wiki/傳習錄/卷中#139) discusses innate knowledge (liangzhi) and its practical cultivation. This case uses these discussions for a comparison of moral-judgment interfaces and does not stitch the bamboo-gazing and Longchang stories together into an unverified instantaneous "moment of discovery". What is cited is a transcription of transmitted sayings, not a measured record of behavioural effects at the time.
> *Systems analysis*: Wang Yangming advanced “**心即理**” [mind is principle] and “**致良知**” [the extension of innate knowledge], emphasising the establishment of moral judgment and practical subjectivity. This book likens it to "devolving the responsibility for moral judgment to the acting agent (edge computing)". But innate knowledge refers to the self-aware judgment capacity of the moral mind (“知善知恶是良知” [knowing good and knowing evil is innate knowledge]), not natural-science knowledge or all empirical facts pre-installed at the factory; cross-agent public knowledge and social cooperation still require objective evidence, argument, and testing.

> 📊 **[Econometric-history and political-science empirical annotation · Case 3.5.2-C] (Anderson's "print capitalism and language integration" and the Prussian 452-county literacy regression)**  
> *Classic monograph anchor*: Anderson's *Imagined Communities* (first edition 1983; this paragraph summarises the thesis and is not a verbatim quotation of a designated edition) discusses the relations among print capitalism, language, and the formation of national communities. "Language integration" is this book's comparative term; "the underlying bus" is likewise this book's engineering analogy for the conditions of symbolic diffusion — it is not attributable to Anderson's own sentences, nor does it license inference to a uniform or inevitable historical path. The specific edition and page numbers of the original must still be supplied when the citation is expanded.  
> *Quantitative study and identification boundary*: Becker and Woessmann (2009, *Quarterly Journal of Economics*) used data on 452 Prussian counties, with distance to Wittenberg as the instrument for the share of Protestant population. In their specification, the literacy-rate gap between wholly Protestant and wholly Catholic counties is estimated at about 9.9 percentage points by the controlled OLS and about 18.9 percentage points by the baseline IV. The original locations are Table II, column 2 (p. 550) and Table III, column 2 (p. 559), respectively. Causal interpretation depends on the exogeneity of the geographic instrument and the exclusion restriction. Economic outcomes are consistent with literacy explaining most, or even all, of the Protestant economic advantage; this is not an identified "100% causal mediation share" and cannot be directly extrapolated to a universal effect of all de-intermediation reforms. This book has not independently reproduced these estimates, nor registered the instrument's exclusion restriction as verified by this book.
> *Verification source*: [Becker & Woessmann (2009), Was Weber Wrong?](https://storre.stir.ac.uk/bitstream/1893/1653/1/BeckerWoessmann2009QJE.pdf).
> *Juxtaposition boundary*: Anderson's historical explanation and the Prussian county-level study differ in object, period, and outcome variables; they are juxtaposed to pose comparative questions and do not validate each other, nor does the literacy estimate validate this book's de-intermediation analogy.

<a id="legacy-v11-1-sec-3-7"></a>
<a id="sec-3-6"></a>

### 3.6 Intermediary Comparison in Software and Organisations

| Architectural dimension | Enterprise deployment example stacking multiple WS-* and component containers | HTTP service example using REST style and JSON payload |
| :--- | :--- | :--- |
| **Payload**<br>(Payload) | SOAP XML Envelope, with WS-* extensions added as needed<br>(analogy: formal expression may aid verification, but may also increase comprehension burden) | JSON payload; volume and processing cost depend on data and implementation<br>(analogy: plain or direct expression may ease access, but may also omit necessary conditions) |
| **Contract**<br>(Contract) | WSDL/XML Schema may describe the message contract<br>(analogy: written rules cut both ways — eliminating ambiguity while adding complexity) | Uniform interface and HTTP methods (GET/POST/PUT), still requiring contract and version management<br>(analogy: lightweight norms still require public boundaries and remedy conventions) |
| **Middleware**<br>(Middleware) | WebLogic/WebSphere and similar containers may be used; not required by SOAP<br>(analogy: centralised authentication may provide reputation and coordination, but may also form exclusive access) | The adapted HTTP service and client; authentication and operations still require implementation<br>(analogy: grass-roots autonomy still has intermediary and maintenance costs, not equivalent to the disappearance of authority) |
| **Barrier**<br>(Barrier) | Depends on needs, toolchain, documentation, and existing team skills<br>(analogy: professional training may provide capability assurance, but may also form unnecessary barriers) | A simple interface may lower entry cost; complex business still requires professional capability<br>(analogy: the vision of broad participation does not mean professional capability is already widely attained) |

This table contrasts two illustrative deployments; it is not a standard of superiority or an era-substitution law: protocol standards, architectural styles, data formats, and commercial deployments must be compared axis by axis; the parenthetical social correspondences are cognitive analogies only. The "software-engineering isomorphism" banner is a research label for a to-be-tested structural correspondence; this table has not yet completed the object-by-object, mapping-preserved/lost, and effect-testing requirements of §1.3, and one cannot register isomorphism as established merely on the strength of an analogy cell.

<a id="legacy-v11-1-sec-3-7-1"></a>
<a id="sec-3-6-1"></a>

#### 3.6.1 Enterprise Java Stack: the Complexity Boundary of SOAP/WS-* Deployment

**Normative Spec (规范条文).**

SOAP is a public message-framework specification, REST is an architectural style, JSON is a data-representation format, and EJB is a component technology; these names do not directly correspond to closed monopoly or open competition. When comparing deployments, one should account separately for contract and message complexity, middleware dependency, licensing and exit conditions, and the full-lifecycle cost under equivalent security, reliability, and business requirements. Where competition and exit channels are lacking, extensions and proprietary bindings beyond demand may increase maintenance impedance; adopting a uniform interface and reducing unnecessary dependency may lower cost, but the REST/JSON label itself does not guarantee openness, ease of use, or cost advantage. If the security, transaction, or interoperability benefit provided by an added mechanism is sufficient to offset its cost, the judgment "normative inflation is parasitism" does not hold.

> 💻 **[Software-engineering isomorphism annotation · Case 3.6.1-A] (Enterprise normative inflation and the lightweight-architecture reflection)**  
> The base framework of SOAP 1.2 and the WS-* extensions that can be stacked in enterprise deployments should be discussed separately. Extensions such as security, addressing, and reliable messaging each have their own uses; stacking can become the "WS-* bloat spiral" only when the project's actual demand is insufficient to offset the configuration, interoperability, and maintenance costs. WebLogic/WebSphere are researchable commercial deployment instances, not a required runtime environment for SOAP, and monopoly or cost runaways cannot be judged from product names alone.
> Roy Fielding's 2000 doctoral dissertation articulated the **REST architectural style**, including constraints such as the uniform interface and statelessness; JSON is one data format available for interfaces, and REST does not require JSON. **Stripping away the redundant ritual is what counts as load reduction; calling every security and reliability mechanism fat merely moves the bill onto the exception path.** This book's engineering comparison should, under equivalent requirements, test configuration effort, change cost, failure recovery, and exit cost; an evolution advantage cannot be inferred directly from a format name.
> *Technical sources*: [W3C SOAP 1.2 messaging framework](https://www.w3.org/TR/soap12-part1/), [Fielding's doctoral dissertation, Chapter 5](https://ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm), [RFC 8259: the JSON data interchange format](https://www.rfc-editor.org/rfc/rfc8259.html).

<a id="legacy-v11-1-sec-3-7-2"></a>
<a id="sec-3-6-2"></a>

#### 3.6.2 Scholastic Monopoly and the Pseudo-Indigenous-Research Trap: the Isomorphism of Paris Theology and Lysenkoism

**Normative Spec (规范条文).**

When a theoretical system originally aimed at "pursuing truth and liberating cognition" is monopolised by an exclusive privileged stratum during institutionalisation, and lacks external competition, exit channels, and empirical error-correction mechanisms, the system may breed an exclusive "ideological-censorship and rent-seeking structure." Through monopolising interpretive rights, accumulating compliance text beyond necessary protection boundaries, or "dogma-shelling" existing knowledge with no incremental contribution, it increases society's cognitive and coordination loss ($\lambda$).

> 📜 **[Historical evidence annotation · Case 3.6.2-A] (The scholasticisation tendency and ideological censorship of the medieval Paris theology institutions)**  
> *Institutional boundary*: ideological censorship involves different actors — university theology institutions, bishops, the papal curia, and secular powers. The Faculty of Theology of the University of Paris, the Sorbonne College, and the designations and organisational boundaries of different periods must be verified separately; they cannot be merged into a single trans-period exclusive institution, nor can theological disputation, judicial jurisdiction, and church financing substitute for one another.
> *Systems analysis*: the Paris theology institutions played a powerful access-filtering and reputation-endorsement role in the European knowledge system, but this cannot be generalised into the sole thought-certification CA of all Europe, nor equated directly with the Roman Curia's church finance and indulgence sales system. It is used here as an analogy for "the impedance effect of high-threshold compliance intermediaries on empirical scientific exploration".

> 📜 **[History-of-science annotation · Case 3.6.2-B] (The pseudo-indigenous-research disaster of Cold-War-era Lysenkoism)**  
> Lysenkoism can be used to discuss the risk of political power suppressing open testing and research error-correction; the experiences of Vavilov and others must be checked against specific archives and studies. Political labels cannot substitute for genetics experiments — that is this case's critical focus; it does not thereby claim that all geneticists were purged, nor attribute the Soviet Union's decades of agricultural performance to a single school alone.

> 💻 **[Theoretical-innovation comparison annotation · Case 3.6.2-C] (Hayek's dispersed-knowledge and price-signal argument (1945) vs scholastic dogma-shelling)**  
> *Hayek's argument and this book's analogy*: Hayek, in ["The Use of Knowledge in Society" (1945), pp. 525—527](https://german.yale.edu/sites/default/files/hayek_-_the_use_of_knowledge_in_society.pdf), discusses dispersed, local, and incomplete knowledge and coordination through price signals. His comparison involves two requirements — centralising all relevant knowledge versus letting individuals adjust their actions using price changes; this book uses it as the engineering analogy of "no participant needs to know all the background details", and does not treat it as a measured total quantity of information or social-cost advantage. The original gives no minimum channel-loss theorem or computational-deadlock proof, nor claims that price adjustment always reaches perfect equilibrium.
> *Identification criteria for "reskinned indigenous research"*: if an alleged innovation merely swaps terminology without adding distinguishable models, evidence, predictions, or tool value, it should accept the "reskin" challenge. `git diff` can inspire a side-by-side comparison, but it cannot substitute for intellectual-history comparison; this criterion also binds this book — a school's never having contributed cannot be pre-judged from its "scholastic" identity alone.

<a id="legacy-v11-1-sec-3-8"></a>
<a id="sec-3-7"></a>

### 3.7 Risk Clues and Mechanism Review

```
                  One risk path of protocol evolution (excerpt of the §3.8 risk branch; recovery branch see that section)
                  
        ┌────────────── [1. New protocol, open direct connection] ──────────────┐
        │  (New communication tools lower some access thresholds, yet resource and rule constraints remain) │
        ▼                                                │
[2. Access-rule change: state licensing and platform fees must be distinguished, and may interweave]
   (Licensing purpose, authority, and remedy see 014; platform service, exclusive control, and net payoff see 005)
        │                                                │
        ▼                                                │
[3. If exclusive fees and error-correction failure increase coordination burden]              │
   (SMS fees, platform skim, etc. must account for service payoff; not directly equal to deadlock)     │
        │                                                │
        └─────────────> [4. New-generation lightweight-tool breakout] ────────┘
           (Telecom / WeChat IM: infrastructure and application layered; broadcast / self-media: channels coexist)
           (SWIFT messaging service and encrypted-asset payment: layered comparison clue, substitution not proven)
```

<a id="legacy-v11-1-sec-3-8-1"></a>
<a id="sec-3-7-1"></a>

#### 3.7.1 Real-world diagnosis: two "code smell" criteria for institutions and ideologies nearing deadlock

**Normative Spec (规范条文).**

A system architect may take the joint appearance of the following two features as a risk clue that warrants review; they are not sufficient or necessary conditions for a system entering a late lifecycle stage or irreversible deadlock:
1. **Regulatory/institutional level: "increasingly speaks less like a human" (less plain language):** the target audience's comprehension and execution cost rises significantly, and this change cannot be explained by task complexity;
2. **Ideological/movement level: "high-frequency exclusion labels replace evidence exchange":** observable fact-checking and error-correction mechanisms are continuously replaced by identity or stance exclusion labels.
When both are present, they should be tested against resource margin, task-completion rate, recovery mechanisms, and external shocks. Whether deadlock has occurred, whether recovery is possible, and whether restructuring is needed must be judged separately; one must not infer inevitable collapse directly from textual symptoms.

> 📰 **[Administrative-pathology annotation · Case 3.7-A] (Modern bureaucratese and administrative deadlock)**  
> *Candidate observation, not yet a frequency estimate*: some official documents show expressions such as “切实压实责任、健全闭环协同、守牢底线” [earnestly consolidate responsibility, improve closed-loop coordination, and firmly hold the bottom line]. This case defines no independent indicator of organisational lifecycle and provides no period, sampling frame, or occurrence frequency, so it is not yet called a general feature of "late bureaucracy"; follow-up work must compare text against actual tasks using independent stage indicators, to avoid circular judgment.
> *Systems analysis*: if these phrases correspond to no verifiable tasks, responsibilities, or exceptions, they may become "liability-disclaiming Padding messages"; if used for necessary coordination, they may also carry real information. Reporting time costs, comprehension errors, and recovery capacity should be compared before judging whether layer-by-layer escalation or "low-power standby" has occurred; the motives of all bureaucrats cannot be diagnosed directly from a word list.

> 📜 **[Fiscal-history annotation · Case 3.7-B] (UK "window tax" avoidance and the Ancien Régime France "salt tax" underground market)**  
> *Historical evidence*:  
> 1. **The UK window tax and avoidance behaviour**: [the UK House of Commons debate record of 9 April 1850](https://hansard.parliament.uk/Commons/1850-04-09/debates/f9bfaf3f-56b7-45f1-af7b-8596ba670ac7/WindowTax) reviews the 1696 introduction and subsequent rate changes, discussing window-blocking avoidance, ventilation, and living conditions. It provides the arguments and quoted materials of the members of the time; the rate tiers of the tax in different periods must be kept apart, and the numbers and health claims in the debate are not directly treated as independent measurements or identified causal effects.
> 2. **Pending research leads on the Ancien Régime French salt tax (Gabelle)**: regional differences in tax regimes, salt smuggling (*faux-saunage*), and enforcement conflicts can serve as research topics on fiscal rules and adaptive behaviour. This section has not yet given regions, periods, tax-price gaps, or locatable historical materials, so "huge price gaps", "armed smuggling", or "severe disruption of commercial order" are not yet treated as verified facts or identified effects. Tax-regime, price, collection, or litigation records must be added before comparison with explanations such as transport costs, supply, and enforcement conditions.
> *Systems analysis*: the design of tax and fee rules may induce adaptive avoidance and informal-market substitution by micro-level agents. When the compliance burden significantly distorts economic incentives, agents hedge by altering the physical form of their assets or shifting to informal transactions, exhibiting the endogenous game response of micro nodes under rigid fiscal constraints.

> 📜 **[Hypothetical judicial-failure example annotation · Case 3.7-C] (Wildcard overmatching)**  
> *Hypothetical scenario*: suppose a disciplinary rule directly encodes everyday harmless behaviour as a guilt signal and allows no counterevidence or review. This case is used to analyse the false-positive mechanism of such rules; when mapping onto a real trial, case and rule texts must be provided separately.  
> *Systems analysis*: this can be analogised to **Wildcard Regex Overmatching and Panic abuse**. Treating behaviour with no diagnostic power as evidence of guilt while sealing off the review interface — punishment can then degenerate into a game of terror; whether it corresponds to some real trial must be evidenced separately with case and rule texts.

> 📰 **[To-be-tested mechanism scenario annotation · Case 3.7-D] (DEI labels and compliance costs)**  
> *Research question*: if an organisation's DEI classification and training keep increasing, do the added requirements improve fairness and task outcomes, or increase comprehension, evidentiary, and compliance burdens? Organisation, institutional version, period, expenditure, and outcomes must be specified, distinguishing organisational adjustment, legal constraints, and market change. This case is a research design; the relation of corporate changes to this mechanism remains to be tested case by case.  
> *Systems analysis*: if the added labels do not improve rights protection while exclusive consultants hold interpretive rights, the "WS-* death spiral" can be used to pose a refutable critique; if the classification improves remedies and the benefits exceed the costs, the parasitism explanation does not hold. Malice can be judged neither from the DEI name alone, nor can fairness slogans exempt cost, evidentiary, and error-correction review; corporate changes — and still less elections — cannot in turn serve as single-cause proof of this mechanism.

<a id="research-process-pattern"></a>
<a id="legacy-v11-1-sec-3-3"></a>
<a id="sec-3-8"></a>

<a id="legacy-v11-1-rfc-006"></a>
<a id="legacy-v11-0-rfc-006"></a>

### 3.8 Candidate Evolution-Process Diagram and Research Clues

**Claim identity:** candidate process pattern (non-numbered research material).
**Dependencies and additional conditions:** Group II comparison question; does not derive stage order or frequency from the postulate.

**Normative Spec (规范条文).**

This section is a candidate process pattern, not a lifecycle law deduced from Group II, nor does it prove these transitions are common. Exploration, diffusion, closure, and refactoring are used to pose comparison questions; systems may jump, reverse, long-term coexist, or locally repair. If interpretive closure and feedback failure occur, maintenance and recovery difficulty may increase, and the effect must be measured separately. The diagram below draws only one risk branch; it does not mean every system must pass through four stages.

```
【Candidate risk-evolution path diagram (non-inevitable convergence path)】

1. The Hack (hacker breakout phase)
   └─ Against the bloated old order, propose a minimal protocol interface (Linus's post / 95 Theses / Hu Shi's vernacular poetry / Wittgenstein's Tractatus Logico-Philosophicus)
        │
        ▼
2. The Fork & Expansion (sink-down fission phase)
   └─ Diffusion and authority-interface-reconfiguration comparison clues (Android ROM-flashing wave / Protestant princes' diffusion / mass literacy / Pure Land nianfo)
        │
        ▼
3. The Institutionalization & Bloat (norm-accumulation phase)
   └─ If interpretive closure, rent dominance, and insufficient correction coexist, normative burden may accumulate
      (platform exclusive taxation and compliance-threshold disputes / WS-* standards-stack bloat / extreme-label politics / scholastic-literati monopoly on interpretive rights)
        │
        ├─► [Healthy branch A: internal repair and rule simplification] ──► [recovery performance and cost to be verified]
        ├─► [Healthy branch B: multi-branch local exploration] ──► [gradual-absorption effect to be verified]
        │
        ▼ (if repair fails and competition and exit channels are lacking)
4. Potential Deadlock & Reboot (deadlock-risk and paradigm-refactoring phase)
   └─ Possible systemic recovery difficulty; at this point one must weigh internal repair, bypass refactoring, and continued operation
      (SOAP/REST deployment repair, coexistence, and gradual-migration comparison / new round of open-source anti-monopoly / scientific revolution / philosophy's turn from metaphysics to logic-language analysis)
```

*Note: This diagram only marks the potential deadlock-evolution risk when intermediary monopoly and feedback failure are unchecked; it is not the single inevitable end-state of system evolution.*
*Note: The materials in the diagram are only research clues awaiting comparison, not empirical proof that each stage is completed or that the order is inevitable. The spread of the theses and doctrinal claims, the vows and organisational conditions of Pure Land nianfo, must be verified separately; the periodisation and interpretation of the scientific revolution and the linguistic turn of philosophy are contested, and other historical examples must also be evidenced item by item. The arrows in the diagram do not prove that technological or ideological substitution is complete; related new intermediaries, reverse processes, and un-transformed cases must also be included.*

<!-- SP:END chapter-03 -->
