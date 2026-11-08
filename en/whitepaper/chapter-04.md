> **Translation record**
> - Chinese source: `社会系统协议学白皮书.md`, block `chapter-04` — 118 lines, 17119 bytes, block sha256 `9c215c9b500c4738b2076d843e7d0fdfc8e1c2368827704ea0e344d617e62f84`, taken as the content between the `<!-- SP:BEGIN chapter-04 -->` and `<!-- SP:END chapter-04 -->` markers and reported by `tools/whitepaper_blocks.py list`; whole-file sha256 `d5ffb73e3db73f8bb42a2ecb39871bf6c55eace8bb72111b63a2ee362134d9c8`, 338639 bytes, 2026-11-08
> - Chinese version / release tag: `v11.2-r20261106` (theoretical version remains v11.2)
> - Translation version: `en-v0.1-ch04`
> - Translation date: 2026-11-08
> - Check status: draft; C12 self-check run after write; independent read-only audit to follow; machine and glossary checks only; no independent professional native-speaker review
> - Pending sync: none at present; to be recorded item by item if the Chinese source is updated
> - Status: phased translation of this chapter block — the normative framework text, RFC 4.1–4.3 specifications, the conditional derivation III-1, the §4.4 application-boundary note and the comparison table are translated; the case-annotation blocks (cases 4.1-A, 4.1-B, 4.1-C, 4.2-A, 4.3-A, 4.4-A, 4.4-B) are **retained in the original Chinese** by design under the C-1 phased plan (T3 not yet passed), so those blocks are held untranslated inside this file
> - Authority: the Chinese SSOT is authoritative; this translation does not constitute a separate set of definitions (C2)
> - Note on group name: Proposition Group III's name is consistent throughout the SSOT (chapter title line 930, the overview tables and the already-landed appendix / chapter-01 all read "第三组：跨期承诺、记录性质与执行条件" → "Proposition Group III: Intertemporal Finality & Expectation Credibility"); unlike Proposition Group II, no internal inconsistency was found

**Scope and edition status.** This file is one block of a **phased** translation. The English edition as a whole is an *abridged adaptation* of the v11.2 whitepaper: the six chapters that carry case-annotation sections are not yet translated, and those annotations remain untranslated by design until the underlying Chinese case materials pass the real-case acceptance stage (T3). Chapter 4 carries case-annotation sections (cases 4.1-A/B/C, 4.2-A, 4.3-A, 4.4-A/B); per the C-1 phased plan those annotations are **retained in the original Chinese** inside this file, so the normative framework text, RFC 4.1–4.3 and the §4.4 application-boundary note are translated while the case-annotation blocks are held in Chinese. Completeness of this block does not imply completeness of the edition, and this translation does not elevate any claim to established status. The block itself runs from the `<!-- SP:BEGIN chapter-04 -->` marker to the `<!-- SP:END chapter-04 -->` marker; the translation record, the chapter glossary and the two notes below precede that boundary and are not part of the translated text.

## Chapter Glossary — Chapter 4

| Chinese | English used in this file | Remark |
| :--- | :--- | :--- |
| 第三组核心命题：跨期承诺、记录性质与执行条件 | Proposition Group III: Intertemporal Finality & Expectation Credibility | group name, unique form in the whole book |
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

