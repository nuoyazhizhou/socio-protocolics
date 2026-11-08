> **Translation record**
> - Chinese source: `社会系统协议学白皮书.md`, block `chapter-03` — 369 lines, 46698 bytes, block sha256 `7933c32d20ed56c764071e6916af32d2058ef3fcd3172d409d379233154621b3`, taken as the content between the `<!-- SP:BEGIN chapter-03 -->` and `<!-- SP:END chapter-03 -->` markers and reported by `tools/whitepaper_blocks.py list`; whole-file sha256 `d5ffb73e3db73f8bb42a2ecb39871bf6c55eace8bb72111b63a2ee362134d9c8`, 338639 bytes, 2026-11-08
> - Chinese version / release tag: `v11.2-r20261106` (theoretical version remains v11.2)
> - Translation version: `en-v0.1-ch03`
> - Translation date: 2026-11-08
> - Check status: draft; C12 self-check run after write; independent read-only audit to follow; machine and glossary checks only; no independent professional native-speaker review
> - Pending sync: none at present; to be recorded item by item if the Chinese source is updated
> - Status: phased translation of this chapter block — the normative framework text, RFC 3.1–3.8 specifications, the falsifiability boundary, the architect's conceptual-boundary statement, the comparison tables and the two ASCII diagrams are translated; the case-annotation blocks (cases 3.1-A, 3.2-A, 3.3-A, 3.3-B, 3.5.1-A, 3.5.1-B, 3.5.2-A, 3.5.2-B, 3.5.2-C, 3.6.1-A, 3.6.2-A, 3.6.2-B, 3.6.2-C, 3.7-A, 3.7-B, 3.7-C, 3.7-D) are **retained in the original Chinese** by design under the C-1 phased plan (T3 not yet passed), so those blocks are held untranslated inside this file
> - Authority: the Chinese SSOT is authoritative; this translation does not constitute a separate set of definitions (C2)
> - Note on group name: the SSOT is internally inconsistent about Proposition Group II's name — the chapter title and table of contents (lines 35, 559) read "中介净贡献、复杂性与规范选择", while the overview tables (lines 274, 2420–2422) and the already-landed appendix / chapter-01 use "中介寄生与兼容层衰减" → "Proposition Group II: Intermediary Parasitism & Compatibility Decay". To keep the English edition internally consistent, this file follows the established landed form "Proposition Group II: Intermediary Parasitism & Compatibility Decay"; the SSOT's name inconsistency is flagged for the maintainer to reconcile.

**Scope and edition status.** This file is one block of a **phased** translation. The English edition as a whole is an *abridged adaptation* of the v11.2 whitepaper: the six chapters that carry case-annotation sections are not yet translated, and those annotations remain untranslated by design until the underlying Chinese case materials pass the real-case acceptance stage (T3). Chapter 3 carries case-annotation sections (the 17 cases listed in the translation record); per the C-1 phased plan those annotations are **retained in the original Chinese** inside this file, so the normative framework text, RFC 3.1–3.8 and the §3.4 architect's conceptual-boundary statement are translated while the case-annotation blocks are held in Chinese. Completeness of this block does not imply completeness of the edition, and this translation does not elevate any claim to established status. The block itself runs from the `<!-- SP:BEGIN chapter-03 -->` marker to the `<!-- SP:END chapter-03 -->` marker; the translation record, the chapter glossary and the two notes below precede that boundary and are not part of the translated text.

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
| 规范守则 | normative precept / rule | RFC-007 (locked title uses "Precepts") |
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
| BGP 路由劫持 | BGP route hijacking | §3.4 meta-annotation |
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

