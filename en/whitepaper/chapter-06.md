> **Translation record**
> - Chinese source: `社会系统协议学白皮书.md`, block `chapter-06` — 55 lines, 7747 bytes, block sha256 `0a717928ca1ffb0b02a47db21c891dfc56f5e7df4e1c227eec50a149abe1b2b355`, taken as the content between the `<!-- SP:BEGIN chapter-06 -->` and `<!-- SP:END chapter-06 -->` markers and reported by `tools/whitepaper_blocks.py list`; whole-file sha256 `d5ffb73e3db73f8bb42a2ecb39871bf6c55eace8bb72111b63a2ee362134d9c8`, 338639 bytes, 2026-11-08
> - Chinese version / release tag: `v11.2-r20261106` (theoretical version remains v11.2)
> - Translation version: `en-v0.1-ch06`
> - Translation date: 2026-11-08
> - Check status: draft; C12 self-check run after write; independent read-only audit to follow; machine and glossary checks only; no independent professional native-speaker review
> - Pending sync: none at present; to be recorded item by item if the Chinese source is updated
> - Status: phased translation of this chapter block — the normative framework text, RFC 6.1 specification, the §6.1.1 TCP and §6.1.2 UDP normative specs, and the Performative-ACK coding constraint are translated; the case-annotation blocks (cases 6.1.1-A, 6.1.2-A, 6.1.2-B) are **retained in the original Chinese** by design under the C-1 phased plan (T3 not yet passed), so those blocks are held untranslated inside this file
> - Authority: the Chinese SSOT is authoritative; this translation does not constitute a separate set of definitions (C2)
> - Note on group name: Proposition Group V's name is consistent throughout the SSOT (chapter title line 1259, the overview tables, the already-landed appendix / chapter-01, and the C12 locked ledger all read "第五组核心命题：传输拓扑与任务反馈" → "Proposition Group V: Transport Topology & Task Feedback"); no internal inconsistency was found.
> - Note on in-block link repointing: the verbatim case block 6.1.2-B contains a repository-relative link `docs/核心案例来源与边界.md`; to resolve under the nested English page it is repointed to `../../docs/核心案例来源与边界.md`, consistent with the cross-chapter link-repointing convention. The Chinese narrative text remains verbatim.

**Scope and edition status.** This file is one block of a **phased** translation. The English edition as a whole is an *abridged adaptation* of the v11.2 whitepaper: the six chapters that carry case-annotation sections are not yet translated, and those annotations remain untranslated by design until the underlying Chinese case materials pass the real-case acceptance stage (T3). Chapter 6 carries case-annotation sections (cases 6.1.1-A, 6.1.2-A, 6.1.2-B); per the C-1 phased plan those annotations are **retained in the original Chinese** inside this file, so the normative framework text, RFC 6.1, and the §6.1.1 / §6.1.2 normative specs are translated while the case-annotation blocks are held in Chinese. Completeness of this block does not imply completeness of the edition, and this translation does not elevate any claim to established status. The block itself runs from the `<!-- SP:BEGIN chapter-06 -->` marker to the `<!-- SP:END chapter-06 -->` marker; the translation record, the chapter glossary and the two notes below precede that boundary and are not part of the translated text.

## Chapter Glossary — Chapter 6

| Chinese | English used in this file | Remark |
| :--- | :--- | :--- |
| 第五组核心命题：传输拓扑与任务反馈 | Proposition Group V: Transport Topology & Task Feedback | group name, unique form in the whole book |
| 6 个核心命题组 | 6 Core Proposition Groups | H3-A landed |
| 19 项有效 SP-RFC | 19 Effective SP-RFC Items | title-case unique |
| 机制类比与经验桥接 | mechanism analogy and empirical bridging | claim identity (016) |
| 动员任务、确认反馈与持续治理 | Mobilisation Task, Acknowledgement Feedback, and Continuous Governance | RFC-016 title |
| 面向连接的可靠有序字节流 | connection-oriented reliable ordered byte stream | §6.1.1 (TCP) |
| 仪式性合规回执 | Performative ACK | §6.1.1 coding constraint |
| 语法层回执 | Syntactic_ACK | §6.1.1 (weighted 0 in $B_{\text{TCP}}$) |
| 拥塞崩溃 | Congestion Collapse | §6.1.2 |
| 战术冻结 | tactical freeze | Tufekci (2017); §6.1.2-B |
| 传闻扩散级联 | rumor diffusion cascade | Vosoughi, Roy & Aral (2018) |
| 优势比 | Odds Ratio | §6.1.2-B (≈1.7) |
| 慢启动 | Slow Start | TCP analogy; §6.1.1-A |

