> **Translation record**
> - Chinese source: `社会系统协议学白皮书.md`, block `chapter-04` — 120 lines, 17816 bytes, block sha256 `dbf0cf8d7268f0326238f236a1ebfb9d5fd6265974586a9a0bd8c41d761278cf`, taken as the content between the `<!-- SP:BEGIN chapter-04 -->` and `<!-- SP:END chapter-04 -->` markers and reported by `tools/whitepaper_blocks.py list`; whole-file sha256 `4bffad3f3f4c4e7d9657c3d3ef98f6515622660f8d95cc1bcea10b2f1eee6674`, 340941 bytes, 2026-11-09
> - Chinese version / release tag: `v11.2-r20261106` (theoretical version remains v11.2)
> - Translation version: `en-v0.1-ch04`
> - Translation date: 2026-11-08
> - Check status: draft; C12 self-check run after write; independent read-only audit to follow; machine and glossary checks only; no independent professional native-speaker review
> - Pending sync: none — synced 2026-11-09 with the same-day Chinese-source revision (T-106 genealogy registration in §1.6; T-104/R-101/R-103 in case 4.4-A); fingerprints refreshed to whole-file `4bffad3f…`/340941 bytes
> - Status: complete translation of this chapter block, including all 7 case-annotation entries (batch 4, 2026-11-09); nothing inside the block is omitted
> - Authority: the Chinese SSOT is authoritative; this translation does not constitute a separate set of definitions (C2)
> - Note on group name: the SSOT is internally inconsistent about Proposition Group III's name — the chapter title and table of contents (lines 36, 930) read "第三组：跨期承诺、记录性质与执行条件" (Intertemporal Commitment, Record Properties, and Execution Conditions), while the overview tables and evidence cards (lines 275, 304, 2424–2426) and the already-landed appendix / chapter-01 use "第三组核心命题：跨期终局性与预期信誉" → "Proposition Group III: Intertemporal Finality & Expectation Credibility". To keep the English edition internally consistent, this file follows the established landed form "Proposition Group III: Intertemporal Finality & Expectation Credibility"; the SSOT's name inconsistency is flagged for the maintainer to reconcile.

**Scope and edition status.** This file is one block of a **phased** translation. As of batch 4 (2026-11-09), this file contains the complete chapter-04 block including the full case-annotation layer: the normative framework text, RFC 4.1–4.3, the conditional derivation III-1 and the §4.4 application-boundary note are translated, and so are all 7 case-annotation entries (cases 4.1-A/B/C, 4.2-A, 4.3-A, 4.4-A/B); the case-annotation sections retain the source's sharp register. The Chinese master source remains authoritative; this translation does not constitute a separate set of definitions (C2). Completeness of this block does not imply completeness of the edition, and this translation does not elevate any claim to established status. The block itself runs from the `<!-- SP:BEGIN chapter-04 -->` marker to the `<!-- SP:END chapter-04 -->` marker; the translation record, the chapter glossary and the two notes below precede that boundary and are not part of the translated text.

## Chapter Glossary — Chapter 4

| Chinese | English used in this file | Remark |
| :--- | :--- | :--- |
| 第三组核心命题：跨期终局性与预期信誉 | Proposition Group III: Intertemporal Finality & Expectation Credibility | group name, unique form in the whole book |
| 6 个核心命题组 | 6 Core Proposition Groups | H3-A landed |
| 19 项有效 SP-RFC | 19 Effective SP-RFC Items | title-case unique |
| 条件模型与经验桥接 | conditional model and empirical bridging | claim identity (008) |
| 性质定义与程序边界 | property definition and procedural boundary | claim identity (009) |
| 执行机制与条件性保护 | execution mechanism and conditional protection | claim identity (010) |
| 外部模型应用综述 | external model application overview | claim identity (non-numbered, §4.4) |
| 履约概率 | fulfilment probability | RFC-008 |
| 回收 | recovery | RFC-008 |
| 投资门槛 | investment threshold | RFC-008 |
| 净现值 | net present value (NPV) | RFC-008 |
| 资本开支 | capital expenditure (CAPEX) | RFC-008 |
| 贴现因子 | discount factor | RFC-008 |
| 幂等性 | idempotence | RFC-009 |
| 持久性 | durability | RFC-009 (ACID) |
| 终局性 | finality | RFC-009 |
| 确定性状态机 | deterministic state machine | RFC-010 |
| 共识算法 | consensus algorithm | RFC-010 |
| 时间锁 | time-lock | RFC-010 |
| 自由裁量缓冲区与异常处理接口 | Bounded Discretion & Exception Handler | RFC-010 |
| Ring-3 保护 | Ring-3 Protection | §4.3 analogy |
| 创造性破坏 | Creative Destruction | §4.4-A |
| 随机游走 | random walk (stochastic) | §4.4-B (Hall) |

