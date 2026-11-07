> **Translation record**
> - Chinese source: `社会系统协议学白皮书.md`, block `chapter-01` — 297 lines, 46337 bytes, block sha256 `6047b34b79fbfe10cc97d61cf67c0fe1b299d5ed5a64ce8927ba078b75a7959d`, taken as the content between the `<!-- SP:BEGIN chapter-01 -->` and `<!-- SP:END chapter-01 -->` markers and reported by `tools/whitepaper_blocks.py list`; whole-file sha256 `d5ffb73e3db73f8bb42a2ecb39871bf6c55eace8bb72111b63a2ee362134d9c8`, 338639 bytes, 2026-11-07
> - Chinese version / release tag: `v11.2-r20261106` (theoretical version remains v11.2)
> - Translation version: `en-v0.1-ch01`
> - Translation date: 2026-11-07
> - Check status: checked sentence by sentence against the Chinese source for claim status, negative guardrails, numbering and symbol scope; machine and glossary checks only; no independent professional native-speaker review
> - Pending sync: none at present; to be recorded item by item if the Chinese source is updated
> - Status: complete translation of this chapter block (chapter 1 contains 0 case-annotation sections, so nothing inside the block is omitted)
> - Authority: the Chinese SSOT is authoritative; this translation does not constitute a separate set of definitions (C2)

**Scope and edition status.** This file is one block of a **phased** translation. The English edition as a whole is an *abridged adaptation* of the v11.2 whitepaper: the six chapters that carry case-annotation sections are not yet translated, and those annotations remain untranslated by design until the underlying Chinese case materials pass the real-case acceptance stage (T3). Chapter 1 carries no case annotations, so nothing is dropped here; completeness of this block does not imply completeness of the edition, and this translation does not elevate any claim to established status. The block itself runs from the `<!-- SP:BEGIN chapter-01 -->` marker to the `<!-- SP:END chapter-01 -->` marker; the translation record, the chapter glossary and the two notes below precede that boundary and are not part of the translated text.

## Chapter Glossary — Chapter 1

| Chinese | English used in this file | Remark |
| :--- | :--- | :--- |
| 白话文运动宣言 | the Vernacular Manifesto | heading term, source-provided |
| 三层递进架构 | three-tier progressive architecture | L1 / L2 / L3, a writing coordinate |
| 胡适悖论 | the Hu Shi Paradox | source-provided |
| 局部结构对应 | structural correspondence | source-provided |
| 机械还原论 | mechanical reductionism | source-provided |
| 硬件—协议纠缠 | hardware–protocol entanglement | source-provided |
| 自顶向下铭刻 | top-down inscription | source-provided |
| 自底向上利用 | bottom-up exploitation | source-provided |
| 基石原语 | primitive objects | O1–O5 |
| 第一性公设 | first-order postulates | P1–P3 |
| 核心命题组 | core proposition groups | groups I–VI |
| 认识论地位 | epistemic status | column heading in §1.5.4 |
| 可证伪判据 | falsification criteria | column heading in §1.5.4 |
| 新增可区分预测 | novel discriminating predictions | column heading in §1.5.4 |
| 生成与证据合同 | generation and evidence contract | §1.5.4 closing paragraph |
| 中介寄生 | intermediary parasitism | group II |
| 兼容层衰减 | compatibility-layer decay | group II |
| 特权环 | privilege ring | group IV |
| 脑裂 | split-brain | group IV |
| 技术债核算 | technical-debt accounting | group VI |
| 演化筛选 | evolutionary selection | group VI |
| 元编译器 | meta-compiler | §1.6 |
| 功能栈 | functional stack | §1.7, L0–L5 |
| 最小性 | minimality | §1.5.4, necessity / sufficiency / minimality |
| 规范守则 | normative rule | 007; "precept" where the source says 戒 |

**Note on claim identities.** In this translation, the five labels used in §1.5 to say what the members of the six groups consist of — citation of established physical results, conditional proposition derivable given assumptions, mechanism hypothesis awaiting test, accounting definition, and normative recommendation — are rendered at the granularity of the source sentence, as an in-text coarse grouping rather than as a taxonomy of claim identities. They do not include `postulate` (the postulates stand separately in §1.5.2), and citation of an established physical result names a relation of citation rather than a claim identity. The five claim identities used consistently throughout this translation are `postulate`, `conditional proposition`, `mechanism hypothesis`, `accounting definition` and `normative objective`; other labels appearing in the group matrix and in the appendix index are descriptive phrases at a finer grain of description, and this translation does not treat them as further claim identities.

**Convention on 公理 / 公理化.** The Chinese source uses 公理 in several places, and the English keeps *axiomatic* / *axioms* wherever it occurs — for example the §1.5 heading (公理体系, rendered "Axiomatic System"), the description of the earlier approach as moving "towards axiomatic organisation" (§1.5.3), the record that postulates were once "conflated with axioms", and the boxed title 公理化金字塔 (rendered "Axiomatic Pyramid"; the source names the same object "Three-Tier Orthogonal Pyramid" in the body text of §1.5.3). These occurrences report the source's own naming and a conflation it rejects. They do not reclassify the 3 First-Order Postulates as axioms, and this translation's own rule against flattening claim identities applies to the five labels set out above, not to this vocabulary, and it is recorded under the term ledger. The word *theorem* is different: it appears only inside negations ("not six proven master theorems"), and is never used to name a member of the six groups.

---

<!-- SP:BEGIN chapter-01 -->
<a id="chapter-1"></a>

# Chapter 1: Research Positioning, Objects, Postulates, and the Boundaries of the Six Proposition Groups

<a id="-00-白话文运动宣言破解胡适悖论与三层架构路线the-vernacular-manifesto--the-three-tier-architecture"></a>
<a id="legacy-v11-1-sec-1-1"></a>
<a id="sec-1-1"></a>

### 1.1 The Vernacular Manifesto: Resolving the "Hu Shi Paradox" and the Three-Tier Architecture

【Epistemological Positioning】
In the evolutionary history of intellectual systems there is a recurrent tension — **the Hu Shi Paradox**:

> **The Hu Shi Paradox**: on the testimony of the participants in the Vernacular Movement themselves, the aim of Hu Shi and the New Culture Movement was not to produce a more abstruse classical scholarship but to **lower the compilation threshold** — to degrade the cultural interpretive authority previously concentrated among a small number of examination-degree literati into a vernacular bus that ordinary people could also read and use. Hu Shi himself attributed the failure of classical Chinese to the spread of education (an expanded literate population made classical Chinese educationally untenable; see "The Meaning of the New Thought", 1919). What this book records is that **participant claim and movement objective**; whether the vernacular **actually** dispersed interpretive authority (changes in literacy rates and in the distribution of interpretive authority) is **a historical effect still awaiting test**, and this book does not substitute a narrative label for that test.
> Yet many theories, immensely penetrating at birth, subsequently re-wrap themselves in labyrinthine jargon in pursuit of a scholarly "purity and rigour", and regress into a "classical Chinese" that the general public can no longer decode.

