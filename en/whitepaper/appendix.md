> **Translation record**
> - Chinese source: `社会系统协议学白皮书.md`, block `appendix` — 334 lines, 36108 bytes, block sha256 `85d514c867b2a02b8628c6b437e8d4f62fa56fa16558807f8af6eb33a1693b81`, taken as the content between the `<!-- SP:BEGIN appendix -->` and `<!-- SP:END appendix -->` markers and reported by `tools/whitepaper_blocks.py list`; whole-file sha256 `d5ffb73e3db73f8bb42a2ecb39871bf6c55eace8bb72111b63a2ee362134d9c8`, 338639 bytes, 2026-11-08
> - Chinese version / release tag: `v11.2-r20261106` (theoretical version remains v11.2)
> - Translation version: `en-v0.1-appendix`
> - Translation date: 2026-11-08
> - Check status: self-check PASS (consistency_check.py --expect-cards 19, all 7 subheadings ×19 uniform); independent read-only audit PASS; machine and glossary checks only; no independent professional native-speaker review
> - Pending sync: none at present; to be recorded item by item if the Chinese source is updated
> - Status: complete translation of this appendix block (the appendix is a navigation and version concordance of the 19 SP-RFC bodies plus 19 generation/evidence cards; it contains no case-annotation sections, so nothing inside the block is omitted)
> - Authority: the Chinese SSOT is authoritative; this translation does not constitute a separate set of definitions (C2)

**Scope and edition status.** This file is one block of a **phased** translation. The English edition as a whole is an *abridged adaptation* of the v11.2 whitepaper: the six chapters that carry case-annotation sections are not yet translated, and those annotations remain untranslated by design until the underlying Chinese case materials pass the real-case acceptance stage (T3). The appendix is a navigation and version index and carries no case annotations, so nothing is dropped here; completeness of this block does not imply completeness of the edition, and this translation does not elevate any claim to established status. The block itself runs from the `<!-- SP:BEGIN appendix -->` marker to the `<!-- SP:END appendix -->` marker; the translation record, the chapter glossary and the two notes below precede that boundary and are not part of the translated text.

## Chapter Glossary — Appendix

| Chinese | English used in this file | Remark |
| :--- | :--- | :--- |
| 第一组核心命题：信道容量与语义边界 | Proposition Group I: Channel Capacity & Semantic Boundary | group name, unique form in the whole book |
| 第二组核心命题：中介寄生与兼容层衰减 | Proposition Group II: Intermediary Parasitism & Compatibility Decay | group name, unique form in the whole book |
| 第三组核心命题：跨期终局性与预期信誉 | Proposition Group III: Intertemporal Finality & Expectation Credibility | group name, unique form in the whole book |
| 第四组核心命题：特权环隔离与脑裂传染 | Proposition Group IV: Privilege Ring Isolation & Split-Brain Contagion | group name, unique form in the whole book |
| 第五组核心命题：传输拓扑与任务反馈 | Proposition Group V: Transport Topology & Task Feedback | group name, unique form in the whole book |
| 第六组核心命题：技术债核算与演化筛选 | Proposition Group VI: Debt Accounting & Evolutionary Selection | group name, unique form in the whole book |
| 6 个核心命题组 | 6 Core Proposition Groups | H3-A landed, title-case unique |
| 19 项有效 SP-RFC | 19 Effective SP-RFC Items | title-case unique |
| O1–O5 | O1 Agent / O2 Protocol / O3 Expectation & Trust / O4 Middleware / O5 Resource & Physical Constraint | primitive-object codes, unique in the whole book |
| P1–P3 | P1 resource background / P2 agent autonomy / P3 expectation-induced equilibrium | assumption codes, unique in the whole book |
| 基础与附加条件 | Foundations and Additional Conditions | evidence-card subheading, 19× uniform |
| 困境与反事实 | Dilemma and Counterfactual | evidence-card subheading, 19× uniform |
| 必要性 | Necessity | evidence-card subheading, 19× uniform |
| 充分性与边界 | Sufficiency and Boundaries | evidence-card subheading, 19× uniform |
| 替代与最小性 | Alternatives and Minimality | evidence-card subheading, 19× uniform |
| 证据与拒绝条件 | Evidence and Rejection Conditions | evidence-card subheading, 19× uniform |
| 当前状态 | Current Status | evidence-card subheading, 19× uniform |

**Note on claim identities.** The 19 claim-identity labels in this appendix are descriptive phrases at the grain of the source sentence (per R7 of the term ledger), not a taxonomy of claim identities. This translation keeps the five canonical claim identities — `postulate`, `conditional proposition`, `mechanism hypothesis`, `accounting definition`, `normative objective` — distinct, and renders the finer descriptive labels by reusing the locked class words (conditional model, social bridging, empirical bridging, normative rule, research norm, semantic application, citation of established physical results, and so on). The labels are not upgraded into proven conclusions.

