> **Translation record**
> - Chinese source: `社会系统协议学白皮书.md`, block `chapter-05` — 207 lines, 26087 bytes, block sha256 `7bf448ef45fbee70fd33d01037f0b0ef774e2092a91a5e59ebf30f47052db52d`, taken as the content between the `<!-- SP:BEGIN chapter-05 -->` and `<!-- SP:END chapter-05 -->` markers and reported by `tools/whitepaper_blocks.py list`; whole-file sha256 `d5ffb73e3db73f8bb42a2ecb39871bf6c55eace8bb72111b63a2ee362134d9c8`, 338639 bytes, 2026-11-08
> - Chinese version / release tag: `v11.2-r20261106` (theoretical version remains v11.2)
> - Translation version: `en-v0.1-ch05`
> - Translation date: 2026-11-08
> - Check status: draft; C12 self-check run after write; independent read-only audit to follow; machine and glossary checks only; no independent professional native-speaker review
> - Pending sync: none at present; to be recorded item by item if the Chinese source is updated
> - Status: phased translation of this chapter block — the normative framework text, RFC 5.1–5.5 specifications, the conditional derivation IV-1, the §5.6 authorisation-implementation / receiver-side-regulation cases and the Syscall Lifecycle diagram are translated; the case-annotation blocks (cases 5.1-A, 5.1-B, 5.1-C, 5.2-A, 5.2-B, 5.2-C, 5.4-A, 5.4-B, 5.5-A, 5.5-B, 5.6.2-A, 5.6.2-B, 5.6.3-A) are **retained in the original Chinese** by design under the C-1 phased plan (T3 not yet passed), so those blocks are held untranslated inside this file
> - Authority: the Chinese SSOT is authoritative; this translation does not constitute a separate set of definitions (C2)
> - Note on group name: Proposition Group IV shows an internal SSOT inconsistency. The overview tables (SSOT lines 276, 305, 2427–2429), the already-landed appendix / chapter-01, and the C12 locked ledger all use "第四组核心命题：特权环隔离与脑裂传染" → "Proposition Group IV: Privilege Ring Isolation & Split-Brain Contagion". However the chapter-05 heading (line 1050) and the table of contents (line 37) read "第四组：权限、冲突、激励与退出" (Authority, Conflict, Incentive, and Exit). This translation follows the landed/locked form for book-wide consistency and flags the heading discrepancy for maintainer reconciliation.

**Scope and edition status.** This file is one block of a **phased** translation. The English edition as a whole is an *abridged adaptation* of the v11.2 whitepaper: the six chapters that carry case-annotation sections are not yet translated, and those annotations remain untranslated by design until the underlying Chinese case materials pass the real-case acceptance stage (T3). Chapter 5 carries case-annotation sections (cases 5.1-A/B/C, 5.2-A/B/C, 5.4-A/B, 5.5-A/B, 5.6.2-A/B, 5.6.3-A); per the C-1 phased plan those annotations are **retained in the original Chinese** inside this file, so the normative framework text, RFC 5.1–5.5, the conditional derivation IV-1, and the §5.6 implementation/regulation cases are translated while the case-annotation blocks are held in Chinese. Completeness of this block does not imply completeness of the edition, and this translation does not elevate any claim to established status. The block itself runs from the `<!-- SP:BEGIN chapter-05 -->` marker to the `<!-- SP:END chapter-05 -->` marker; the translation record, the chapter glossary and the two notes below precede that boundary and are not part of the translated text.

## Chapter Glossary — Chapter 5