**If *Socio-Protocolics*, to gratify the formalist fastidiousness of a few theoreticians, stripped out all the vital computer-engineering language and rewrote itself as a mathematical scripture legible only to doctoral students in game theory, then from its very first day this work would have departed from the cross-group engineering rule it sets for itself — `SP-RFC-007` (the "plain-language rule").**

Why does this book insist on "operating systems, TCP/UDP, kernel and user space, compilers, garbage collection" as its backbone vocabulary?

Because in an age when digitalisation and large models are reshaping everything:

1. **Engineering thinking is a high-compression translator for understanding civilisational coordination**: computing systems such as Linux and the Internet supply **industrial-grade reference implementations** of privilege isolation, reliable transmission, failure recovery and incremental migration. On that basis the book proposes, as its unified modelling programme, the "unified meta-compiler for computing systems engineering": compiling cross-disciplinary mechanisms into comparable interfaces and state models. The operating experience of industrial systems is not a structure-preserving proof for social systems; cross-domain application must still specify agents, objectives, resources and threat models, and must test its predictive gain against existing explanations.
2. **Computer terminology is a candidate cognitive compression tool for contemporary readers**: many people are familiar with experiences such as "lag, crash, bandwidth, packet loss, cheat plug-ins, permission prompts". The book uses these to explain coordination mechanisms; whether this is easier to understand and more accurate than existing social-science formulations still has to be tested through comprehension and transfer tasks with target readers.

The book therefore establishes a **"single body, twin tracks, three-tier progressive architecture"**, refusing to split into two versions that cannot talk to each other, and instead achieving throughout an organic unity of academic rigour and public communication:

- **L1 the dissemination tier (geek vernacular / The Vernacular)**: uses TCP/UDP, kernel, syscall, compiler and GC as cognitive lenses, raises mechanism questions from historical cases, and explains to non-specialist readers; readability and actual decision value must be tested separately;
- **L2 the theoretical tier (multi-agent object model / The Theoretical Spec)**: takes Agent, Protocol, Expectation, Middleware and Resource as primitive objects, and the three orthogonal first-order postulates (finite physical impedance, agent autonomy, expectation induction) as its modelling starting point; it organises the six core proposition groups together with the conditional models, mechanism hypotheses, fault diagnosis and normative engineering precepts of the 19 effective SP-RFC items. Each item carries its own additional assumptions, derivation and testing duties; the academic load-bearing wall is built by discharging those duties item by item.
- **L3 the measurement tier (dynamic simulation and micro-econometrics / The Future Mathematical Layer)**: in future, as AI-agent societies spread, it is to be parameterised further through numerical simulation and multi-agent games.

**Note on coordinate systems**: L1/L2 are the twin tracks of writing and argument; L3 is a future direction for measurement research; Level 0/1/2 of §1.5 organise the postulates, the proposition groups and the RFCs respectively; and the L0–L5 of Chapter 1 stratifies by system function. **The three coordinate systems do not map onto one another by number**; Ring-0/3 in the functional stack is in turn an analogy for a privilege boundary, not a theoretical tier.


<a id="sec-01"></a>
<a id="legacy-v11-1-sec-1-2"></a>
<a id="sec-1-2"></a>

### 1.2 The Limits of Common Simplifying Narratives and This Book's Engineering Entry Point

This book responds chiefly to the following three common simplifying narratives; they do not represent the whole of historical, political-science or sociological research:

- **Heroic historiography and moral dualism**: attributing historical turning points solely to the moral sanctity or corruption of individual leaders, while ignoring organisational, resource and institutional conditions;
- **Mechanical determinism and historical fatalism**: substituting slogans such as "the productive forces determine the relations of production" or "historical inevitability" for concrete mechanisms, and skipping the testable explanation of the information, incentive and execution links;
- **Cultural-label explanation**: reducing civilisational differences to fixed "cultural genes and national character", renaming the outcome that needs explaining, and supplying no comparable mechanism of action.

This book attempts to supplement these with a cross-domain interface vocabulary describing "how information is encoded, compiled, routed, filtered, executed and fed back within a network of agents". Institutional economics, organisation theory and communication research have already discussed transaction costs, dispersed knowledge, power and communication; the specific inheritance and differences are set out in §1.6. Whether engineering terminology can deliver incremental explanatory power still has to be compared against those existing explanations.


<a id="-02-计算系统同构假说the-socio-computing-isomorphism-hypothesis"></a>
<a id="legacy-v11-1-sec-1-3"></a>
<a id="sec-1-3"></a>

### 1.3 The Socio-Computing Isomorphism Hypothesis

**Core proposition**:
This book advances the following **hypothesis awaiting test**: in specified large-scale coordination settings, state confirmation, privilege boundaries, feedback latency and commitment mechanisms may bear a comparable **structural correspondence** to computer systems engineering, distributed network protocol stacks and compiler architecture. Objects must be defined case by case, structure-preserving mappings established and boundaries of applicability tested; the hypothesis does not presuppose that every social transition satisfies it.

Human law, ethics, organisations and state power can be modelled for coordination by drawing on a "language and communication protocol substrate". Signal-to-noise ratio, bandwidth, latency, abstraction level and driver interface are candidate explanatory variables; their influence on the complexity of social coordination must be defined and calibrated independently, and compared against rival explanations grounded in resources, education and institutions.


<a id="-03-碳硅本体边界与内生博弈层the-carbon-silicon-ontological-boundary"></a>
<a id="legacy-v11-1-sec-1-4"></a>
<a id="sec-1-4"></a>

### 1.4 The Carbon–Silicon Ontological Boundary and the Endogenous Game Layer

【Methodological boundary statement】
(Note: this statement belongs to research methodology and the delimitation of explanatory scope; it adds no system postulate and does not independently serve as a premise for theoretical derivation.)
This protocolics sharply distinguishes "structural correspondence" from "mechanical reductionism". Human social systems and computing systems may be given structural mappings in state confirmation, privilege control and the dynamics of protocol evolution, subject to case-by-case verification; but they differ non-negligibly in the ontological character of the physical executing subject:

1. **The hardware execution layer and the acting-subject layer must be distinguished**: logic gates perform state transitions under a specified hardware model and have no private objective in the sense of O1; this does not mean that hardware never fails or is never affected by load. An autonomous AI running on silicon hardware can also serve as an Agent, so "carbon/silicon" is the explanatory entry point of this section and cannot replace the modelling criterion of whether an entity has objectives and strategic choice;
2. **Two-way entanglement and the endogenous game in carbon-based systems (hardware–protocol entanglement)**:
   Physical computing nodes (persons) in a social network are "**adaptive game-playing agents with local private objective functions, incomplete information and bounded rationality**":
   - **Code reshaping hardware (top-down inscription)**: protocol code (law, morality, religious doctrine, ideology) may, through long-run runtime invocation, alter people's learning, beliefs and behavioural habits; the specific neural mechanisms require independent evidence and cannot be derived directly from the protocol mapping (i.e. "belief firmware pre-installation");
   - **Hardware playing back against itself (bottom-up exploitation)**: when the compatibility-layer rent-seeking or malicious system calls imposed by a protocol exceed a node's tolerance threshold, the node by no means waits passively for a circuit breaker; it may exploit a local information advantage to choose "**privately setting up middleware to collect rent**", "**strategic disengagement through slowdown (lying flat)**" and "**forging handshake receipts (formalistic deception)**".

