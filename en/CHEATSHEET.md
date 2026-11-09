> **Translation record**
> - Chinese source: `核心概念速查手册_CheatSheet.md` (sha256 `067525cd297b95d6faa8a5ac8b2e5d349a933d369a84da8d96d00fc5317029c4`, 40602 bytes, 2026-11-09)
> - Chinese version / release tag: `v11.2-r20261106` (theoretical version remains v11.2)
> - Translation version: `en-v0.1`
> - Translation date: 2026-11-09
> - Check status: checked sentence by sentence against the Chinese source for claim status, negative guardrails and numbering; machine and glossary checks only; no independent professional native-speaker review
> - Pending sync: none at present; to be recorded item by item if the Chinese source is updated
> - Status: complete translation
> - Authority: the Chinese SSOT is authoritative; this translation does not constitute a separate set of definitions (C2)

# Socio-Protocolics: Core Concepts CheatSheet (L1 Cognitive Cache)
> **Language / 语言**: **English** | [简体中文](../核心概念速查手册_CheatSheet.md)  
> **Positioning**: a high-density theory CheatSheet, a plug-and-play L1 memory base across sessions, and a protocol for fast-loading AI context.
> **Version**: v11.2 (Orthogonal Axiomatic Foundation Edition)
> **Structural revision (2026-10-26)**: v11.2, 19 RFC items numbered consecutively 001—019; for older numbering see the version comparison.
> **Full whitepaper**: [Socio-Protocolics Core Architecture Whitepaper v11.2](whitepaper/chapter-01.md)
> **Evidentiary status**: distinguishes externally published empirical research, this book's conditional models and mechanisms awaiting test, and simulations with assumed inputs; the CheatSheet does not report that this book has completed original social-empirical verification.

**How to use this card**: This card is a cache of the main text. The definitions and boundaries of the primitives, postulates and the six proposition groups are in Whitepaper §1.5; the RFCs are checked against the clauses in the main text; the indicators are defined in §8.3, with the §8.4 reference implementation and the §8.5 operationalisation checked against it. Omitting an expansion does not cancel a condition; cases and analogies do not add new theorems.

---

## I. The 5 Primitive Objects, the 3 First-Order Postulates and the 6 Core Proposition Groups (The L2 Primitives & Propositions)

### 1. The 5 Primitive Objects
* **O1: Agent (intelligent agent)**: an adaptive game-playing unit with a private objective function $U_i$, a discount factor $\beta_i \in (0, 1)$, finite memory and bounded rationality (a person, firm, political party, state, or AI Agent). The level of analysis must be fixed in advance; a single study does not count a state and its internal members twice as independent nodes.
* **O2: Protocol (protocol specification)**: $\mathcal P=\langle\Sigma,\mathcal S,\delta,\mathcal R\rangle$ — in order, the message syntax, state space, transition rules and reward/penalty rules; a formalised instance additionally lists the action set, initial state, ordering, authority, faults, and safety/liveness conditions.
* **O3: Expectation & Trust**: for agent $i$ under its information set $\mathcal I_{i,t}$ and protocol $\mathcal P_t$, the subjective probability distribution is $\mu_{i,t}(A)=\Pr_i(S_{t+1}\in A\mid\mathcal I_{i,t},\mathcal P_t)$; different agents' beliefs may differ. For an integrable function $f$, the expected value is $\mathbb E_i[f(S_{t+1})]=\int f(s)\,d\mu_{i,t}(s)$; the expected value is not treated as the distribution. Trust attaches to a specific performance event and can serve as a verification cache; it is not equivalent to the entire belief distribution, and the basis and the expiry conditions must be stated.
* **O4: Middleware (intermediary interpretation layer)**: a structure that performs translation, authentication, routing, supervision or coordination; its net contribution may be positive or negative. Only the subclass exhibiting exclusive control together with non-productive rent extraction falls under the rent-seeking compatibility-layer analysis.
* **O5: Resource & Energy (physical hard constraints)**: $\Omega$ uniformly denotes the resource feasibility domain / constraint set delimited by available energy, land, physical channel capacity and irreversible time; thermodynamic laws constrain resource conversion.

### 2. The 3 First-Order Postulates
* **SP-POSTULATE-1 (The Finite World & Non-Zero Impedance Postulate)** ★ the physical and epistemological cornerstone of the whole book: the realisation of any real complex adaptive system is constrained by an irreversible flow of time, a finite physical energy budget and cognitive bandwidth; encoding, parsing, routing and acknowledgement across nodes consume resources and time. Under a given physical channel model, the reliable communication rate is bounded by Shannon capacity. A Wittgensteinian "conceptual boundary" (taken from 4.114 of the *Tractatus Logico-Philosophicus*, 1921, and the discussion of vague boundaries in the *Philosophical Investigations* §68/§71) is used to pose a semantic research question; this book does not presuppose that linguistic boundaries are sharp, and its bridging to coordination capacity must be defined and tested independently under RFC-001 and cannot be derived directly from a physical capacity result. **Anti-Happy-Path Centricity**: cover abnormal and normal paths, and test low-frequency, high-loss events first; the "99% exception path" is a non-empirical cautionary expression, not a number of paths, a running time or an accident proportion. Boundary condition first.
* **SP-POSTULATE-2 (The Agent Autonomy Postulate)**: the Agent has an independent objective function $U_i$ and time discounting $\beta_i$, retains the freedom of strategic deviation, and is by no means a mechanically passive instruction executor or a logic gate.
* **SP-POSTULATE-3 (The Expectation-Induced Equilibrium Postulate)**: $\mathcal{P}_t \longrightarrow \mu_{i,t} \longrightarrow \text{expected utility and incentives} \longrightarrow \text{strategic choice and action}$. A protocol influences expectations and incentives through rule broadcast and performance signals and induces an equilibrium tendency; it does not presuppose mechanical execution or the general convergence of an arbitrary learning process.

### 3. The 6 Core Proposition Groups and the Three-Tier Orthogonal Pyramid