| Chinese | English used in this file | Remark |
| :--- | :--- | :--- |
| 第四组核心命题：特权环隔离与脑裂传染 | Proposition Group IV: Privilege Ring Isolation & Split-Brain Contagion | group name, unique form in the whole book (landed/locked; see note above) |
| 6 个核心命题组 | 6 Core Proposition Groups | H3-A landed |
| 19 项有效 SP-RFC | 19 Effective SP-RFC Items | title-case unique |
| 权限模型与社会桥接 | authority model and social bridging | claim identity (011) |
| 状态区分与机制假说 | state distinction and mechanism hypothesis | claim identity (012) |
| 有限两行动博弈的条件推导 | conditional derivation of a finite two-action game | claim identity (013) |
| 制度实例化与规范边界 | institutional instantiation and normative boundary | claim identity (014) |
| 识别边界与应用假说 | identification boundary and application hypothesis | claim identity (015) |
| 用户态资源保护 | user-mode resource protection | Ring-3 |
| Ring-3 保护 | Ring-3 Protection | §5.1 analogy |
| Ring-0 | Ring-0 | highest privilege level |
| 系统调用 | system call (Syscall) | §5.4 / §5.6 |
| 网络分区 | Network Partition | §5.2 |
| 脑裂 | Split-Brain | §5.2 |
| 可信承诺 | Credible Commitment | North & Weingast (1989); §5.1-C |
| 动态不一致性 | Time Inconsistency | Kydland & Prescott (1977); §5.1-C |
| 互补性垄断 | Complementary Monopolies | Olson (1993); §5.2-C |
| 流寇 / 坐寇 | roving bandits / stationary bandits | Olson; §5.2-C |
| 严格占优 | Strict Dominance | §5.3 |
| 纳什均衡 | Nash Equilibrium | §5.3 |
| 拜占庭雪崩 | Byzantine avalanche | §5.3 |
| 责任归因偏差与假性自愿叙事 | Attribution Distortion & Pseudo-Voluntary Narrative | §5.5 |
| 选择熵 | Choice Entropy | $H(\text{Choice})$, §5.5 |
| 特权环穿越 | Privilege-Ring Crossing | §5.6.1 diagram |
| 僵化经院化 | Scholastic Bloat | §5.6.1 (Entropic Trap) |
| 内核恐慌 | Kernel Panic | §5.6.2 |
| 恶意系统调用反模式 | Malicious Syscall Anti-Pattern | §5.6.2 |
| BGP 路由劫持 | BGP Hijacking | §5.2 analogy |
| 恶意在途截留 | Rogue Transit | §5.2 analogy |
| 合法拒绝或撤销程序 | lawful denial or revocation procedure | §5.4 |

**Note on claim identities.** The claim-identity labels in this chapter (RFC 011: authority model and social bridging; RFC 012: state distinction and mechanism hypothesis; RFC 013: conditional derivation of a finite two-action game; RFC 014: institutional instantiation and normative boundary; RFC 015: identification boundary and application hypothesis) are descriptive phrases at the grain of the source sentence (per R7 of the term ledger), not a taxonomy of claim identities. This translation keeps the five canonical claim identities — `postulate`, `conditional proposition`, `mechanism hypothesis`, `accounting definition`, `normative objective` — distinct, and renders the finer descriptive labels by reusing the locked class words. The labels are not upgraded into proven conclusions; the negation guardrails in the source (does not / cannot / has not / one cannot / has not yet been proven) are preserved. Note also that SP-RFC-014 itself states that "applying for authorisation" and "constraining power" are not formally absolutely orthogonal, which is an explicit correction of the orthogonality metaphor within the source and is preserved as such.

**Convention on link re-pointing.** Every in-page anchor that lives in another chapter (`#rfc-evidence-XXX`) is re-pointed to the Chinese source `../../社会系统协议学白皮书.md#…` so the build does not report a missing anchor; these resolve once the corresponding English chapter lands. Anchors that live in this file (`#chapter-5`, `#sp-rfc-011`…`#sp-rfc-015`, `#sec-5-1`…`#sec-5-6-3`, `#application-policy-expectations`) remain same-page links.

---

<!-- SP:BEGIN chapter-05 -->
<a id="chapter-5"></a>

## Chapter 5: Proposition Group IV — Privilege Ring Isolation & Split-Brain Contagion



<a id="sp-rfc-011"></a>
<a id="legacy-v11-1-sec-5-1"></a>
<a id="sec-5-1"></a>

<a id="legacy-v11-1-rfc-013"></a>
<a id="legacy-v11-0-rfc-009"></a>

### 5.1 SP-RFC-011 | Privilege Isolation and Constraints on the Executor