**Note on claim identities.** The claim-identity labels in this chapter (RFC 008: conditional model and empirical bridging; RFC 009: property definition and procedural boundary; RFC 010: execution mechanism and conditional protection; §4.4: external model application overview) are descriptive phrases at the grain of the source sentence (per R7 of the term ledger), not a taxonomy of claim identities. This translation keeps the five canonical claim identities — `postulate`, `conditional proposition`, `mechanism hypothesis`, `accounting definition`, `normative objective` — distinct, and renders the finer descriptive labels by reusing the locked class words. The labels are not upgraded into proven conclusions; the negation guardrails in the source (does not / cannot / has not) are preserved.

**Convention on cross-chapter links.** In-page anchors that live in another English chapter or the appendix (#rfc-evidence-XXX, #sp-rfc-XXX) are linked directly to their corresponding English pages, maintaining full link closure within the English edition. Anchors that live in this file remain same-page links.

---

<!-- SP:BEGIN chapter-04 -->
<a id="chapter-4"></a>

## Chapter 4: Proposition Group III — Intertemporal Finality & Expectation Credibility



<a id="sp-rfc-008"></a>
<a id="legacy-v11-1-sec-4-1"></a>
<a id="sec-4-1"></a>

<a id="legacy-v11-1-rfc-009"></a>
<a id="legacy-v11-0-rfc-007"></a>

### 4.1 SP-RFC-008 | Performance Probability, Recovery, and Investment Threshold

**Claim identity:** conditional model and empirical bridging.
**Dependencies and additional conditions:** P2/P3; cash flows, recovery, discounting, horizon, and decision rules are specified separately.
**Generation and evidence card:** [G008](appendix.md#rfc-evidence-008).

**Normative Spec (规范条文).**
Long-run capital expenditure (CAPEX) depends on expected cash flows, rule fulfilment probability, cost of capital, investment horizon, and default-recovery conditions. For a given investment project $i$, the following may be used as a conditional analytical framework:
$$\text{NPV}_i=\sum_{t=1}^{T}\beta_i^t\left[p_{it}R_{it}+(1-p_{it})Q_{it}\right]-I_i.$$
Here $p_{it}$ is the fulfilment probability, $R_{it}$ the cash flow upon fulfilment, $Q_{it}$ the cash flow or recovery upon default, and $I_i$ the initial investment. Holding other conditions fixed and where $R_{it}>Q_{it}$, a fall in fulfilment probability lowers the project's net present value; only after the net present value crosses the decision threshold — and financing and waiting options are taken into account — can one infer non-investment. The variance of rule lifetime may serve as a testable risk proxy; it cannot by itself determine CAPEX, nor does it imply that every node's capital expenditure permanently falls to zero or that the discount factor necessarily tends to zero.

**Conditional derivation III-1: comparative statics of single-period fulfilment probability.** Within the finite-horizon model above, holding the discount factor, initial investment, and each period's fulfilment and default cash flows fixed, change one period's probability from $p_{it}$ to $p_{it}^{\prime}$, both in $[0,1]$. Subtracting the old from the new net present value, the other terms cancel, giving:
$$\Delta\mathrm{NPV}_i=\beta_i^t(p_{it}^{\prime}-p_{it})(R_{it}-Q_{it}).$$
Since $0<\beta_i<1$, when $R_{it}>Q_{it}$ and $p_{it}^{\prime}<p_{it}$, this difference is strictly negative; it is zero if the two cash flows are equal, and its sign reverses if default recovery is higher. This proves the conditional relationship within the given cash-flow model; it does not prove that real-world probabilities, cash flows, or discount factors are mutually independent. When other terms move jointly with policy, recomputation is required. Under the static net-present-value investment rule, a numerical decline does not mean the project has crossed the investment threshold, still less can one infer that aggregate capital expenditure or marriage/fertility necessarily falls to zero.

> 📜 **[Cross-border financial evidence annotation · Case 4.1-A] (Argentina's exchange-rate regime adjustments and the multi-stage shift of sovereign credit)**  
> *Citation of historical facts*: in 1991 Argentina passed the Convertibility Plan Law (*Ley de Convertibilidad*), setting 10,000 australes to 1 US dollar; after the new peso entered circulation in 1992, the exchange relation was 1 peso to 1 US dollar. This convertibility arrangement constituted an anti-inflation rule, accompanied by phased inflows of foreign capital; in the severe economic and bank-run crisis that erupted in late 2001, the government successively imposed withdrawal restrictions (*Corralito*) and declared default on external debt; in early 2002 the new government further formally abolished the 1:1 fixed exchange rate and carried out forced asymmetric pesification (*Asymmetric Pesification*).  
> *Source location*: [the 1991 Convertibility Law](https://www.argentina.gob.ar/normativa/nacional/ley-23928-1991-328); [the 1991 Decree No. 2128](https://www.argentina.gob.ar/normativa/nacional/decreto-2128-1991-7384/texto). The remaining policy and credit effects must still be supplemented with evidence separately.  
> *Systematic analysis*: Argentina's late-2001 debt default, its 2002 exit from the convertibility arrangement and the forced conversion of bank deposits are connected but multi-stage events differing in policy nature and domain of impact. These policy changes may affect public expectations about monetary credibility and safe-asset demand; the direction and magnitude of the effects must be examined together with survey, deposit and exchange-rate data; the responses are heterogeneous, and the evolution of monetary behaviour must be examined separately by specific policy, inflation cycle and external liquidity environment — it cannot be simply reduced to sovereign credit permanently falling to zero from that point on.

> 📜 **[Ancient-history evidence annotation · Case 4.1-B] (Treaty changes between the late Roman Empire and the Visigoths and commitment risk)**  
> *Citation of historical facts*: in 376 CE the Roman Empire allowed the Visigoths to cross the Danube and enter; the provisioning, resettlement and officials' conduct after entry were entangled with conflict; after the Battle of Adrianople in 378, Rome and the Gothic groups reached an arrangement in 382. The nature of that arrangement, the groups involved and its terms are thinly recorded, and scholars differ on whether it was a treaty (*foedus*) or a surrender (*deditio*); *foederati* denotes allies or associated soldiers, not the name of a treaty. According to Zosimus, in 408, after the death of Stilicho, soldiers attacked the wives and children of barbarian soldiers; one cannot conclude from this that they all belonged to the same Gothic legion. In 410 Alaric led his forces in the sack of Rome; the specific causation of the long-term evolution above must still be verified item by item.  
> *Source location*: [Ammianus, Book 31 (English translation)](https://www.tertullian.org/fathers/ammianus_31_book31.htm) covers 376—378 and does not witness the events of 382 or 410; [Zosimus, *New History* 5.35 (English translation)](https://www.livius.org/sources/content/zosimus/zosimus-new-history-5/zosimus-new-history-5.35/) recounts the events of 408; [the formal bibliographic record of Mark Hebblewhite, *Theodosius and the Limits of Empire* (Routledge, 2020)](https://www.routledge.com/Theodosius-and-the-Limits-of-Empire/Hebblewhite/p/book/9781138102989) and [the transcription of the relevant chapter](https://ebrary.net/252932/history/_focdus_) are used separately: the former locates the bibliography, the latter presents the author's interpretation; the specific page numbers and the consistency of the transcription with the published edition remain to be checked, and the remaining events and disagreements must be further verified.  
> *Systematic analysis*: the relations between the late Roman Empire and the Gothic groups spanned decades, encompassing a multi-stage evolution of entry-and-resettlement crisis, cooperation under different arrangements, contests over pay and provisions, and political conflict. The provisioning and admission disputes around 376 can serve as a lead for studying intertemporal trust; their connection to later events and the competing explanations still require independent examination; this book uses it as a mechanism reference case for examining how “incomplete commitments and unilateral default accelerate the disintegration of systemic defence” when a sovereign centre faces external heterogeneous collaborators, not as a historical proof of a single cause.

> 👵 **[Cross-generational contract evidence annotation · Case 4.1-C] (SLA adjustments and rule risk in the evolution of intergenerational financing of public pensions)**  
> *Institutional-evolution evidence*: the old-age and disability insurance system established by the German Empire in 1889 initially contained funded elements, and after the major reform of 1957 it gradually settled into the typical pay-as-you-go (PAYG) dynamic-balance mechanism, whose macro operation relies on the intergenerational rolling arrangement of “contributions from the active labour force supporting the benefits of already-retired generations”. Yet in many modern countries, facing demographic change towards fewer children and an ageing population plus fiscal pressure, sovereigns often push back the statutory retirement age, adjust benefit formulas or tighten eligibility, triggering wide controversy over unilateral re-contracting of the long-term service agreement (SLA) and rule credibility.  
> *Source location*: [the German Federal Constitutional Court's ruling of 7 April 2022, 1 BvL 3/18 et al., English version, para. 24](https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/EN/2022/04/ls20220407_1bvl000318en.html) locates the institutional background of the entry into force in 1891 and the 1957 financing reform; that background narrative does not prove the trust, participation or family-decision effects discussed below, and other countries and specific adjustments require separate sources.  
> *Systematic analysis*:  
> 1. **The protocol parable of unilateral service downgrade and rule risk (Sovereign Downgrade & Protocol Re-contracting)**: in a centralised architecture, after decades of paying social-insurance contributions, users often face rule adjustments at the delivery stage. Although in legal doctrine and public finance statutory social security differs from private advance-payment contracts in civil and commercial dealings, and benefit adjustments usually follow legislative or administrative procedures, from the micro agent's point of view frequent rule changes lacking adequate transition periods and remedies may induce trust erosion akin to a unilateral downgrade of a software Terms of Service;  
> 2. **Micro-level trust decline and heterogeneous choices**: if micro nodes identify default risk in the central pool, they may lower their trust expectations toward the system. Their coping strategies may include multidimensional adjustments, such as reducing long-term liquidity injections into the central pool (adjustments to participation and employment strategies), increasing precautionary savings and reconsidering family planning. The specific direction depends on expected benefits, vested entitlements, exit costs and alternative protection; one must not assume that all nodes take disconnection as the only option; fertility decline and economic growth are also driven by multiple long-term trends such as income levels, child-rearing costs, female labour-force participation and cultural attitudes.



<a id="sp-rfc-009"></a>
<a id="legacy-v11-1-sec-4-3"></a>
<a id="sec-4-2"></a>

<a id="legacy-v11-1-rfc-011"></a>
<a id="legacy-v11-0-rfc-011"></a>

### 4.2 SP-RFC-009 | Retry Idempotence, Record Durability, and Finality

**Claim identity:** property definition and procedural boundary.
**Dependencies and additional conditions:** fixed request, rule version, evidence set, and authorisation-review procedure.
**Generation and evidence card:** [G009](appendix.md#rfc-evidence-009).

**Normative Spec (规范条文).**
1. **Semantic invariance and procedural protection:** if property rights, jurisdiction, and the relations of rights and obligations can be rewritten at will without due process, agents' long-run expectations are disturbed. One should independently examine the dispersion of textual-interpretation authority, procedural constraints, and ex-post remedy mechanisms; one cannot assert a type-system collapse merely from textual change.
2. **Layered inspection of idempotence, durability, and finality:** for the same request identifier $k$ that should be de-duplicated, idempotence requires that repeated submission adds no further business effect, i.e. $F_k(F_k(s))=F_k(s)$; distinct requests must not be merged merely because they share an operation name. The durability of ACID requires that a committed result is not lost under the specified fault model, and subsequent authorised transactions may still change the current state. Finality additionally means that a confirmed record will not be revoked or replaced under the specified rules and trust assumptions. When inspecting ex-post reload, one must fix the transaction identity, rule version, and evidence set, and distinguish repeated penalty, rewriting of historical records, and appending a corrective record per pre-announced review rules; merely having $Verify(Tx,t_0)\ne Verify(Tx,t_0+\Delta t)$ is insufficient to conclude arbitrary rollback.

> 📰 **[Procedural-justice case annotation · Case 4.2-A] (Procedural retroactivity and rule-stability disputes in university disciplinary investigations)**  
> *Empirical observation*: in the evolution of university administrative and self-regulatory rules (e.g. the successive rounds of litigation around Title IX procedures), the focus of dispute has often concentrated on the evidentiary standard for establishing “informed consent (Consent)” and on procedural retroactivity. This book distinguishes three situations in its analysis; the specific rules and rulings must still be verified separately: ① no valid consent objectively existed at the time of the conduct (truth discovered afterwards); ② the party clearly withdrew consent during the conduct; ③ the burden of proof is changed, or new adjudication standards are applied retroactively, ex post and without procedural constraints.  
> *Source location*: [the 2024 Title IX rule (89 FR 33474)](https://www.govinfo.gov/app/details/FR-2024-04-29/2024-07915); [the 2026 Federal Register note on the rule's and litigation's history](https://www.govinfo.gov/content/pkg/FR-2026-09-29/html/2026-19929.htm). According to the history recorded in the latter, the 2024 rule was vacated by the courts in 2025, and in the same year the Department of Education announced enforcement under the previous framework; the rule of 29 September 2026 re-codified the relevant provisions into the CFR while retaining the listed adjustments — it is not a verbatim restoration of all of the 2020 text. This example cites the regulatory history; specific conduct must still be distinguished by period, jurisdiction and applicable version; this book's three-situation analysis does not equal a proven consensus of the judiciary.  
> *Systematic analysis*: when institutional enforcement lacks explicit rules of proof, appeal deadlines and boundaries of final remedy, the parties face asymmetric retroactive adjudication risk. This book proposes a mechanism awaiting test: this risk may alter long-run expectations and interaction strategies, but this case provides no specific case samples, behavioural measurement or identification design, and on that basis one cannot conclude that over-defensive behaviour has occurred or estimate its causal effect; existing preferences, public opinion and other rule changes must all be treated as competing explanations. The foundation for protecting all parties' lawful rights and interests lies in upholding explicit procedural rule of law and two-way adversarial remedy mechanisms.



<a id="sp-rfc-010"></a>
<a id="legacy-v11-1-sec-4-4"></a>
<a id="sec-4-3"></a>

<a id="legacy-v11-1-rfc-012"></a>
<a id="legacy-v11-0-rfc-017"></a>

### 4.3 SP-RFC-010 | Deterministic Execution and Conditional Commitment

**Claim identity:** execution mechanism and conditional protection.
**Dependencies and additional conditions:** initial state, input ordering, consensus, authority, faults, and asset control are specified separately.
**Generation and evidence card:** [G010](appendix.md#rfc-evidence-010).

**Normative Spec (规范条文).**
A deterministic state machine produces identical results under identical initial states and identical ordered inputs, and can be used to reduce arbitrary discretion in cross-period clearing. If one further requires multiple nodes to agree on a consistent history, one must also specify the consensus algorithm, membership and authority model, fault and attack thresholds, network assumptions, protocol-upgrade authority, and finality criteria; the recurrence $s_{n+1}=\delta(s_n,tx_n)$ may represent the execution rule, but this recurrence relation by itself does not prove history is immutable. Cryptographic signatures and time-locks constrain authorisation and execution timing respectively, and — where the stated assumptions hold — raise the difficulty of unauthorised ledger alteration; evaluation of "default resistance" must be limited to the states and assets the protocol actually controls, and the counter-example conditions under which the commitment fails must be stated explicitly. Given that real social contracts are endogenously incomplete, deterministic auto-execution (such as smart contracts or rigid administrative rules) applies only to standard paths with complete, verifiable state; for unforeseeable physical or social edge anomalies, the protocol must still reserve a procedurally-constrained "Bounded Discretion & Exception Handler" to avoid strangling legitimate room for correction through rigid lock-in.

> 💻 **[Cryptography–institution isomorphism annotation · Case 4.3-A] (Bitcoin's algorithmic cap and smart contracts hedging against sovereign rug pulls)**  
> *Engineering comparison*: this book compares Bitcoin's issuance and validation rules and Ethereum's contract execution with the problem of intertemporal commitment as a mechanism comparison; from this one does not infer that Satoshi Nakamoto designed the system in response to the Argentina or pension cases listed in this book. On-chain execution is further constrained by input ordering, consensus, upgrade authority and fault conditions, and smart contracts are not generalised into an unconditional, unwritable automatic-payment guarantee.  
> *Systematic analysis*: signatures, consensus and time-locks can reduce certain unilateral ledger-alteration powers; their scope of protection depends on trust assumptions, upgrade authority, key management and the assets actually controlled. Ring-3 Protection is here an analogy for authority boundaries; from cryptographic unforgeryability one cannot directly infer that legal rights, off-chain resources or long-run purchasing power are irrevocable.



<a id="application-policy-expectations"></a>
<a id="legacy-v11-1-sec-4-2"></a>
<a id="sec-4-4"></a>

<a id="legacy-v11-1-rfc-010"></a>
<a id="legacy-v11-0-rfc-008"></a>

### 4.4 Macro cross-period expectations and policy application-boundary note

**Claim identity:** external model application overview (non-numbered application material).
**Dependencies and additional conditions:** P2/P3 background; consumption, financing, information, and policy models each state their conditions separately.

**Normative Spec (规范条文).**
This section is an application overview of external models; the consumption and policy models it cites must each state their conditions, and are not a direct inference from 008. Micro-level agents' expectations, information credibility, and property-rights safety boundary are the mechanisms macro policy transmission must examine; aggregate demand, supply shocks, financing constraints, and fiscal-monetary arrangements must also be brought into the specific model. An incredible rule commitment may weaken transmission, but one cannot infer from micro defensive behaviour alone that all macro control necessarily fails. One should separately identify policy shocks, agent constraints, and observable outcomes.

> 📜 **[Theoretical isomorphism annotation · Case 4.4-A] (2024 Acemoglu/Johnson/Robinson & 2025 Mokyr/Aghion/Howitt: inclusive protocols and the hard wall facing frontier innovation)**  
> *Citation of theory*: the 2024 Nobel Memorial Prize in Economic Sciences was awarded to Acemoglu, Simon Johnson and Robinson, systematically proposing the macro divide of “inclusive institutions vs extractive institutions”; the 2025 prize followed immediately, awarded to Joel Mokyr, Philippe Aghion and Peter Howitt — Mokyr for identifying the prerequisites of sustained growth through technological progress, and Aghion and Howitt for the theory of sustained growth through creative destruction (note: the official citation states the two halves separately; “cultural-institutional” and “frontier” are this book’s summarising additions, not official wording).  
> *Systematic analysis*: these studies supply comparable theoretical mechanisms for institutional incentives, knowledge diffusion and innovation competition. This book can propose an engineering mapping via open-source knowledge protocols, property-rights interfaces and edge trial-and-error, but the awards themselves do not constitute “rigorous computer-system proof”. The constraints facing catch-up and frontier innovation must be compared in specific models; one cannot infer directly, from an organisation being labelled “closed-source” or “extractive”, that it will necessarily hit the wall and deadlock.  
> *Controversy note*: the framework’s identification strategy remains contested: Albouy (2012) questions the reliability of the settler-mortality data; Acemoglu, Johnson & Robinson (2012) reply that the findings are robust; Glaeser et al. (2004) question the causal direction from institutions to growth, arguing that human capital is the more fundamental source of growth.  
> *Sources*: [the 2024 popular-science background page (NobelPrize.org)](https://www.nobelprize.org/prizes/economic-sciences/2024/popular-information/); [the 2025 press release (NobelPrize.org)](https://www.nobelprize.org/prizes/economic-sciences/2025/press-release/).

> 📜 **[Theoretical isomorphism annotation · Case 4.4-B] (2026 Hall and Woodford: micro intertemporal expectations and the boundary of macro policy transmission)**  
> *Citation of theory*: the 2026 Nobel Memorial Prize in Economic Sciences was awarded to Robert E. Hall and Michael Woodford in recognition of their outstanding contributions to laying the microfoundations of macroeconomic stabilisation policy.  
> *Systematic analysis*:  
> 1. **Hall's intertemporal consumption model (Hall, 1978)**: under that model's conditions, the marginal utility of consumption has a random-walk property, and consumption itself approximately follows the corresponding process; this is a proposition about whether given information can forecast future changes in consumption, and it cannot be interpreted as transitory income or subsidies having absolutely no effect on the level of consumption. New income news, asset changes and financing conditions must still be examined in specific models and data; one does not infer from this that all agents necessarily stop consuming or having children.
> 2. **Expectations, commitment and policy transmission**: credible intertemporal policy arrangements can influence agents' expectations and decisions; for whether a specific easing works, one should list the model, constraints and evidence, and one does not infer directly from policy controversy that credibility falls to zero or that any stimulus is ineffective. The official 2026 prize announcement likewise stressed the stabilising role of well-timed fiscal and monetary measures.
> *Sources*: [Hall (1978), original paper](https://web.stanford.edu/~rehall/Stochastic-JPE-Dec-1978.pdf); [the official 2026 prize in economic sciences announcement](https://www.kva.se/en/news/the-prize-in-economic-sciences-2026/).

<!-- SP:END chapter-04 -->