Evidence classification: Group I distinguishes established physical results from social-bridging hypotheses; Groups II/V are dominated by mechanism hypotheses; Groups III/IV contain conditional propositions with assumptions attached, with real-world bridging and behavioural dynamics tested separately; Group VI distinguishes accounting definitions, an independent probability model and a screening hypothesis. Uniform grouping does not imply a uniform proof status.

* **Proposition Group I: Channel Capacity & Semantic Boundary** (modelling starting point P1; related RFC-001, 002, 003): physical capacity and social-semantic bridging are separated; the coordination effect is tested separately.
* **Proposition Group II: Intermediary Parasitism & Compatibility Decay** (modelling starting point P1/P2/O4; related RFC-004, 005, 006; cross-group normative rule RFC-007): serial loss, rent-seeking feedback, approval latency and protection benefit are each tested separately; a non-numbered candidate process diagram is listed separately at the end of the chapter.
* **Proposition Group III: Intertemporal Finality & Expectation Credibility** (modelling starting point P2/P3; related RFC-008, 009, 010): project performance, record properties and execution conditions are each defined separately; the chapter-end consumption and policy application does not follow from the investment model. The time discount factor is $\beta_i$; when the discrete-period discount rate is $r_i$, $\beta_i=1/(1+r_i)$.
* **Proposition Group IV: Privilege Ring Isolation & Split-Brain Contagion** (P1/P2/P3 used by sub-model; related RFC-011, 012, 013, 014, 015): authority constraints, conflict states, payoff comparison, specific authorisation and exit identification are each tested separately; the whole group is not covered by any one sub-model.
* **Proposition Group V: Transport Topology & Task Feedback** (modelling starting point P1/P2/P3; related RFC-016): TCP/UDP is a cognitive analogy; tasks, resources, responsibility and recovery capability are tested separately.
* **Proposition Group VI: Debt Accounting & Evolutionary Selection** (P1 budget background; P2 used separately for incentives; related RFC-017, 018): net burden is accounted on a common boundary, and branching and mature feedback are tested under a finite budget; no conservation of total debt or necessary victory of parallelism is claimed. The cross-group tooling/research norm RFC-019 sits in Chapter 8 and is not counted as a deductive clause of this group.

---

The arrows among postulates, proposition groups and RFCs denote modelling dependency and navigation attribution; each item lists its own additional conditions. A group table does not imply that all sub-models share the same premise, and does not imply a complete proof without additional assumptions; "orthogonal" denotes a division of responsibilities, and formal independence requires separate proof. P1–P3 are modelling conventions and constitutive starting points whose empirical content is still tested item by item; no unified failure count and no automatic stopping rule of the form "N consecutive cases and the programme is demoted" is set. The "unified meta-compiler" is a unified modelling programme whose incremental value is tested separately in three classes — **expressive gain / explanatory gain / predictive gain** (they do not share a single threshold) — and is checked against definitional stability, comprehension cost and predictive gain relative to existing explanations.

Conditional-derivation index: in the main text, III-1 of §4.1 establishes the effect of a change in performance probability on project net present value with other terms fixed; IV-1 of §5.3 establishes the unique static equilibrium under strict dominance in a finite two-action game. Neither substitutes for the validation of social bridging, empirical identification or learning dynamics.

## II. Index of the 19 Active SP-RFC Entries