**Claim identity:** authority model and social bridging.
**Dependencies and additional conditions:** O2 and the specific execution structure; independent review, remedy, and compensation are specified separately.
**Generation and evidence card:** [G011](../../社会系统协议学白皮书.md#rfc-evidence-011).

**Normative Spec (规范条文).**
Modern rule-of-law property rights can be likened to user-mode resource protection with clear authority boundaries (Ring-3 Protection). In a conventional operating system, user-mode isolation is enforced with the kernel's participation and cannot by itself constrain the kernel itself; the social mapping must therefore also show how constraints such as independent review, separation of powers, remedy, and compensation act upon the power executor. When expropriation authority lacks these constraints and can expand arbitrarily, agents face a higher risk of property-rights withdrawal, and long-term investment may be suppressed; the degree and duration should be judged by institutional conditions and evidence — one cannot assert from the Ring-3 analogy alone that the capital-sinking function permanently falls to zero.

> 📜 **【法治演进注疏 · 案例 5.1-A】（1215 年英格兰《大宪章》的特权边界确立）**  
> *原条文意译与范围*：1215年《大宪章》第39条列明对自由人的处分限制：除非依据其同侪的合法裁判或依国法，否则不得作该条所列的拘禁、剥夺等处置。“或依国法”是条件分支，并非说依法处置也一律禁止；当时自由人的范围也不能直接等同现代普遍公民权利。参见[第39条拉丁原文与译文](https://magnacarta.cmp.uea.ac.uk/read/magna_carta_1215/Clause_39)。
> *系统学分析*：在协议学上，这是约束最高特权级（Ring-0）随意越界操作的重要制度里程碑。尽管第 39 条最初适用的“自由人”范围有限，并非现代普遍公民权利的直接宣言，但在后续数个世纪的宪制演进中（包括 1628 年爱德华·柯克爵士推动的《权利请愿书》以及 1679 年《人身保护法》等相继立法），该原则历经司法判例与成文立法的双重泛化（API Widening），逐步扩展为普遍的人身与财产法律保障。它与普通法体系相互演化，成为制度学中讨论约束王权、增强可信承诺的重要历史机制参考，但不可将其简单线性推导为工业革命的唯一决定因素。

> 📜 **【暴力越界注疏 · 案例 5.1-B】（津巴布韦与委内瑞拉的内存越界大溃败）**  
> *案例范围*：津巴布韦农地征收与委内瑞拉企业征用、石油行业裁员，可用于研究产权、治理与生产能力的关系。PDVSA裁员涉及多种岗位，不能把员工总数全记为工程师；具体人数、职业构成、时期及征收程序须依原记录核验，本段暂不报告精确人数。
> *系统学分析*：无充分约束的 `sys_unmap_all()` 可类比任意剥夺资源控制权的风险，但不能代替两国各自的事件时间线。产出与通胀变化还涉及财政货币、行业管理、外部条件等因素；本段不以未经同口径核验的倍数或单一事件解释所有后果。

> 📊 **【新制度经济学与宏观实证注疏 · 案例 5.1-C】（诺斯-温加斯特可信承诺、利率历时变化与 EPU 投资弹性实测）**  
> *经典专著与诺奖锚点*：诺贝尔经济学奖得主道格拉斯·诺斯（Douglass North）与政治学家巴里·温加斯特（Barry Weingast）在经典文献《宪制与承诺》（*Constitutions and Commitment*, 1989）中指出，1689 年《权利法案》等宪制安排通过强化议会预算权与司法独立性，显著增强了对王权（Ring-0）任意征用财产权的制度约束，提供了讨论主权者“**可信承诺（Credible Commitment）**”的经典历史案例；这一机制与 2004 年诺贝尔经济学奖得主基德兰德和普雷斯科特（Kydland & Prescott, 1977）关于“**动态不一致性（Time Inconsistency）**”的分析具有紧密的理论关联。  
> *外部经验研究述评*：  
> 1. **可信承诺与长期公共信用的历史证据**：North & Weingast（1989，pp. 822–824）记载，英国政府在光荣革命之后的 1690 年代初以约 14% 利率取得部分初期长期贷款；至该年代末降至约 6%–8%，1730 年代约为 3%。作者同时讨论政府举债规模的扩大，将这些历时变化作为可信承诺增强的证据。它们不是制度切换后即时发生的单一风险溢价下降，也不能将政府债务的增长改称全社会长期资本池增长。
> 2. **政策不确定性与投资的经验关联**：Baker、Bloom 与 Davis（2016, *Quarterly Journal of Economics*）以报刊中经济、政策与不确定性相关报道的频率构造 EPU 指数。在美国季度 VAR 中，一次约 90 点的 EPU 创新——相当于 2005–2006 至 2011–2012 的均值变化——对应总投资约 6% 的峰值下降。此处定位于2016年3月10日作者稿文内第24页及附图C7。作者同时报告企业层面及 12 国面板分析，但提醒宏观响应未必具有因果解释。该结果支持继续研究规则不确定性与投资的关系，不能视为企业 CAPEX 对契约寿命方差的一标准差结构弹性。
> *核查来源*：[Baker, Bloom & Davis (2016), Measuring Economic Policy Uncertainty, 作者公开稿](https://www.policyuncertainty.com/media/EPU_BBD_Mar2016.pdf)；[Baker, Bloom & Davis (2016), 期刊发表页](https://doi.org/10.1093/qje/qjw024)。



<a id="sp-rfc-012"></a>
<a id="legacy-v11-1-sec-5-2"></a>
<a id="sec-5-2"></a>

<a id="legacy-v11-1-rfc-014"></a>
<a id="legacy-v11-0-rfc-010"></a>

### 5.2 SP-RFC-012 | Resource Cutoff, Communication Partition, and Conflicting Writes

**Claim identity:** state distinction and mechanism hypothesis.
**Dependencies and additional conditions:** P1 resource background; communication, authority, arbitration, and competitive incentive are each defined separately.
**Generation and evidence card:** [G012](../../社会系统协议学白皮书.md#rfc-evidence-012).

**Normative Spec (规范条文).**
When a central node can no longer continuously transfer to edge nodes the resources needed to sustain collaboration, service degradation, relationship decoupling, or control-right competition may appear. A network partition refers only to communication isolation; only when multiple nodes or partitions simultaneously claim valid write authority over the same resource and produce conflicting decisions does it constitute the split-brain referred to here. If arbitration, authority isolation, and stop-write-on-disconnect mechanisms are effective, a partition may manifest as a partial service pause without rewriting confirmed state. Mapping this mechanism onto regional warlordism requires separately proving the link between resource cutoff, failure of constraints, and competitive expropriation; the analogies of local malicious in-transit interception (Rogue Transit) and BGP-route hijacking with forged jurisdiction should also be checked separately, and cannot be inferred from fiscal distress alone.

> 📜 **【历史实证注疏 · 案例 5.2-A】（神圣罗马帝国的强盗骑士与路障网络）**  
> *待核历史比较线索*：神圣罗马帝国的商道通行、关税特权与被称为“强盗骑士”的武装，可以用于研究合法收费和暴力勒索的边界；具体时期、关卡与权利文本须逐案核验，关卡分布与频度须由史料确定。  
> *系统学分析*：在途控制者截留资源可类比 Rogue Transit；伪造跨域权限另作 BGP Hijacking 类比。不能将帝国地方特权直接解释为现代中央转移支付中断，也不能从收费纠纷推出商旅全面断绝或冲突性多主写入。

> 📜 **【近代历史注疏 · 案例 5.2-B】（17—18 世纪之交公权私掠船的制度癌变）**  
> *待核历史比较线索*：私掠许可证、战时授权及停战后的武装就业，可用于研究委托暴力与撤权成本。须区分战争、条约、武装群体和海盗活动的时期，不能把“海盗黄金时代”整体起点归于一次停战，也不报告未定位的瞬时转化人数。  
> *系统学分析*：委托暴力的权限撤销可能面临实际执行阻力；可类比撤销凭证后仍保有行动能力的节点。是否转为海盗、能否清除及损害范围须另证，不能由分发权限推出永远不可撤销。

> 📊 **【封建割据与双垄断加价实证注疏 · 案例 5.2-C】（莱茵河关卡暴增与 Olken-Barron 卡车勒索实测）**  
> *经典理论锚点*：曼瑟尔·奥尔森在《独裁、民主与发展》（1993，*APSR*）中用“流寇”与“坐寇”区分不同时间视野下的掠夺激励：若统治者预期能长期控制税基，自利动机也可能促使其维持秩序与部分公共品；若任期显著缩短，没收现有资产的相对收益可能上升。因此，财政断流与暴力竞争可能加剧短视掠夺，但须检验其是否改变任期预期、税基利益和约束机制。多重关卡的收费外部性属于另一条可检验机制，不能据此断言所有地方节点必然流寇化或无限设卡。
> *外部经验研究述评*：  
> 1. **神圣罗马帝国莱茵河在途截留机制**：中世纪后期帝国中央控制力松弛时期，莱茵河干道领主关卡与过路税费大量繁衍，形成典型多重分散设卡与在途抽取结构，显著增加了长途商业航运的交易与通关成本；原始文献具体设卡数与累计税率因航段、货物与统计口径而异，但其呈现的互补垄断（Complementary Monopolies）租金抽取模式，成为制度经济学讨论分权掠夺与协调失败的典型历史参考；  
> 2. **路障市场结构与勒索定价**：Olken 与 Barron（2009, *Journal of Political Economy*）派调查员随行记录印尼亚齐相关路线的 304 趟运输，直接观察 6000 余次非法付款。研究利用和平协议后撤军引起的关卡变化，发现部分关卡消失后，剩余路段的平均单站付款上升，与互补性垄断的定价机制相符。非法付款平均约占每趟总运输成本的 13%（原论文表1相应成本口径使用工资资料齐全的282趟，不把304趟总样本移作每列分母）。这些发现支持将收费站之间的策略互动纳入分析；本文未据此给出“分散收费比统一收费高近一倍”的可核验估计。
> *核查来源*：[Olken & Barron (2009), The Simple Economics of Extortion](https://economics.mit.edu/sites/default/files/publications/090701%20Trucking%20paper%20JPE%20published.pdf)。



<a id="sp-rfc-013"></a>
<a id="legacy-v11-1-sec-5-3"></a>
<a id="sec-5-3"></a>

<a id="legacy-v11-1-rfc-015"></a>
<a id="legacy-v11-0-rfc-012"></a>

### 5.3 SP-RFC-013 | Predatory Gain, Strict Dominance, and Static Equilibrium

**Claim identity:** conditional derivation of a finite two-action game.
**Dependencies and additional conditions:** P2-type choice; complete net payoff, strict dominance over all opponent strategies; dynamics argued separately.
**Generation and evidence card:** [G013](../../社会系统协议学白皮书.md#rfc-evidence-013).

**Normative Spec (规范条文).**
**Freeing malicious nodes from penalties raises the plunder incentive:** absence of slashing lowers the cost of plunder, but $\text{Penalty}_{\text{slash}}=0$ and $E[R_{\text{plunder}}]>0$ by themselves do not guarantee that plunder dominates cooperation. In a clearly specified two-strategy static game, if every node accurately maximises net expected utility and, for all opponent strategies $a_{-i}$, $Q_i(D,a_{-i})>Q_i(H,a_{-i})$, then plunder $D$ strictly dominates cooperation $H$, and universal plunder forms the unique Nash equilibrium. Whether a real system converges to this state, and whether a Byzantine avalanche or physical downtime appears, still requires stating the strategy-update mechanism, resource thresholds, and fault-tolerance boundaries.

**Conditional derivation IV-1: strict dominance and the unique static equilibrium.** Restricted explicitly to a normal-form game with a finite number of nodes, where each node has only the two actions cooperation $H$ and plunder $D$; $Q_i(a_i,a_{-i})$ denotes the net expected utility given in the payoff table. If for every node $i$ and every pure-strategy opponent profile $a_{-i}$ we have $Q_i(D,a_{-i})>Q_i(H,a_{-i})$, then for any mixed opponent strategy the probability-weighted average of the positive difference remains strictly positive, so $H$ is not a best response. No Nash equilibrium can assign positive probability to $H$; when all choose $D$, each node is again making the unique best response, so it is the unique Nash equilibrium, ruling out other mixed-strategy equilibria as well.
This conclusion applies only to this two-action payoff table. If extra strategies are allowed, reputation and punishment from repeated interaction are brought into the strategy space, or the strict inequality fails, the dominance condition must be re-examined; even if the static-equilibrium conclusion holds, it has not yet been proven that an arbitrary learning process converges, still less that communication split-brain, resource exhaustion, or physical collapse is proven.



<a id="sp-rfc-014"></a>
<a id="legacy-v11-1-sec-5-4"></a>
<a id="sec-5-4"></a>

<a id="legacy-v11-1-rfc-016"></a>
<a id="legacy-v11-0-rfc-013"></a>

### 5.4 SP-RFC-014 | Authorisation Interface for Specific Public Objectives

**Claim identity:** institutional instantiation and normative boundary.
**Dependencies and additional conditions:** specified jurisdiction, public objective, authorisation, and procedure; not every collaboration must enter the kernel.
**Generation and evidence card:** [G014](../../社会系统协议学白皮书.md#rfc-evidence-014).

**Normative Spec (规范条文).**
User space (Ring-3) can continuously organise collaboration through autonomous rules, community norms, contracts, and technical standards. For programmes that require nationwide coercive enforcement, public taxation, or statutory education standards, the authorisation and procedure interface that enters the national kernel (Ring-0) — call it a system call (Syscall) — is an important path to that specific objective. State recognition, institutional nesting, and direct state adoption are distinct relations; one cannot take becoming a state-default daemon as the uniform success criterion for all ideas, paradigms, or technology movements.

> **Institutional interface boundary and empirical-limitation statement**:
> 1. **Delimitation of its relation to SP-RFC-011**: SP-RFC-011 specifies how those in power are subject to institutional constraint and responsibility isolation, while SP-RFC-014 specifies what authorisation procedure a specific public objective depends on. "Applying for authorisation" and "constraining power" are highly interwoven and overlapping in real institutions and legal systems; one cannot claim that the two are formally absolutely orthogonal merely because their logical directions are opposite.
> 2. **Conceptual illustration, not fully automated code**: this item is currently a conceptual framework for institutionalised authorisation interfaces, not a fully automated machine-executable specification; an implementable institutional interface must delimit the jurisdiction, the scope of authorised actors, the statutory list of authorised acts, lawful denial or revocation procedures, and an independent channel for objection and remedy.

> 📜 **【历史实证注疏 · 案例 5.4-A】（胡适与 1920 年白话文训令：Syscall 成功合入国家标准库）**  
> *同期材料*：[《京师学务局教育行政月刊》1920年第1卷第7期，扫描第8页](https://upload.wikimedia.org/wikipedia/commons/6/6e/NLC404-01J002135-24988_%E4%BA%AC%E5%B8%AB%E5%AD%B8%E5%8B%99%E5%B1%80%E6%95%99%E8%82%B2%E8%A1%8C%E6%94%BF%E6%9C%88%E5%88%8A_1920%E5%B9%B41%E5%8D%B77%E6%9C%9F.pdf#page=8)所载1920年1月23日京师学务局训令第四号，案奉“教育部訓令第一二號”（据同期扫描件 OCR 转录与教育部训令编号体系核定为第十二号），要求当年秋季国民学校一二年级“先改国文为语体文”（简体转写）。此处仅按所链京师学务局转发令所载转录，教育部 1920 年 1 月 12 日咨各省区第三十八号已定位（《教育公报》第 7 年第 2 期公牍第 12 页，1920 年 2 月 20 日；据梁培东 2019、学术史谭 2023 两文转引），该期影像本轮未取得，不作终局认定。中央部令与地方转发令须区分；该材料不表示全国政府公文一律改白话，也不表示胡适个人制定了该行政命令。
> *系统学分析*：1920 年教育部训令体现了白话文进入国民教育制度的关键节点。白话文从民间的思想倡议，正式写入国家法定的国民学校标准（进入系统调用与基础环境）。此处以系统调用（Syscall）类比制度授权接口，但文件规定、教材供给、师资培训与不同区域的实际普及应分别考察，不能等同于全网节点在单一指令下即时完成同步切换。

> 📜 **【跨文明注疏 · 案例 5.4-B】（君士坦丁《米兰敕令》与《萨洛尼卡敕令》：基督教的制度化与特权环演进）**  
> *法令文本*：通常称为《米兰敕令》的313年文书，在[拉克坦提乌斯所存文本的英译](https://sourcebooks.fordham.edu/source/edict-milan.asp)中涉及宗教选择及基督教团体财产返还；[《狄奥多西法典》XVI.1.2的拉丁文与380年2月27日日期标注](https://www.thelatinlibrary.com/theodosius/theod16.shtml)及[法令英译](https://sourcebooks.fordham.edu/source/theodcodeXVI.asp)则规定获认可的三位一体信仰并区分异端。两者可用于比较容忍、财产权与正统授权的不同接口，不把后者当作所有宗教实践在同一天同步切换的证明。
> *系统学分析*：本书将上述不同法律安排类比为授权接口的演变。法律文本可以确认规则表达，实际执行、扩散与政治动机须另证；不能由授权推出传播效果，更不能把君士坦丁与狄奥多西的不同措施压成一次Syscall。



<a id="sp-rfc-015"></a>
<a id="legacy-v11-1-sec-5-5"></a>
<a id="sec-5-5"></a>

<a id="legacy-v11-1-rfc-017"></a>
<a id="legacy-v11-0-rfc-015"></a>

### 5.5 SP-RFC-015 | Feasible Choice Set, Exit, and Voluntariness Identification

**Claim identity:** identification boundary and application hypothesis.
**Dependencies and additional conditions:** clearly specified feasible alternative, exit cost, monopoly control, and observed denominator.
**Generation and evidence card:** [G015](../../社会系统协议学白皮书.md#rfc-evidence-015).

**Normative Spec (规范条文).**
When a central node monopolises basic resources and service interfaces and forcibly bundles indispensable basic services with other obligations, the terminal's feasible choice set may shrink markedly. If the accountability explanation merely invokes formal signing consent without disclosing alternative options, exit costs, and historical coerced contributions, an attribution distortion and pseudo-voluntary narrative arises. One should separately test resource control rights, bundling conditions, feasible exit paths, and ledger records before assessing their effect on trust. Observing choice entropy $H(\text{Choice})=0$ only shows that the choice set is concentrated within the sample; both preference homogeneity and deprivation of feasible alternatives can produce this phenomenon, so the constraint, exit cost, and feasible choice set must be identified independently.

> 📜 **【反垄断工程实证 · 案例 5.5-A】（从“公司市镇（Company Town）”到操作系统强行捆绑）**  
> *制度史实*：19 世纪美国阿巴拉契亚等地区煤矿建立的“公司市镇（Company Town）”常因排他性代币（Company Scrip）、专属商店（Truck System）与住房捆绑引发严重争议；劳工面临高昂退出成本与有限替代选项，成为反垄断与劳动法研究中关于非自愿绑定的经典议题。在反垄断司法史上，如围绕微软将 IE 浏览器与 Windows 操作系统捆绑的诉讼中，司法焦点同样集中于平台是否利用市场支配地位剥夺了下游竞争者与消费者的可行替代选择。类比旨在揭示结构性锁定机制，具体个案的自愿性认定仍须依据法定要件、价格证据与司法判决检验。  
> *系统学分析*：当关键生存接口被排他控制、退出代价高且替代渠道被封堵时，单一选择不能单独证明自愿。拿“自愿负债、买定离手”跳过这些约束，是在掩盖需要核验的权力关系；本段是机制批评，不是已证明的拓扑学命题。

> 📜 **【制度经济注疏 · 案例 5.5-B】（工农业价格剪刀差与历史贡献归因偏差）**  
> *文献线索与核对范围*：Knight & Song（1999）, *The Rural-Urban Divide*，以及林毅夫、蔡昉、李周《中国的奇迹：发展战略与经济改革》（1994），是研究城乡关系、重工业优先战略与资源转移的文献入口。本节尚未补齐支撑统购统销、相对价格与迁移限制各项论述的章节页码，不能将书名入口当作逐项核验完成。宏观资源转移的规模、时期和归属须分别追溯；本节不报告其量化估计。
> *作者主张与机制解释*：本书建议在讨论跨期分担时披露早期制度约束与群体间资源流；是否据此分配后期权益，仍需明示采用的公平准则、群体边界、时期、计量单位和个体归属规则。资源转移事实本身不自动给出个体法定权益或唯一分配比例。“历史贡献记录与事后责任归因脱节”及 `git commit --amend` 仅是对选择性归因的批评类比，不证明史料被删除或确定某主体负有因果责任；其对信任的效果另作经验检验。



<a id="legacy-v11-1-sec-5-6"></a>
<a id="sec-5-6"></a>

### 5.6 Authorisation Implementation, Carriage, and Receiver-Side Regulation Cases



<a id="legacy-v11-1-sec-5-6-1"></a>
<a id="sec-5-6-1"></a>

#### 5.6.1 Relation between authorisation and implementation

The diagram below shows only the institutionalised branch that requires state authorisation; autonomy, contracts, and technical standards can continue to evolve at Ring-3 without uniformly entering the kernel. Post-entry rigidity is a risk path to be examined, not an inevitable life cycle.

```
┌────────────────────────────────────────────────────────────────────────┐
│      Privilege-Ring Crossing & Syscall Lifecycle Model (Syscall Lifecycle)     │
├────────────────────────────────────────────────────────────────────────┤
│  Userland / Ring-3                                                            │
│   - Civilian exploration / civic literature / fringe thought / open-source   │
│     drafts (fault-tolerant sandbox, but no hardware-scheduling authority)     │
│       │                                                                      │
│       ▼ On needing state authorisation, issue a system call                  │
│         (Trap / Software Interrupt)                                          │
│ ──────────────────────────────────────────────────────────────────────────  │
│  Kernel Space / Ring-0                                                        │
│   - Constitutional text / statutory standards / compulsory-education syllabus │
│     / official daemons (holds the privilege of violent scheduling)            │
│       │                                                                      │
│       ▼ If exit, review and feedback fail, institutional rigidity             │
│         (Entropic Trap) may arise                                            │
│  Scholastic Bloat                                                             │
│   - may become a privilege firewall that hinders innovation; specific        │
│     organisations must prove this independently                               │
└────────────────────────────────────────────────────────────────────────┘
```



<a id="legacy-v11-1-sec-5-6-2"></a>
<a id="sec-5-6-2"></a>

#### 5.6.2 Malicious and out-of-bounds syscalls: privilege instructions burning through physical hardware (The Malicious Syscall Anti-Pattern)

**Normative Spec (规范条文).**
When a sovereign kernel, detached from the carrying capacity of the underlying physical hardware, forcibly issues high-cost Syscalls lacking type checking and graceful-degradation fault tolerance, it may exhaust the underlying fault-tolerance margin and significantly raise the systemic risk of micro-level disconnection, production paralysis, and kernel panic.

> 📜 **【历史实证注疏 · 案例 5.6.2-A】（脱离物理现实的重税与系统负荷）**  
> *待核材料*：窗税的议会争论见§3.7-B；法国旧制度包税人制度在本节仅保留为研究线索，尚缺具体合同、时期和地区材料。须分别核对国家财政收入与风险分配、征收者激励、纳税者负担及可行替代机制，不预设包税必然比所有替代方案更有害。
> *候选机制*：若指定征收规则的全成本超出部分主体承载能力且缺少转嫁或缓冲路径，可检验收缩、退出和非正规交易等反应；本节没有提供这些效果的发生率或因果估计，工程类比只组织待核问题。

> **【政策文本比较 · 案例 5.6.2-B】（野猪名录调整，独立于财政案例）**  
> *政策文本与官方说明*：[国家林草局2023年第17号公告](https://www.forestry.gov.cn/c/www/gkzfwj/509750.jhtml)公布新版名录；[局网站刊载的政策解读](https://www.forestry.gov.cn/c/www/gkzcjd/510106.jhtml)说明野猪被调出，并提醒该调整不等于可以随意捕杀。本例限于2023年的政策演进事实，不提供当前个案执法建议，也不把名录修改视为已经测得最优治理效果。



<a id="legacy-v11-1-sec-5-6-3"></a>
<a id="sec-5-6-3"></a>

#### 5.6.3 Broadcast channel and receiver-side responsibility

> 📜 **【冷战历史注疏 · 案例 5.6.3-A】（冷战东德对西方广播电视接收的规制与信道张力）**  
> *实证观察*：冷战时期东德（民主德国）对居民接收西方广播电视信号的政策、社会压力与执法规制经历了不同历史阶段的变化。在 1950–1960 年代（如 1961 年柏林墙建立前后及“自由德国青年团”展开天线整肃运动期间），公开收看收听西方节目被官方视为严重的意识形态渗透与政治违纪，组织传播或公开聚集收听可能面临国家安全机关（Stasi）的搜查、拘留或特定罪名指控（如涉及煽动或叛乱等不同法条）；至 1970 年代后期（尤其埃里希·昂纳克执政中后期），私人家庭收看西德电视在事实上被有限默认容忍，但公开传播与特定政治敏感群体依然受到严密监控。  
> *系统学分析*：这是协议学中讨论**广播信道物理属性与制度语义管制**的典型案例。广播在给定频率、功率、地形和接收设备下具有一定覆盖范围，不按政治边界自动停止传播。系统当无法在物理发射端实施有效阻断时，往往转向对接收端施加法律、社会或行政压力。这种发送端与接收端的责任倒置，导致微观节点在获取客观物理信号时面临不对称的制度合规成本；不同时期的执法强度差异亦表明，信息管制的实际阻抗取决于国家的外部技术可行性与内部社会治理成本的动态平衡。

<!-- SP:END chapter-05 -->