**Note on claim identities.** The claim-identity label in this chapter (RFC 016: mechanism analogy and empirical bridging) is a descriptive phrase at the grain of the source sentence (per R7 of the term ledger), not a taxonomy of claim identities. This translation keeps the five canonical claim identities — `postulate`, `conditional proposition`, `mechanism hypothesis`, `accounting definition`, `normative objective` — distinct, and renders the finer descriptive label by reusing the locked class word. The label is not upgraded into a proven conclusion; the negation guardrails in the source (cannot / does not / are not auto-derived / one cannot predict) are preserved.

**Convention on link re-pointing.** Every in-page anchor that lives in another chapter (`#rfc-evidence-XXX`) is re-pointed to the Chinese source `../../社会系统协议学白皮书.md#…` so the build does not report a missing anchor; these resolve once the corresponding English chapter lands. The repository-relative link `docs/核心案例来源与边界.md` inside the verbatim case block 6.1.2-B is re-pointed to `../../docs/核心案例来源与边界.md` to resolve under the nested English page. Anchors that live in this file (`#chapter-6`, `#sp-rfc-016`, `#sec-6-1`, `#sec-6-1-1`, `#sec-6-1-2`) remain same-page links.

---

<!-- SP:BEGIN chapter-06 -->
<a id="chapter-6"></a>

## Chapter 6: Proposition Group V — Transport Topology & Task Feedback



<a id="sp-rfc-016"></a>
<a id="legacy-v11-1-sec-6-1"></a>
<a id="sec-6-1"></a>

<a id="legacy-v11-1-rfc-018"></a>
<a id="legacy-v11-0-rfc-018"></a>

### 6.1 SP-RFC-016 | Mobilisation Task, Acknowledgement Feedback, and Continuous Governance

