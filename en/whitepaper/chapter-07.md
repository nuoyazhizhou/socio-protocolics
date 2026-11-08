> **Translation record**
> - Chinese source: `社会系统协议学白皮书.md`, block `chapter-07` — 195 lines, 29819 bytes, block sha256 `d411ff2bc9ee70f34b81b61c0778d0fb8cd4764d1c227eec50a149abe1b2b355`, taken as the content between the `<!-- SP:BEGIN chapter-07 -->` and `<!-- SP:END chapter-07 -->` markers and reported by `tools/whitepaper_blocks.py list`; whole-file sha256 `d5ffb73e3db73f8bb42a2ecb39871bf6c55eace8bb72111b63a2ee362134d9c8`, 338639 bytes, 2026-11-08
> - Chinese version / release tag: `v11.2-r20261106` (theoretical version remains v11.2)
> - Translation version: `en-v0.1-ch07`
> - Translation date: 2026-11-08
> - Check status: draft; C12 self-check run after write; independent read-only audit to follow; machine and glossary checks only; no independent professional native-speaker review
> - Pending sync: none at present; to be recorded item by item if the Chinese source is updated
> - Status: phased translation of this chapter block — the normative framework text, RFC 7.1 (SP-RFC-017) and 7.2 (SP-RFC-018) specification texts, the §7.3 normative specs, and the §7.2 candidate-operationalization block are translated; the case-annotation blocks (cases 7.1-A, 7.1-B, 7.1-C, 7.1-D, 7.2-A, 7.2-B, 7.3.1-A, 7.3.1-B, 7.3.2-A, 7.3.2-B) are **retained in the original Chinese** by design under the C-1 phased plan (T3 not yet passed), so those blocks are held untranslated inside this file
> - Authority: the Chinese SSOT is authoritative; this translation does not constitute a separate set of definitions (C2)
> - Note on group name: **internal inconsistency found and flagged for maintainer reconciliation** — the SSOT chapter-07 heading reads "第六组：迁移核算与试验筛选" (gloss: Migration Accounting & Trial Screening), whereas the book-wide locked form (overview tables, the already-landed appendix and chapter-01, and the C12 locked ledger line 14) reads "第六组核心命题：技术债核算与演化筛选" → "Proposition Group VI: Debt Accounting & Evolutionary Selection". This translation follows the locked/whole-book form for consistency (same precedent as Group II and Group IV); the SSOT heading variant is left to the maintainer to reconcile. RFC 017's own title ("迁移净负担与技术债核算" → "Migration Net Burden and Technical-Debt Accounting") and the body's "迁移核算" (migration accounting) are kept as the specific RFC-level term, distinct from the group name.
> - Note on link repointing: the cross-chapter anchors `[G017]`/`[G018]` (evidence cards) and `[SP-RFC-004]` are re-pointed to the Chinese source `../../社会系统协议学白皮书.md#…`; `[SP-RFC-017]` is a same-page anchor in this file and stays. The Chinese narrative text and the verbatim case blocks remain as in the SSOT.

**Scope and edition status.** This file is one block of a **phased** translation. The English edition as a whole is an *abridged adaptation* of the v11.2 whitepaper: the six chapters that carry case-annotation sections are not yet translated, and those annotations remain untranslated by design until the underlying Chinese case materials pass the real-case acceptance stage (T3). Chapter 7 carries case-annotation sections (cases 7.1-A/B/C/D, 7.2-A/B, 7.3.1-A/B, 7.3.2-A/B); per the C-1 phased plan those annotations are **retained in the original Chinese** inside this file, so the normative framework text, RFC 7.1, RFC 7.2, and the §7.3 normative specs are translated while the case-annotation blocks are held in Chinese. Completeness of this block does not imply completeness of the edition, and this translation does not elevate any claim to established status. The block itself runs from the `<!-- SP:BEGIN chapter-07 -->` marker to the `<!-- SP:END chapter-07 -->` marker; the translation record, the chapter glossary and the two notes below precede that boundary and are not part of the translated text.

## Chapter Glossary — Chapter 7

| Chinese | English used in this file | Remark |
| :--- | :--- | :--- |
| 第六组核心命题：技术债核算与演化筛选 | Proposition Group VI: Debt Accounting & Evolutionary Selection | group name, unique form in the whole book (locked form; SSOT heading variant flagged) |
| 6 个核心命题组 | 6 Core Proposition Groups | H3-A landed |
| 19 项有效 SP-RFC | 19 Effective SP-RFC Items | title-case unique |
| 迁移净负担与技术债核算 | Migration Net Burden and Technical-Debt Accounting | RFC 017 title |
| 多分支试验与成熟反馈筛选 | Multi-Branch Trial and Mature-Feedback Screening | RFC 018 title |
| 核算定义与方案比较 | accounting definition and option comparison | claim identity (017) |
| 条件概率模型、经验筛选与设计规范 | conditional-probability model, empirical screening, and design norm | claim identity (018) |
| 增量旁路（Strangler Fig Pattern） | incremental bypass (Strangler Fig Pattern) | §7.1 engineering guideline |
| 大集市（Bazaar） | Bazaar (mode) | §7.2 analogy |
| 大教堂（Cathedral） | Cathedral (mode) | §7.2 analogy |