**Convention on cross-chapter links.** In-page anchors that live in another English chapter or the appendix (#rfc-evidence-XXX, #sp-rfc-XXX) are linked directly to their corresponding English pages, maintaining full link closure within the English edition. Anchors that live in this file remain same-page links.

---


<!-- SP:BEGIN appendix -->
## Appendix: Navigation and Version Concordance of the 19 SP-RFC Bodies

<a id="rfc-directory"></a>

### Entry Points to the 19 SP-RFC Bodies

| New number | Group | Standalone body section | Claim identity |
|---|---|---|---|
| SP-RFC-001 | I | [2.1 Physical Channel and Semantic Decoding](chapter-02.md#sp-rfc-001) | citation of established physical results, conditional model, and social bridging |
| SP-RFC-002 | I | [2.2 Naming and Common Identification](chapter-02.md#sp-rfc-002) | empirical mechanism hypothesis |
| SP-RFC-003 | I | [2.3 Textual Stability and Cross-Context Interpretation](chapter-02.md#sp-rfc-003) | semantic propagation application |
| SP-RFC-004 | II | [3.1 Conditional Retention Rate of Serial Compatibility Layers](chapter-03.md#sp-rfc-004) | conditional model |
| SP-RFC-005 | II | [3.2 Normative Complexity and Intermediary Rent-Seeking Feedback](chapter-03.md#sp-rfc-005) | conditional mechanism hypothesis |
| SP-RFC-006 | II | [3.3 Approval Latency, Mission Deadline, and Protection Benefit](chapter-03.md#sp-rfc-006) | conditional judgment and application comparison |
| SP-RFC-007 | II | [3.4 Architect's Understandability, Rights, and Migration Precepts](chapter-03.md#sp-rfc-007) | cross-group normative rule |
| SP-RFC-008 | III | [4.1 Performance Probability, Recovery, and Investment Threshold](chapter-04.md#sp-rfc-008) | conditional model and empirical bridging |
| SP-RFC-009 | III | [4.2 Retry Idempotence, Record Durability, and Finality](chapter-04.md#sp-rfc-009) | property definition and procedural boundary |
| SP-RFC-010 | III | [4.3 Deterministic Execution and Conditional Commitment](chapter-04.md#sp-rfc-010) | execution mechanism and conditional protection |
| SP-RFC-011 | IV | [5.1 Privilege Isolation and Constraints on the Executor](chapter-05.md#sp-rfc-011) | authority model and social bridging |
| SP-RFC-012 | IV | [5.2 Resource Cutoff, Communication Partition, and Conflicting Writes](chapter-05.md#sp-rfc-012) | state distinction and mechanism hypothesis |
| SP-RFC-013 | IV | [5.3 Predatory Gain, Strict Dominance, and Static Equilibrium](chapter-05.md#sp-rfc-013) | conditional derivation of a finite two-action game |
| SP-RFC-014 | IV | [5.4 Authorisation Interface for Specific Public Objectives](chapter-05.md#sp-rfc-014) | institutional instantiation and normative boundary |
| SP-RFC-015 | IV | [5.5 Feasible Choice Set, Exit, and Voluntariness Identification](chapter-05.md#sp-rfc-015) | identification boundary and application hypothesis |
| SP-RFC-016 | V | [6.1 Mobilisation Task, Acknowledgement Feedback, and Continuous Governance](chapter-06.md#sp-rfc-016) | mechanism analogy and empirical bridging |
| SP-RFC-017 | VI | [7.1 Migration Net Burden and Technical-Debt Accounting](chapter-07.md#sp-rfc-017) | accounting definition and option comparison |
| SP-RFC-018 | VI | [7.2 Multi-Branch Trial and Mature-Feedback Screening](chapter-07.md#sp-rfc-018) | conditional-probability model, empirical screening, and design norm |
| SP-RFC-019 | Cross-group / Chapter 8 | [8.1 AI Tool Control and Exploratory Early-Warning](chapter-08.md#sp-rfc-019) | application and research norm |

Legacy numbers must be converted through the [version concordance](../V11_2_NUMBERING.md); an old and a new number that are identical may point to different content. Legacy references use the `legacy-v11-0-rfc-XXX` or `legacy-v11-1-rfc-XXX` entry points, and do not claim that an unversioned old link still carries the same meaning.

```
================================================================================
Namespace: SP-RFC (Socio-Protocolics Request for Comments)
SP-RFC-8899: in-project umbrella identifier (Umbrella Meta-Spec; not counted among the 001–019 clauses)
Status: Research Draft / Open to Review (not an adopted external standard)
Category: Civilizational Systems Architecture
Framework: 3 Postulates / 6 Core Proposition Groups / 19 Consecutive RFC Entries; v11.2 numbering
================================================================================
```

| Logical identity and number | Normative / term name | Affiliated core proposition and formalised mechanism | Historical / engineering comparison and evidence boundary |
| :--- | :--- | :--- | :--- |
| **【citation of established physical results, conditional model, and social bridging】<br>SP-RFC-001** | **Physical Channel and Semantic Decoding**<br>body [2.1](chapter-02.md#sp-rfc-001) | **Proposition Group I: Channel Capacity & Semantic Boundary**<br>The physical-capacity theorem and the candidate social model $C\le kI$ are kept separate; the semantic mapping of $N_{\text{padding}}$ awaits calibration. | Stylistic and terminology thresholds can be studied as objects of comprehension cost; their effect on engineer training and collaboration must be identified independently, and no unmeasured inter-generational shortening magnitude is reported. |
| **【empirical mechanism hypothesis】<br>SP-RFC-002** | **Naming and Common Identification**<br>body [2.2](chapter-02.md#sp-rfc-002) | **Proposition Group I: Channel Capacity & Semantic Boundary**<br>Dispersed experience can form a citable interface through conceptual encapsulation; the gains in identification and coordination are tested separately. | Conceptual naming may lower cross-agent identification and coordination cost; the gain is to be compared. Judicial relief depends on the evolution of legal sources; naming does not constitute a pre-emptive monopoly over a judicial entry point. |
| **【semantic propagation application】<br>SP-RFC-003** | **Textual Stability and Cross-Context Interpretation**<br>body [2.3](chapter-02.md#sp-rfc-003) | **Proposition Group I: Channel Capacity & Semantic Boundary; related to Group V tasks**<br>Byte hashing does not guarantee semantic consistency; the costs of understandability, stability, and interpretive coordination must be specified by a model. | Fixing a canon and cross-language dissemination each have their conditions; no undefined product upper bound or a "zero tampering for a millennium" is claimed. |
| **【conditional model】<br>SP-RFC-004** | **Conditional Retention Rate of Serial Compatibility Layers**<br>body [3.1](chapter-03.md#sp-rfc-004) | **Proposition Group II: Intermediary Parasitism & Compatibility Decay**<br>$\eta=\prod_i(1-\lambda_i)$; a serial arrangement adds no output or recovery model, and geometric decay must be accompanied by equal rates or a uniform positive lower bound. | The net contribution of a compatibility layer must be compared against feasible alternatives; wars and the rise and fall of empires still require independent historical materials and multi-factor analysis. |
| **【conditional mechanism hypothesis】<br>SP-RFC-005** | **Normative Complexity and Intermediary Rent-Seeking Feedback**<br>body [3.2](chapter-03.md#sp-rfc-005) | **Proposition Group II: Intermediary Parasitism & Compatibility Decay**<br>Where exclusive rights, a dominant non-productive net payoff, and insufficient competition/exit/error-correction coexist, test the complexity–rent-seeking feedback; an institutionalised scenario must satisfy the same conditions. | [different paths of UNIX/GNU/Linux](chapter-03.md#sec-3-2); [complexity-boundary comparison of SOAP/WS-* deployments](chapter-03.md#sec-3-6-1); [discussion of institutional boundaries and Lysenkoism](chapter-03.md#sec-3-6-2) (the church-finance controversy and the university theological review are studied separately; the Sorbonne is not equated with an indulgence-selling institution). |
| **【conditional judgment and application comparison】<br>SP-RFC-006** | **Approval Latency, Mission Deadline, and Protection Benefit**<br>body [3.3](chapter-03.md#sp-rfc-006) | **Proposition Group II: Intermediary Parasitism & Compatibility Decay**<br>For a specific task, $Latency_{Audit}>TTL_{mission}$ may cause timeout; strictly distinguish four consequences — original-path delay, available alternative bypass, local task failure, and systemic governance failure; prudent review is not rent-seeking, and speed does not automatically increase net benefit. | The classified applicability of the UK's 1865 Locomotive Act and its 1896 amendment; one cannot infer from a local timeout that an entire industry is zeroed out or that a malicious bypass is certain to succeed. |
| **【cross-group normative rule】<br>SP-RFC-007** | **Architect's Understandability, Rights, and Migration Precepts**<br>body [3.4](chapter-03.md#sp-rfc-007) | **Cross-group normative rule; Group II keeps the entry point and also cites Groups I/IV/VI**<br>1. the minimal-plain-language precept; 2. the cut-the-rent-seeking precept; 3. the decisive-refactoring precept. | [Hu Shi's materials on sorting the national heritage](chapter-02.md#sec-2-4-3); [the interface analogy of Luther and Wang Yangming](chapter-03.md#sec-3-5-2); [the interface of Huineng and Pure Land practice](chapter-03.md#sec-3-5-1); [comparison of REST/JSON deployment conditions](chapter-03.md#sec-3-6-1); a cross-section comparison clue does not mean the rule's effect is already verified. |
| **【conditional model and empirical bridging】<br>SP-RFC-008** | **Performance Probability, Recovery, and Investment Threshold**<br>body [4.1](chapter-04.md#sp-rfc-008) | **Proposition Group III: Intertemporal Finality & Expectation Credibility**<br>$NPV_i=\sum_t\beta_i^t[p_{it}R_{it}+(1-p_{it})Q_{it}]-I_i$; performance, remedy, and investment threshold act jointly. | Credible commitment is a candidate mechanism; the effects of financial crises, social-security participation, and marriage/fertility must be identified separately. |
| **【property definition and procedural boundary】<br>SP-RFC-009** | **Retry Idempotence, Record Durability, and Finality**<br>body [4.2](chapter-04.md#sp-rfc-009) | **Proposition Group III: Intertemporal Finality & Expectation Credibility**<br>Idempotence under the same request identifier $F_k(F_k(s))=F_k(s)$; durability, finality, and authorisation update are defined separately. | Fix the transaction, rule, and evidence before comparison; a lawful review and an in-action withdrawal of authorisation are not arbitrary rewriting of history. |
| **【execution mechanism and conditional protection】<br>SP-RFC-010** | **Deterministic Execution and Conditional Commitment**<br>body [4.3](chapter-04.md#sp-rfc-010) | **Proposition Group III: Intertemporal Finality & Expectation Credibility**<br>$s_{n+1}=\delta(s_n,tx_n)$; beyond determinism, ordered input, consensus, authority, and fault conditions are still required. | Signature- and time-lock-constrained protocol-controlled state and assets do not guarantee off-chain reserves, purchasing power, or resistance to physical coercion. |
| **【authority model and social bridging】<br>SP-RFC-011** | **Privilege Isolation and Constraints on the Executor**<br>body [5.1](chapter-05.md#sp-rfc-011) | **Proposition Group IV: Privilege Ring Isolation & Split-Brain Contagion**<br>Ring-3 privilege protection relies on a trusted kernel; constraining Ring-0 requires separate review, remedy, and power checks. | The engineering analogy of rule-of-law property rights; expropriation must be analysed by jurisdiction, condition, and compensation procedure; it does not imply that investment is necessarily zeroed. |
| **【state distinction and mechanism hypothesis】<br>SP-RFC-012** | **Resource Cutoff, Communication Partition, and Conflicting Writes**<br>body [5.2](chapter-05.md#sp-rfc-012) | **Proposition Group IV: Privilege Ring Isolation & Split-Brain Contagion**<br>Resource cutoff, communication partition, and conflicting multi-master writes are tested separately; arbitration and stop-write-on-disconnect can protect safety. | Local in-transit interception and cross-domain forged jurisdiction are analogous respectively to Rogue Transit and BGP Hijacking. |
| **【conditional derivation of a finite two-action game】<br>SP-RFC-013** | **Predatory Gain, Strict Dominance, and Static Equilibrium**<br>body [5.3](chapter-05.md#sp-rfc-013) | **Proposition Group IV: Privilege Ring Isolation & Split-Brain Contagion**<br>Plunder dominance requires a complete net-utility comparison against the relevant opponent's strategies; group convergence requires a given dynamic. | Zero penalty is one of the incentive factors; cooperative gain, reputation, long-term tax base, and fault-tolerance mechanisms must be examined jointly. |
| **【institutional instantiation and normative boundary】<br>SP-RFC-014** | **Authorisation Interface for Specific Public Objectives**<br>body [5.4](chapter-05.md#sp-rfc-014) | **Proposition Group IV: Privilege Ring Isolation & Split-Brain Contagion**<br>An authorisation Syscall is involved only when goals such as state enforcement are required; autonomy and technical standards can continue to evolve at Ring-3. | Hu Shi's vernacular writing entered the national-school standard through the 1920 forwarding order of the Beijing School Administration Bureau; the Edict of Milan; the UK window-tax avoidance and local negative externalities (see [Case 3.7-B](chapter-03.md#sec-3-7-1)). |
| **【identification boundary and application hypothesis】<br>SP-RFC-015** | **Feasible Choice Set, Exit, and Voluntariness Identification**<br>body [5.5](chapter-05.md#sp-rfc-015) | **Proposition Group IV: Privilege Ring Isolation & Split-Brain Contagion**<br>A single choice $H(\text{Choice})=0$ must be identified together with the feasible alternative set, exit cost, and monopoly constraint; one cannot separately presume voluntariness or coercion. | The Appalachian coal-company town tokens tied to exclusive stores; the Microsoft Windows Internet Explorer bundling antitrust litigation; the attribution-controversy ledger of the historical agricultural–industrial price-scissors contribution. |
| **【mechanism analogy and empirical bridging】<br>SP-RFC-016** | **Mobilisation Task, Acknowledgement Feedback, and Continuous Governance**<br>body [6.1](chapter-06.md#sp-rfc-016) | **Proposition Group V: Transport Topology & Task Feedback**<br>TCP/UDP serve as transport-mechanism analogies; organisational reliability depends on application-layer feedback, resources, and recovery. | Li Zicheng and Zhu Yuanzhang can be used for historical comparison; one cannot infer governance success or failure from a protocol name or the number of ACKs. |
| **【accounting definition and option comparison】<br>SP-RFC-017** | **Migration Net Burden and Technical-Debt Accounting**<br>body [7.1](chapter-07.md#sp-rfc-017) | **Proposition Group VI: Debt Accounting & Evolutionary Selection**<br>$\Delta\text{Burden}_{\text{net}}=NPV(\text{Cost}_{\text{migration}}+\text{Loss}_{\text{implicit}}+\text{Maintenance}_{\text{new}})-NPV(\text{Debt}_{\text{legacy}})$; compare net burden after unifying the boundary and lifecycle. | Retain the Catch-Block fault-tolerance asset and the Strangler Fig incremental migration; a non-zero cost does not mean the net burden is always non-negative. |
| **【conditional-probability model, empirical screening, and design norm】<br>SP-RFC-018** | **Multi-Branch Trial and Mature-Feedback Screening**<br>body [7.2](chapter-07.md#sp-rfc-018) | **Proposition Group VI: Debt Accounting & Evolutionary Selection**<br>With independent and fixed success rates, $P=1-\prod_k(1-p_k)$; under a general budget constraint $\sum_{k=1}^K\text{Cost}_k+C_{\text{merge}}(K)\le\text{Budget}$ (simplified to $K\cdot\text{Cost}_{\text{fork}}\le\text{Budget}$ when costs are equal and merge overhead is ignored); the feedback window is $T_{\text{latency}}\le\Delta t<T_{\text{environment}}$. | Branch horse-racing among operating systems such as Linux; the TCP/IP vs OSI protocol-route competition; the Xiaogang Village and Special-Zone concurrent trial-and-error; clues from WeChat's multi-team parallel iteration (parameters await verification against the enterprise's original records); the architect is the trunk merger. |
| **【application and research norm】<br>SP-RFC-019** | **AI Tool Control and Exploratory Early-Warning**<br>body [8.1](chapter-08.md#sp-rfc-019) | **Cross-group tooling/research norm, located in Chapter 8; keeps the Group VI entry point and relates to Groups II/IV, not a deductive corollary of VI**<br>A risk-proxy score exceeding a preset threshold triggers only a data and mechanism review; the threshold is uncalibrated and does not authorise physical intervention; bypass decisions compare benefit, rights, and migration risk separately. | Candidate comparison of LLM tool control rights, exit, and independent audit; the four proxy inputs and one composite score are not yet calibrated and cannot serve as a deterministic social diagnosis. |

<a id="rfc-evidence-cards"></a>

### RFC Generation and Evidence Cards

The cards below are item-by-item traceability entries to the body text; they add no RFC, no claim
category, and no proven conclusion. The P/O column lists modelling invocations; additional
assumptions and normative objectives are listed separately; "verification not yet completed" does not
erase a qualified formal derivation, nor does it upgrade a code test into a social empirical result.
Source localisation and gaps are in [Core Case Sources and Boundaries](../case_sources_and_boundaries.md).

<a id="rfc-evidence-001"></a>

#### G001 | Physical Channel and Semantic Decoding

**Body and identity**: [SP-RFC-001](chapter-02.md#sp-rfc-001); citation of established physical results, conditional model, and social bridging.

- **Foundations and Additional Conditions**: O1 (audience), O2 (encoding and rules), O5 (channel and time); P1. Also given: bandwidth, signal-to-noise ratio, task, accuracy, and the assumptions of no serial overlap / no retry.
- **Dilemma and Counterfactual**: A finite channel and the audience's decoding capacity limit the end-to-end transmission of the same task; removing an available decoding path may cause a specified task to fail, but failure cannot be presumed from a stylistic name.
- **Necessity**: No language, style, or training method is proven necessary; examine the alternative decoding path that succeeds without that option.
- **Sufficiency and Boundaries**: Within the given serial model, the payload throughput formula is the sum of transmission and decoding latency; source encoding and prior learning are counted separately, accuracy is reported separately, and the payload ratio is not treated as goodput already discounted by successful delivery; it does not guarantee social collaboration performance, nor does it cover pipelining, retry, and comprehension error.
- **Alternatives and Minimality**: Compare combinations of r, d, and accuracy, plus pipelining and error-correction schemes; no proof that plain language or another encoding is minimal or unique.
- **Evidence and Rejection Conditions**: Algebra in §2.1; social bridging must independently measure r, d, and task outcome, and be compared with existing explanations such as cognitive load; when precision suffices to exclude a pre-registered improvement, reject the corresponding local prediction.
- **Current Status**: The citation of established physical results and the bounded algebra are kept separate; social bridging has not yet completed verification.

<a id="rfc-evidence-002"></a>

#### G002 | Naming and Common Identification

**Body and identity**: [SP-RFC-002](chapter-02.md#sp-rfc-002); empirical mechanism hypothesis.

- **Foundations and Additional Conditions**: O1 (participant), O2 (name and common-reference rule); P1 (resource background). Also given: object content, prior knowledge, retrieval/citation task, and the object under intervention estimation.
- **Dilemma and Counterfactual**: Experience is dispersed and mutual reference is costly; lacking a shared name may raise cost, but description, alias, or existing rules can also accomplish the task.
- **Necessity**: Unified word form is not a proven necessary condition; effective collaboration without a unified name can reject that necessity claim, and does not automatically negate a local naming gain.
- **Sufficiency and Boundaries**: Having a name does not guarantee understanding, recognition, adoption, or coordination success; these processes must be measured separately.
- **Alternatives and Minimality**: Compare description, alias, stable name, and glossing tools; the overall intervention and the independent naming effect after excluding length are designed separately under §8.5.1; no unique scheme is proven.
- **Evidence and Rejection Conditions**: Pre-register correct reference, retrieval time, accurate citation, and collaboration outcome, plus minimum gain and error; control content, familiarity, and training, and a qualified comparison that excludes improvement narrows or rejects the local prediction.
- **Current Status**: empirical mechanism hypothesis; existing textual clues do not equal effect identification, and verification has not yet been completed.

<a id="rfc-evidence-003"></a>

#### G003 | Textual Stability and Cross-Context Interpretation

**Body and identity**: [SP-RFC-003](chapter-02.md#sp-rfc-003); semantic propagation application.

- **Foundations and Additional Conditions**: O1 (heterogeneous audience), O2 (text and interpretation task), O3 (audience belief, listed separately only as an expected mechanism); P1 (background). Also given: version, language, context, and interpretive resources.
- **Dilemma and Counterfactual**: The same bytes may be interpreted by different audiences as different senses; removing version identification or interpretive resources may increase errors on a specified task, but it is not a necessary outcome.
- **Necessity**: No proof that text locking or annotation is a necessary condition for all dissemination; existing common knowledge may make the task succeed.
- **Sufficiency and Boundaries**: A hash can check byte change under specified trust conditions, but cannot sufficiently guarantee interpretive consistency or collaboration success.
- **Alternatives and Minimality**: Compare version identifiers, annotation, local interpretation, and other coordination mechanisms; no general trade-off upper bound is established, nor is minimality or uniqueness proven.
- **Evidence and Rejection Conditions**: Execute H003-V and H003-I separately; register the improvement magnitude and error of specified version identification, interpretive consistency, and task performance, pre-specify the success criterion and multiple-comparison handling for a single, common, or stratified primary metric, and reject the corresponding local prediction under §2.3.
- **Current Status**: semantic propagation application; property boundaries and untested local hypotheses are listed separately, and empirical verification has not yet been completed.

<a id="rfc-evidence-004"></a>

#### G004 | Conditional Retention Rate of Serial Compatibility Layers

**Body and identity**: [SP-RFC-004](chapter-03.md#sp-rfc-004); conditional model.

- **Foundations and Additional Conditions**: O4 (serial intermediary), O5 (same traffic); P1. Assumes a conditional retention rate at each stage, no added output or recovery path, and an explicit unit of measurement.
- **Dilemma and Counterfactual**: Serial stages may lose traffic stage by stage; adding a loss stage lowers the retention rate within the bounded model, but added verification or output can change the net contribution.
- **Necessity**: Low loss does not require deleting every intermediary; retention rate is not a necessary and sufficient indicator for judging the value of all intermediaries.
- **Sufficiency and Boundaries**: Within the stated model, conditional retention rates multiply; geometric/exponential decay needs equal rates or a uniform positive lower bound, and cannot rely only on each stage's loss being positive.
- **Alternatives and Minimality**: Compare the output, verification, right protection, and recovery of feasible alternatives; no proof that the fewest layers is the optimal architecture.
- **Evidence and Rejection Conditions**: Independently record each stage's input, output, addition, and recovery; build a separate model when addition/recovery exists. Olken's missing expenditure is not a stage-loss parameter; see the source ledger for the caliber.
- **Current Status**: The conditional model is derivable; social application and parameter estimation have not yet completed verification.

<a id="rfc-evidence-005"></a>

#### G005 | Normative Complexity and Intermediary Rent-Seeking Feedback

**Body and identity**: [SP-RFC-005](chapter-03.md#sp-rfc-005); conditional mechanism hypothesis.

- **Foundations and Additional Conditions**: O1 (strategic agent), O4 (intermediary), O2 (exclusive right and constraint); P2, with P1 only as a cost background. Also given: net payoff, competition, exit, and error-correction conditions.
- **Dilemma and Counterfactual**: Exclusive control may make complexity maintenance and non-productive payoff mutually reinforcing; removing an approval while retaining shadow control does not necessarily change that incentive.
- **Necessity**: Complexity, charging, or approval time are not necessary and sufficient evidence of rent-seeking; exclusive control and non-productive payoff must be identified independently.
- **Sufficiency and Boundaries**: Given payoff dominance and insufficient constraint, only a testable feedback mechanism is formed, and it does not guarantee that all organisations change in the same direction.
- **Alternatives and Minimality**: Compare competition, public explanation, alternative verification, and a bypass with remedy; when complexity has a protective benefit, account for it separately, and no proof that uniform deletion is optimal.
- **Evidence and Rejection Conditions**: Verify the control right, the associated payoff, the actual work destination, and the net cost; test whether the complexity change follows the payoff incentive; a precise comparison that excludes the predicted feedback rejects that application.
- **Current Status**: conditional mechanism hypothesis; existing cases do not constitute verification of the whole feedback, and verification has not yet been completed.

<a id="rfc-evidence-006"></a>

#### G006 | Approval Latency, Mission Deadline, and Protection Benefit

**Body and identity**: [SP-RFC-006](chapter-03.md#sp-rfc-006); conditional judgment and application comparison.

- **Foundations and Additional Conditions**: O1 (task agent), O2 (approval path), O4 (reviewer), O5 (time and resource); P1. Fixed task TTL, alternative path, protection requirement, and right constraint.
- **Dilemma and Counterfactual**: Approval latency may exceed a path's task deadline; the counterfactual must compare delay, bypass, task failure, and governance failure separately.
- **Necessity**: Approval speed is not a condition for identifying rent-setting; the original rule lacking a protection benefit is also not a necessary condition for refactoring.
- **Sufficiency and Boundaries**: Exceeding the TTL at most shows that a given path may fail to meet the deadline; it does not sufficiently imply task or whole-industry failure.
- **Alternatives and Minimality**: Compare the original rule that meets the stated protection requirement, the long-term permit, the exemption-from-application, and the alternative verification, and count the migration cost; no proof that the shortest process is uniquely optimal.
- **Evidence and Rejection Conditions**: Record the times of first attempt, acceptance, supplement, withdrawal, overdue, and decision; report the full denominator and the risk-reduction effect; compare protection and full cost at sufficient precision.
- **Current Status**: conditional judgment and application comparison; the latency and effect of specific tasks still require measurement, and verification has not yet been completed.

<a id="rfc-evidence-007"></a>

#### G007 | Architect's Understandability, Rights, and Migration Precepts

**Body and identity**: [SP-RFC-007](chapter-03.md#sp-rfc-007); cross-group normative rule.

- **Foundations and Additional Conditions**: O1 (affected agent), O2 (specification), O4 (intermediary), O5 (cost); P1/P2 as modelling background. Also state explicitly the normative objectives of understandability, lawful right, and error correction.
- **Dilemma and Counterfactual**: There are trade-offs among complexity, protection, and migration; lacking an understandable explanation or remedy may increase errors and right harm, but cannot predict inevitable collapse.
- **Necessity**: The three precepts are not universally necessary commands derived from facts; whether to adopt them depends on the public objective and the right boundary.
- **Sufficiency and Boundaries**: Following the precepts does not sufficiently guarantee real understanding, absence of rent-seeking, or migration success; implementation results are verified separately.
- **Alternatives and Minimality**: Compare professional text plus explanation, competitive verification, in-place repair, and bypass; disclose the cost item by item, and no proof that the three precepts are minimal or unique.
- **Evidence and Rejection Conditions**: The normative reason, the benefited and harmed agents, and the remedy must be reviewable; implementation is verified by blind test, actual authority, and migration result; see the cross-group formal-compliance pressure gauge.
- **Current Status**: cross-group normative rule; the value argument and effect assessment are registered separately, and no natural law is claimed.

<a id="rfc-evidence-008"></a>

#### G008 | Performance Probability, Recovery, and Investment Threshold

**Body and identity**: [SP-RFC-008](chapter-04.md#sp-rfc-008); conditional model and empirical bridging.

- **Foundations and Additional Conditions**: O1 (investor), O3 (subjective performance probability), O5 (input); P2/P3. Given term, discounting, performance and default cash flows, and decision rule.
- **Dilemma and Counterfactual**: Uncertain cross-period recovery may lower a project's attractiveness; when only the performance probability changes, the direction of the result depends on the difference between performance and default cash flows.
- **Necessity**: High performance probability is not a necessary condition for all investment; high default recovery, compensation, and other benefits can change the choice.
- **Sufficiency and Boundaries**: The conditional derivation III-1 sufficiently gives the direction of NPV change within that cash-flow model; it does not sufficiently imply crossing the investment threshold or a decline in total CAPEX.
- **Alternatives and Minimality**: Compare remedy, guarantee, financing, and waiting options; do not designate a certain commitment arrangement as the unique mechanism.
- **Evidence and Rejection Conditions**: Verify whether probability, cash flow, and discounting change jointly; empirical prediction requires a control and a threshold, and failure of the premise is not an algebraic refutation.
- **Current Status**: The bounded comparative statics derivation is given; real-parameter identification and social bridging have not yet completed verification.

<a id="rfc-evidence-009"></a>

#### G009 | Retry Idempotence, Record Durability, and Finality

**Body and identity**: [SP-RFC-009](chapter-04.md#sp-rfc-009); property definition and procedural boundary.

- **Foundations and Additional Conditions**: O2 (request, state, record, and review rule), O3 (expected for application layer); P1 (fault background), P3 (expectation background). Fixed request identifier, version, and evidence.
- **Dilemma and Counterfactual**: Retry amplification, loss of an already-committed result, and revocation of a confirmation record are different failures; the absence of de-duplication, recovery, or finality rules can each separately expose a risk.
- **Necessity**: Idempotence is required only for the same request that should be de-duplicated; not all operations must be idempotent, nor is the current state required to be permanently unchanged.
- **Sufficiency and Boundaries**: Idempotence does not guarantee durability or finality; durability does not prohibit an authorised update; finality requires explicit rules and trust assumptions.
- **Alternatives and Minimality**: Compare de-duplication identifier, de-duplication storage, recovery log, and append correction record; do not minimise the lawful review into a deletion target.
- **Evidence and Rejection Conditions**: Inject retry, agreed fault, and authorised review separately; check business effect and record; behavioural consequences such as interaction strategy require specific samples and identification design.
- **Current Status**: property definition and procedural boundary; specific system tests and behavioural hypotheses have not yet completed verification.

<a id="rfc-evidence-010"></a>

#### G010 | Deterministic Execution and Conditional Commitment

**Body and identity**: [SP-RFC-010](chapter-04.md#sp-rfc-010); execution mechanism and conditional protection.

- **Foundations and Additional Conditions**: O2 (state machine, ordering, and execution rule), O1 (executor), O3 (conditional commitment); P1/P2/P3 used separately for fault, strategy, and expected application.
- **Dilemma and Counterfactual**: Node execution divergence and unilateral rewriting of a commitment are different risks; the same code does not automatically provide a consistent history or off-chain redemption.
- **Necessity**: Determinism is not a necessary mechanism for all social commitments; procedurally constrained discretion and manual clearing can serve as alternatives.
- **Sufficiency and Boundaries**: With the same initial state and ordered input, the result is the same; a consistent history additionally requires consensus, members, authority, network, and fault assumptions; protection is limited to actually controlled assets.
- **Alternatives and Minimality**: Compare the error, cost, exception, and remedy of manual/hybrid execution versus deterministic execution; retain bounded discretion, and no proof that a fully automatic scheme is minimal or unique.
- **Evidence and Rejection Conditions**: Test input ordering, fault threshold, escalation, key, and asset boundary; record the commitment-failure condition; the formal recurrence cannot substitute for these tests.
- **Current Status**: execution mechanism and conditional protection; specific institutions and implementation effects have not yet completed verification.

<a id="rfc-evidence-011"></a>

#### G011 | Privilege Isolation and Constraints on the Executor

**Body and identity**: [SP-RFC-011](chapter-05.md#sp-rfc-011); authority model and social bridging.

- **Foundations and Additional Conditions**: O2 (authority rule and execution structure), O1 (power agent), O3 (trusted expectation); P2/P3 background. Also given: review, remedy, and actual enforcement capacity.
- **Dilemma and Counterfactual**: The highest-privilege agent may cross user-space protection; setting authority only on the user cannot by itself constrain the kernel.
- **Necessity**: A particular Ring division is not a necessary condition for all constraints; actual independent review, mutual checks, or other mechanisms must be compared.
- **Sufficiency and Boundaries**: A formal authority matrix does not sufficiently guarantee that the executor is constrained; the accessibility of remedy, resources, and enforcement effect are verified separately.
- **Alternatives and Minimality**: Compare separation of powers, external review, compensation, and audit, counting coordination cost and emergency exceptions; no proof that a certain authority structure is uniquely minimal.
- **Evidence and Rejection Conditions**: Trace actual privilege escalation, over-reach, emergency authority, and remedy execution; when the log is generated by the supervised party, check independently managed retention, event coverage, and integrity, and cross-check actual authority against remedy materials; a checksum cannot prove no omission or content truth; reviewer capture or out-of-rule shared authority constitutes an implementation counter-example.
- **Current Status**: authority model and social bridging; a model distinction does not equal effective real-world constraint, and verification has not yet been completed.

<a id="rfc-evidence-012"></a>

#### G012 | Resource Cutoff, Communication Partition, and Conflicting Writes

**Body and identity**: [SP-RFC-012](chapter-05.md#sp-rfc-012); state distinction and mechanism hypothesis.

- **Foundations and Additional Conditions**: O5 (resource), O4 (transport node), O2 (write and arbitration rule); P1, with strategic conflict using P2 separately. Explicit fault, disconnect, and authority model.
- **Dilemma and Counterfactual**: Resource cutoff, communication partition, and competitive multi-master writes each have occurrence conditions; one cannot write a single fiscal cutoff as an automatic split-brain chain.
- **Necessity**: Communication partition is not a sufficient condition for conflicting writes; resource shortage is also not a sufficient condition for malicious hijacking.
- **Sufficiency and Boundaries**: Stop-write or arbitration can protect safety in partial-fault models, but does not guarantee availability or physical resource recovery.
- **Alternatives and Minimality**: Compare stop-write, authorised arbitration, communication recovery, and resource resupply, making the safety/availability cost explicit; no general minimal configuration.
- **Evidence and Rejection Conditions**: Collect resource, connectivity, authorisation, and write logs separately; when the state is not satisfied, judge inapplicable and do not thereby negate other state distinctions.
- **Current Status**: state distinction and mechanism hypothesis; specific historical or organisational application has not yet completed verification.

<a id="rfc-evidence-013"></a>

#### G013 | Predatory Gain, Strict Dominance, and Static Equilibrium

**Body and identity**: [SP-RFC-013](chapter-05.md#sp-rfc-013); conditional derivation of a finite two-action game.

- **Foundations and Additional Conditions**: O1 (utility-maximising agent), O2 (action and payoff rule); P2. Finite nodes, only H/D two actions, strict dominance of net utility against all opponent strategies.
- **Dilemma and Counterfactual**: Given the payoff table, D strictly dominates H; zero penalty may lower the cost of D, but by itself does not determine the complete net-utility ordering.
- **Necessity**: Zero penalty and positive predatory gain are insufficient to prove dominance; cooperative gain, reputation, and future cost must be included.
- **Sufficiency and Boundaries**: The conditional derivation IV-1 proves that this two-action game has a unique static equilibrium; it does not sufficiently prove arbitrary learning convergence, resource exhaustion, or collapse.
- **Alternatives and Minimality**: Changing payoffs, introducing additional strategies, or repeated interaction requires rebuilding the game; that proof does not select a minimal institutional prescription.
- **Evidence and Rejection Conditions**: Verify all relevant net payoffs and the strategy space; dynamic application specifies the update process separately, and when assumptions are broken, narrow the application rather than claim the derivation is wrong.
- **Current Status**: The bounded normal-form game derivation is given; real payoff identification and dynamic convergence have not yet completed verification.

<a id="rfc-evidence-014"></a>

#### G014 | Authorisation Interface for Specific Public Objectives

**Body and identity**: [SP-RFC-014](chapter-05.md#sp-rfc-014); institutional instantiation and normative boundary.

- **Foundations and Additional Conditions**: O1 (authoriser and affected agent), O2 (jurisdiction and procedure); P2/P3 as implementation and expectation background. Also given: public objective, lawful authority, and right constraint.
- **Dilemma and Counterfactual**: Some objectives require state enforcement, public taxation, or statutory standards; without corresponding authorisation, the objective may not be lawfully completed.
- **Necessity**: State authorisation is involved only when the objective and jurisdiction require it; autonomy, contract, and industry standards are not invalid for not entering the core.
- **Sufficiency and Boundaries**: An authorisation text does not sufficiently guarantee actual implementation, adoption, or beneficial effect; purpose, scope, term, and remedy are verified separately.
- **Alternatives and Minimality**: Compare autonomy, contract, and applicable authorisation paths, retaining refusal, revocation, and review; no proof that state entry into the core is universally optimal.
- **Evidence and Rejection Conditions**: Trace the authorising agent, authority, sub-authorisation, use, term, and actual execution; cross-check the authorisation document and process version in effect at execution, plus change and revocation records; an education order proves only the regulation, not nationwide immediate adoption.
- **Current Status**: institutional instantiation and normative boundary; specific authorisation and effect must be verified by jurisdiction, and universal empirical verification has not yet been completed.

<a id="rfc-evidence-015"></a>

#### G015 | Feasible Choice Set, Exit, and Voluntariness Identification

**Body and identity**: [SP-RFC-015](chapter-05.md#sp-rfc-015); identification boundary and application hypothesis.

- **Foundations and Additional Conditions**: O1 (choosing agent), O2 (bundling and exit rule), O5 (resource and migration cost); P1/P2. Explicit sample denominator, feasible alternative, and constraint.
- **Dilemma and Counterfactual**: Formal consent may coexist with infeasible exit; a single choice may come from either preference alignment or constraint.
- **Necessity**: $H(\text{Choice})=0$ is neither a sufficient identification condition for voluntariness nor for coercion; non-exit does not prove the absence of an alternative.
- **Sufficiency and Boundaries**: An alternative list and an exit button are insufficient to prove feasibility; the full cost, basic services, and post-exit consequences must be counted.
- **Alternatives and Minimality**: Compare interoperability, portability, alternative supply, and remedy; disclose rights and allocation criteria; no proof that a unified exit design is minimally sufficient.
- **Evidence and Rejection Conditions**: Include those who attempted exit and those who did not join; cross-check the actual choice set; historical resource flows, the original author's explanation, and this book's equity criteria are evidenced separately, and a macro contribution does not automatically map to individual rights.
- **Current Status**: identification boundary and application hypothesis; specific voluntariness and behavioural effect have not yet completed verification.

<a id="rfc-evidence-016"></a>

#### G016 | Mobilisation Task, Acknowledgement Feedback, and Continuous Governance

**Body and identity**: [SP-RFC-016](chapter-06.md#sp-rfc-016); mechanism analogy and empirical bridging.

- **Foundations and Additional Conditions**: O1 (task participant), O2 (delivery and confirmation rule), O4 (feedback network), O5 (resupply); P1/P2/P3 as resource, strategy, and expectation background.
- **Dilemma and Counterfactual**: Mobilisation does not automatically bring delivery, resource recovery, and continuous governance; deleting feedback may harm a specified task, but other feedback channels can compensate.
- **Necessity**: The TCP protocol name or ACK form is not a necessary condition for a reliable organisation; a UDP upper layer or a non-digital channel can also provide feedback.
- **Sufficiency and Boundaries**: The number of receipts does not sufficiently prove delivery; a formal ACK with weight 0 still requires independently verified traceable feedback.
- **Alternatives and Minimality**: Compare the task outcome and cost of different feedback, resupply, and recovery schemes; it does not carry the 014 authorisation, and no proof that a single topology is minimal or unique.
- **Evidence and Rejection Conditions**: Using the full task as the denominator, independently sample-verify state delivery, reopening, and failure; after controlling other resources and feedback, test the local prediction of continuous governance.
- **Current Status**: mechanism analogy and empirical bridging; message-diffusion research is not an organisational-survival theorem, and verification has not yet been completed.

<a id="rfc-evidence-017"></a>

#### G017 | Migration Net Burden and Technical-Debt Accounting

**Body and identity**: [SP-RFC-017](chapter-07.md#sp-rfc-017); accounting definition and option comparison.

- **Foundations and Additional Conditions**: O5 (comparable resource and time), O2 (migration and maintenance scheme), O1 (cost bearer); P1 (budget background). Fixed task, lifecycle, price, and discounting.
- **Dilemma and Counterfactual**: Omitting migration cost, implicit asset, or old burden may misjudge the scheme; a non-zero cost cannot imply debt conservation.
- **Necessity**: This accounting caliber is not the only necessary expression for all decisions; right, safety, and distribution constraints must be retained, and one cannot look only at net present value.
- **Sufficiency and Boundaries**: Complete and non-duplicated input suffices to compute the net burden within that boundary, but does not sufficiently prove overall social net benefit or that migration should occur.
- **Alternatives and Minimality**: Compare in-place repair, full replacement, incremental bypass, and no action; identify the value of repair assets independently; no proof that the incremental approach is optimal in all scenarios.
- **Evidence and Rejection Conditions**: Give the cost-agent matrix, old-mechanism repair records, risk, and sensitivity; avoid inferring implicit assets backwards after failure; recompute when an omission or transfer is found, and an identity definition does not count as verification.
- **Current Status**: accounting definition and option comparison; risk frequency, parameters, and specific-scheme effect have not yet completed verification.

<a id="rfc-evidence-018"></a>

#### G018 | Multi-Branch Trial and Mature-Feedback Screening

**Body and identity**: [SP-RFC-018](chapter-07.md#sp-rfc-018); conditional-probability model, empirical screening, and design norm.

- **Foundations and Additional Conditions**: O1 (trial and screening agent), O2 (branch and screening rule), O5 (budget and time); P1, with P2 used only for the separately listed maintainer incentive. Fixed independent success/failure events and each $p_k$.
- **Dilemma and Counterfactual**: Discovery, correct screening, feasible deployment, and migration gain are different events; common failure, short-term proxy, and resource crowding can decouple them.
- **Necessity**: $K>1$ is not a necessary condition for every task's success; high-frequency feedback and independence are also not universal necessary conditions for all organisational learning.
- **Sufficiency and Boundaries**: The independent model computes only the probability that at least one branch succeeds; it does not sufficiently guarantee identifying the successful branch, deployment, or net gain.
- **Alternatives and Minimality**: Compare single-branch under the same budget, heterogeneous multi-branch, and multi-time-scale observation; correlated-event models are allowed; no proof that maximum K or shortest cycle is optimal.
- **Evidence and Rejection Conditions**: Register all branches, probability calibers, maturity results, selection errors, and migration accounting through the four-stage interface; reject the corresponding local application when precision suffices to exclude a prior gain.
- **Current Status**: The conditional probability is derivable; empirical screening and design choice have not yet completed verification.

<a id="rfc-evidence-019"></a>

#### G019 | AI Tool Control and Exploratory Early-Warning

**Body and identity**: [SP-RFC-019](chapter-08.md#sp-rfc-019); application and research norm.

- **Foundations and Additional Conditions**: O1 (user and executor), O2 (tool authority), O4 (provider and measurement intermediary), O5 (cost); P1/P2 background. List tool objective, exit objective, and research objective separately.
- **Dilemma and Counterfactual**: Tool invocation may exceed authority, provider control may raise exit cost, and a proxy score may be misused; the three risks are evidenced separately.
- **Necessity**: A certain deployment, a certain score, or a colour is neither necessary nor sufficient evidence for authority authorisation; a manual stamp also cannot replace an independent authorisation basis.
- **Sufficiency and Boundaries**: A whitelist and parameter validation only guarantee the measured boundary; the radar generates only an uncalibrated review flag, and does not sufficiently identify malice, legality, or real-world health.
- **Alternatives and Minimality**: Compare the benefit and cost of open source, on-device, interoperability, and audit; scoring may be withheld before calibration, and no proof that a unified tool architecture is minimal or unique.
- **Evidence and Rejection Conditions**: Tool-authority testing, provider-exit comparison, and metric external validity are each discharged separately; preserve model, input source, missing data, and research status; PBR/PNR must be obtained by the same document and configuration pairing or independently cross-checked; a scalar being legal does not equal source or pairing being verified. An automatic authorisation interface from score to physical intervention is prohibited.
- **Current Status**: application and research norm; code behaviour is testable, but social measurement and predictive gain have not yet completed verification.
<!-- SP:END appendix -->