**Claim identity:** mechanism analogy and empirical bridging.
**Dependencies and additional conditions:** task transformation, resources, responsibility, and recovery capability are measured separately; the names TCP/UDP do not determine success or failure.
**Generation and evidence card:** [G016](../../社会系统协议学白皮书.md#rfc-evidence-016).

#### 6.1.1 TCP Architecture: Connection-Oriented Reliable Collaborative Network

**Normative Spec (规范条文).**
TCP provides a connection-oriented, reliable, ordered byte stream and can be used to analogise acknowledgement and feedback within organisations; organisational resilience depends on application-layer responsibility tracking, resource replenishment, and fault recovery, and cannot be inferred from the transport-protocol name or the number of ACKs. Reliable mechanisms can also be built atop UDP — see QUIC (RFC 9000).

> 📜 **【历史实证注疏 · 案例 6.1.1-A】（稳扎稳打的慢启动算法）**  
> *史料引证*：[《明史》卷136《朱升传》](https://zh.wikisource.org/wiki/明史/卷136#朱升)记述朱升答“高筑墙，广积粮，缓称王”，并称太祖“善之”。这支持官史中存在该建议的记载，不单独证明其执行强度、持续年数或对胜利的因果贡献；清修官史的叙事仍须互证。
> *系统学分析*：朱元璋的方针可类比为有反馈的渐进扩容（Slow Start），但不是实际采用 TCP 算法。筑城、屯粮与组织建设如何影响战果，仍需结合兵员、财政、军事技术和对手条件判断。

> **Coding constraint guarding against "performative acknowledgement (Performative ACK)":** Meyer and Rowan (1977, AJS 83(2):340–363) discuss how formal structure and actual activity can decouple, which offers a theoretical clue for examining superficial compliance but does not directly prove that any specific organisation sends false acknowledgements at high frequency. Building on this, this book proposes an exploratory measurement coding convention (see §8.3.4 and [G016](../../社会系统协议学白皮书.md#rfc-evidence-016)): a mere textual statement, or a receipt unaccompanied by verifiable resource/state delivery, is recorded only as a syntactic-layer receipt (`Syntactic_ACK`, weighted 0 in $B_{\text{TCP}}$); only closed-loop feedback accompanied by independent third-party sampling verification, physical delivery, or traceable accountability records may be counted into the effective $B_{\text{TCP}}$. This is a coding choice of this book; its measurability and validity must be tested separately and are not auto-derived from the classic literature.

#### 6.1.2 UDP Analogy: Unidirectional Diffusion's Mobilisation Advantage and Governance Boundary

**Normative Spec (规范条文).**
UDP provides connectionless datagram transmission and by itself guarantees no reliable delivery, ordering, or congestion control; it is not equivalent to broadcast, and reliable mechanisms can also be provided by upper-layer protocols. The "UDP broadcast" in this section only analogises unidirectional diffusion and does not directly map a transport protocol onto an organisational type. When moving into complex governance, one should test whether expropriation and resupply, responsibility tracking, negotiated acknowledgement, and fault-recovery capacity can bear the added load; if these capacities remain persistently insufficient, rapid mobilisation may expose governance fragility. If the organisation compensates through layered coordination, existing administrative networks, or other feedback mechanisms, the risk inference must be narrowed or withdrawn — one cannot predict collapse merely from the mode of dissemination. Organisational-level "congestion collapse" is here a mechanism analogy awaiting testing, not a direct corollary of a network theorem.

> 📜 **【历史材料与机制注疏 · 案例 6.1.2-A】（口号广播与治理接口的落差）**  
> *史料引证*：[《明史》卷309《李自成传》](https://zh.wikisource.org/wiki/明史/卷309)记载“迎闯王，不纳粮”的动员口号，同时记载大顺设置六政府及地方官、入京后拷掠旧官索财，以及山海关战败后撤离北京。既有设官记录，便不能说其“完全缺失”行政结构；存在索财行为，也不能直接推出没有任何财政来源。该书为清修官史，相关叙事与归因仍须与其他材料互证。
> *系统学分析*：口号不是财政部，打下城门也不等于接通税收、补给和行政接口。“不纳粮”可作为低复杂度动员信息的切片，不能把整个政权编码成一个 bit，也不能由口号直接反推它没有组织能力。本书提出的候选机制是：动员承诺、持续资源征集与行政执行之间的张力，可能削弱治理韧性；这一解释须与军事失败、外部压力、社会支持及既有行政网络的延续程度比较。若材料显示财政与行政能够持续运作，而败退主要由军事冲击解释，就不能将其归结为“UDP 转治理”的内生死锁。本例用于展示机制比较，不作为已识别因果效应或预测能力的证据。

> 📊 **【计算社会学与政治学实证注疏 · 案例 6.1.2-B】（图费克奇“战术冻结”机制讨论与 MIT 信息瀑布动力学实测）**  
> *经典专著锚点*：图费克奇在《推特与催泪瓦斯》（2017）讨论网络化运动可能出现的“战术冻结”。本书将快速广播类比UDP，将持续协商、确认与后勤磨合类比TCP；这是工程解释框架，不是对两种传输协议决定政治成败的证明。快速聚集可能绕过部分组织能力建设，后续能否谈判、调整策略或治理，还取决于参与者、资源、对手及纠错机制，须用比较材料检验。
> *外部经验研究述评*：麻省理工学院 Vosoughi、Roy 与 Aral 团队发表于《科学》（*Science*, 2018）的研究，追踪了 2006–2017 年间约 300 万用户参与的约 12.6 万个传闻扩散级联（涵盖真、假及混合类别；级联数不等于互不重复的新闻故事数）。该研究发现虚假新闻在扩散深度、广度与速度上显著高于真实传闻；模型估计的转发优势比（Odds Ratio 约 1.7，通俗常称 70% more likely to be retweeted）代表特定控制条件下两组发生优势p/(1-p)的比值，不能理解为在任意基准概率下都增加 70%，亦不可直接等同于情绪唤醒的因果操纵效应。该研究的测量对象是消息扩散，并未直接检验实体组织的治理能力或生存期。
> *机制假说与研究卡规范（避免事后循环定义）*：本书提出待检验的任务机制假说：当动员转入持续资源分配、协商与执行等治理任务，而组织的责任追踪、协调、资源供给或故障恢复能力持续不足以承受新增负载时，可能出现任务失配。须事前固定观察窗口与不足判据，并独立记录四个候选维度：（1）能力，包括专职沟通节点、双向确认规则、责任记录、后勤供给和恢复安排；（2）任务负载，包括并发事务、外部冲突和资源调用峰值；（3）持续时间，采用时序记录；（4）结果状态，区分制度化妥协、有序缩容、分裂和瓦解。四维不是唯一合格设计，列齐也不完成因果识别。若分层协调、既有行政网络或其他机制补足能力，应收窄或撤回对应风险推断；补足确认与反馈本身不保证组织稳定。检验须比较任务负载、外部冲击与既有组织能力等解释，保留过程追踪、比较研究和事件定义明确时的组织生存分析（Survival Analysis）等方法；不能依据最终失败反贴“UDP”标签，也不由消息真假或扩散速度推出组织成败。
> *核查来源*：[Vosoughi、Roy与Aral（2018），作者论文页](https://www.media.mit.edu/publications/the-spread-of-true-and-false-news-online/)。约1.7的优势比对应原论文Fig.4B，不是任意基准概率下固定增加70%。变量、样本、估计口径及未复现范围统一见[来源台账](../../docs/核心案例来源与边界.md)。

<!-- SP:END chapter-06 -->