**Convention on link re-pointing.** Every in-page anchor that lives in another chapter (`#rfc-evidence-XXX`, `#sp-rfc-004`) is re-pointed to the Chinese source `../../社会系统协议学白皮书.md#…` so the build does not report a missing anchor; these resolve once the corresponding English chapter lands. Anchors that live in this file (`#chapter-7`, `#sp-rfc-017`, `#sec-7-1`, `#sec-7-2`, `#sec-7-3`, `#sec-7-3-1`, `#sec-7-3-2`) remain same-page links.

<!-- SP:BEGIN chapter-07 -->

<a id="chapter-7"></a>

## Chapter 7 — Proposition Group VI — Debt Accounting & Evolutionary Selection

<a id="sp-rfc-017"></a>
<a id="legacy-v11-1-sec-7-1"></a>
<a id="sec-7-1"></a>

<a id="legacy-v11-1-rfc-019"></a>
<a id="legacy-v11-0-rfc-021"></a>

### 7.1 SP-RFC-017 | Migration Net Burden and Technical-Debt Accounting

**Claim identity:** accounting definition and option comparison.
**Dependencies and additional conditions:** P1 budget background; same task, lifecycle, price, and discounting basis.
**Generation and evidence card:** [G017](../../社会系统协议学白皮书.md#rfc-evidence-017).

**Normative Spec (规范条文).**
Finite resources and irreversible time bound the feasible set of options, but they do not by themselves prove that the total volume of technical debt is conserved, nor that every system must incur some fixed number of defects. This item requires comparing the net burden of maintaining the old system against migrating to a new system under one and the same task boundary, lifecycle, price, and discounting basis:
$$\Delta \text{Burden}_{\text{net}} = \text{NPV}\left(\text{Cost}_{\text{migration}} + \text{Loss}_{\text{implicit}} + \text{Maintenance}_{\text{new}}\right) - \text{NPV}\left(\text{Debt}_{\text{legacy}}\right)$$
where $\text{Cost}_{\text{migration}}$ is the switching/adaptation expenditure, $\text{Loss}_{\text{implicit}}$ is the fault-tolerance experience that may be lost, and $\text{Maintenance}_{\text{new}}$ is the operating/maintenance burden of the new system; $\text{Debt}_{\text{legacy}}$ is the comparable burden of continuing to maintain the old option, avoiding double-counting the same outlay within it — here "double-counting" means the same outlay inside one option being entered twice; the migration option and the continue-old option are counterfactual comparisons of each other, not two cash flows realised at the same time, so the old maintenance appearing on both sides does not constitute double-counting. During the transition, old-system maintenance, dual-track joint debugging, and new-system maintenance must be itemised and assigned ownership separately, and compared against the old option over the same observation period. $\Delta\text{Burden}_{\text{net}}<0$ means the net burden is reduced within this accounting boundary; it does not mean all rights, fairness, and safety constraints are already satisfied; the net burden must be split by bearing subject into cost, compensation or transfer, and risk, and a negative total does not rule out cost-shifting between subjects. Each item may carry error; assumptions and sensitivities must be reported, and one cannot presuppose that implicit assets are necessarily positive.

The following are risk hypotheses, epistemic constraints, and engineering-implementation suggestions related to migration accounting; **they are not derived from the above accounting definition alone**. The occurrence conditions, frequency, and impact of the risks must be tested separately, and the choice of a norm must state its objective and cost.

* **Risk hypothesis A: perfect preconditions and analysis paralysis (Analysis Paralysis Risk):**
  When "eliminate all historical technical debt and reach a flawless architecture" is set as a precondition for action, sustained planning, dispute, and rework may crowd out delivery and maintenance resources. Whether analysis paralysis occurs should be compared, within a pre-fixed task, budget, and deadline, against decision waiting, rework cost, and effective delivery; one cannot judge the system stalled directly from "pursuing perfection", nor treat necessary review or evidence-based deferment of action as paralysis wholesale. This item is a to-be-tested risk judgment, not an accounting-style mathematical inference.
* **Risk hypothesis B: radical overhaul and loss of implicit assets (Radical Overhaul Risk):**
  If the replacement fails to identify or verify the still-useful boundary handling, collaboration conventions, and fault-tolerance experience in the old system, migration may lose implicit assets and add failure, coordination, or recovery burden. Loss of implicit assets must be independently confirmed by the old mechanism's actual operating function and historical repair records in production, and cannot be reverse-inferred after a refactor fails. This section does not yet give an occurrence-frequency or effect-size estimate; specific testing requires a separately designed comparison. The old mechanism may also mainly retain net harm or privilege rent; one cannot presuppose its value is necessarily positive. Full replacement, in-place repair, and incremental bypass (Strangler Fig Pattern) must be compared within the same task and lifecycle for cost, benefit, risk, and rights impact; no approach is assumed universally optimal, nor is a single failure taken as proof that "rewrites always fail".
* **Epistemic self-referential constraint: this book also accepts migration accounting (Epistemic Self-Referential Constraint):**
  **SP-RFC-017 also constrains *Sociological Protocolics* itself.** It does not presuppose the next refactor is necessarily better, nor that the next layer of abstraction is necessarily higher. Conventions and compromises may retain a "survivor Catch-Block fault-tolerance library", but may also retain sustained harm and unproductive rent; retention or replacement must both be evidenced, one cannot take "having survived to the present" as proof of validity, nor overturn everything solely on theoretical elegance.
* **Engineering implementation guideline: out-of-band trial and incremental migration (Strangler Fig Implementation Guideline):**
  **"Out-of-band spec probing (Out-of-Band Spec), host-traffic incremental migration (Strangler Fig Migration)."** Out-of-band exploration and in-production migration set their budget, safety, rights, and evaluation conditions separately; the sandbox trial is used to obtain evidence, not on the premise that the alternative is already proven superior. When in-place repair is ineffective or too costly, and the alternative's expected net benefit, rights protection, and risk are acceptable, the verified option may be considered for incremental hook-in to the production trunk. Migration retains necessary compatibility interfaces, incremental diversion, and a revertible boundary, and states each item's applicable conditions; one cannot derive from a "deadlock" label alone that a full rewrite is required. Maintenance of this book continues to obey the established incremental-revision boundary.

> 💻 **【软件工程与架构反思 · 案例 7.1-A】（Netscape 重写争议与既有修复经验的迁移风险）**  
> *工程评论来源*：Joel Spolsky 的 [Things You Should Never Do, Part I](https://www.joelonsoftware.com/2000/04/06/things-you-should-never-do-part-i/)以 Netscape 的重写决策批评丢失既有修复经验的风险。这是可争论的工程案例与判断；本文不把未在此给出统计口径的市场份额或公司衰退完全归因于重写。  
> *系统学分析*：老代码的丑陋可能承载真实边界处理，也可能只是负担。应比较测试覆盖、迁移成本、竞争环境与替代路径；未知 Bug 属于需估计的迁移风险；一次商业竞争结果不能证明所有重构必败。

> 💔 **【微观亲密关系与组织治理 · 案例 7.1-B】（“完美伴侣/完美下属”幻觉与代价重分配）**  
> *机制假设情境（非统计结论）*：更换关系或组织结构可能减少既有摩擦，也可能引入新协调成本；存在改善、恶化及无明显变化等不同结果。本例用于提示迁移时核算隐性资产，不报告“相当比例”“无一例外”或固定数量级的未知Bug为已经测得的社会学事实。
> *系统学结论*：**成熟的架构师不追求“没有技术债的乌托邦”，成熟的架构师懂得“哪一种技术债是我当下愿意且有能力承担的权衡（Trade-off）”。**

> 📜 **【宏观文明演进与激进乌托邦 · 案例 7.1-C】（王安石变法与法国大革命恐怖时期：候选比较）**  
> *候选比较，非已识别的因果结论*：  
> 1. 王安石变法涉及多项政策与执行争议，可研究地方信息、财政激励、推行速度和纠错能力；不能将不同政策与阶段压成一次“全量并发重写”，再以此断定基层整体休克；*史料缺口*：本条未给出王安石变法的一手史料出处，分期与评价须另行核验，候选史籍仅作检索方向，不构成已完成的出处核对；  
> 2. 法国大革命恐怖时期可作为战争、内部政治竞争、财政状况与惩戒制度相互作用的候选比较。应分别核验资源压力（`P1/O5`）、程序抗辩与权利救济（`SP-RFC-009/011`）的变化，以及它们与暴力升级的时序关系；不预设外部压力或纯洁性观念能够单独解释恐怖政策，也不把“道德技术债清洗”当作已识别原因；  
> *文献入口与缺口*：[William Doyle，The French Revolution: A Very Short Introduction，第2版（OUP，2019）](https://academic.oup.com/book/28443)。本轮只核书目、目录与摘要，未通读相关章节；具体战争、叛乱与指券变化的时间范围、作用及不同史学解释仍待逐项定位，不能用这一入口替代事实链或学派共识的核验。
> *系统学批评*：清除“所有不完美的人”不能代替修复制度接口。若以纯洁口号封死反证与救济，重构就可能摧毁适应能力；但不完美本身也不自动有益，应区分容错资产和持续伤害。

> 🏛️ **【宪政容错工程与普通法实证 · 案例 7.1-D】（麦迪逊天使悖论与普通法的 Catch-Block 库）**  
> *宪政文本与工程解释*：[《联邦党人文集》第51篇（1788-02-06），Founders Online](https://founders.archives.gov/documents/Hamilton/01-04-02-0199)讨论政府既控制被治理者、又约束自身的困难，可启发防御性编程、权力制衡与Watchdog类比。该文本不能证明制宪会议全部议程仅针对异常路径，也不提供现代BFT算法的故障模型或安全性证明；正常治理能力与滥权防护须同时评估。
> *法律文本与机制比较*：[1966年7月26日司法先例实践声明](https://publications.parliament.uk/pa/ld199697/ldinfo/ld08judg/redbook/redbk-04.htm)同时强调先例的确定性、适度改变的必要性，以及追溯变动对契约和财产安排的影响。它可启发 Catch-Block、兼容与增量更新的比较，但不能证明普通法整体优于法典制度，或用一份声明解释数百年制度连续性。

<a id="sp-rfc-018"></a>
<a id="legacy-v11-1-sec-7-2"></a>
<a id="sec-7-2"></a>

<a id="legacy-v11-1-rfc-020"></a>
<a id="legacy-v11-0-rfc-022"></a>

### 7.2 SP-RFC-018 | Multi-Branch Trial and Mature-Feedback Screening

**Claim identity:** conditional-probability model, empirical screening, and design norm.
**Dependencies and additional conditions:** branch success/failure, independence, fixed probability, budget, and observation window to be set separately.
**Generation and evidence card:** [G018](../../社会系统协议学白皮书.md#rfc-evidence-018).

**Normative Spec (规范条文).**
When the state space, uncertainty, and computational demand of a given task exceed a single node's resources or knowledge capacity, comparing multi-branch exploration against a single-branch option may be considered. Finiteness alone does not prove that every finite task cannot be exhausted centrally, nor that parallel net benefit is necessarily positive. Whether there is gain depends on task, budget, branch correlation, cost, consequence observation, and screening; the following probability, feedback, and governance conditions each bear their own burden of argument:

1. **Parallel experimentation mechanism (Parallel Experimentation / Racing, $K \ge 1$) and its preconditions:**
   First fix $K$, the task, the mature observation period, the budget, and each branch's success probability $p_k$, and require the success/failure events to be mutually independent, only then can one write:
   $$P_{\text{evolution}}(K) = 1 - \prod_{k=1}^{K} (1 - p_k)$$
   Considering the Merge Maintainer's cost of evaluating, verifying, and conflict-resolving multi-branch results, $C_{\text{merge}}(K)$ (its relation to branch count $K$ must be modelled or estimated separately by organisational form, shared verification, and conflict structure, with no monotonic or super-linear assumption), the general form under a finite budget constraint is written as:

$$\sum_{k=1}^K \text{Cost}_k + C_{\text{merge}}(K) \le \text{Budget}$$

   Only when each branch's trial cost is constant $\text{Cost}_{\text{fork}}$ and the merge-coordination overhead is negligible ($C_{\text{merge}}(K) \approx 0$) does it simplify to $K\cdot\text{Cost}_{\text{fork}}\le\text{Budget}$. The budget formula only delimits the feasible set of options; it does not fix the sign of net evolutionary gain. Under a given budget, adding branches may change single-branch investment, success probability, and merge cost; whether net benefit falls also requires defining success value, the relation between investment and success probability, screening error, and deployment cost before comparison. When there are common failure sources or inter-branch resource crowding, a joint model should be built separately; "sufficiently heterogeneous" cannot substitute for mutual independence. If one discusses approaching 1 under infinitely many branches, additional sufficient conditions such as $\sum_kp_k=\infty$ may be added; this is not the realistic premise of a finite-budget trial.

2. **PDCA feedback loop and result-latency constraint:**
   Each trial branch iterates via **Plan $\to$ small-step Do $\to$ pain-point Check $\to$ prune wrong branches and correct (Act)**. But under the direct-observation-result and single-window screening design discussed in this book, the feedback cycle usually needs to be longer than the observable latency of critical consequences ($\Delta t_{\text{feedback}} \ge T_{\text{latency}}$), while shorter than the time scale at which the macro environment undergoes qualitative change; this inequality is an engineering-parameter constraint under a specific trial framework, and does not exclude alternative governance schemes introducing multi-time-scale nested feedback, dynamic continuous updating, or high-frequency proxy indicators, nor may it serve as a universal necessary condition for all effective organisational learning. If short-term proxy indicators diverge from long-term goals, prematurely pruning options whose long-term consequences have not yet appeared may increase the mis-selection risk biased toward short-term performance; direction and magnitude must be tested by observation latency, screening rules, and comparison results.

3. **Bazaar maintainer and kernel-injection mechanism (Bazaar Maintainer & Merge Interface):**
   The architect acts as the **evolutionary racetrack gatekeeper and trunk merge maintainer (Merge Maintainer)**: protecting real feedback, screening branches by the mature observation period and extracting a minimal Linter norm, then performing a revertible incremental merge (`git merge`). The trunk may be a self-governing project, a community protocol, or an industry standard; only when the target requires nationwide mandatory enforcement, public taxation, or statutory education standards must it enter the corresponding national-authorisation interface (`Syscall`) to reach Ring-0.

**Discovery—screening—deployment—migration interface:** the four stages each bear their own evidence; the subsequent success is not written into the definition of a "successful branch". The table below is the interface spec of this trial design, not a new theorem derived from the independent probability formula.

| Stage | Inputs and conditions | Output | Evidence and stop/revert conditions |
| :--- | :--- | :--- | :--- |
| Discovery | Pre-fix task, success criterion, observation period, all branches, budget, and success/failure correlation structure | At least one candidate meeting that criterion; use the probability formula above only when independent | Retain failed and unobserved branches, probability estimates, and common failure sources; switch models if conditions fail, do not reverse-infer independence from survivor count |
| Screening | Mature consequences, measurement error, long-term goals, and comparison schemes; disclose maintainer conflicts of interest | Candidate ranking and uncertainty; may choose not to merge yet | Report false-elimination / false-retention, deferred effects, and review; retain branches or adjust observation design when sample insufficient or long-term consequences not yet apparent |
| Deployment | Verified candidate, actual operating resources, failure and rights boundary; targets needing national authority verified per 014 | Scoped, time-bound, revertible trial deployment; self-governing targets use applicable self-governing procedure | Inadequate authorisation does not prove efficacy, 016 receipt does not bear authorisation; if protection constraints fail, suspend, recover, or review |
| Migration comparison | Trial-deployment results and the old, repair, and alternative options under the same task and lifecycle | Account net burden per 017, inter-subject cost, and sensitivity, then choose | Count exploration, screening, merge, and deployment cost, avoid duplication; when rights, safety, or bearable risk are unsatisfied, even if burden falls, do not auto-migrate on that basis |

Discovery probability is not equal to correct-selection probability, still less to deployment probability or net-benefit probability. When there is neutral drift, historical lock-in, selection bias, or goal change, each should be recorded separately; "final survival" cannot be reverse-defined as long-term optimal.

```text
              Evolutionary racetrack and PDCA falsification mechanism (Bazaar Engine vs Cathedral Deadlock)
 [Bazaar mode]: multi-branch within budget (K > 1) + limited feedback window (T_latency <= Delta t < T_environment)

   Fork-1 (folk scripts / Linux 0.01 / Chrome Canary)        --> [real anomaly report (Check)] -+
   Fork-2 (local dialect / 386BSD / Xiaogang village HRS)      --> [real anomaly report (Check)] -+->
   Fork-K (open-source lib / GNU Hurd / Shenzhen SEZ)          --> [real anomaly report (Check)] -+
                                                                            |
                                                                            v (Act: rapid iterative fix)
   winning branch emerges --> [Key Person / Merge Maintainer: extract norm Linter] --> [merge into self-governing / industry trunk; Syscall when national authorisation needed]

 [Cathedral mode]: single-threaded top-down design (K = 1) + feedback loop tending to block (illustrative quantity, not a defined measurable metric)

   central omniscient blueprint (K=1) --> stress test under anomalous-path pressure (non-proportional) --> [subordinate padding / concealment to mask]
                                                                            |
                                                                            v (Check-Act loop broken)
   possible feedback failure, adaptation lag, or coordination failure; must be tested with task data and alternative explanations
```

*Diagram note:* the figure above depicts the failure scenario of "single branch with feedback loop tending to block", **not a definition of all centralised or closed-source systems** — centralised systems may equally possess feedback channels. Fork-1 / Fork-2 / Fork-K are **illustrative**, not measured counts, and do not determine the value of $K$ in a specific situation.

> 💻 **【操作系统与网络史实证 · 案例 7.2-A】（Linux 早期发布、TCP/IP 与 OSI 路线竞争、Chrome 多通道试验）**  
> *工程史实*：  
> 1. **Linux早期发布与分支比较**：[Linux 0.01原始发行说明](https://www.kernel.org/pub/linux/kernel/Historic/old-versions/RELNOTES-0.01)公开源码，明确自称未成熟、硬件支持有限，并请求使用者协助移植。它支持讨论开放试用与反馈接口。GNU Hurd、Plan 9、MINIX、BSD与Linux有不同目标、时点和资源，不能当作同一预算下随机分配的试验组；本例不据最终采用规模倒推某种架构或PDCA必胜。
> 2. **TCP/IP与OSI路线竞争**：体系模型、协议实现和产业采用须分别讨论。TCP/IP逐步获得广泛采用，但OSI并非全部“死于纸面”；IS-IS等机制实际进入IP及双栈网络。市场结果涉及实现、互操作、部署和组织条件，不能单凭“顶层设计/民间试错”标签认定唯一原因。原始例证见[RFC1195](https://www.rfc-editor.org/rfc/rfc1195)。
> 3. **Chrome的多通道试验**：Chromium团队2010年8月2日发布的[Google Chrome in a Coal Mine](https://blog.chromium.org/2010/08/google-chrome-in-coal-mine.html)说明，Canary在此前数日推出，拟比Dev更频繁更新、容纳高风险改动，并允许与较稳定通道并存。它可支持“试验分支与主干隔离”的接口比较，不证明更新越快越好，也不能单独解释Chrome与IE的市场变化。

> 📊 **【制度哲学与跨国治理注疏 · 案例 7.2-B】（哈耶克自发秩序、波普尔进化认识论与中苏体制演化分流）**  
> *经典理论与本书解释*：哈耶克关于分散知识与秩序的讨论、波普尔的问题—试探—纠错图式，可为分支试验与反馈提供启发；这是本书的工程映射，不能把思想来源当作本书算法的原典证明，也不能由相似图式推出严格同构或最优性。另须区分两个层面：全局计划与参与者在局部规则下作选择并非同一层面的主张，局部规则下的有意维护与自发秩序不天然冲突；可研究维护者的控制范围与利益冲突，不预设此处存在理论冲突。
> *苏东剧变与 1978 中国改革的演化动力学分流*：  
> 1. **苏联体制研究线索**：可研究集中计划、指标报告与纠错渠道的具体运作；不能把所有时期与组织一概设为 $K=1$、零反馈，再由解体倒推出“热力学雪崩”。政治、资源、国际环境及内部改革均须纳入替代解释；  
> 2. **改革开放研究线索**：地方试验、政策反馈和渐进调整可作为多分支与增量合并的比较对象。分支权、独立性、国家支持、试验成本、选择偏差和成熟观察期需独立测量；不能由成功追认“最高效 PDCA”，也不把其他国家转型差异归于单一迁移策略；  
> 3. **企业赛马研究线索**：可考察移动产品开发中的并行团队、资源和筛选过程。微信的团队数、启动时点与迭代周期须以企业原始记录核验；本例不把未定位的精确数量与发布频率当作已证参数。

> 🔬 **Candidate operationalization and application-model falsification · §7.2**
> 1. **Evolution-effectiveness measurable operators:**
>    - **Active racing-branch count**: $K_{\text{active}} = \sum_{i=1}^n \mathbb{I}(\text{Fork}_i \text{ has an independent production runtime environment and heterogeneous trial rights})$; this count does not measure independence — branches that are heterogeneous but share a failure source can still be counted into $K_{\text{active}}$, in which case the independent-product formula above must not be applied and a joint model built separately;
>    - **PDCA loop period**: $\overline T_{\text{PDCA}}=t_{\text{Act}}-t_{\text{Plan}}$, should satisfy $T_{\text{latency}}\le\overline T_{\text{PDCA}}<T_{\text{environment}}$; if no such feasible window exists, adjust the observation period, task, or trial design, and do not solve it by mechanically raising frequency.
>    - **Feedback-completeness candidate indicator (Feedback SNR)**: real anomalies must be defined by independent logs, sampled verification, and omission rate; one may compare verified error reports against record completeness, but cannot directly measure feedback quality with "error-text volume / compliance-text volume". Here SNR is an engineering analogy, not the Shannon physical signal-to-noise ratio.
> 2. **Counterexample judgement and applicable boundary**: pre-register task, budget, mature observation period, branch success rate and independence, comparison group, and minimum predicted gain. When the premises are independently verified and estimation precision suffices, if the comparison data exclude the predicted gain range, reject that application model. Each instance's to-be-tested prediction must register the outcome variable and prediction direction or interval before observation; instances that do not pre-give the outcome variable and prediction direction or interval are descriptive only, and do not claim to have completed prediction testing. This item does not require all application predictions to be positive-gain, nor sets a uniform gain threshold, $\Delta$, or confidence level. A $K=1$ system prospering continuously does not falsify the probability-racing formula; when no feasible feedback window exists or common failure sources are present, a separate model should be built, and "real feedback" must not be defined after the fact by success or failure.

<a id="legacy-v11-1-sec-7-4"></a>
<a id="sec-7-3"></a>

### 7.3 Architecture and migration case comparison

"Cathedral / Bazaar" in this book are two lenses for comparing control rights, interface openness, and trial style; they do not exhaust organisational types. Closed-source, centralised, compatibility burden, and branch exploration are not the same dimension; real systems may mix them; historical comparison must be verified separately.

*Identity of the cases in this section:* the following case comparisons are used to raise testable comparison questions and implementation suggestions; they are candidate comparisons and normative suggestions, not newly added accounting definitions or probability clauses; borrowing the conditional model of [SP-RFC-004](../../社会系统协议学白皮书.md#sp-rfc-004) does not equal establishing another accounting definition.

**Comparison index of human organisation and operating-system routes**

| Operating-system route | Comparison object and applicable boundary |
| :--- | :--- |
| 1. Windows mode<br>(compatibility-layer maintenance) | The Holy Roman Empire / Habsburg may serve as a comparison object for existing interfaces and alliances; compatibility benefit, rent-seeking cost, and failure recovery must be accounted separately, and one cannot directly infer imperial collapse |
| 2. Linux mode<br>(open spec and native development) | North American constitutional founding / UNIX-C may serve as a comparison object for interface recombination; reducing some coupling still has historical assets, migration, and ecosystem cold-start cost, with no presupposed "clean slate"; this mapping applies only to the dimension "textual interface spec + derivable implementation": the Constitutional Convention's closed deliberation and the public debate in the publication and ratification stages must be verified by period, and the confidentiality of the deliberation stage cannot deny its subsequent openness |
| 3. iOS / hybrid-kernel mode<br>(core standard and franchise access) | Early-modern mercantilist franchise system, Roman Empire and High-Tang statute law may serve as research clues for access, central rule, and local implementation; central control, local custom, and franchise scope must be verified by period, and not directly lumped as the same walled garden or hybrid architecture |
| 4. Android mode<br>(open base and branches) | Hundred Schools of thought / vernacular-language spread may serve as a comparison object for diversity exploration; adoption scale, version divergence, and maintenance cost must be verified by period, overall, and task |

<a id="legacy-v11-1-sec-7-4-1"></a>
<a id="sec-7-3-1"></a>

#### 7.3.1 Compatibility-layer trap vs clean-slate refactor: comparing compatibility burden and migration options

**Normative Spec (规范条文).**
A centralised system may pursue consistency through control rights and unified review, but may also form exclusive interfaces and compatibility burden; net contribution must be compared against feasible alternatives. Only when satisfying the same-basis, serial, and no-new-output-or-recovery-path conditions of [SP-RFC-004](../../社会系统协议学白皮书.md#sp-rfc-004) is the conditional retention rate $\eta_n=\prod_i(1-\lambda_i)$ used, where $\lambda_i$ is the loss rate of layer $i$ relative to its input; layer-wise conditional ratios multiplied do not require statistical independence, and must not be confused with the independent success/failure events of 018. Social application must be measured independently, and one cannot directly equate efficiency loss with an organisation crossing its survival threshold. A clean-slate refactor (Clean-Slate Spec) in an isolated sandbox may try to reduce historical coupling, but must compare in-place repair, full replacement, and incremental bypass per [SP-RFC-017](#sp-rfc-017), accounting for migration, adaptation, governance, ecosystem cold-start, and implicit robust-asset loss, and stating rights, safety, and revert conditions; no migration approach is assumed universally optimal.

> 📜 **【历史实证注疏 · 案例 7.3.1-A】（神圣罗马帝国的特权兼容负担：查理四世、哈布斯堡与三十年战争分期取证）**  
> *文本定位与比较问题*：伏尔泰在[《风俗论》第70章（Garnier版第11卷，法文转录）](https://fr.wikisource.org/wiki/Essai_sur_les_m%C5%93urs/Chapitre_70)讥讽神圣罗马帝国“既不神圣，也不罗马，更非帝国”。这是作者的评价，不能作为帝国不存在治理能力的事实证明。皇帝、帝国议会、法院与邦国、市镇的具体权限和协商过程，仍须按时期与制度材料核验，不概括为底层治理完全受制于旧特权。
> *系统学分析*：既有特权契约与协调接口可用于提出兼容收益和维护负担的比较问题。三十年战争中的财政、军事与政治条件须另有史料检验；不能把战争直接写成帝国因“转译效率趋零”而消亡，也不能由层级数量断定死锁。所引伏尔泰讥讽的论述对象与其成书时期相关，与哈布斯堡时期及三十年战争须分期取证，不能相互替代。

> 💻 **【软件工程同构 · 案例 7.3.1-B】（从 Multics 到 UNIX/Linux：设计借鉴、独立实现与生态依赖）**  
> 1960 年代末，贝尔实验室、GE 和 MIT 联合开发 Multics 操作系统，由于设计目标过于庞杂及多方协调成本高昂，贝尔实验室于 1969 年退出项目。随后 Ken Thompson、Dennis Ritchie 等人在**借鉴** Multics 诸多开创性思想（如分层文件系统与文本接口理念）的基础上，探索极简实用主义的计算环境，创造了早期 UNIX。Linus Torvalds 后来开发的 Linux 宏内核同样强调紧凑实用与高效模块化。  
> *维度区分与来源*：上述过程包含三个**不同维度**，不能互相替代或合并——**(a) 设计思想借鉴**：UNIX／Linux 承袭 Multics 的部分理念；**(b) 代码独立实现**：[Linux 0.01 原始发行说明](https://www.kernel.org/pub/linux/kernel/Historic/old-versions/RELNOTES-0.01)明载 “uses no code from minix or other sources”；**(c) 宿主与生态依赖**：同份说明载明内核 “has been made under minix”、早期需以 minix 引导，且文件系统 “needed to be minix compatible for practical reasons”。因此本例属“借鉴＋独立实现＋宿主依赖”的混合，**既不是零继承的纯净重写，也不能据此称为既有系统的增量重构**。UNIX 一系的演进另见[Dennis Ritchie，The Evolution of the Unix Time-sharing System](https://pdos.csail.mit.edu/6.828/2008/readings/ritchie79evolution.html)（作者回忆，属一手叙述，不等于本书工程类比的证明）。本节不以后续采用规模反证架构优越。

<a id="legacy-v11-1-sec-7-4-2"></a>
<a id="sec-7-3-2"></a>

#### 7.3.2 Walled Garden vs Open Reach: the governance-philosophy mapping of iOS and Android

**Normative Spec (规范条文).**
Open specs and branch rights may lower some access cost and permit heterogeneous trial; benefit depends on resources, maintenance, coordination, and exit conditions. Version fragmentation, malicious middleware, and common dependencies may also raise cost; disaster resilience and adoption rate must be compared against feasible alternatives.

> 💻 **【软件工程同构 · 案例 7.3.2-A】（iOS 平台佣金、围墙花园与合规边界争议）**  
> 苹果 iOS 是极致的大教堂模式：统一的 UI 规范、严格的 App Store 审核准入、核心分发与审核接口由平台控制。它提供了极高的一致性与安全性。但 App Store 历史上对应用内数字交易普遍征收 30% 佣金（自2021年起对符合资格的小型开发者适用15%费率）；不同地区、订阅期与交易类型的差异本节未核，须另取来源，引发了开发者阵营（如 Epic Games 诉讼）与多国监管立法（如欧盟《数字市场法》DMA 第6(4)条要求被指定的守门人允许第三方应用商店或网页分发，地域范围为欧盟，义务主体限于被指定的守门人；法条全文本节未逐条复核）关于平台排他性抽税与合规成本的激烈争议。 费率适用须按账户资格、交易类型、地区和当年条款核对；[Apple小型开发者计划公告](https://www.apple.com/newsroom/2020/11/apple-announces-app-store-small-business-program/)覆盖小型开发者资格与生效节点，不覆盖后来所有地区、订阅期与交易规则，此类差异须另取来源，本节按待核处理。

> 💻 **【软件工程同构 · 案例 7.3.2-B】（Android 开放底座与平民识字、白话文普及：候选比较）**  
> *候选比较，非已识别的因果结论*：谷歌的 Android（基于 AOSP）在智能终端市场获得广泛采用，涉及开源授权、硬件多厂商适配与应用分发生态等多重条件。可据此提出“降低接入与运行门槛有助于技术普及”的候选解释，并与历史上的**平民识字与白话文普及**作比较。两者的中间机制并不相同：工程接入门槛、识字教育与师资供给、出版与发行渠道、标准制定须分别取证，不能互相替代。采用规模本身不能证明门槛效应，也不能据此判定某种制度安排最优；本节不因尚未完成大规模计量而禁止讨论，但其量化检验仍待另定比较设计。*来源缺口*：Android 采用史与本比较所涉教育、出版史材料尚未给出可核出处，暂按候选解释处理。

<!-- SP:END chapter-07 -->