> 📊 **【现代制度经济学与计量实证注疏 · 案例 3.1-A】（奥尔森“制度硬化症”、泰恩特复杂性收益递减与村级缺失支出实证）**  
> *经典专著锚点*：制度经济学家曼瑟尔·奥尔森（Mancur Olson）在名著《国家的兴衰》（*The Rise and Decline of Nations*, 1982）中分析了分利集团累积与制度僵化（Institutional Sclerosis）对经济增长活力的抑制机制；历史人类学家约瑟夫·泰恩特（Joseph Tainter）在《复杂社会的崩溃》（*The Collapse of Complex Societies*, 1988）中探讨了复杂性投资的边际回报递减问题；与现代合规负担的联系属于本书的机制映射。两项经典提供了组织与系统面临维护成本攀升的演化机制洞察，不应机械简化为所有制度必然走向绝对锁死崩溃的普遍数量规律。  
> *外部经验研究述评*：  
> 1. **村级项目支出缺口与审计效果**：Olken（2007, *Journal of Political Economy*）在印尼 608 个村庄开展道路项目随机实验，以申报支出与独立工程成本估计的对数差衡量缺失支出（文中以百分比近似解释），样本均值约为 24%；该绝对水平对材料损耗等测量假设敏感。将政府审计概率由约 4% 提高至 100%，使缺失支出降低约 8 个百分点。608 为实验村庄总数，具体指标及回归的有效样本须按原论文表3、表4分别报告。本研究支持审计机制能够影响村级资源流失，未直接估计行政传输层数或各层损耗系数；若采用四层、每层 8% 的设定，所得效率约 71.6% 仅为本书的假设算例。其中 8% 为各层条件损耗率的演示取值，并非由 Olken 的审计效应估计取得。
> *核查来源*：[Olken (2007), Monitoring Corruption: Evidence from a Field Experiment in Indonesia](https://economics.mit.edu/sites/default/files/publications/Monitoring%20Corruption%20Evidence%20from%20a%20Field.pdf)。
> 2. **监管篇幅、限制词计数与经济绩效**：RegData 以法规中的限制性词语计数作为监管规模的代理；其 4.0 版覆盖 1970–2020。Mercatus Center 的 2020 年发布材料报告，2019 年 CFR 约含 1.03 亿词及 108 万处限制性词语。另据 Dawson 与 Seater（2013, *Journal of Economic Growth*），基于 CFR 篇幅时间序列的模型估计发现监管累积与产出及全要素生产率增长下降有关。两项研究的时期、指标与估计对象不同；限制词计数不等于净社会成本，也不直接检验本书的中间件损耗公式。具体增长损失与金额须在提供最终发表版页码、估计式及反事实口径后单列。
> *核查来源*：[QuantGov, The History of RegData](https://www.quantgov.org/history)；[Mercatus Center, Quantifying Regulation in US States with State RegData 2.0](https://www.mercatus.org/research/data-visualizations/quantifying-regulation-us-states-state-regdata-20)；[Dawson & Seater (2013), Federal regulation and aggregate economic growth](https://link.springer.com/article/10.1007/s10887-013-9088-y)。

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

> 💻 **【软件与思想史同构 · 案例 3.2-A】（从解放者到恶龙的系统轮回）**  
> *UNIX/GNU/Linux的不同路径*：FSF[自身历史记录](https://www.fsf.org/history/)区分1983年GNU公告与1984年正式启动；Linux 0.01发行说明则记录了一个带有明确限制的源码试验。本书据此比较许可目标、试验环境与接口开放，不将后来的法律争议倒置为这些项目早年启动的原因，也不据时间先后认定全球开发者迁移的唯一动因。
> *思想史比较线索（待材料）*：教义诠释、教会财政、大学神学审查与国家授权应按时期和机构分别研究；本书不把它们合成一个千年不变的“中间商”。若解释权排他、收益与可核验服务脱节且纠错受阻，可提出封闭中介风险假说；若材料显示开放争论、有效服务或内部改革，该解释就须收缩。本段只定位待核问题，不登记为已完成的历史案例检验。
> **系统学提醒**：曾经推动开放的规范也可能需要修正；是否封闭、是否失效及能否内部恢复，须逐项举证。不能从“入核”直接推出清洗或重构必要。

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

> 📜 **【技术规制史实 · 案例 3.3-A】（英国《机动车法案（红旗法）》与规制阻抗）**  
> *史实引证*：[1865年《机动车法案》原刊第3、4条](https://www.legislation.gov.uk/ukpga/Vict/28-29/83/pdfs/ukpga_18650083_en.pdf)规定，适用道路上的非畜力机动车至少配备三人，其中一人在车前至少60码（约55米）步行持红旗引导；一般公路限速4英里/小时，城市、城镇或村庄内限速2英里/小时。此处报告1865年条文，不把后续沿革简化为所有车辆一直适用同一规则。  
> *系统学分析*：人员配置、步行先导与限速要求，给适用车辆的道路运行设定了可定位的约束；这些要求是否、以及在多大程度上增加测试成本或延缓技术迭代，是本书提出的待检验机制问题，不能仅凭法条推出“显著阻抗”或产业后果。[1896年法案第1、4条及附表](https://www.legislation.gov.uk/ukpga/Vict/59-60/36/pdfs/ukpga_18960036_en.pdf)对符合定义的轻型机动车豁免列明的既有规定，并另设速度上限；这支持规则发生调整，不证明放宽的净收益或此前限制的历史净损害。比较仍须纳入安全保护、实施状况与可行替代方案。

> 💻 **【现代开源穿透 · 案例 3.3-B】（自主智能体时代的 AI 飞控与去中心化非对称穿透）**  
> *技术边界*：审批耗时与电子围栏效果必须按设备、任务和适用规则分别核查，不能预置所有任务都需要数天人工审批；分类规则、免申请或长期许可路径亦须纳入。开源飞控与导航方案可以改变部分技术依赖，但不能据此断言监管整体失效。
> 1. **AI 辅助代码原型**：大语言模型可用于生成或修改姿态控制与航路点巡航的代码原型，但本书未提供可复现的工时、精度或稳定性评测，不能据此宣称门槛归零或数小时即可获得高性能飞控。生成代码与经验证的控制器须区分，性能应在具体设备、任务与基线下通过仿真、硬件在环及适用的实机测试评估；
> 2. **开源飞控与硬件集成**：ArduPilot、PX4 与公开销售的器件、3D 打印工艺可作为开放工具链的研究实例；控制板适配、传感器、执行机构、电源与结构集成仍有成本。本书未提供完整物料清单、适配记录或制作工时，不能将单颗芯片报价和打印时间当作整机成本或可部署性能的证据；
> 3. **旁路边界**：视觉惯性里程计（VIO）或光流等技术可作为研究特定导航依赖的例子；本书没有提供足以证明所有无线电反制与电子围栏普遍失效的数据。应按设备、任务和威胁模型测量实际成功率。
> *系统学讽刺*：行政监管若只增加守法者的填表负担，却拿不出相应安全收益，当然值得追问。但讽刺不能代替分母：绕过一种防护不等于全部防御为零，审批摩擦也不等于所有合法企业都被掐死。
> *系统学结论*：**若指定任务的审批时延超过任务期限（$Latency_{\text{Audit}}>TTL_{\text{mission}}$），该路径可能无法按时完成任务；应同时核验免申请、长期许可和替代路径。总体吞吐、风险降低及恶意绕过率须分别测量。形式化审核不能替代真实安全结果。**

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
> Addressing readers' prudent question of whether the whitepaper's own use of "non-idempotent deadlock," "Ring-3 memory isolation," and "BGP route hijacking" also fabricates jargon, this theory establishes a reciprocal testing principle:  
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

> 📜 **【思想史注疏 · 案例 3.5.1-A】（六祖惠能对复杂义理的 Bypass 旁路）**  
> *典籍引证*：《六祖坛经》（敦煌写本与后出的宗宝本在文句上互有异同；宗宝本为后出通行本，记其偈语为“菩提本无树，明镜亦非台，本来无一物，何处惹尘埃”，早期敦煌本则记作“佛性常清净，何处有尘埃”等）。惠能顿悟叙事强调直指自性，后世禅门进一步提炼为“教外别传、不立文字、直指人心、见性成佛”的门径概括。  
> *版本核查*：[CBETA敦煌本T2007，T48第338a页7—8行](https://raw.githubusercontent.com/cbeta-org/xml-p5/master/T/T48/T48n2007.xml)；[宗宝编通行本T2008，T48第349a页7—8行](https://raw.githubusercontent.com/cbeta-org/xml-p5/master/T/T48/T48n2008.xml)。顿悟叙事和传承组织须分别解释，不以本段认定历史首次。
> *系统学分析*：本书用 Bypass 类比顿悟叙事中的实践接口重组；文本允许提出是否减少部分注疏负担的问题，但不提供参与门槛或人口效果的实测值。师承、戒律和共同体仍须分别考察，不能由偈语推出现实中的“零中介”。 减少一类转译要求也不排除新经典、师承或认证中介的形成；“旁路—新中介再生”应作为竞争机制另取制度材料检验，不预设中介总量下降。

> 📜 **【思想史注疏 · 案例 3.5.1-B】（净土宗：降低调用门槛的持名念佛）**  
> *典籍引证*：善导《观无量寿佛经疏》卷四讨论正行、助业与杂行，并将专念弥陀名号称为正定之业，置于深心及回向发愿的教义语境中。参见[CBETA T1753，T37第272页a栏28行至b栏13行](https://raw.githubusercontent.com/cbeta-org/xml-p5/master/T/T37/T37n1753.xml)。本例不以此断言易行道的历史首次，也不把称名解释为脱离教义条件的单条执行指令。
> *系统学分析*：可比较称名、观想与其他实践的学习要求，以“轻量级调用接口”提出参与成本假说；不同阶层是否更易参与、产生多大效果，仍需受众及制度材料检验，不能以教义主张替代社会测量。

<a id="legacy-v11-1-sec-3-6-2"></a>
<a id="sec-3-5-2"></a>

#### 3.5.2 Martin Luther and Wang Yangming: the Edge-Computing Analogy of Authority-Interface Reconfiguration

**Normative Spec (规范条文).**

When an authority interface is closed or translation cost is too high, one may compare an edge-computing path that devolves part of the judgment responsibility to the acting agent. "Justification by faith" and "to extend innate knowledge" are used in this book to pose mechanism analogies; they do not mean that all public facts can be self-verified by a local CPU with zero hops; empirical knowledge still requires external evidence, and the roles of teaching, pastoral office, lineage, and community must be investigated separately.

> 📜 **【思想史注疏 · 案例 3.5.2-A】（“撕碎教皇 API”的批判性类比与德语圣经）**  
> *文本与版本*：[《九十五条论纲》英译](https://www.luther.de/en/95thesen.html)第21、27、36条等讨论赎罪券许诺、金钱及悔罪的关系，不支持把1517年的路德概括为主张取消全部教会中介。[Gruber馆藏1522年新约说明](https://gruber.lstc.edu/luthers_bible/1522.php)及[1534年完整德译圣经版本记录](https://gruber.lstc.edu/luthers_bible/1534.php)支持相应出版节点；本例不依赖“教堂门张贴”细节，也不由译本出版推出全民识字或德语规范由一人制定。
> *系统学分析*：路德提出“信徒皆祭司（Priesthood of all believers）”，本书据此类比部分权威中介的重组；共同祭司身份不等于取消公共宣道与牧职。德语译本传播与识字、教育及语言整合的关系须结合制度、地区与时期检验，不能由译本出版直接推出全民识字或工业跃迁的充分原因。

> 📜 **【思想史注疏 · 案例 3.5.2-B】（阳明心学：从云端拉取到本地 CPU 缓存命中的类比）**  
> *可定位文本（转述）*：[《传习录》卷上第34条](https://zh.wikisource.org/wiki/傳習錄/卷上#34)讨论心与理、善恶；[卷中《答顾东桥书》第139条](https://zh.wikisource.org/wiki/傳習錄/卷中#139)讨论良知及其实际工夫。本例据这些论述作道德判断接口的比较，不用格竹与龙场故事拼接一个未经核验的即时“发现时刻”。所引为传世语录转录，不是当时行为效果的实测记录。
> *系统学分析*：王阳明提出“**心即理**”与“**致良知**”，强调道德判断与实践主体性的确立。本书将其比作“把道德评判责任下沉到行动主体（边缘计算）”。但良知所指为道德心性的自觉判断能力（“知善知恶是良知”），并非自然科学知识或全部经验事实的出厂预装；跨主体的公共知识与社会协作依然需要客观证据、论证与检验。

> 📊 **【计量经济史与政治学实证注疏 · 案例 3.5.2-C】（安德森“印刷资本主义与语言整合”与普鲁士 452 县识字率回归）**  
> *经典专著锚点*：安德森《想象的共同体》（*Imagined Communities*，首版1983；本段为论旨概括，非指定版次的逐字引文）讨论印刷资本主义、语言与民族共同体形成的关系。“语言整合”是本书的比较用语；“底层总线”亦为本书对符号传播条件的工程类比，不归属于安德森原句，也不据此推出统一或必然的历史路径。原典具体版次与页码仍须在引用展开时补齐。  
> *量化研究及识别边界*：Becker 与 Woessmann（2009, *Quarterly Journal of Economics*）利用普鲁士 452 县资料，以距维滕贝格距离为新教人口比例的工具变量。在其规格中，全新教县与全天主教县的识字率差，控制后 OLS 估计约为 9.9 个百分点，基准 IV 估计约为 18.9 个百分点。原文定位分别为表II第2列（第550页）及表III第2列（第559页）。因果解释依赖地理工具的外生性与排除限制。经济结果与识字率可以解释新教经济优势的大部、甚至全部相一致；这不是已识别的“100% 因果中介份额”，也不能直接外推为所有去中介化改革的普遍效应。 本书未独立复现这些估计，也不把工具变量的排除限制登记为已由本书验证。
> *核查来源*：[Becker & Woessmann (2009), Was Weber Wrong?](https://storre.stir.ac.uk/bitstream/1893/1653/1/BeckerWoessmann2009QJE.pdf)。
> *并置边界*：安德森的历史解释与普鲁士县级研究的对象、时期和结果变量不同；并列用于提出比较问题，不构成两者相互验证，识字率估计也不验证本书的去中介化类比。

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

> 💻 **【软件工程同构 · 案例 3.6.1-A】（企业级规范膨胀与轻量化架构反思）**  
> SOAP 1.2 的基础框架与企业部署中可叠加的 WS-* 扩展应分开讨论。安全、寻址、可靠消息等扩展有各自用途；当项目实际需求不足以抵偿配置、互操作和维护成本时，叠加才可能成为“WS-* 膨胀螺旋”。WebLogic/WebSphere 是可研究的商业部署实例，不是 SOAP 的必需运行环境，也不能仅由产品名称判定垄断或成本失控。
> Roy Fielding 于 2000 年博士论文中阐述了 **REST 架构风格**，包括统一接口、无状态等约束；JSON 则是可供接口使用的一种数据格式，REST 并不要求 JSON。**把多余的仪式拆掉，才叫减负；把所有安全与可靠性机制都叫赘肉，只会把账单搬到异常路径。** 本书的工程比较应在等效需求下检验配置工作量、变更成本、故障恢复和退出成本，不能从格式名称直接推出演进优势。
> *技术来源*：[W3C SOAP 1.2 消息框架](https://www.w3.org/TR/soap12-part1/)、[Fielding 博士论文第5章](https://ics.uci.edu/~fielding/pubs/dissertation/rest_arch_style.htm)、[RFC 8259：JSON 数据交换格式](https://www.rfc-editor.org/rfc/rfc8259.html)。

<a id="legacy-v11-1-sec-3-7-2"></a>
<a id="sec-3-6-2"></a>

#### 3.6.2 Scholastic Monopoly and the Pseudo-Indigenous-Research Trap: the Isomorphism of Paris Theology and Lysenkoism

**Normative Spec (规范条文).**

When a theoretical system originally aimed at "pursuing truth and liberating cognition" is monopolised by an exclusive privileged stratum during institutionalisation, and lacks external competition, exit channels, and empirical error-correction mechanisms, the system may breed an exclusive "ideological-censorship and rent-seeking structure." Through monopolising interpretive rights, accumulating compliance text beyond necessary protection boundaries, or "dogma-shelling" existing knowledge with no incremental contribution, it increases society's cognitive and coordination loss ($\lambda$).

> 📜 **【历史实证注疏 · 案例 3.6.2-A】（中世纪巴黎神学机构的经院化倾向与思想审查）**  
> *机构边界*：思想审查涉及大学神学机构、主教、教廷及世俗权力等不同主体。巴黎大学神学部、索邦学院及不同时期的相关称谓与组织边界须分别核实，不能合写成一个跨时期的排他机构；神学论辩、司法权限与教会筹资也不能相互替代。
> *系统学分析*：巴黎神学机构在欧洲知识体系中起到了强大的准入过滤与信誉背书作用，但不能概括为全欧洲唯一思想认证 CA，亦不直接等同于罗马教廷的教会财政与赎罪券销售体系。此处以此类比“高门槛的合规中介对经验科学探索的阻抗效应”。

> 📜 **【科学史注疏 · 案例 3.6.2-B】（冷战时期李森科主义的伪自研灾难）**  
> 李森科主义可用于讨论政治权力压制公开检验与科研纠错的风险；瓦维洛夫等人的遭遇须依具体档案与研究核对。政治标签不能替代遗传学实验，这是本例的批判焦点；不由此宣称所有遗传学家均被清洗，或把苏联数十年农业表现单独归因于一个学派。

> 💻 **【理论创新对比 · 案例 3.6.2-C】（哈耶克分散知识与价格信号论证（1945） vs 经院教条套壳）**  
> *哈耶克的论证与本书类比*：哈耶克在[《知识在社会中的运用》（1945），第525—527页](https://german.yale.edu/sites/default/files/hayek_-_the_use_of_knowledge_in_society.pdf)讨论分散、局部且不完备的知识与价格信号协调。其比较涉及集中全部相关知识与让个体借助价格变化调整行动两种要求；本书据此作“无需每个参与者获知全部背景细节”的工程类比，不把它当作测得的信息总量或社会成本优势。原文未给出最低信道损耗定理或计算死锁证明，也不主张价格调整总能达到完美均衡。
> *“换皮自研”的识别判据*：如果所谓创新只替换术语，却没有新增可区分的模型、证据、预测或工具价值，就应接受“换皮”的质疑。`git diff` 可启发对照，但不能替代思想史比较；这一判据同样约束本书，不能凭“经院”身份预先判定某学派从未有贡献。

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

> 📰 **【行政病理注疏 · 案例 3.7-A】（现代官僚黑话与行政死锁）**  
> *候选观察，尚非频度估计*：部分公文可见“切实压实责任、健全闭环协同、守牢底线”等表达。本例未界定组织生命周期的独立指标，也未提供时期、抽样框或出现频率，暂不称其为“科层制晚期”的普遍特征；后续须以独立阶段指标比较文本与实际任务，避免循环判定。
> *系统学分析*：若这些词语不能对应可核验任务、责任和例外，可能成为“免责 Padding 报文”；若用于必要协调，也可能有实际信息。应比较报表耗时、理解差错和恢复能力，再判断是否发生层层加码或“低功耗待机”，不能从词表直接诊断所有官僚的动机。

> 📜 **【财政历史注疏 · 案例 3.7-B】（英国“窗税”规避与法国旧制度“盐税”地下市场）**  
> *历史实证*：  
> 1. **英国窗税与规避行为**：[1850年4月9日英国下院辩论记录](https://hansard.parliament.uk/Commons/1850-04-09/debates/f9bfaf3f-56b7-45f1-af7b-8596ba670ac7/WindowTax)回顾1696年开征及后续税率变化，讨论堵窗避税、通风和居住条件。它提供当时议员的论证与转引材料；税制不同时期的档位须分开，辩论中的数字与健康主张不直接视为独立测量或已识别因果效应。
> 2. **法国旧制度盐税（Gabelle）的待核研究线索**：地区税制差异、食盐走私（*faux-saunage*）与执法冲突可作为财政规则和适应行为的研究题目。本节尚未给出地区、时期、税价差及可定位史料，因此暂不以“巨大价差”“武装走私”或“严重扰乱商业秩序”作为已核事实及已识别效果。须补税制、价格、征收或诉讼记录，再与运输成本、供给和执法条件等解释比较。
> *系统学分析*：税费规则的设计可能诱发微观主体的适应性规避与非正规市场替代。当合规负担显著扭曲经济激励时，主体通过改变物理资产形态或转向非正规交易进行避险，展现了微观节点在刚性财政约束下的内生博弈反应。

> 📜 **【假设性司法失效示例 · 案例 3.7-C】（通配符过载）**  
> *假设情境*：设某惩戒规则把日常无害行为直接编码为有罪信号，且不允许反证与复核。本例用于分析此类规则的误报机制；对应真实审判时须另提供案件与规则文本。  
> *系统学分析*：这可类比 **Wildcard Regex Overmatching 与 Panic 滥用**。把不具诊断力的行为当罪证，又封死复核接口，惩戒就可能退化为恐怖游戏；是否对应某一真实审判，须另以案件与规则文本举证。

> 📰 **【待检验机制情境 · 案例 3.7-D】（DEI 标签与合规成本）**  
> *研究问题*：若某组织的 DEI 分类与培训不断增加，新增要求是否改善公平与任务结果，还是增加理解、举证和合规负担？须指定组织、制度版本、时期、支出与结果，区分组织调整、法律约束和市场变化。本例是研究设计，企业变化与该机制的关系尚待逐案检验。  
> *系统学分析*：若新增标签没有改善权利保障，却由排他顾问把持解释权，可用“WS-* 死亡螺旋”提出可反驳的批评；若分类改善救济且收益超过成本，该寄生解释便不成立。既不能凭 DEI 名称判恶意，也不能用公平口号豁免成本、举证与纠错审查；企业变动和选举更不能反过来充当这一机制的单因果证明。

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