**Key conclusion**: the systemic contraction discussed by socio-protocolics **rests on the rational game-playing and expectation adjustment of micro-level autonomous nodes**. When a central node destroys transactional finality (`SP-RFC-009`) or abuses malicious system calls, micro-level agents facing high uncertainty tend to choose defensive self-protection strategies — for example, cutting back long-horizon capital expenditure (CAPEX) or shortening contractual commitment terms — **provided that all of the following hold**: (i) judicial remedy is costly and ineffective; (ii) alternative remedies such as reputation and governance structures are unavailable; (iii) the appropriable ex-post quasi-rent created by dedicated investment is exposed to opportunistic appropriation; and (iv) the net payoff from breach and plunder is dominant. Whether this mechanism further transmits to family formation and fertility decisions is an **external empirical hypothesis requiring a separate action set and payoff matrix and independent testing**; it is not a direct corollary of this book's baseline model. The theory is a natural extension of micro-level game theory and institutional-contract analysis onto distributed communication topologies.


<a id="-04-协议学核心对象模型与公理体系layer-2-theoretical-primitive-spec"></a>
<a id="legacy-v11-1-sec-1-5"></a>
<a id="sec-1-5"></a>

### 1.5 Core Object Model and Axiomatic System of Protocolics (Layer 2: Theoretical Primitive Spec)

> **Coordinate hint**: "Layer 2" in this section's title refers to the **theoretical tier** of the twin writing-and-argument tracks (see "Note on coordinate systems" in §1.1); the Level 0/1/2 pyramid of §1.5.3 and the L0–L5 functional stack of §1.7 do not map onto each other by number.

To supply the L1 dissemination tier with explicit theoretical objects, this section establishes the 5 primitive objects, the 3 first-order postulates and the 6 core proposition groups of "multi-agent protocolics", and organises models, patterns and applications through 19 effective SP-RFC items (including the normative rule 007). This three-tier structure distinguishes postulates, conditional models, mechanism hypotheses and normative recommendations; a "core proposition group" is a **catalogue level** that organises related questions and **does not confer the same evidential identity on the items it contains**; those items comprise, respectively, citations of established physical results, conditional propositions derivable given assumptions, mechanism hypotheses awaiting test, accounting definitions and normative recommendations. Each item must state its model, quantifiers, additional conditions, derivation and counter-example boundary; historical cases and engineering mappings serve to propose and test mechanisms, and do not substitute for proof.

#### 1.5.1 The 5 Primitive Objects

**Definition and citation convention**: O1–O5 are governed by the "definition" of the numbered entries below; the object diagram is a summary. The three postulates are governed by the entries bearing SP-POSTULATE numbers in this section; the epistemic status, conditions and counter-example boundaries of the six groups are governed by the six-row matrix in this section. RFCs are governed by the corresponding normative text and its boundaries, with the appendix indexing them by number; the quick-reference card is a cache and does not establish separate definitions. Diagrams, cases and summaries must not cancel these conditions; newly discovered inconsistencies should be taken back to these entry points for revision.

```text
┌────────────────────────────────────────────────────────────────────────┐
│                The 5 Primitive Classes: Object Topology                │
├────────────────────────────────────────────────────────────────────────┤
│  [O1: Agent]                                                           │
│   ├── attributes: private objective U_i, time discount beta_i in (0,1),│
│   │   finite memory M_i                                                │
│   └── behaviour: update expectation (UpdateExpectation),               │
│       select action (SelectAction)                                     │
│                                                                        │
│  [O2: Protocol]                                                        │
│   ├── attributes: message syntax Sigma, state space S,                 │
│   │   transition rule delta, reward/penalty rule R (including Slash)   │
│   └── behaviour: broadcast rules (Broadcast),                          │
│       verify signatures (Verify)                                       │
│                                                                        │
│  [O3: Expectation & Trust]                                             │
│   ├── attributes: subjective probability mu_{i,t} over future states,  │
│   │   conditioned on the information set and the protocol              │
│   └── influence: jointly with utility, information and update rules,   │
│       shapes action; equilibrium convergence is not guaranteed         │
│                                                                        │
│  [O4: Middleware]                                                      │
│   ├── attributes: service cost, productive gain, exclusive rights,     │
│   │   and possible non-productive rent                                 │
│   └── behaviour: translation, authentication, routing, supervision,    │
│       coordination; net contribution compared with alternatives        │
│                                                                        │
│  [O5: Resource & Energy]                                               │
│   └── attributes: constraint set Omega over energy, land, physical     │
│       channels, and irreversible time                                  │
└────────────────────────────────────────────────────────────────────────┘
```

1. **O1: Agent**:
   * **Definition**: an adaptive acting unit within a system that possesses an independent objective function $U_i$, resource constraints, a time discount factor $\beta_i \in (0, 1)$, the capacity for strategic choice and locally incomplete information; the survival-and-reproduction motive of biological subjects is one source of objectives and is not a necessary attribute of firms, organisations or AI agents.
   * **Scope of instantiation**: individuals, households, firms, guilds, parties, the state apparatus, and future autonomous AI agents.
2. **O2: Protocol**:
   * **Definition**: the shared rule set coordinating multi-agent action and information transfer, $\mathcal{P}=\langle\Sigma,\mathcal{S},\delta,\mathcal{R}\rangle$, where $\Sigma$ is the message syntax, $\mathcal{S}$ the protocol state space, $\delta$ the state transition rule and $\mathcal{R}$ the reward-and-penalty rule set; "Slash" in the diagram is one penalty operation within $\mathcal{R}$. The deterministic reference model takes $\delta:\mathcal{S}\times A\to\mathcal{S}$, where $A$ is the set of legal actions defined for that instance. Stochastic transitions or strategic deviation require a separate model; a shared norm cannot stand in for actual behaviour.
   * **Instantiation requirements and scope**: natural language, codified statute, ritual taboo, monetary contract and communication protocol may all serve as objects of study; every formal instance must separately list its initial state, participant privileges, the correspondence between actions and messages, message ordering and delivery assumptions, a failure or adversarial behaviour model, and the safety and liveness conditions to be tested. Until these definitions are complete, the quadruple is used as a conceptual framework.