For the per-item P/O, additional conditions, dilemma, counterfactual and evidence status, see the [Whitepaper Generation and Evidence Cards](whitepaper/appendix.md#rfc-evidence-cards). Necessity, sufficiency and minimality are tested separately; a counterfactual failure does not by itself establish sufficiency or uniqueness, and a normative objective requires a separate statement of reasons. Empirical validation that has not been completed continues to be marked as such, and is not replaced by passing the automated checks or by filling in a card.

> **[Architectural-tier note]**: 19 consecutive numbers 001—019; 007 is the cross-group normative rule, 003 is a semantic application, and 019 is the Chapter 8 tooling/research norm. The former 006/010 are retained as non-numbered materials; the 19 items are not called proven corollaries.

### 1. Proposition Group I: Channel Capacity & Semantic Boundary — Clauses and Application Index
* **[citation of established physical results, conditional model and social bridging] SP-RFC-001 [Physical Channel and Semantic Decoding]**: the $I_{\text{phys}}=B_{\text{Hz}}\log_2(1+P_S/P_N)$ of a given Gaussian physical channel is kept separate from the candidate social model $C\le kI$. The latter must define the task, units and identification conditions; semantic padding can increase decoding cost but can also provide error correction or shared context, and a collapse of coordination to zero does not follow from the amount of rhetoric. "Theorem" is a naming label used by this book and does not mean that social bridging has received a mathematical proof.
    * **[Candidate model 2.1-1: the trade-off between transmission and decoding time]**: with the encoded amount I fixed, compression rate r>0 and symbol rate B>0, an average decoding latency d>0 is measured independently; a non-overlapping serial model gives the payload throughput $\Phi=rB/(1+Bd)$, counting only transmission and decoding; the encoding / prior-learning cost and the accuracy rate are reported separately and are not equal to a measured successfully delivered goodput. For small B compare r, for large B compare r/d; one cannot judge a winner from the "classical / vernacular" label alone, and the bridging of d to genre, task and audience is tested separately.
* **[empirical mechanism hypothesis] SP-RFC-002 [Naming and Common Identification]**: naming structures dispersed experience into a system-level concept that can be disputed and cited, and may lower cross-agent identification and coordination cost; the gain must be tested by comparison. The feasibility of judicial scheduling and remedy still depends on existing sources of law and procedural evolution. First distinguish the overall effect of naming and compression from the independent effect of naming, then control for or factor out length, content, familiarity and training; for the candidate comparison protocol see the main text §2.2, G002 and §8.5.1; no separate set of definitions is set up.
* **[semantic propagation application] SP-RFC-003 [Textual Stability and Cross-Context Interpretation]**: a source-code hash can verify byte changes but cannot ensure consistency of interpretation; the same source code can be ported across platforms. It is distinguishable from the task of 002 (002 concerns symbol-recognition coordination, 003 concerns consistency of interpretation across audiences), but no general impossibility triangle has been established; tests are implemented through input/output/falsifiable protocols. The main index is Group I, related to Group V; it is not a direct corollary of 001/002/016. Local tests split into H003-V version identification and H003-I interpretation mechanism; the main indicators and the overall success / multiple-comparison rules are registered in advance; rejecting a predetermined improvement does not amount to overturning the byte/semantic property boundary.

### 2. Proposition Group II: Intermediary Parasitism & Compatibility Decay — Models, Patterns and the Normative Rule
* **[conditional model] SP-RFC-004 [Conditional Retention Rate of Serial Compatibility Layers]**: for a serial arrangement with no added output/recovery path, the conditional retention rate is $\eta_n=\prod_i(1-\lambda_i)$; $\lambda_i$ is defined relative to that layer's own input, and multiplying the per-layer conditional ratios does not require statistical independence, which distinguishes it from 018's independent success/failure model. Equal loss rates give a geometric form, and a uniform positive lower bound gives an exponential upper bound. Positive loss or the number of layers alone does not entail collapse; the productive benefit of an intermediary must be compared and accounted.
* **[conditional mechanism hypothesis] SP-RFC-005 [Normative Complexity and Intermediary Rent-Seeking Feedback]**: within a pre-defined period of protocol operation, when exclusive access/interpretive authority exists, non-productive net payoff dominates, and effective competition, exit and independent error correction are insufficient, test the complexity—rent-seeking feedback; net burden, rent and task failure are measured separately. The institutionalisation scenario is retained only when the same conditions are met; not every bureaucratised gain is folded into 005.
* **[conditional judgment and application comparison] SP-RFC-006 [Approval Latency, Mission Deadline, and Protection Benefit]**: for a specified task, if approval latency exceeds the task TTL, a timeout may occur; four consequences must be distinguished — delay on the original path, availability of a low-cost bypass, local task failure, and system-governance failure. Careful review is not equivalent to rent-seeking, and removing approval does not by itself increase net benefit. Whether overall legitimate throughput falls and whether malicious behaviour is suppressed must each be measured separately; a local bypass capability cannot be written up as comprehensive zero defence; drone rules provide for classified approval, application-free and long-term licences. Even where the original rule has a protection benefit, an alternative that meets the same protection and rights requirements at lower full cost can still be compared; the absence of a protection benefit is not a necessary condition for improvement.
* **[cross-group normative rule] SP-RFC-007 [Architect's Understandability, Rights, and Migration Precepts]**: the following recommendations take lower unnecessary coordination cost, the protection of lawful rights and the retention of error-correction capability as their design objectives; they are not universal commands derived automatically from descriptive regularities, and costs, alternatives and remedy arrangements must be compared.
    1. **Precept of plain language**: provide an intelligible interface and test comprehension and execution effects; retain necessary exceptions, negations and rights safeguards, and do not use syntactic complexity itself as grounds for abolition.
    2. **Precept of cutting off rent-seeking**: compare the intermediary's net contribution with feasible alternative mechanisms; open competition and bypass for non-productive monopolies, and retain independent review and third-party remedy.
    3. **Precept of decisive refactoring**: after risks and migration costs have been verified, incubate an alternative protocol in an independent userland sandbox; production migration follows Strangler Fig incremental traffic splitting and a reversible boundary.

Non-numbered research material: the [candidate process diagram](whitepaper/chapter-03.md#research-process-pattern) raises longitudinal comparison questions of exploration, diffusion, enclosure and refactoring; it has not established an obligatory order or frequency.

### 3. Proposition Group III: Intertemporal Finality & Expectation Credibility — Clauses and Application Index
* **[conditional model and empirical bridging] SP-RFC-008 [Performance Probability, Recovery, and Investment Threshold]**: project net present value depends on performance probability, breach recovery, cash-flow timing and discounting. With other conditions equal and performance return above breach recovery, a fall in performance probability lowers net present value; only crossing the threshold causes exit from the investment. The variance of rule lifetime cannot on its own determine CAPEX, and pension or marriage/fertility behaviour requires a separately established mechanism.
* **[property definition and procedural boundary] SP-RFC-009 [Retry Idempotence, Record Durability, and Finality]**: repeated submission of the same request identifier should not add business effects; ACID durability, historical finality and an updatable current state are different properties. Before comparing Verify, the transaction, rule version and evidence set must be fixed; correcting an error under existing review rules is not equivalent to arbitrary rollback. US Title IX must be analysed under specific school rules, evidence and procedures; subsequently establishing that there was no valid consent at the time is not equivalent to retrospectively reversing a valid authorisation through a change of mind.
* **[execution mechanism and conditional protection] SP-RFC-010 [Deterministic Execution and Conditional Commitment]**: the same initial state and ordered inputs produce the same output; resistance to breach also depends on consensus, authority, fault thresholds, escalation and finality rules. Signatures and time locks constrain only the states and assets controlled by the protocol and cannot automatically guarantee off-chain performance or resistance to physical coercion.

Non-numbered application material: the [consumption and policy expectations note](whitepaper/chapter-04.md#application-policy-expectations) retains the external model's conditions and is not treated as a direct corollary of the investment model.

### 4. Proposition Group IV: Privilege Ring Isolation & Split-Brain Contagion — Clauses and Application Index
* **[authority model and social bridging] SP-RFC-011 [Privilege Isolation and Constraints on the Executor]**: Ring-3 is a privilege-boundary analogy; ordinary userland isolation cannot by itself constrain Ring-0. Stability of property rights also requires independent review, constraints on power, remedy and compensation; a higher risk of withdrawal may dampen investment, and does not entail that all CAPEX is permanently reduced to zero.
* **[state distinction and mechanism hypothesis] SP-RFC-012 [Resource Cutoff, Communication Partition, and Conflicting Writes]**: resource cutoff, communication partition and split-brain are distinct states. Split-brain arises only when multiple controlling parties accept conflicting decisions about the same resource; arbitration or write-stop on loss of contact can preserve safety. Local plunder requires separately established failures of incentives and constraints; a local malicious relay and cross-domain forgery of jurisdiction are analogies to Rogue Transit and BGP Hijacking respectively.
* **[conditional derivation of a finite two-action game] SP-RFC-013 [Predatory Gain, Strict Dominance, and Static Equilibrium]**: zero confiscation and positive predatory gain are not sufficient to derive the dominance of wrongdoing. Strict dominance holds only when, against all relevant opponent strategies, the net expected utility of predation exceeds that of every alternative action; group convergence and system failure still require dynamic and fault-tolerance conditions.
* **[institutional instantiation and normative boundary] SP-RFC-014 [Authorisation Interface for Specific Public Objectives]**: nationwide enforcement, public taxation or statutory education objectives require a corresponding state authorisation interface (Syscall); autonomy, contracts and technical standards can keep evolving in Ring-3. Its real-world overlap with 011 is not formal orthogonality; an implementable interface must delimit the jurisdiction, the authority subject, the statutory list of acts and the revocation-and-remedy procedure. The inclusion of Hu Shi's vernacular in a Ministry of Education directive is an institutionalisation path for a specific objective, not a uniform success criterion for all paradigms; the cost of mandatory invocation must be analysed under specific authority and remedy conditions.
* **[identification boundary and application hypothesis] SP-RFC-015 [Feasible Choice Set, Exit, and Voluntariness Identification]**: when basic subsistence or a core platform interface is exclusively monopolised, exit costs are high and feasible alternatives are artificially blocked, an observed single choice ($H(\text{Choice}) = 0$) cannot on its own serve as proof of "voluntary preference"; structural lock-in must be identified together with monopoly constraints, exit costs and the historical ledger of coerced investment (for example company-town token bundling and operating-system exclusive-bundling disputes).

### 5. Proposition Group V: Transport Topology & Task Feedback — Clauses and Application Index
* **[mechanism analogy and empirical bridging] SP-RFC-016 [Mobilisation Task, Acknowledgement Feedback, and Continuous Governance]**: TCP/UDP is used as a cognitive analogy: TCP provides a connection-oriented reliable ordered byte stream, while UDP by itself does not guarantee reliable delivery; reliability can also be provided by an upper-layer protocol over UDP, for example QUIC. Organisational resilience should test application-layer acknowledgement, responsibility tracing, feedback, resource resupply and failure-recovery mechanisms, and cannot be derived from the name of a transport protocol or the number of ACKs. "Build high walls, store grain broadly, and be slow to claim kingship" can be read as an analogy for feedback-driven gradual scaling; if one-way mobilisation never establishes the acknowledgement and coordination mechanisms required for governance, it may become more fragile after the transition to complex governance. This mechanism hypothesis must be tested against mixed organisations and counterexamples, and does not adopt the as-yet-undefined ACK_Depth ratio formula or the Load→Host limit formula.

### 6. Proposition Group VI: Debt Accounting & Evolutionary Selection — Clauses and Application Index
* **[accounting definition and option comparison] SP-RFC-017 [Migration Net Burden and Technical-Debt Accounting]**: after unifying the boundary, time window and discounting basis, compare the net present value of the old system's burden, the new system's maintenance, migration and the loss of hidden assets; the change in net burden may be positive or negative. There is no free refactoring, nor is there a conclusion that total technical debt is necessarily conserved. Retain the survivor Catch-Block fault-tolerance library and verify migration gain and reversibility with an incremental bypass (Strangler Fig). Analysis paralysis and rewrite loss are risk hypotheses awaiting test; this book's self-restraint and migration recommendations are not deductive corollaries of the accounting formula.
* **[conditional-probability model, empirical screening, and design norm] SP-RFC-018 [Multi-Branch Trial and Mature-Feedback Screening]**: under a model in which branch successes/failures are independent and each success probability is fixed, $P_{\text{evolution}}(K)=1-\prod_{k=1}^K(1-p_k)$. Approaching 1 requires additional conditions, for example $\sum_kp_k=\infty$; a finite budget requires $\sum_{k=1}^{K}\text{Cost}_k + C_{\text{merge}}(K)\le\text{Budget}$ (explicitly including the merge-coordination cost $C_{\text{merge}}(K)$); only when all branches have equal cost does it simplify to $K\cdot\text{Cost}_{\text{fork}}\le\text{Budget}$ (ignoring merge-coordination overhead), and common failure modes weaken the gain from adding branches. Under a single-window screening design the feedback period generally requires $T_{\text{latency}}\le\Delta t_{\text{feedback}}<T_{\text{environment}}$ (a constraint on specific engineering parameters, not excluding nested feedback on multiple time scales); if no such time window exists, the trial design should be adjusted, and the feedback latency cannot be mechanically driven to zero. Fitness is not presupposed to be proportional to feedback frequency. The architect, as gatekeeper of the evolutionary racecourse and Bazaar Maintainer & Merge Architect, protects real feedback, retains reversible branches and performs incremental merging. Discovery, screening, deployment and migration each discharge their evidence duties through the main text's four-stage interfaces: the independent-probability formula describes only that at least one branch succeeds; deployment follows the applicable authorisation boundary of 014, migration is accounted under 017, and budget feasibility does not guarantee net benefit.

---


### 7. Cross-Group Tooling and Research Norm (Chapter 8 Entry Point)

* **[application and research norm] SP-RFC-019 [AI Tool Control and Exploratory Early-Warning]**: this item is an application/research norm, not a deductive corollary of Group VI. Natural language can be converted via an LLM into some tool calls, but authority and execution verification are still required. Centralised model control may increase exit, audit and coordination costs; open source, on-device and interoperability are options awaiting comparison. Socio-Radar's four proxy inputs and composite score are an uncalibrated research norm only; a threshold only triggers review and does not automatically authorise a real-world circuit break.

---

## III. The L0-L5 Socio-Protocol Stack Architecture Model

In this section L0–L5 denotes the system functional stack; it is not equal to the writing layers L1/L2 (and the future L3), nor to the theoretical Levels 0/1/2 of postulates → proposition groups → RFCs. Ring-0/3 denotes a privilege-boundary analogy.

| Protocol layer | Tasks and objects |
| :--- | :--- |
| 5. User application layer (Userland / Ring-3) | Civil commercial contracts, academic inquiry, civic literature, self-organised coordination |
| 4. System-call interface (Syscall / ABI) | Constitutional adoption, legislative interface, litigation entry, compulsory-education national standards |
| 3. Organisational kernel layer (Kernel / Ring-0) | Allocation of power, bureaucratic process scheduling, fiscal clearing, GC collection |
| 2. Transport and routing layer (Transport & Route) | TCP acknowledgement and UDP connectionless datagrams as analogies for feedback/diffusion; UDP is not equivalent to broadcast or emotionalisation, and organisational reliability is tested separately |
| 1. Language compilation and driver layer (Codec/Driver) | Character sets, a genre-grammar compiler, tax mobilisation / physical drives |
| 0. Physical hardware layer (Physical Hardware) | Human neurons, physical land, grain and equipment, physical coercive force |


---

### 3.1 Isomorphism Matrix of Four Operating Systems and Human Collaboration

The four modes are comparison dimensions; they cannot exhaust institutional types or substitute for historical causation; "native refactoring" also has migration and fault-tolerance costs.

| Mode and control | Engineering / historical comparison object | Candidate benefit | Costs and conditions to be checked |
| :--- | :--- | :--- | :--- |
| iOS / centralised cathedral | Rome and the High Tang as comparisons of privilege boundaries | Unified experience and review | Exclusive charging and compliance thresholds; inevitable rebellion is not presupposed |
| Windows / compatibility-layer maintenance | The Holy Roman Empire, the Habsburgs | Retaining existing interfaces and alliances | Maintenance, rent-seeking and failure recovery; net contribution must be compared |
| Linux / open-source norms and native development | Early constitution-making, UNIX/C | Reducing some historical coupling | Ecosystem cold start, migration and hidden fault-tolerance assets; non-zero historical baggage |
| Android / open-source base and forks | The Hundred Schools of Thought, the spread of the vernacular | Allowing forks and diverse exploration | Version fragmentation and middleware; prevalence must state the period and denominator |

---

## IV. System Deadlock Diagnostic Matrix

### 4.1 Mapping Table of Symptoms and Candidate Mechanisms

| Symptom | Candidate mechanism and verification question | Global Reference Case |
| :--- | :--- | :--- |
| **Regulations not written in plain language** | May increase comprehension and execution costs; necessary complexity must be distinguished from disclaimer padding | Verify through audience comprehension, task errors and recovery capability; do not judge the signal-to-noise ratio to be zero or the system deadlocked from writing style alone |
| **Frenzied labelling in currents of thought** | Labels may squeeze out evidence and error correction; semantic change cannot on its own identify malice or polarisation | Check diffusion, evidence exchange and concrete changes in firms; do not treat the subdivision of DEI labels directly as the cause of wholesale layoffs |
| **Cross-segment predation by public power** | Resource cutoff, conflicting writes and predatory incentives must each be verified; in-transit interception and cross-domain forgery of authority are different analogies | Historical checkpoints and privateering forces may serve as comparison leads to be checked; split-brain, route hijacking or inevitable predation cannot be diagnosed from fiscal shortage alone |
| **Disputes over social-contract trust** | Compare the authorisation at the time of the act, existing rules and subsequent evidence; distinguish review from arbitrary rollback | US Title IX must be applied to specific schools and cases; it cannot be generalised into "a later change of mind can overturn valid consent", still less directly attributed to youth social trends |
| **Common sense reversed into a charge** | Responsibility inverted between sender and receiver; institutional punishment imposed on indiscriminate physical signals | The political regulation of receiving Western broadcasts and the rectification of antennas in Cold War East Germany at different periods; the British window tax forcing citizens to brick up windows |
| **Theoretical shell as fake indigenous research** | Absence of a falsification mechanism; `sed -i` batch replacement and closed-source monopoly | Soviet Lysenkoism substituting political dogma for genetic experiments; the medieval Sorbonne's monopoly on convoluted scholastic commentary |
| **Disputes over intergenerational welfare commitments** | Changes to benefit rules may affect long-term expectations; jurisdiction, period, accrued rights and alternative safeguards must be checked | Participation and family planning are heterogeneous; universal youth non-payment or zero fertility cannot be derived directly from a policy statement, and individual data and controlled comparison are needed |
| **Monopoly bundling and choice lock-in** | Exclusive control of key factors, high exit costs suppressing feasible alternatives, inducing structural dependence | Coal-mining company-town tokens tied to exclusive services; operating systems forcibly bundling specific components; access to scarce public services tied to asset queue rights |
| **Formalist security theatre** | Whether approval latency conflicts with the task TTL should be tested by task category and logs | Drones have application-free and long-term licence paths; administrative impedance for a specific task is not equivalent to a nationwide uniform 72 hours or the sudden death of an entire industry |
| **Risk of in-place full rewrite** | Compare full-lifecycle costs with the Catch-Block assets that may be lost; collapse cannot be diagnosed from the name of a reform | The Netscape rewrite dispute and the migration risk of existing fix experience; the Wang Anshi reforms and the French Revolution serve only as multi-factor historical research leads, not as verification of the net-burden formula |
| **Branch restriction and slow feedback** | Check common failure sources, resources and the feedback window; K=1 is not automatically equivalent to failure | Hurd has development and trial systems with limited production maturity; engineering competition requires multi-factor comparison |

> ⚠️ **Uncalibrated research-indicator notice**: the indicator definitions and fixed thresholds listed in this table are **a conceptual formalisation and reference architecture, plus a future research agenda for computational sociology**. In the absence of calibration on large samples of real-world corpora and of confusion-matrix validation for false positives/negatives, they are uncalibrated exploratory indicators and **must not be used directly for deterministic collapse diagnosis of real institutions and micro-organisations**.

### 4.2 Social Seismograph: Four Proxy Inputs and One Composite Score (Socio-Radar Mathematical Matrix)

| Dimension indicator | Mathematical definition | Uncalibrated illustrative threshold | Scope of interpretation |
| :--- | :--- | :--- | :--- |
| **Semantic Drift Index<br>(SDI)** | $\text{SDI}(w)=\frac12\left(1-\frac{\vec v_w(t_0)\cdot\vec v_w(t)}{\|\vec v_w(t_0)\|\|\vec v_w(t)\|}\right)\in[0,1]$<br>$a_{\text{drift}}=\Delta^2\text{SDI}/\Delta t^2$ | Illustrative threshold: $a_{\text{drift}}>\theta\land\text{SDI}>0.40$; not yet calibrated | The per-word list and the global partition are kept separate; θ=0.25, the sampling interval defaults to one fixed unit, and only a ratio strictly >0.15 raises a word-list signal to the global red zone (uncalibrated, not a multiple-testing correction); a local hit does not by itself change the global colour; word_reviews is passed explicitly and duplicates are rejected, and the warm-start acceleration is None; the indicator cannot be used to judge malice, illegality or collapse. |
| **Rhetorical Padding Ratio<br>(PBR)** | $\text{PBR}=1-\text{TokenCount}(\text{Prune}(D,\mathcal L_{padding}))/\text{TokenCount}(D)$<br>$\text{PNR}=\frac{1-\text{PBR}}{\text{PBR}+\epsilon}\cdot H_{\text{norm}}$ | Illustrative thresholds: $\text{PBR}>0.65\land\text{PNR}<0.20$; $\text{PBR}>0.85$; not yet calibrated | ε=10⁻⁶ is used only for PNR; PNR is not normalised, its range is [0,1/ε], and its current upper bound is 10⁶; at PBR=0 it still depends on entropy. Fix the tokenizer and its version, the word list and the pruning configuration; count the retained subsequence directly and do not re-tokenize; input is non-empty and only deletions, no additions, are made. A word-list hit is not equivalent to zero meaning, and comprehension and execution costs must be verified independently. |
| **System-Call Impedance<br>(SIR)** | $\text{SIR}=\alpha\bar d_{\text{norm}}+(1-\alpha)R_{\text{drop}}\in[0,1]$; baseline $\alpha=0.50$; distance normalisation consistent with SSOT §8.3.3 / §8.4 | Illustrative threshold: $\text{SIR}>\theta_{\text{impedance}}$; not yet calibrated | A composite indicator of semantic distance and actual rejection; the sampling and denominator must be disclosed, and it is not automatically equivalent to institutional failure. |
| **Middleman Polarisation Measure<br>(MPM)** | $\text{MPM} = \frac{\sum_{\text{gate}} C_B(v)}{\sum C_B(u)} \cdot (1 - \frac{B_{\text{TCP}}}{B_{\text{Total}}})$ | $\text{MPM}>0.70$ is an illustrative review line only | The reference code only consumes an external MPM; the graph and betweenness/traffic encoding have not yet been implemented; the source of the measurement artefact must be attached. An exploratory structural indicator given a topology graph and a traffic proxy; the TCP/UDP subscripts denote traceable-feedback / unseen-feedback samples encoded under the same window, and missing classifications report coverage separately; MPM > 0.70 only triggers review and does not determine the truth of content, subjective manipulation or group polarisation |
| **System Health Index<br>(SHI)** | with the mean of per-word SDI $\overline{SDI}$ and PBR/SIR/MPM as four inputs, $SHI=\sigma(\omega_0-k\mathcal R)$; $k=5.0,\omega_0=2.50$ are illustrative parameters | Illustrative score paths: $\ge0.75$, $[0.45,0.75)$, $<0.45$; for the full conditions and the red-priority rule see the SSOT §8.3.5 overview; uncalibrated | A composite score of the four proxy inputs, not a fifth independent observation; direct conditions can still override the score path. The red zone is not equivalent to real-world collapse, and the green zone is not a health certification. |

### 4.3 Candidate Empirical Measurement Protocol and Quantitative Operators (The Operationalization Protocol & Operators)

*   **Rhetorical noise and effective-information ratio (PBR & SNR/PNR)**:
    $V(D)$ is the set of distinct tokens actually appearing in the original text after fixed tokenization and before pruning; $P(w)$ is its relative frequency in the original text, and the entropy denominator uses $\log_2|V(D)|$, not the size of an external total word list. The entropy of a single token type is recorded as 0, and an empty document is recorded as missing. PBR/PNR use the two-tuple returned by the same document under the same configuration; external imports must be recomputed or independently checked, and a legal scalar range is not equivalent to a verified pairing or source.

    $$
    \text{PBR}(D) = 1 - \frac{\text{TokenCount}(\text{Prune}(D,\mathcal L_{padding}))}{\text{TokenCount}(D)}, \quad \text{PNR}(D) = \frac{1 - \text{PBR}(D)}{\text{PBR}(D) + \epsilon} \cdot H_{\text{norm}}(D)
    $$

    TokenCount is synonymous with SSOT §8.3.2: tokenize the original text once, and after pruning count the retained tokens directly. The unweighted simple form without entropy $SNR=\text{TokenCount}(\text{Prune}(D,\mathcal L_{padding}))/(\text{TokenCount}(D)-\text{TokenCount}(\text{Prune}(D,\mathcal L_{padding})))$ does not report a finite value when the denominator is zero; an empty document counts as missing data. SNR is a text-length proxy, while PNR additionally contains an entropy weight and a stability term; the two are different, and neither is equal to a physical signal-to-noise ratio. Save the original PNR value and ε and run a sensitivity analysis for near-zero padding; logarithm, truncation and scaling are separately named research candidate variables, are not uniformly enforced, and do not directly replace the engine's raw input or carry over the original thresholds. $PBR>0.65$ and $PNR<0.20$ are one of the yellow-zone conditions, and $PBR>0.85$ is a direct red-zone trigger; both are uncalibrated illustrative thresholds, and real-world channel deafness is not judged from them.
*   **Language-bus perplexity–length proxy experiment (Exploratory Perplexity-Length Benchmark)**:

    $$
    \text{Impedance\_Ratio} = \frac{\sum \text{PPL}(\text{Classical}) \times \text{Tokens}(\text{Classical})}{\sum \text{PPL}(\text{Vernacular}) \times \text{Tokens}(\text{Vernacular})}
    $$

    An exploratory benchmark experiment design awaiting execution: compare the perplexity × Token-length product of Li Shanlan's classical-Chinese translation with that of vernacular textbooks; this product is not equal to total cross-entropy or human comprehension cost, and cross-genre comparison must control for propositional equivalence and undergo independent behavioural testing (it is not treated as a measured conclusion until a complete measurement record has been provided).
*   **Hierarchical adjacent-drift summary and end-to-end independent validation (Hierarchical Drift & End-to-End Validation)**:

    $$
    d_i=1-\cos(\mathbf v(T_{i-1}),\mathbf v(T_i)),\quad p_{local}=\prod_i(1-d_i).
    $$

    This signed similarity product is not a traffic retention rate. If independent traffic measurement gives a loss of 0.32 at each of four layers, only the serial no-recovery model gives $0.68^4\approx21.4\%$. Semantic distance cannot be treated directly as traffic loss; the start/end semantics and the actual task outcome must be tested independently.
*   **Carbon-Silicon Ontological Boundary Principle (Carbon-Silicon Ontological Principle)**:
    Human nodes are adaptive game-playing Agents with private objective functions; whether equilibrium, dynamic convergence or deadlock occurs requires incentive, update and resource models to be given separately, and cannot be derived directly from "rationality" and "malicious calls".

---

## V. Typical Call Stack Tracebacks

### 5.1 Idempotence Failure Example of Duplicate Charging for the Same Request (Traceback: Duplicate Request)
The following call stack is a fictional teaching example (illustrative output, not an executable program); it tests the extra effects caused by repeated execution of the same request identifier and does not refer to any specific judicial system or determination of sexual consent.
```text
# Traceback (illustrative, not executable):
# request_id = "payment-001"; immutable_rule_version = "v1"
# retry_same_request(request_id)
#   deduplication_store.find(request_id) -> unavailable
#   charge_again(request_id) -> DuplicateEffectError
# Review: verify transaction identity, rule version, evidence and appeal path.
# A correction under an existing review rule is not arbitrary historical rollback.
```

### 5.2 Candidate Failure Branch after Fiscal Stress (Illustrative Routing Branch)
The following is a fictional teaching branch (illustrative output, not an executable program); fiscal exhaustion, heartbeat loss, conflicting authorisation and malicious hijacking are distinct events that must be identified separately and are not an automatically occurring exception chain.
```text
# Traceback (most recent call last):
  File "civilization/kernel/fiscal_dispatcher.py", line 1024, in transfer_payment_heartbeat
    send_gas_subsidy(region_node)
  File "network/topology/inter_provincial_bus.py", line 55, in send_gas_subsidy
    raise FiscalExhaustionTimeout("Treasury balance depleted; heartbeat ACK missing")

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "network/edge/provincial_police_gateway.py", line 77, in on_heartbeat_lost
    enable_autonomous_revenue_mode(target=ForeignNetworkTraffic)
  File "network/routing/bgp_daemon.py", line 194, in enable_autonomous_revenue_mode
    raise BGPRouteHijackError("[SP-RFC-012] Hypothetical cross-domain actor forges a jurisdiction prefix")
# Contagion Alert: [SP-RFC-013] Central punishment = 0; Propagation depends on relative payoffs, learning and enforcement; not all nodes must convert.
```

### 5.3 Fictional Call Stack for Intergenerational Commitment Adjustment (Illustrative Pension Commitment Branch)
The following call stack only illustrates one hypothetical rule change (illustrative output, not an executable program) and does not serve as a factual determination about any specific policy or individual's behaviour.
```text
# Traceback (most recent call last):
  File "civilization/welfare/pension_pool.py", line 40, in payout_retirement_benefit
    verify_staking_proof(citizen_id, duration_years=40)
  File "civilization/protocol/time_lock_sla.py", line 128, in verify_staking_proof
    return treasury_pool.execute_settlement(citizen_id, required=REQUIRED_PAYOUT)
  File "government/provincial/civil_affairs_patch.py", line 2026, in execute_settlement
    raise SovereignRugPullException("State offloads SLA: 'Individual is the primary responsible party for eldercare'")
# SovereignRugPullException: [SP-RFC-008] Unilateral protocol downgrade detected;
# Root CA revoked: 40-year multi-generational time-lock breached by authority.
# Illustrative branch only: participation and family plans depend on benefits, exit costs and preferences; no universal Nash or zero-birth conclusion.
```

---

Research output should preferentially use `evaluate_research_flags` and `research_score` / `research_zone`; the old health naming is kept for compatibility only. A snapshot carries the reference version, the declared model/measurement configuration and the input source; missing metadata are listed separately, and `provenance_verified=False` does not automatically verify the source; it is always `uncalibrated` and `research_only=True`. No computation is performed when a necessary value is missing. It is not a physical circuit break, not an automatic authorisation and not a health certification, but research review only; even a human stamp cannot substitute for an independent basis for authorisation. For the implementation stress test see the [007 cross-group verification table](whitepaper/chapter-03.md#sp-rfc-007).

## VI. Cognitive Cache and Fast-Invocation Prompts (System Prompts for AI Integration)

When this theory needs to be retrieved in a later session, the following short prompt can be used to wake the cache directly:
> *"Based on the v11.2 core framework of Socio-Protocolics (the 3 first-order postulates → the 6 Core Proposition Groups → the 19 Effective SP-RFC Items, including the 007 rule; for the former merge relations see the version comparison), analyse [a social phenomenon / historical event / institutional change] from the perspectives of the protocol stack, the compiler, memory protection, retry idempotence and finality protection; distinguish mechanism hypotheses, case explanations and conclusions already supported by evidence."*
## Appendix: Mapping of Core Figures and Ecological Niches (Key Architects & Paradigms)

| Figure / school | Era and background | Ecological niche in Socio-Protocolics | Core contribution and systems interface |
| :--- | :--- | :--- | :--- |
| **Ludwig Wittgenstein** | 1920 Continental philosophy of logic | **Pioneer of inspiration from philosophy of language** | "The limits of my language mean the limits of my world"; provides philosophical inspiration, while coordination capacity and channel computation must be modelled and verified separately |
| **Hu Shi** | 1917 New Culture Movement | **Promoter of literary norms and the ecosystem (analogous to a Compiler/Linter maintainer)** | Proposed a literary reform programme and took part in vernacular writing and educational dissemination; the "Eight Don'ts" and punctuation serve as a Linter/Lexer analogy, and are not equivalent to single-handedly setting Chinese grammar. The 1920 directive concerned vernacular writing in specific grades of national schools, a Syscall for a specific educational interface, not an immediate switch of all official documents |
| **Zhao Yuanren** | 20th-century linguistics | **A comparison case for phonetic and written disambiguation** | Homophonic texts can serve as a stress test for a specific encoding; it does not establish that the everyday vernacular cannot be spelt, does not treat Chinese characters as a collision-free hash, nor does it invent a single writing route jointly established with Hu Shi |
| **Dennis Ritchie (Ritchie)** | 1970 Bell Labs | **Founder of modern digital systems** | Created the C language and early UNIX; advanced open system-call practice and inspired the later IEEE POSIX family of standards |
| **Martin Luther** | 1517 Reformation | **Pioneer of anti-middleware open sourcing** | "The priesthood of all believers" (reorganising the authority intermediary while retaining the teaching ministry); the 1522 German New Testament and the 1534 complete Bible advanced standard German and popular literacy |
| **Huineng, the Sixth Patriarch / Shandao** | Tang-dynasty Chan / Pure Land Buddhism | **Minimal interface / lowering the barrier** | Huineng's sudden-enlightenment narrative and the later Chan summary "not relying on written words" are analogous to bypassing convoluted scholastic commentary; Shandao's name-recitation practice is analogous to a low-barrier direct call (still relying on a doctrinal context such as faith, vow and practice, not unconditional mechanical execution) |
| **Wang Yangming** | Ming-dynasty revolution in the School of Mind | **Chief architect of edge computing** | "The mind is principle; the extension of intuitive knowledge" (moral judgement responsibility devolved to the acting subject, the unity of knowing and doing; not equivalent to pre-installed empirical and natural-science knowledge) |
| **Benedict Anderson / Scott**| 1983/1998 political sociology | **The language bus and state legibility**| Anderson: print capitalism advancing the linguistic integration of the national community; Scott: the state-legibility interface and standardised governance tools |
| **Mancur Olson (Olson)** | 1982/1993 institutional economics | **Compatibility-layer hardening and the roving-bandit model** | *The Rise and Decline of Nations*: distributional coalitions piling up into institutional sclerosis (SP-RFC-004); the roving vs stationary bandit model explaining split-brain fragmentation (SP-RFC-012) |
| **Douglass North & Weingast** | 1989 new institutional economics | **Credible commitment and memory isolation** | The change over time in British public credit: some long-term borrowing at about 14% in the early 1690s, about 6%–8% by the end of that decade, and about 3% in the 1730s; it cannot be equated with a single institutional switch or growth of the whole society's capital pool |
| **Friedrich Hayek** | 20th-century Austrian School | **Dispersed knowledge and communication mechanisms** | *The Use of Knowledge in Society* analyses how price signals coordinate dispersed knowledge; it has not demonstrated minimal channel loss or universal optimality |
| **Zeynep Tufekci (Tufekci)** | 2017 political sociology | **Network mobilisation and tactical freezing** | Discusses the organisational capacity and strategy-adjustment dilemmas of some networked movements; TCP/UDP is this book's mechanism analogy and does not entail that entering governance necessarily causes instant implosion |
| **Acemoglu / Johnson / Robinson** | 2024 Nobel Prize in Economics | **Macro-architects of institutions** | Inclusive vs extractive institutions; *Power and Progress* sets elite monopoly over technical protocols against broad-based distribution |
| **Mokyr / Aghion / Howitt** | 2025 Nobel Prize in Economics | **Open-source knowledge and frontier disruption** | Mokyr: useful knowledge and mechanisms of knowledge exchange, which this book takes as an open-source knowledge bus analogy; Aghion/Howitt: creative destruction and related growth models; near the technological frontier, innovation incentives and knowledge-dissemination constraints may change and must be compared in a specific model, and inevitably hitting a wall cannot be derived from the "closed-source" label |
| **Hall (Hall) & Woodford** | 2026 Nobel Prize in Economics | **Intertemporal consumption and policy expectations** | Hall (1978) derives, under model conditions, the random walk of the marginal utility of consumption; expectation management and commitment are one of the policy transmission mechanisms, and this does not mean that temporary subsidies are absolutely ineffective or that any easing necessarily fails |
| **Geoffrey Bowker & Susan Leigh Star (Bowker & Star)** | 1999 Science and Technology Studies (STS) | **Classification politics and underlying information infrastructure** | *Sorting Things Out* demonstrates that every standardised system of classification and naming is accompanied by invisible work, elevating certain group perspectives while marginalising others; mapped to Group I **SP-RFC-002 (Naming Conventions and Inter-Subject Common Identification)**, constraining the theory from treating unified naming as a default neutral cost-reduction tool |
| **Laura DeNardis (Laura DeNardis)** | 2009 Internet governance and international politics | **Internet protocol politics and standard battles** | *Protocol Politics* takes IPv4 exhaustion and IPv6 migration inertia as cases to argue that "protocol is politics", revealing power and rent-seeking contests in standards-setting; mapped to the meta-layer lens and Group VI **SP-RFC-017 (Technical Debt Accounting and Net Dual-Track Migration Burden)**, providing an empirical baseline for migration impasses |
| **Alexander Galloway & Eugene Thacker (Galloway & Thacker) / Deleuze** | 2004/2007 media and critical software studies | **Diagrams of decentralized network control** | Deleuze (1990) proposed "societies of control"; Galloway et al. formalized TCP/IP, DNS and RFC specifications as control diagrams under decentralized networks; this book inherits this lineage of "protocol as a social lens", with its incremental contribution lying in advancing to formal axioms (O1–O5 primitives, 3 postulates, 19 clauses) and cross-epoch historical institutional analysis |

---


Numbering follows v11.2; the [old–new numbering and chapter correspondence](V11_2_NUMBERING.md) retains a traceability entry point for old citations.