**Convention on link re-pointing.** Every in-page anchor that lives in another chapter (`#rfc-evidence-XXX`) is re-pointed to the Chinese source `../../社会系统协议学白皮书.md#…` so the build does not report a missing anchor; these resolve once the corresponding English chapter lands. Anchors that live in this file (`#chapter-4`, `#sp-rfc-008`…`#sp-rfc-010`, `#sec-4-1`…`#sec-4-4`, `#application-policy-expectations`) remain same-page links.

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
**Generation and evidence card:** [G008](../../社会系统协议学白皮书.md#rfc-evidence-008).

**Normative Spec (规范条文).**
Long-run capital expenditure (CAPEX) depends on expected cash flows, rule fulfilment probability, cost of capital, investment horizon, and default-recovery conditions. For a given investment project $i$, the following may be used as a conditional analytical framework:
$$\text{NPV}_i=\sum_{t=1}^{T}\beta_i^t\left[p_{it}R_{it}+(1-p_{it})Q_{it}\right]-I_i.$$
Here $p_{it}$ is the fulfilment probability, $R_{it}$ the cash flow upon fulfilment, $Q_{it}$ the cash flow or recovery upon default, and $I_i$ the initial investment. Holding other conditions fixed and where $R_{it}>Q_{it}$, a fall in fulfilment probability lowers the project's net present value; only after the net present value crosses the decision threshold — and financing and waiting options are taken into account — can one infer non-investment. The variance of rule lifetime may serve as a testable risk proxy; it cannot by itself determine CAPEX, nor does it imply that every node's capital expenditure permanently falls to zero or that the discount factor necessarily tends to zero.

**Conditional derivation III-1: comparative statics of single-period fulfilment probability.** Within the finite-horizon model above, holding the discount factor, initial investment, and each period's fulfilment and default cash flows fixed, change one period's probability from $p_{it}$ to $p_{it}^{\prime}$, both in $[0,1]$. Subtracting the old from the new net present value, the other terms cancel, giving:
$$\Delta\mathrm{NPV}_i=\beta_i^t(p_{it}^{\prime}-p_{it})(R_{it}-Q_{it}).$$
Since $0<\beta_i<1$, when $R_{it}>Q_{it}$ and $p_{it}^{\prime}<p_{it}$, this difference is strictly negative; it is zero if the two cash flows are equal, and its sign reverses if default recovery is higher. This proves the conditional relationship within the given cash-flow model; it does not prove that real-world probabilities, cash flows, or discount factors are mutually independent. When other terms move jointly with policy, recomputation is required. Under the static net-present-value investment rule, a numerical decline does not mean the project has crossed the investment threshold, still less can one infer that aggregate capital expenditure or marriage/fertility necessarily falls to zero.

> 📜 **【跨国金融实证 · 案例 4.1-A】（阿根廷汇率制度调整与主权信用多阶段变迁）**  
> *史实引证*：1991 年阿根廷通过《可兑换计划法》（*Ley de Convertibilidad*），规定 10,000 奥斯特兑 1 美元；1992 年新比索投入流通后，兑换关系为 1 比索兑 1 美元。这一可兑换安排构成反通胀规则，并伴随阶段性外资流入；在 2001 年底爆发的严重经济与银行挤兑危机中，政府相继实施提款限制（*Corralito*）并宣布对外债务违约；2002 年初新政府进一步正式废止 1:1 固定汇率，并推行强制非对称比索化（*Asymmetric Pesification*）。  
> *来源定位*：[1991 年可兑换法](https://www.argentina.gob.ar/normativa/nacional/ley-23928-1991-328)；[1991 年第 2128 号法令](https://www.argentina.gob.ar/normativa/nacional/decreto-2128-1991-7384/texto)。其余政策与信用效果仍须分别补证。  
> *系统学分析*：阿根廷 2001 年底债务违约、2002 年退出可兑换安排与银行存款强制转换，属于相连但政策性质与影响领域不同的多阶段事件。这些政策变更可能影响公众对货币信用的预期与避险需求，影响方向和程度需结合主体调查、存款与汇率数据检验；相关反应具有异质性，其货币行为演变需按具体政策、通胀周期与外部流动性环境分别检验，不能简单归结为主权信用自此永久归零。

> 📜 **【古代历史实证 · 案例 4.1-B】（晚期罗马与西哥特同盟盟约变迁及承诺风险）**  
> *史实引证*：公元 376 年罗马帝国允许西哥特人渡过多瑙河入境，入境后的供给、安置和官员行为与冲突有关；378 年阿德里安堡战役后，罗马与哥特群体在 382 年达成安排。该安排的性质、涉及群体及条款记载不足，学界对其为条约（*foedus*）还是归附（*deditio*）存在不同解释；*foederati* 指同盟者或相关军人，不是条约名称。据佐西穆斯记载，408 年斯提里科死后有士兵袭击蛮族士兵的妇女与子女；不能据此认定他们均属同一支哥特军团。410 年阿拉里克率部洗劫罗马；上述长期演变的具体因果仍须逐项查证。  
> *来源定位*：[Ammianus，卷 31（英译）](https://www.tertullian.org/fathers/ammianus_31_book31.htm)涉及 376—378 年，不见证 382 或 410 年事件；[佐西穆斯《新历史》5.35（英译）](https://www.livius.org/sources/content/zosimus/zosimus-new-history-5/zosimus-new-history-5.35/)记述 408 年事件；[Mark Hebblewhite, *Theodosius and the Limits of Empire*（Routledge，2020）正式书目](https://www.routledge.com/Theodosius-and-the-Limits-of-Empire/Hebblewhite/p/book/9781138102989)与[相关章节转录](https://ebrary.net/252932/history/_focdus_)分开使用：前者定位书目，后者呈现作者解释，具体页码及转录与出版版本的一致性尚待核对，其余事件及分歧须继续核验。  
> *系统学分析*：晚期罗马与哥特群体的关系跨越数十年，包含迁入安置危机、不同安排下的合作、军费粮饷博弈与政治冲突的多阶段演进过程。376 年前后的供给和接纳争议可作为研究跨期信任的线索，其与之后事件的关联及竞争解释仍需独立考察；本书将其作为考察主权中心在面对外部异构协作者时“承诺不完备与单方违约加剧系统性防御解体”的机制参考案例，而非单一因果的历史证明。

> 👵 **【跨代契约实证 · 案例 4.1-C】（公共养老金代际筹资演化中的 SLA 调整与规则风险）**  
> *制度演进实证*：德意志帝国 1889 年建立的养老与伤残保险制度初期包含基金积累要素，至 1957 年重大改革后逐步确立起典型的现收现付制（Pay-As-You-Go）动态平衡机制，其宏观运作依赖“活跃劳动力缴费支撑已退休代际待遇”的跨代滚动安排。然而在现代多个国家，面对少子老龄化的人口结构变动与财政压力，主权者常通过推迟法定退休年龄、调整待遇计发公式或收紧准入，引发关于长期服务协议（SLA）单方重构与规则信用的广泛争议。  
> *来源定位*：[德国联邦宪法法院2022年4月7日裁定，1 BvL 3/18等，英文版第24段](https://www.bundesverfassungsgericht.de/SharedDocs/Entscheidungen/EN/2022/04/ls20220407_1bvl000318en.html)为1891年生效及1957年筹资改革的制度背景定位；该背景叙述不证明下述信任、参保或家庭决策效果，其他国家及具体调整须另给来源。  
> *系统学分析*：  
> 1. **单方面服务降级与规则风险的协议学比喻（Sovereign Downgrade & Protocol Re-contracting）**：在中心化架构下，用户在连续数十年缴纳社保后，交付阶段常面临规则调整。尽管从法理与公共财政上，法定社会保障不同于民商事私人预付款合同，调整待遇通常遵循立法或行政程序，但在微观主体看来，缺乏充分过渡期与救济途径的频繁规则变更，可能诱发类似软件服务协议（Terms of Service）单方降级的信任损耗；  
> 2. **微观节点的信任下降与异质性选择**：若微观节点识别出中心池的违约风险，可能降低对该系统的信任预期。其应对策略可能包括多维度调整，例如减少对中心池的长期流动性注入（参保与就业策略调整）、增加预防性储蓄与家庭计划再考量。具体方向取决于预期待遇、既有权益、退出成本与替代保障，不应假设所有节点以断联作为唯一选择；少子化与经济增速还受到收入水平、抚养成本、女性劳动参与及文化观念等多种长期趋势驱动。



<a id="sp-rfc-009"></a>
<a id="legacy-v11-1-sec-4-3"></a>
<a id="sec-4-2"></a>

<a id="legacy-v11-1-rfc-011"></a>
<a id="legacy-v11-0-rfc-011"></a>

### 4.2 SP-RFC-009 | Retry Idempotence, Record Durability, and Finality

**Claim identity:** property definition and procedural boundary.
**Dependencies and additional conditions:** fixed request, rule version, evidence set, and authorisation-review procedure.
**Generation and evidence card:** [G009](../../社会系统协议学白皮书.md#rfc-evidence-009).

**Normative Spec (规范条文).**
1. **Semantic invariance and procedural protection:** if property rights, jurisdiction, and the relations of rights and obligations can be rewritten at will without due process, agents' long-run expectations are disturbed. One should independently examine the dispersion of textual-interpretation authority, procedural constraints, and ex-post remedy mechanisms; one cannot assert a type-system collapse merely from textual change.
2. **Layered inspection of idempotence, durability, and finality:** for the same request identifier $k$ that should be de-duplicated, idempotence requires that repeated submission adds no further business effect, i.e. $F_k(F_k(s))=F_k(s)$; distinct requests must not be merged merely because they share an operation name. The durability of ACID requires that a committed result is not lost under the specified fault model, and subsequent authorised transactions may still change the current state. Finality additionally means that a confirmed record will not be revoked or replaced under the specified rules and trust assumptions. When inspecting ex-post reload, one must fix the transaction identity, rule version, and evidence set, and distinguish repeated penalty, rewriting of historical records, and appending a corrective record per pre-announced review rules; merely having $Verify(Tx,t_0)\ne Verify(Tx,t_0+\Delta t)$ is insufficient to conclude arbitrary rollback.

> 📰 **【程序正义案例注疏 · 案例 4.2-A】（高校纪律调查中的程序溯及力与规则稳定性争议）**  
> *实证观察*：在高校行政与自律规程演变中（如围绕 Title IX 程序的多轮司法诉讼），争议焦点常集中于“知情同意（Consent）”认定的证据标准与程序追溯力。本书在分析中区分三类情形，具体规则和裁判仍须分别核验：① 行为发生时客观上即不存在有效同意（事后发现真相）；② 行为过程中当事人明确撤回同意；③ 事后在缺乏程序约束下改变举证责任或追溯适用新判定标准。  
> *来源定位*：[2024 年 Title IX 规则（89 FR 33474）](https://www.govinfo.gov/app/details/FR-2024-04-29/2024-07915)；[2026 年联邦公报关于规则及诉讼沿革的说明](https://www.govinfo.gov/content/pkg/FR-2026-09-29/html/2026-19929.htm)。据后者所载沿革，2024年规则在2025年被法院撤销，教育部同年宣布按此前框架执法；2026年9月29日规则将相应条文重新编入CFR，并保留所列调整，并非逐字恢复全部2020年文本。本例引用历史沿革，具体行为仍须区分时段、法域和适用版本；本书三类分析不等于已证明司法界共识。  
> *系统学分析*：当制度执行缺少明确的举证规则、申诉时限与终局救济边界时，当事人将面临不对称的追溯性裁决风险。本书提出待检验机制：这种风险可能改变长期预期及交往策略，但本例未提供具体案件样本、行为测量或识别设计，不能据此认定过度防御行为已经发生或估计其因果效果；既有偏好、舆论与其他规则变化均须作为竞争解释。保护各方合法权益的根本，在于坚持明确的程序法治与双向抗辩救济机制。



<a id="sp-rfc-010"></a>
<a id="legacy-v11-1-sec-4-4"></a>
<a id="sec-4-3"></a>

<a id="legacy-v11-1-rfc-012"></a>
<a id="legacy-v11-0-rfc-017"></a>

### 4.3 SP-RFC-010 | Deterministic Execution and Conditional Commitment

**Claim identity:** execution mechanism and conditional protection.
**Dependencies and additional conditions:** initial state, input ordering, consensus, authority, faults, and asset control are specified separately.
**Generation and evidence card:** [G010](../../社会系统协议学白皮书.md#rfc-evidence-010).

**Normative Spec (规范条文).**
A deterministic state machine produces identical results under identical initial states and identical ordered inputs, and can be used to reduce arbitrary discretion in cross-period clearing. If one further requires multiple nodes to agree on a consistent history, one must also specify the consensus algorithm, membership and authority model, fault and attack thresholds, network assumptions, protocol-upgrade authority, and finality criteria; the recurrence $s_{n+1}=\delta(s_n,tx_n)$ may represent the execution rule, but this recurrence relation by itself does not prove history is immutable. Cryptographic signatures and time-locks constrain authorisation and execution timing respectively, and — where the stated assumptions hold — raise the difficulty of unauthorised ledger alteration; evaluation of "default resistance" must be limited to the states and assets the protocol actually controls, and the counter-example conditions under which the commitment fails must be stated explicitly. Given that real social contracts are endogenously incomplete, deterministic auto-execution (such as smart contracts or rigid administrative rules) applies only to standard paths with complete, verifiable state; for unforeseeable physical or social edge anomalies, the protocol must still reserve a procedurally-constrained "Bounded Discretion & Exception Handler" to avoid strangling legitimate room for correction through rigid lock-in.

> 💻 **【密码学与制度同构 · 案例 4.3-A】（比特币算法上限与智能合约对冲主权 Rug Pull）**  
> *工程比较*：本书将比特币的发行与验证规则、以太坊的合约执行，与跨期承诺问题作机制比较；不据此推断中本聪针对本书列举的阿根廷或养老金案例而设计系统。链上执行还受输入排序、共识、升级权限和故障条件约束，不将智能合约概括为无条件不可改写的自动兑付保证。  
> *系统学分析*：签名、共识与时间锁可以减少某些单方改账权限；其保护范围取决于信任假设、升级权限、密钥管理和实际控制的资产。Ring-3 Protection 在此是权限边界类比，不能从密码学不可伪造直接推出法律权利、链外资源或长期购买力不可撤回。



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

> 📜 **【理论同构 · 案例 4.4-A】（2024 阿西莫格鲁/约翰逊/罗宾逊 & 2025 莫基尔/阿吉翁/豪伊特：包容性协议与前沿创新硬墙）**  
> *理论引证*：2024 年诺贝尔经济学奖授予阿西莫格鲁（Acemoglu）、西蒙·约翰逊（Simon Johnson）与罗宾逊（Robinson），确立了“包容性制度 vs 榨取性制度”的宏观分野；2025 年诺贝尔经济学奖紧接着授予乔尔·莫基尔（Joel Mokyr）、菲利普·阿吉翁（Philippe Aghion）与彼得·豪伊特（Peter Howitt），表彰其对“持续技术进步的文化制度前提”与“创造性破坏（Creative Destruction）前沿增长模型”的贡献。  
> *系统学分析*：这些研究为制度激励、知识传播与创新竞争提供了可比较的理论机制。本书可用开源知识协议、产权接口与边缘试错提出工程映射，但获奖本身不构成“严密的计算机系统证明”。追赶与前沿创新面临的约束须在具体模型中比较；不能由组织被贴上“闭源”或“榨取性”标签，直接推出其必然撞墙死锁。

> 📜 **【理论同构 · 案例 4.4-B】（2026 年霍尔与伍德福德：微观跨期预期与宏观政策传导边界）**  
> *理论引证*：2026 年诺贝尔经济学奖授予罗伯特·霍尔（Robert E. Hall）与迈克尔·伍德福德（Michael Woodford），表彰其奠定宏观稳定政策微观基础的突出贡献。  
> *系统学分析*：  
> 1. **霍尔的跨期消费模型（Hall, 1978）**：在该模型条件下，消费边际效用具有随机游走性质，消费本身近似服从相应过程；这是关于给定信息能否预测未来消费变化的命题，不能解释成临时收入或补贴绝对不影响消费水平。收入新消息、资产变化和融资条件等仍须在具体模型与数据中检验；不由此推出所有主体必然停止消费或生育。
> 2. **预期、承诺与政策传导**：可信的跨期政策安排可以影响主体预期与决策；对具体宽松是否有效，应列出模型、约束和证据，不从政策争议直接推出信誉归零或任意刺激均无效。2026年官方获奖说明同样强调了适时财政、货币措施的稳定作用。
> *来源*：[Hall（1978）原论文](https://web.stanford.edu/~rehall/Stochastic-JPE-Dec-1978.pdf)；[2026年经济学奖官方说明](https://www.kva.se/en/news/the-prize-in-economic-sciences-2026/)。

<!-- SP:END chapter-04 -->