3. **O3: Expectation & Trust**:
   * **Definition**: the subjective probability distribution $\mu_{i,t}(A)=\Pr_i(S_{t+1}\in A\mid\mathcal I_{i,t},\mathcal P_t)$ of agent $i$ under its information set $\mathcal I_{i,t}$ and protocol $\mathcal P_t$; different agents' beliefs may differ. For an integrable function $f$, the expected value is $\mathbb E_i[f(S_{t+1})]=\int f(s)\,d\mu_{i,t}(s)$; the expected value is not treated as the distribution. Trust can serve as a protocol cache that reduces repeated verification, but the performance event trusted, the basis of verification and the conditions under which the cache expires must all be stated; not every belief is called trust, and no additional physical "confidence field" is assumed.
4. **O4: Middleware**:
   * **Definition**: a topological structure $\mathcal{M}$ located between terminal agents and performing protocol translation, authentication, routing, supervision or coordination. An intermediary may reduce search, contracting and enforcement costs, and may also extract non-productive rent by virtue of exclusive interpretive authority; its net contribution must be compared with feasible alternative mechanisms and cannot be judged directly from the existence or the number of layers.
   * **Scope of instantiation**: certification bodies, judicial and arbitration organisations, industry associations, platforms and administrative agencies. Only the subclass exhibiting exclusive control together with non-productive rent extraction falls under the rent-seeking compatibility-layer analysis developed later.
5. **O5: Resource & Physical Constraint**:
   * **Definition**: the resource feasibility domain $\Omega$ delimited by available energy, land, physical communication channel capacity and irreversible time; thermodynamic laws constrain resource conversion, and the laws themselves are not treated as disposable resources. Resource constraints bound feasible strategies and carrying capacity; the consequences of overload also depend on scheduling, degradation and recovery mechanisms, and total system deadlock cannot be derived from finiteness alone.

#### 1.5.2 The 3 First-Order Postulates

This book takes the following **three first-order postulates** as its modelling starting point. "Orthogonal" denotes a **division of responsibilities** among finite constraints, agent action and belief mechanisms; it does not mean that the postulates have been shown to be formally independent of one another or self-evidently true. Concrete mechanisms beyond the postulates still require scenario assumptions; the duties of proof or testing for conditional propositions, mechanism hypotheses and normative rules are stated separately.

**Identity and failure conditions of the postulates**: P1–P3 are **modelling conventions and constitutive starting points** of this book, not proven physical laws, and not definitional identities that the book can self-certify; at the same time they are not insulated from experience — the energy, time and channel constraints embedded in P1 are subject to physical testing, and the agent agency of P2 and the expectation–incentive transmission of P3 are empirically examinable mechanism assumptions, whose empirical consequences are discharged item by item through the operationalisable conditions and rejection conditions of the conditional models, mechanism hypotheses and accounting definitions in each chapter. If, in a specified setting, a systematic counter-example arises against the applicability premises of a postulate (for example, expectation guidance does not change behaviour, or agents have no feasible freedom to deviate), the **domain of applicability of that postulate should be restricted, or a local revision made**, with the question of revision adjudicated on the evidence of a specific research design; this book sets no unified failure count, no unified threshold and no automatic stopping rule of the form "N consecutive cases and the programme is demoted", nor does it exempt the empirical content of a postulate from testing merely because the postulate is a modelling convention.

* **SP-POSTULATE-1 【The Finite World & Non-Zero Impedance Postulate】★ the physical and epistemological cornerstone of the whole book**:
  > The realisation of any real complex adaptive system is constrained by an irreversible flow of time, a finite physical energy budget and cognitive bandwidth; encoding, parsing, routing and acknowledgement across nodes consume resources and time. Under a given physical channel model, the reliable communication rate is bounded by Shannon capacity. A Wittgensteinian "conceptual boundary" is used to pose a semantic research question — an image taken from the "delimitation" of 4.114 in the *Tractatus Logico-Philosophicus* (1921) and from the discussion of vague boundaries in the *Philosophical Investigations* (§68/§71); this book does not presuppose that linguistic boundaries are sharp, nor does it adopt a reading based solely on the *Tractatus*. Its bridging to coordination capacity must be defined and tested independently under RFC-001 and cannot be derived directly from a physical capacity result.
  > 1. **Anti-Happy-Path Centricity**: the analysis of complex systems must cover abnormal paths such as timeout, packet loss, graceful degradation and power loss, and in particular must test low-frequency, high-loss events. This text retains "99% abnormal paths" as a cautionary expression that prioritises the abnormal, and does not interpret it as a measured number of paths, running time or accident proportion; normal-state throughput and abnormal-state loss should be assessed separately.
  > 2. **Boundary Condition First**: both success cases and failure cases must enter the comparison; fault-tolerance investment is set by probability of occurrence, severity of consequence and cost of recovery, and the elimination of every defect is not made a precondition for action.

* **SP-POSTULATE-2 【The Agent Autonomy Postulate】**:
  > The micro-level acting unit of the system is an adaptive Agent possessing an independent private objective function $U_i$, a time discount factor $\beta_i \in (0, 1)$, finite memory and incomplete information. The Agent selects strategies according to its private objective and possesses freedom of strategic deviation; utility may include altruism, norm compliance or organisational objectives, and the agent is by no means a mechanically passive instruction executor or a passive logic gate.

* **SP-POSTULATE-3 【The Expectation-Induced Equilibrium Postulate】**:
  > A protocol influences agents' expectations and actions through rule broadcast and performance signals, and does not treat the subject as a mechanical executor. Let $\mu_{i,t}(A)=\Pr_i(S_{t+1}\in A\mid\mathcal I_{i,t},\mathcal P_t)$ denote the subjective probability of future states for agent $i$ under its information set; different agents' beliefs may differ, and expected utility may be computed further for integrable payoffs.
  > $$\mathcal P_t\longrightarrow\mu_{i,t}\longrightarrow\text{expected utility and incentives}\longrightarrow\text{strategic choice and action}$$
  > "Expectation-induced equilibrium" means that rules can alter the incentive conditions and the direction of choice at equilibrium. The existence and uniqueness of a Nash equilibrium, and whether a strategy-update process converges, must each be argued under a specified game model; this postulate does not presuppose general convergence for an arbitrary learning process.

---

#### 1.5.3 Formal Diagnosis: Separating Conceptual Overlap from the Orthogonal Pyramid Refactoring

In moving from case-driven writing towards axiomatic organisation, earlier versions exhibited two kinds of conceptual overlap; the statistical term "collinearity" is not used here as a tested conclusion:
1. **Meta-concept level confusion**: postulates that serve as the modelling starting point were at one time placed alongside RFCs or conflated with axioms, and the normative rule SP-RFC-007 was mixed in with descriptive conditional propositions;
2. **Undivided mechanism crossings**: intermediary rent-seeking, finality, split-brain and privilege boundaries appear in several RFCs; joint citation of the same mechanism is not necessarily redundant, but the object, conditions and output of each clause must be stated.

To reduce level confusion and to organise crossing mechanisms explicitly, the book establishes a **three-tier orthogonal pyramid**; "orthogonal" denotes a division of responsibilities and does not mean that every conceptual crossing has been eliminated or that formal independence has been proven:

```text
┌────────────────────────────────────────────────────────────────────────┐
│                Three-Tier Orthogonal Axiomatic Pyramid                 │
├────────────────────────────────────────────────────────────────────────┤
│  [Level 0] The 3 First-Order Postulates                                │
│   P1: Finite world, non-zero impedance (physics/channel/anomaly-first) │
│   P2: Agent autonomy (private utility U_i, discount beta_i)            │
│   P3: Expectation-induced equilibrium (rules shape beliefs;            │
│       existence and convergence require separate proof)                │
├───────────────────────────────────┬────────────────────────────────────┤
│                                   │ Model dependency and proof duties  │
│                                   │ ▼                                  │
├───────────────────────────────────┴────────────────────────────────────┤
│  [Level 1] The 6 Core Proposition Groups                               │
│   * Group I   Channel Capacity & Semantic Boundary                     │
│       capacity vs semantic bridging separated; effects uncalibrated    │
│   * Group II  Intermediary Parasitism & Compatibility Decay            │
│       net contribution compared; loss model needs conditions           │
│   * Group III Intertemporal Finality & Expectation Credibility         │
│       performance probability and remedy affect NPV, entry threshold   │
│   * Group IV  Privilege Ring Isolation & Split-Brain Contagion         │
│       rights, payoffs, update dynamics jointly drive plunder spread    │
│   * Group V   Transport Topology & Task Feedback                       │
│       diffusion and acknowledgement as analogy; governance feedback    │
│       tested separately                                                │
│   * Group VI  Debt Accounting & Evolutionary Selection                 │
│       net burden accounted; racing/PDCA bounded by budget and lag      │
├───────────────────────────────────┬────────────────────────────────────┤
│                                   │ Instantiation and application index│
│                                   │ ▼                                  │
├───────────────────────────────────┴────────────────────────────────────┤
│  [Level 2] 19 Consecutively Numbered Items, Including the 007 Rule     │
│   Current IDs run 001—019, identified separately by model, pattern,    │
│   application and normative status                                     │
│   * SP-RFC-007 is explicitly the three precepts for the system         │
│     architect against system freeze (a normative operating rule)       │
│   * Model, candidate pattern and application norm each carry their own │
│     evidential duty; none is called a proven corollary                 │
└────────────────────────────────────────────────────────────────────────┘
```

---

#### 1.5.4 The Six Core Proposition Groups and the 19 Effective SP-RFC Items: Dependency and Division-of-Labour Index

```text
Three postulates P1/P2/P3: resource constraints, agent autonomy, belief influence
    + object definitions O1—O5 + sub-model assumptions / external results / design objectives
    └─► specific conditional relations, empirical hypotheses, accounting or normative choices
          indexed by the six groups; a group name does not serve as a shared premise of proof
          for all of its clauses

I   Channel capacity and semantic boundary        P1 resource background; semantics/adoption modelled separately
    001 channel and decoding; 002 naming; 003 cross-context interpretation application
II  Intermediary parasitism and compatibility decay  P1/P2/O4 background; privilege/payoff/comparison separate
    004 serial retention; 005 complexity—rent-seeking; 006 approval latency; 007 cross-group design rule
    non-numbered candidate process diagram listed separately at the end of the chapter
III Intertemporal finality and expectation credibility  P2/P3 background; each clause conditions separate
    008 investment model; 009 record properties; 010 execution conditions
    non-numbered consumption and policy application notes listed separately at the end of the chapter
IV  Privilege ring isolation and split-brain       P1/P2/P3 used separately by sub-model
    011 privilege constraints; 012 conflict states; 013 payoff comparison; 014 authorisation;
    015 choice identification
V   Transport topology and task feedback           P1/P2/P3 background; task-feedback bridge awaiting test
    016 acknowledgement, resources and recovery in mobilisation and governance tasks
VI  Technical-debt accounting and evolutionary selection  P1 budget background; P2 used for incentives
    017 migration accounting; 018 probabilistic conditional model and feedback screening
Cross-group tooling / research norm: 019 sits in Chapter 8 and relates to II/IV/VI;
    it is not a deductive corollary of VI
```

The arrows in the diagram denote modelling dependency and normative attribution; they do not mean that every strict proof has already been completed from the three postulates. The six groups are a question index, not six proven master theorems. Every claim must separately state its object, additional assumptions, external results, and reasoning or empirical basis; the premises of one sub-model inside a group cannot be imposed on all the clauses of that group, and a clause summary cannot then be turned around to "prove" the same clause. The two static conditional conclusions in Groups III and IV appear respectively in §4.1 "conditional derivation III-1" and §5.3 "conditional derivation IV-1". Social bridging, empirical identification and dynamic convergence carry separate testing duties.

**Numbering and identity**: the effective IDs in v11.2 run consecutively from 001 to 019. 007 is the cross-group normative rule, 003 is a semantic dissemination application, and 019 is the Chapter 8 cross-group tooling/research norm; none of them becomes a proven corollary by virtue of its number. The former 006/010 of v11.1 are retained as non-numbered materials and are not absorbed by other clauses. Old numbers are reached through versioned entry points.

**Division of labour among adjacent clauses (cited by RFC number; no separate clause is created from a short name)**:

| Crossing theme | Clause division of labour and body entry point |
| :--- | :--- |
| Intermediary and complexity | [004](../../社会系统协议学白皮书.md#sp-rfc-004): serial loss; [005](../../社会系统协议学白皮书.md#sp-rfc-005): exclusive rights and complexity feedback; [§3.8 candidate process diagram (non-numbered material)](../../社会系统协议学白皮书.md#research-process-pattern): candidate process diagram; [006](../../社会系统协议学白皮书.md#sp-rfc-006): review latency and mission deadline. Shared mechanisms; none stands in for another's proof. |
| Intertemporal commitment | [008](../../社会系统协议学白皮书.md#sp-rfc-008): project cash flow and entry threshold; [§4.4 consumption and policy application notes (non-numbered material)](../../社会系统协议学白皮书.md#application-policy-expectations): consumption and policy expectations; [009](../../社会系统协议学白皮书.md#sp-rfc-009): repetition effects and historical finality; [010](../../社会系统协议学白皮书.md#sp-rfc-010): ordered state execution and its privilege and consensus conditions. |
| Privilege and failure | [011](../../社会系统协议学白皮书.md#sp-rfc-011): privilege protection; [012](../../社会系统协议学白皮书.md#sp-rfc-012): conflicting writes and partitioning; [013](../../社会系统协议学白皮书.md#sp-rfc-013): payoff comparison and behavioural dynamics; [014](../../社会系统协议学白皮书.md#sp-rfc-014): state authorisation interface; [015](../../社会系统协议学白皮书.md#sp-rfc-015): exit constraints and choice identification. |
| Dissemination and tooling | [016](../../社会系统协议学白皮书.md#sp-rfc-016): feedback and mobilisation tasks; [003](../../社会系统协议学白皮书.md#sp-rfc-003): Group I semantic dissemination application; [019](../../社会系统协议学白皮书.md#sp-rfc-019): application and research norm for AI tooling and exploratory early warning. |
| Migration and screening | [017](../../社会系统协议学白皮书.md#sp-rfc-017): net-burden accounting on a common boundary; [018](../../社会系统协议学白皮书.md#sp-rfc-018): branch success rates and observation windows under a finite budget; [007](../../社会系统协议学白皮书.md#sp-rfc-007): normative action selection made on the basis of verification results. |

| Core proposition group | Epistemic status and derived norms | Preconditions and conditions of validity | Formal model or mechanism relation | Novel Predictions | Falsification criteria |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **Proposition Group I: Channel Capacity & Semantic Boundary**<br>(Channel Capacity & Semantic Boundary Proposition Group) | **citation of established physical results / conditional model / semantic application**<br>`P1 resource background; semantic adoption conditions stated separately`<br>index: RFC-001, 002, 003 | 001 specifies the channel and decoding model; 002 specifies the name, content, audience and coordination task; 003 specifies text, version, context and interpretive result. Each defines its own conditions, and no social effect is derived from resource finiteness alone. | Sub-model examples (they do not replace the other clauses of the group): $I_{\text{phys}}=B_{\text{Hz}}\log_2(1+P_S/P_N)$ applies only within a given physical model; $C\le kI$ is a social bridging hypothesis awaiting calibration, and padding may produce decoding cost or error-correction gain. | In pre-registered tasks and controls, test how a change in comprehension cost affects coordination throughput, comparing explanations grounded in education, resources and institutions; do not derive a training period or a coordination radius directly from a writing style. | Before observing results, register the applicable population, the control or identification design, independent measures of task success and coordination throughput, the time window, the minimum attenuation magnitude predicted by the theory, and the error/power requirements. Where premises have been independently verified and measurement precision suffices, an empirical instance is not supported if an equivalence test or interval estimate excludes the pre-registered predicted range, and the bridging hypothesis and boundary of applicability must then be reviewed. A merely "statistically non-significant" result does not count as a refutation; before full operationalisation, it is not reported that the social bridging proposition has passed or has been falsified. |
| **Proposition Group II: Intermediary Parasitism & Compatibility Decay**<br>(Intermediary Parasitism & Compatibility Decay Proposition Group) | **conditional model / mechanism hypothesis / norm**<br>`P1+P2 and O4 background`<br>index: RFC-004, 005, 006<br>related rule: RFC-007 | 004 requires serial arrangement, conditional loss and no added output or recovery; 005 requires exclusive control, a dominant non-productive net payoff and insufficient constraint; 006 requires a specified approval path, mission deadline and protection benefit; 007 is a normative choice. The non-numbered candidate process diagram is listed separately and does not prove that the stages are obligatory. | Sub-model examples (they do not replace the other clauses of the group): for a serial arrangement with no added output or recovery, $\eta_n=\prod_i(1-\lambda_i)$; a geometric form requires equal rates, and an exponential upper bound requires a uniform positive lower bound; normative inflation requires a separate argument for its incentive mechanism. | With tasks and feasible alternatives fixed in advance, test whether an added non-productive layer reduces effective throughput; the relation between statutory word counts and TFP cannot substitute for a direct test of this model. | Estimate layer loss independently and pre-specify a throughput prediction interval; if observation on the same basis persistently exceeds the error tolerance, the applicability of the serial model should be rejected. Neither the number of layers alone nor "no significant decline" is sufficient to adjudicate. |
| **Proposition Group III: Intertemporal Finality & Expectation Credibility**<br>(Intertemporal Finality & Expectation Credibility Proposition Group) | **conditional proposition / record property / execution mechanism**<br>`P2+P3 modelling background`<br>index: RFC-008, 009, 010 | 008 specifies performance and recovery cash flows, discounting and the decision threshold; 009 specifies request, rule, de-duplication and review; 010 separately lists execution, ordering, consensus and privilege. Consumption and policy application at the end of the chapter list their own external model conditions; the conditions of the investment model do not govern the whole group. | Sub-model examples (they do not replace the other clauses of the group): $NPV_i=\sum_t\beta_i^t[p_{it}R_{it}+(1-p_{it})Q_{it}]-I_i$; with other terms fixed and $R_{it}>Q_{it}$, a fall in the probability of performance lowers net present value; exit from the investment must also clear the threshold. | Distinguish performance risk, financing constraints and demand shocks; test the differential effect of a rule change on projects with sunk costs. Marriage and fertility effects and aggregate liquidity effects require separately built models. | Pre-specify the sample, the shock, the identification strategy and the minimum effect; where the conditions hold and a reliable estimate excludes the range of the expected effect, reject that application model. Statistical non-significance is not in itself a falsification. |
| **Proposition Group IV: Privilege Ring Isolation & Split-Brain Contagion**<br>(Privilege Ring Isolation & Split-Brain Contagion Proposition Group) | **privilege / conflict model and conditional game**<br>`P1/P2/P3 listed separately by sub-model`<br>index: RFC-011, 012, 013, 014, 015 | 011 lists privilege and remedy; 012 lists communication/resources and conflicting writes; 013 lists two actions, a payoff table and strict dominance, with dynamics argued separately; 014 lists a specific objective and authorisation; 015 lists the feasible choice set and exit. The conditions of 013 cannot stand for the whole group. | Sub-model examples (they do not replace the other clauses of the group): under the static conditions above, plunder strictly dominates cooperation, and universal plunder is the unique Nash equilibrium. Convergence towards that equilibrium, communication partitioning, split-brain and physical collapse are distinct propositions. | Test how sanctions, cooperative returns and reputational change affect the choice to plunder; a fiscal revenue-sharing arrangement or a zero-penalty regime cannot on its own predict rapid collapse of the whole network. | If a complete payoff comparison shows that cooperation is not strictly dominated, the application premise of "plunder dominates" should be rejected; if a specified dynamic does not converge, reject the corresponding convergence model. Payoffs must be tested with independent data rather than inferred backwards from behaviour. |
| **Proposition Group V: Transport Topology & Task Feedback**<br>(Transport Topology & Task Feedback Proposition Group) | **mechanism hypothesis of task feedback**<br>`P1+P2+P3 modelling background`<br>index: RFC-016 | First specify the change in mobilisation or governance task, the resources, and the acknowledgement and error-correction channels, then compare actual coordination capacity. Do not infer an organisational type from the name of a transport protocol; without a threshold or dynamic model, no phase transition is promised. | Sub-model examples (they do not replace the other clauses of the group): TCP/UDP serve as a transport-mechanism analogy; organisational resilience separately tests application-layer acknowledgement, resupply and recovery. Textual stability and interpretive consistency are dealt with separately in Group I's 003, and shared membership in dissemination is not a derivation. | In samples comparable in task, scale and resources, test the contribution of acknowledgement and error-correction mechanisms to governance continuity, allowing a reliable feedback layer to be built above UDP. | Pre-fix the governance task, scale, duration and reliability indicators; after controlling for other feedback channels, if a sufficiently precise comparison excludes the pre-specified effect range, reject the application of that mechanism, and do not afterwards label organisations as TCP or UDP according to success or failure. |
| **Proposition Group VI: Debt Accounting & Evolutionary Selection**<br>(Debt Accounting & Evolutionary Selection Proposition Group) | **accounting definition / conditional probability / screening hypothesis**<br>`P1 budget background; P2 used for implementation incentives`<br>index: RFC-017, 018 | 017 unifies the task, lifecycle, price and discounting boundary; 018 specifies success and failure events, probabilities, independence, budget and observation window. The tooling and research norm of Chapter 8 carries a separate calibration duty and does not count as a deductive conclusion of this group. | Sub-model examples (they do not replace the other clauses of the group): with independent and fixed $p_k$, $P_{\text{evolution}}(K)=1-\prod_{k=1}^K(1-p_k)$; a finite budget does not guarantee that this approaches 1. Refactoring burden is compared by migration net present value, and PDCA satisfies $T_{\text{latency}}\le\Delta t<T_{\text{environment}}$. | Under the same budget, the same maturity observation period and a pre-registered task, test the discovery rate and net benefit of heterogeneous multiple branches with effective feedback against a single branch; do not presuppose that K=1 necessarily fails or that all winners come from the margins. | Pre-register branch success-rate estimates, independence tests, costs, comparison group and minimum gain; where conditions are verified and precision suffices, if the data exclude the predicted gain range, reject that application model. Where no feasible feedback window exists, or common failure sources dominate, the independent horse-racing model does not apply; "effective feedback" must not be defined after the fact by success or failure. |

**Scope of symbols and names**: $Q_{it}$ in §4.1 is the cash flow in the breach state, in the same units as $R_{it}$; $Q_i(a_i,a_{-i})$ in §5.3 is the net expected utility of a given game, not a recovery amount. $B_{\mathrm{Hz}}$ in §2.1 is bandwidth in hertz, whereas $B$ in the candidate model is symbols per second; $\mathcal R_{\mathrm{deadlock}}$ in §8.3 is a proxy score and is distinct from the reward-and-penalty rule set $\mathcal R$ of O2. The same letter does not mean that the terms can be substituted directly. Group VI adopts "technical-debt accounting and evolutionary selection": §7.1 defines the net-burden comparison and §7.2 separates the independent probability model from the real-world screening hypothesis; **no conservation of total debt is claimed**.

**Generation and evidence contract**: P/O constraints delimit the objects that can be modelled and the feasible domain, and cannot on their own select a unique institution. In the appendix [generation and evidence card](../../社会系统协议学白皮书.md#rfc-evidence-cards), every RFC records the primitive objects used, the postulates, the additional assumptions, the coordination predicament, the counterfactual failure, the alternative mechanism and the evidence status; the identity of the body text is not elevated by filling in a card. "Bootstrap" here denotes dependency and interface navigation, and does not claim that real institutions must have evolved historically in the order of the six groups.

Necessity, sufficiency and minimality are checked separately: with additional conditions, objectives and failure criteria fixed, a comparison that removes a mechanism tests only whether it is necessary; whether the objective is reached once the mechanism is added tests whether it is sufficient; only by deleting its components and comparing against feasible alternatives is it tested whether it is minimal within that scope. The three questions may not be substituted for one another, and a local performance loss need not be inflated into systemic entropy death. A formal proposition is checked for its quantifiers and counter-models; an empirical hypothesis is registered in advance with its comparison group, minimum meaningful improvement and error; an accounting definition is checked for its boundary and for double counting or omission; a normative rule states separately its objective, rights and costs, and does not derive an obligation automatically from a fact. A comparison not yet executed is marked "awaiting test", and an imagined counter-example is not registered as a real-world refutation already discovered.

Where minimality has not been tested, the text states "not shown to be minimal or unique"; sufficiency holds only for the stated objectives and failure model. Four cases are recorded separately: insufficient precision with indifference becomes insufficient evidence; unmet conditions become not applicable; missing measurement becomes missing; and actual rejection of the prediction becomes rejected. None of them is merged into either pass or failure.


<a id="-05-跨学科学术雷达对齐与计算系统工程大一统元编译器cross-disciplinary-academic-radar--the-socio-computing-meta-compiler"></a>
<a id="legacy-v11-1-sec-1-6"></a>
<a id="sec-1-6"></a>

### 1.6 Cross-Disciplinary Academic Radar & The Socio-Computing Meta-Compiler

【Epistemic synthesis】
*Socio-Protocolics* takes the unified meta-compiler for computing systems engineering as its meta-theoretical positioning, mapping mechanisms from mainstream economics, political science, history and cybernetics into a unified engineering expression. The correspondences below state which research this book inherits and recombines; they do not mean that the original authors have endorsed the six core proposition groups or any of their extrapolated conclusions. Coase's comparison of coordination costs, Hayek's communication of dispersed knowledge, North's institutional incentives and the North–Weingast credible-commitment mechanism all constitute theoretical predecessors against which this book must compare itself head-on. The incremental contribution of the book should take the concrete form of more stable cross-layer operational definitions, explicit boundary conditions or discriminating predictions; these gains must be tested in comparison with existing theory. The comparison baseline is the literature and theory named in §1.6.1; "named" does not equal "checked one by one", and the item-by-item comparison is carried by a dedicated research design, whose controls, interpretation ranges and reporting duties are defined per project. Gains are tested in three separate classes — **expressive gain** (easier to understand, lower learning cost, tested through readers' comprehension and transfer tasks), **explanatory gain** (covering a mechanism, boundary or anomaly that existing explanations leave unaddressed) and **predictive gain** (yielding a discriminating and rejectable prediction); the three classes do not share a single threshold or a unified failure count.

#### 1.6.1 Cross-Disciplinary Academic Radar Cross-Mapping Table

| The six core proposition groups of protocolics | Established social-science term / theoretical system | Core literature and major scholars | Existing explanations and comparison boundary | Engineering mapping and gain awaiting test |
| :--- | :--- | :--- | :--- | :--- |
| **Proposition Group I: Channel Capacity & Semantic Boundary** | Seeing like a state (legibility);<br>print-capitalism | James C. Scott, *Seeing Like a State* (1998);<br>Benedict Anderson, *Imagined Communities* (1983) | Scott and Anderson address state legibility, media and community construction; comparison with this book must hold the object of study and the outcome variable constant. | A decoding-cost hypothesis is proposed with compilers and bus protocols; task throughput must be measured independently and calibrated, and no upper bound on social coordination can be computed directly. |
| **Proposition Group II: Intermediary Parasitism & Compatibility Decay** | Institutional sclerosis;<br>distributional coalitions;<br>diminishing marginal returns of complex societies | Mancur Olson, *The Rise and Decline of Nations* (1982);<br>Joseph A. Tainter, *The Collapse of Complex Societies* (1988);<br>Dawson & Seater (2013) | Olson, Tainter and the institutional measurement literature have already supplied mechanisms of distributional coalitions, complexity cost and growth; this book must state its new variables and discriminating predictions. | For a serial arrangement with no added output or recovery, $\eta=\prod_i(1-\lambda_i)$ may be used; equal-rate or uniform-positive-lower-bound conditions are stated separately, and net loss and deadlock paths must be tested with independent data. |
| **Proposition Group III: Intertemporal Finality & Expectation Credibility** | Time inconsistency;<br>credible commitment;<br>economic policy uncertainty (EPU) | Kydland & Prescott (2004 Nobel);<br>North & Weingast, "Constitutions and Commitment" (1989);<br>Baker, Bloom & Davis (2016) | Time inconsistency, credible commitment and EPU have each already addressed policy incentives and expectations; they must not be summarised as lacking micro-level mechanisms. | Performance and remedy conditions are expressed through rollback, time-lock SLAs and state machines; investment, marriage and fertility, and capital flows are identified separately, and a terminology mapping does not constitute a complete causal explanation. |
| **Proposition Group IV: Privilege Ring Isolation & Split-Brain Contagion** | Roving versus stationary bandits;<br>state building and organised predation;<br>distortions of fiscal federalism (note: the term is used in Weingast's 1995 sense of a commitment device — "distortion" names the failure modes that the framework is meant to **prevent**, such as bailouts and soft budgets, local protectionism, rent-seeking and distributional coalitions; the original argument is that federal competition **weakens** rather than causes these distortions) | Mancur Olson, *Power and Prosperity* (2000);<br>Charles Tilly, *Coercion, Capital, and European States* (1990);<br>Weingast (1995) | Olson, Tilly and the fiscal-federalism models address different configurations of power, tax base and incentives; conditions and predictions must be compared one by one. | Ring-0/3, BGP and Byzantine faults are used to describe privilege and communication problems; plunder dominance, group convergence and physical collapse are modelled separately and are not derived automatically from the analogy. |
| **Proposition Group V: Transport Topology & Task Feedback** | Tactical freezing in street-network protest;<br>the strength of weak ties and the resilience of strong ties | Zeynep Tufekci, *Twitter and Tear Gas* (2017);<br>Mark Granovetter (1973) | Tufekci and Granovetter address mobilisation, organisational capacity and connection structure; the name of a transport protocol cannot substitute for these mechanisms. | TCP/UDP are used as a transport-mechanism analogy; the gain from application-layer acknowledgement, resources and recovery is compared, and a reliable feedback layer may be formed above UDP. |
| **Proposition Group VI: Debt Accounting & Evolutionary Selection** | Creative destruction;<br>the use of knowledge in society;<br>institutional evolution and the cost of radical restructuring | Joseph Schumpeter (1942);<br>Friedrich Hayek (1945);<br>Philippe Aghion (2025 Nobel) | Schumpeter, Hayek and the institutional-evolution literature supply mechanisms of innovation and dispersed knowledge; this book must compare costs and feedback design against specific models. | A unified technical-debt net-present-value boundary; the gain from multiple-branch selection is tested under budget, independence and $T_{\text{latency}}\le\Delta t<T_{\text{environment}}$, and high frequency is not equated with high fitness. |

#### 1.6.2 Positioning and Comparative Testing of the "Unified Meta-Compiler"

"Scholars in the established disciplines each hold one piece of the puzzle" is this book's summary of the fragmentation of cross-domain interfaces; it is not a blanket verdict that existing disciplines lack mechanisms, methods or explanatory power. Measurement-based identification, historical source criticism, institutional analysis and protocol engineering have different objects and evidentiary standards; the value of a unified language should show itself in making these results comparable and in making gaps in reasoning visible.

This book uses computing systems engineering as its own **virtual machine** and **meta-compiler**:
1. Extract the mechanisms of privilege, communication, recovery and migration from industrial implementations such as Linux and TCP/IP; the faults and costs present in concrete implementations must likewise be included, and "zero entropy" or globally deadlock-free operation must not be assumed.
2. Compile social problems into candidate models that state agents, objectives, resources, states, interfaces and failure conditions. An engineering implementation is not an equivalent copy of a social object, and the analogy must state item by item what has been preserved and what has been lost.
3. For example, the "compatibility-layer loss" of imperial decline can be given a serial model through $\eta=\prod_i(1-\lambda_i)$, but loss, output and recovery mechanisms must be estimated independently and then compared against explanations grounded in war, public finance or ecology; a core dump must not be treated as a historical measurement already obtained.
4. For example, social polarisation can be used to test the relation among semantic coordination cost, rule rollback and exit choices; "semantic hashing" and transactional deadlock are mechanism analogies, and agent motivation or a complete causal chain cannot be inferred from embedding distance.

**The unified meta-compiler for computing systems engineering is retained as a meta-theoretical research programme and a unified modelling language.** Whether it yields an incremental contribution is to be adjudicated by the stability of its definitions, its comprehension cost, its cross-model comparability and its predictive gain relative to existing explanations; this book does not on that basis claim to have completed a formal proof or an empirical validation of the whole of social experience.


<a id="legacy-v11-1-sec-1-7"></a>
<a id="sec-1-7"></a>

### 1.7 The System Functional Stack and Its Coordinate Systems

> **Coordinate and identity note**: L0–L5 in this table are a **functional-stack coordinate** (see "Note on coordinate systems" in §1.1: neither the L1/L2/L3 writing coordinates nor the Level 0/1/2 pyramid of §1.5 maps onto this stack by number; Ring-0/3 is an analogy for a privilege boundary). This table is a **mapping lens, not a social ontology**; the relations among the layers are candidate analogies to be tested case by case (see also the distinction in §1.4 between the hardware execution layer and the acting-subject layer).

**The L0-L5 Socio-Protocol Stack**

| Protocol layer | Task and object |
| :--- | :--- |
| 5. User application layer (Userland / Ring-3) | Private commercial contracts, scholarly inquiry, civic literature, self-organised coordination |
| 4. System call interface (Syscall / ABI) | Constitutional adoption, legislative interface, litigation entry point, national standard for compulsory education |
| 3. Organisational kernel layer (Kernel / Ring-0) | Allocation of power, scheduling of bureaucratic processes, fiscal clearing, GC reclamation |
| 2. Transport and routing layer (Transport & Route) | TCP acknowledgement and connectionless UDP datagrams as an analogy for feedback and diffusion; organisational reliability tested separately |
| 1. Language compilation and driver layer (Codec/Driver) | Character sets, stylistic and grammatical compilers, taxation and mobilisation / physical drivers |
| 0. Physical hardware layer (Physical Hardware) | Human neurons, physical land, grain and equipment, physical coercive force |

<!-- SP:END chapter-01 -->
