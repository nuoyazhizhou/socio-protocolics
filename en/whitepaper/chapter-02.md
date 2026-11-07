> **Translation record**
> - Chinese source: `社会系统协议学白皮书.md`, block `chapter-02` — 212 lines, 26501 bytes, block sha256 `852a158084dae15eed299f73fbd99fb6b3275e4283ae5583a5d2082c2a500c15`, taken as the content between the `<!-- SP:BEGIN chapter-02 -->` and `<!-- SP:END chapter-02 -->` markers and reported by `tools/whitepaper_blocks.py list`; whole-file sha256 `d5ffb73e3db73f8bb42a2ecb39871bf6c55eace8bb72111b63a2ee362134d9c8`, 338639 bytes, 2026-11-08
> - Chinese version / release tag: `v11.2-r20261106` (theoretical version remains v11.2)
> - Translation version: `en-v0.1-ch02`
> - Translation date: 2026-11-08
> - Check status: draft; C12 self-check run after write; independent read-only audit to follow; machine and glossary checks only; no independent professional native-speaker review
> - Pending sync: none at present; to be recorded item by item if the Chinese source is updated
> - Status: phased translation of this chapter block — the normative framework text, RFC 2.1–2.3 and the §2.4–§2.5 specifications are translated; the case-annotation blocks (cases 2.1-A/B/C, 2.2-A, 2.3-A, 2.4.1-A, 2.4.2-A/B/C/D, 2.4.3-A, 2.5-A) are **retained in the original Chinese** by design under the C-1 phased plan (T3 not yet passed), so those blocks are held untranslated inside this file
> - Authority: the Chinese SSOT is authoritative; this translation does not constitute a separate set of definitions (C2)

**Scope and edition status.** This file is one block of a **phased** translation. The English edition as a whole is an *abridged adaptation* of the v11.2 whitepaper: the six chapters that carry case-annotation sections are not yet translated, and those annotations remain untranslated by design until the underlying Chinese case materials pass the real-case acceptance stage (T3). Chapter 2 carries case-annotation sections (cases 2.1-A/B/C, 2.2-A, 2.3-A, 2.4.1-A, 2.4.2-A/B/C/D, 2.4.3-A, 2.5-A); per the C-1 phased plan those annotations are **retained in the original Chinese** inside this file, so the normative framework text, RFC 2.1–2.3 and the §2.4–§2.5 specifications are translated while the case-annotation blocks are held in Chinese. Completeness of this block does not imply completeness of the edition, and this translation does not elevate any claim to established status. The block itself runs from the `<!-- SP:BEGIN chapter-02 -->` marker to the `<!-- SP:END chapter-02 -->` marker; the translation record, the chapter glossary and the two notes below precede that boundary and are not part of the translated text.

## Chapter Glossary — Chapter 2

| Chinese | English used in this file | Remark |
| :--- | :--- | :--- |
| 第一组核心命题：信道容量与语义边界 | Proposition Group I: Channel Capacity & Semantic Boundary | group name, unique form in the whole book |
| 6 个核心命题组 | 6 Core Proposition Groups | H3-A landed, title-case unique |
| 19 项有效 SP-RFC | 19 Effective SP-RFC Items | title-case unique |
| 物理结果引用 | citation of established physical results | claim identity (001) |
| 条件模型 | conditional model | claim identity (001) |
| 社会桥接 | social bridging | claim identity (001) |
| 经验机制假说 | empirical mechanism hypothesis | claim identity (002) |
| 语义传播应用 | semantic propagation application | claim identity (003) |
| 机制假说 | mechanism hypothesis | claim identity (awaiting test) |
| 信道容量 | channel capacity | engineering compression primitive |
| 香农容量 | Shannon capacity | under AWGN model |
| 维特根斯坦式语言边界 | Wittgensteinian language boundary | candidate social-bridging analogy |
| 串行载荷吞吐 | serial payload throughput | Candidate Model 2.1-1 |
| 节点匹配 | node fitness | Candidate Model 2.1-1 |
| 命名 | naming | RFC 002 |
| 共同识别 | common identification | RFC 002 |
| 文本稳定 | textual stability | RFC 003 |
| 跨语境解释 | cross-context interpretation | RFC 003 |
| 源码哈希锁定 | source-hash lock | cognitive analogy, RFC 003 |
| 可读性 | legibility | Scott's term, Case 2.4.2-C |
| Bazaar Maintainer | Bazaar Maintainer | architect niche, §2.4.2 |
| 内联汇编 | inline assembly | §2.4.3 |
| 逆向工程 | reverse engineering | §2.5.1 |
| 受控内联汇编 | controlled inline assembly | §2.4.3 |
| O1–O5 | O1 Agent / O2 Protocol / O3 Expectation & Trust / O4 Middleware / O5 Resource & Physical Constraint | primitive-object codes, unique in the whole book |
| P1–P3 | P1 resource background / P2 agent autonomy / P3 expectation-induced equilibrium | assumption codes, unique in the whole book |

**Note on claim identities.** The claim-identity labels in this chapter (RFC 001: citation of established physical results, conditional model, and social bridging; RFC 002: empirical mechanism hypothesis; RFC 003: semantic propagation application) are descriptive phrases at the grain of the source sentence (per R7 of the term ledger), not a taxonomy of claim identities. This translation keeps the five canonical claim identities — `postulate`, `conditional proposition`, `mechanism hypothesis`, `accounting definition`, `normative objective` — distinct, and renders the finer descriptive labels by reusing the locked class words (conditional model, social bridging, empirical mechanism hypothesis, semantic propagation application, and so on). The labels are not upgraded into proven conclusions; the negation guardrails in the source (does not / cannot / has not) are preserved.

**Convention on link re-pointing.** Every in-page anchor that lives in another chapter (`#sp-rfc-XXX`, `#rfc-evidence-XXX`, `#sec-X-Y`) is re-pointed to the Chinese source `../../社会系统协议学白皮书.md#…` so the build does not report a missing anchor; these resolve once the corresponding English chapter lands. Anchors that live in this file (`#chapter-2`, `#sp-rfc-001`…`#sp-rfc-003`, `#sec-2-1`…`#sec-2-5-1`) remain same-page links.

---

<!-- SP:BEGIN chapter-02 -->
<a id="chapter-2"></a>

## Chapter 2: Proposition Group I — Channel Capacity & Semantic Boundary

This chapter first lists three SP-RFCs, then language and cross-civilisation cases; the cases do not automatically constitute clause verification.


<a id="sp-rfc-001"></a>
<a id="legacy-v11-1-sec-2-1"></a>
<a id="sec-2-1"></a>

<a id="legacy-v11-1-rfc-001"></a>
<a id="legacy-v11-0-rfc-001"></a>

### 2.1 SP-RFC-001｜Physical Channel and Semantic Decoding

**Claim identity:** citation of established physical results, conditional model, and social bridging.  
**Dependencies and additional conditions:** P1; given the channel, task, encoding, audience and comprehension-accuracy are listed separately.  
**Generation and evidence card:** [G001](../../社会系统协议学白皮书.md#rfc-evidence-001).

**Normative Spec (规范条文).**

> This section retains "channel capacity" as an engineering compression primitive, but distinguishes the physical theorem from the social-bridging hypothesis. Under a physical model of additive white Gaussian noise with given bandwidth and power constraints, the Shannon capacity is $I_{\text{phys}}=B_{\text{Hz}}\log_2(1+P_S/P_N)$ (bits/second), where $P_S/P_N$ is the ratio of signal power to noise power within that bandwidth. Capacity is the limit of asymptotically reliable communication under the corresponding channel model; it is not equal to the measured rate of any finite message, and finite-blocklength applications must list block length, admissible error rate and latency requirements separately. It does not directly give the radius of social collaboration, language prevalence, or the engineer-training cycle.
> The social-bridging step must first define the task, success criterion, common knowledge, encoding scheme and collaboration metric $C$ independently, then estimate the relation among comprehension cost, information transfer and task performance. $C\le kI$ and the signal-to-noise expression containing $N_{\text{padding}}$ are merely **candidate social models** before calibration: semantic noise is not identical to physical-noise power, and the dimensionality of $k$, parameter identification and scope of application must each be proven separately. Padding may increase decoding cost, or may provide error correction or common context; one cannot infer from rhetoric alone that throughput goes to zero or that the collaboration circle necessarily shrinks.
> In formal citation and scholarly reference, one must strictly distinguish "physical channel-capacity and decoding-latency results (proven physical conclusions)" from "the Wittgensteinian-channel-capacity candidate social-bridging model (mechanism hypothesis awaiting test)"; this section uses the composite name "Wittgenstein–channel-capacity" only as an engineering index label, and does not borrow the certainty of a physical theorem to endorse the social-bridging hypothesis.
>
> **Candidate Model 2.1-1: Serial Payload Throughput & Node Fitness (串行载荷吞吐与节点匹配).**
> Fix the task, encoding scheme and comprehension accuracy; let r be the effective payload-coded bits per symbol, B be symbols per second (not identical to the physical bandwidth $B_{\text{Hz}}$ above), and d be the independently measured average decoding seconds per symbol. Assuming transmission and decoding are serial, non-overlapping and without retry, the payload throughput from the total latency of these two stages is:
>
> $$\Phi_{\mathrm{payload}}=\frac{rB}{1+Bd}.$$
>
> **Measurement scope:** the numerator is the payload-coded amount for the given task; timing includes only transmission and decoding, not source-side encoding, prior learning or training. If these costs affect scheme choice, they must be accounted separately. Comprehension accuracy must be measured and reported separately; this formula does not discount successfully delivered payload by accuracy, and is not directly called the measured goodput.
>
> Under a bandwidth bottleneck, with fixed r and d, B tending to zero gives throughput approximately rB; under a decoding bottleneck, as B grows large throughput tends to r/d. The latter still requires comparing the ratio of compression rate to decoding overhead, and one cannot judge a winner merely because one style is shorter or more plain. The relation of d to audience, context, text and training is a social-bridging quantity awaiting test; one must not infer from this algebraic expression that decoding cost grows exponentially, that classical Chinese necessarily fails, or that plain vernacular necessarily attains globally maximal throughput or social deadlock. When overlapping pipelines, comprehension error and feedback retry exist, a separate model is required; for detailed settings and the literature divergence see Case 2.1-C.

> 📜 **【历史实证注疏 · 案例 2.1-A】（古典书写与大众理解成本的分层）**  
> *可定位文本*：胡适《文学改良刍议》（1917）列出“须言之有物”“须讲求文法”“务去滥调套语”“不避俗字俗语”等主张。它可用于研究作者提出的表达规范；作者的主张本身不证明读者理解成本已经下降。参见[原文转录](https://zh.wikisource.org/wiki/文學改良芻議)。
> *系统学分析（候选机制）*：可提出一个局部假说：在指定法令任务、受众训练与解释资源条件下，语法、典故及术语要求可能增加理解与转译成本；口头转述、注释或地方实践也可能缓冲这些成本。须用内容可比的文本和受众任务，分别测量理解正确率、时延与执行偏差；不由胡适的表达主张推出基层历史效果已经成立。

> 💻 **【软件工程同构 · 案例 2.1-B】（字符集与接口解码失败）**  
> **解码类比（非社会定理的证据）**：只按 ASCII 验证的解析器遇到超出其范围的 UTF-8 字节，可能拒绝输入、替换字符或进入错误处理。结果取决于编码声明、校验和恢复规则；字符编码不是 CPU 指令集，解码不匹配也不等于全部逻辑必然失效。

> 📐 **【候选模型注疏 · 案例 2.1-C】（串行载荷吞吐与解码成本的条件权衡）**  
> *模型设定*：固定任务、命题集及编码方案，I表示所选有效载荷的编码比特数，不直接称为已测得的“语义比特”。设压缩率r>0（比特/符号）、传输速率B>0（符号/秒）、该受众和任务下独立测得的平均解码时延d>0（秒/符号），符号数N=I/r。假设传输与解码不重叠、无丢包重试、理解正确率固定；计时与正确率口径沿用模型2.1-1，不计源端编码及事前学习成本。  
> *条件代数*：$T_{\mathrm{total}}=N/B+Nd$，故 $\Phi_{\mathrm{payload}}=I/T_{\mathrm{total}}=rB/(1+Bd)$。这里只证明该组假设下的代数关系；若各阶段流水重叠，则需另用瓶颈模型，不能继续直接相加。
> *可检验边界*：B很小时吞吐近似rB；B很大时趋向r/d。比较文体必须同时比较r、d和理解正确率，不能只凭“文言/白话”标签判定任何一方胜出。把d参数化为认知难度与处理速率之比也须独立校准，不能直接用教育年限或可读性年级指数代替这两项物理单位。  
> *文献与证据状态*：Smith与Levy（2013）研究特定语料中词语可预测性与阅读时间的对数关系；Brothers与Kuperberg（2021）在其他设计中报告线性关系。两者的分歧涉及可预测性与处理时间的函数形式，不能合并为所有受众和文体通用的统一函数，也不能直接把其估计换算为本模型的d。载荷吞吐式来自列明假设下的时延相加，不是这些阅读研究或物理容量定理直接给出的社会结论。
> *核查来源*：[Smith & Levy（2013）原论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC3709001/)；[Brothers & Kuperberg（2021）原论文](https://pmc.ncbi.nlm.nih.gov/articles/PMC7584137/)。


<a id="sp-rfc-002"></a>
<a id="legacy-v11-1-sec-2-2"></a>
<a id="sec-2-2"></a>

<a id="legacy-v11-1-rfc-002"></a>
<a id="legacy-v11-0-rfc-002"></a>

### 2.2 SP-RFC-002｜Naming and Common Identification

**Claim identity:** empirical mechanism hypothesis.  
**Dependencies and additional conditions:** P1 background; name content, audience prior knowledge, citation and collaboration process are defined separately.  
**Generation and evidence card:** [G002](../../社会系统协议学白皮书.md#rfc-evidence-002).

**Normative Spec (规范条文).**

> Naming can organise scattered experience into communicable, contestable and researchable concepts, thereby lowering cross-agent identification and coordination cost; but this does not mean that unnamed objective facts cannot be handled by the judiciary or existing rules at all, nor does it mean that naming necessarily brings an absolute monopoly on interpretive authority. The evolutionary validity of an interface declaration depends on legal sources, procedural rules and the competitive interpretation of multiple agents.
>
> **Test entry:** Execute according to the candidate comparison protocol listed under [G002](../../社会系统协议学白皮书.md#rfc-evidence-002) and §8.5.1, distinguishing the overall intervention effect of naming and compression from the independent effect of naming; pre-register the task, comparison objects, primary metrics, minimum meaningful improvement magnitude and error requirements. An existing name or case clue does not equal identified naming gain; when sufficient precision excludes the predetermined improvement, narrow or reject the corresponding local prediction.

> 📰 **【现实案例注疏 · 案例 2.2-A】（“性骚扰”概念演进与制度接口成型）**  
> *案件与书目定位*：1977年哥伦比亚特区联邦巡回上诉法院在[Barnes v. Costle, 561 F.2d 983](https://openjurist.org/561/f2d/983/barnes-v-m-costle)中，针对原告所诉因拒绝上司性要求而遭职场不利对待的情形，认定其主张可落入Title VII性别歧视禁令，并撤销原审简易判决。麦金农1979年的专著《职场女性的性骚扰》（*Sexual Harassment of Working Women: A Case of Sex Discrimination*，参见[耶鲁大学出版社著录](https://yalebooks.yale.edu/book/9780300022995/sexual-harassment-of-working-women/)）以副题标示了性别歧视的论证对象；此处核对的是书目，不替代原书内容研究。两项材料可定位判决与专著的先后，不能据此认定该案发生在概念命名之前，也不能单独识别命名对救济的净效果。
> *系统学分析*：概念命名可提供“API 封装与接口声明”的交流工具；能否降低路由摩擦、是否产生新的解释垄断，应结合实际案件、程序与竞争机制比较，不能把命名本身当成已经测得的协调增益。本例限定的是“司法救济须等待该专著出版”的说法，不是命名增益的正面效果检验，也不是“未命名即可救济”的独立证明。


<a id="sp-rfc-003"></a>
<a id="legacy-v11-1-sec-2-3"></a>
<a id="sec-2-3"></a>

<a id="legacy-v11-1-rfc-003"></a>
<a id="legacy-v11-0-rfc-019"></a>

### 2.3 SP-RFC-003｜Textual Stability and Cross-Context Interpretation

**Claim identity:** semantic propagation application.  
**Dependencies and additional conditions:** Group I; version, context and interpretation task are defined separately, not a direct corollary of SP-RFC-002.  
**Generation and evidence card:** [G003](../../社会系统协议学白皮书.md#rfc-evidence-003).

**Normative Spec (规范条文).**

This section's primary index is Group I and is associated with the Group V propagation task; it is not a direct corollary of SP-RFC-016.

**Division of labour with SP-RFC-002:** SP-RFC-002 tests whether names and shared symbols improve identity recognition and network coordination among nodes; SP-RFC-003 tests whether the same text or version receives consistent interpretation across heterogeneous audiences and contexts. Although the two tasks are clearly distinguished conceptually, "tasks being distinguishable" has not yet established an independent mathematical trade-off law; this item currently mainly completes dimension definition and misuse-prevention protocol, and does not claim to have proven a general "impossibility triangle" or $\mathrm{Portability}\times\mathrm{HashLock}\le\mathrm{Constant}$.
Here "source-hash lock" is a cognitive analogy: a cryptographic hash, under a given algorithm and trusted reference digest, serves to detect physical byte changes, but does not guarantee consistency of semantic interpretation across different cognitive agents. Fixing a native-language canon can strengthen version identifiability, yet interpretive divergence may still exist; cross-platform porting may also preserve the same source.
>
> **Test and falsification protocol:**
> - **Input conditions:** specify the text and version set (explicit source or canon version), the target audience distribution (language background, prior knowledge and cognitive habits), and the concrete cross-context interpretation/execution task;
> - **Measurement output:** independently measure **version identifiability** (whether the specified version within the input set can be accurately identified), **cross-audience interpretation consistency** (variance of understanding across groups) and **actual collaborative-task performance**;
> - **Hypothesis under test and rejection conditions:** this item does not presuppose a general text-lock–propagation trade-off. For a specified task, register local hypotheses separately: H003-V — relative to a given alternative, version identification or reference digest improves version identifiability; H003-I — under the same version, audience and resource conditions, a specified annotation or local interpretation mechanism improves interpretation consistency or task performance. Before the experiment, fix the treatment, control, primary metrics, minimum meaningful improvement magnitude, error interval and sample design; one may set single, common or stratified primary metrics, but must pre-specify the overall success criterion and the corresponding multiple-comparison handling, and must not cherry-pick interpretation after seeing the results; if a qualified comparison excludes the predetermined improvement with sufficient precision, reject or narrow the corresponding local prediction. Observing high lock with low interpretation variance, or success without annotation, only bounds the scope of the corresponding empirical hypothesis, and does not refute the property boundary that "byte consistency does not guarantee semantic consistency"; when there is no difference but insufficient precision, record insufficient evidence rather than treating it as a counter-example.

> 📜 **【文本见证与待核线索 · 案例 2.3-A】（耶路撒冷会议记述与正典版本问题）**  
> *文本见证*：[《使徒行传》15:19—29](https://www.biblegateway.com/passage/?search=Acts%2015&version=NRSVUE)记载针对外邦信徒的决定，未要求其受割礼，但仍保留若干禁戒；不能概括为取消全部规范。[《加拉太书》2章](https://www.biblegateway.com/passage/?search=Galatians%202&version=NRSVUE)包含保罗关于接纳与同席争议的叙述。这里核对的是传世经文译文，不是独立会议纪要，也没有据此识别传播扩张的因果效果。
> *本书机制解释与缺口*：上述材料可用于提出成员条件与跨群体接入的接口问题，但不能证明某次规则调整单独推动了希腊罗马世界的传播。《古兰经》的启示、结集、标准化、译本地位及地方释义须分阶段、传统和任务研究；本节尚未提供可定位史料，暂保留为正典研究线索，不以“文本锁定”证明实践或语义长期一致。


<a id="legacy-v11-1-sec-2-4"></a>
<a id="sec-2-4"></a>

### 2.4 Language-Reform Interfaces, Samples and Compatibility Cases


<a id="legacy-v11-1-sec-2-4-1"></a>
<a id="sec-2-4-1"></a>

#### 2.4.1 Language as I/O and Compiler: the leap from Assembly (Classical Chinese) to C (Vernacular)

**Normative Spec (规范条文).**

In this book's engineering mapping, literary styles can be analogised to Serialization Protocol and Language Spec, literary-reform proposals to a Linter, and new punctuation to the boundary hints of a Lexer. They are used to raise questions of comprehension, translation and adoption cost; they do not imply that natural language equals programming language, nor that Hu Shi alone devised all the grammar or punctuation of modern Chinese. "Assembly → C" is an analogy aimed at the audience, and cannot replace the historical explanation of literature, aesthetics, education and political communication.

> 📜 **【史料与机制假说 · 案例 2.4.1-A】（文言数学文本与初学者理解成本）**  
> *可定位史料*：李善兰与伟烈亚力《代微积拾级》（1859）的[序言](https://zh.wikisource.org/wiki/代微積拾級/序)讨论代数、微分、积分及公式代入。它可作为比较不同表述方式的文本材料；本例提出不同表述与受众理解成本的比较问题；实际差异仍须以平行命题和行为任务测量。  
> *系统学分析*：文言断句、词义与术语门槛可能增加初学者的解码负担；白话教材是否降低理解成本、对不同受众与工程教育产生多大影响，须以可复现任务、语料、受众背景和对照设计检验。此处仅提出机制解释，不报告未经测量的认知算力比例、阅读速率或培养周期缩短幅度。平行语料的候选比较见§8.5.2；具体教材、任务、受众与抽样仍须事前指定。若应用模型2.1-1，另测r、d及正确率；LLM困惑度不能直接替代人类解码时延。


<a id="legacy-v11-1-sec-2-4-2"></a>
<a id="sec-2-4-2"></a>

#### 2.4.2 The Niche and Historical Mechanics of Norm-Setters (Key Figures)

**Normative Spec (规范条文).**

New protocols can evolve through user-space (Ring-3) multi-branch trial-and-error and PDCA-environment selection; this mechanism must satisfy budget, branch independence, observable results and feedback-window conditions, and does not presuppose that any single branch must fail or that all winners come from the margins. An architect can act as "the Bazaar Maintainer & Merge Architect of the evolution racetrack", protecting genuine feedback, extracting Linter norms and implementing reversible incremental merges. The trunk may be autonomous, contractual or an industry standard; the corresponding authorisation interface is taken only when goals such as state enforcement are required. Specific selection follows [SP-RFC-018](../../社会系统协议学白皮书.md#sp-rfc-018) for maturity criteria, comparison windows, branch budgets and stop-or-defer observation rules; it does not require every branch to survive, nor does it replace instance design with a uniform timeout auto-termination.

```
[User-space multi-branch horse race: citizens' storybooks / street-vendor vernacular / local dialects] ──(compare after results mature; feedback frequency bounded by latency)─┐
                                                                                   │
                                                                                   ▼
[Key-Figure niche: identify the winning branch, act as Bazaar Maintainer] ──(filter noise / write Linter)──┤
[Hu Shi's "Essay on Literary Reform" (Eight Don'ts) / Dennis Ritchie extracting the C spec]                       │
                                                                                   ▼
[Merge into autonomous / community / industry trunk; take the Syscall path when state authorisation is needed] <──(incremental merge)─────────┘
[State-authorisation example: 1920 Ministry of Education decree; industry-interface example: POSIX; analyse the two paths separately]
```

> 📜 **【历史实证注疏 · 案例 2.4.2-A】（先秦儒学草案的体系化挂载与制度化演变）**  
> *史料说明*：本书以孔子及后世儒学作为规范形成的研究案例。[《汉书》卷六《武帝纪》篇末“赞”](https://zh.wikisource.org/wiki/漢書/卷006#〖贊〗)含“罢黜百家，表章六经”及兴太学等概括；这是史家评价，不是可据以断代或逐字引用的单次行政诏令。博士设置、教育和人才选任的具体制度、纪年及实施范围仍须分别核查，不以一段赞语证明全部制度化过程。
> *系统学分析*：先秦儒家文本经后续整理、诠释及汉代制度采纳，形成多阶段的权威与治理接口。本书以此比较规范与授权的关系，不假设孔子单独起草一套完整国家协议，也不把制度化当作一次即时入核。

> 💻 **【软件工程同构 · 案例 2.4.2-B】（Dennis Ritchie 与 C 规范的历史不可替代性）**  
> Dennis Ritchie 对 C 语言及早期 UNIX 的贡献，为系统软件的可移植性提供了重要基础。本书据此把胡适的接口整理与传播工作类比为“C 语言之父 + 部分自由软件倡导者”的生态位；这是贡献比较，不是“没有某位个人就不可能出现任何开源替代”的历史反事实证明。

> 📊 **【政治学与媒介史量化实证注疏 · 案例 2.4.2-C】（斯科特“国家可读性”与欧洲活字印刷网络扩张实测）**  
> *经典专著锚点*：政治人类学家詹姆斯·C·斯科特（James C. Scott）在《国家的视角》（*Seeing Like a State*, 1998）中探讨了国家如何通过度量衡标准化、固定姓氏与地籍册等工具将复杂的异构地方习俗转化为“**可读性（Legibility）**”接口以便利治理与税收；这种由上至下的标准化旨在重塑国家治理视角，并不等同于大众对规范的自发理解，亦可能重排中介权力结构。  
> *量化研究及适用边界*：Dittmar（2011, *Quarterly Journal of Economics*）利用欧洲城市人口资料检验早期印刷技术采用与城市增长的关系，采用多变量回归、广义双重差分及以距美因茨距离为工具变量的估计。文中 202 城市是平衡面板，其他规格使用更大的样本；主结果变量是城市人口对数增长。研究支持早期采用印刷技术的城市在 1500–1600 年增长较快，但数值须连同表号、样本与增长口径报告，不宜概括为经济规模均高出 30%–60%，也不单独证明通信带宽具有跨情境的决定性作用。IV解释依赖工具相关性，以及在所列控制条件下距美因茨距离不经其他途径影响城市增长等识别假设；不同规格的样本和变量口径须分别核对。本书引用该研究的条件性解释，未独立复现其估计，也不把排除限制登记为已由本书验证。
> *核查来源*：[Dittmar (2011), Information Technology and Economic Change: The Impact of the Printing Press](https://people.bu.edu/chamley/764-23/Dittmar.pdf)；[Dittmar (2011), 期刊发表页](https://doi.org/10.1093/qje/qjr035)。

> 📜 **【协议工程比较注疏 · 案例 2.4.2-D】（字符、语音与迁移：Soft Fork 的边界）**  
> *工程解释与证据边界*：字符辨识、语音理解与历史文本访问是不同任务。以《施氏食狮史》这类刻意构造的同音文本作压力测试，可以提出特定编码和上下文的消歧问题；不能由极端古文样例推出日常白话语音接近100%解码失败，也不能把汉字直接等同密码学哈希或无碰撞校验码。  
> *系统学分析*：Soft Fork / Hard Fork 可帮助比较字符集转换、复音词、上下文冗余、教材和古籍检索的迁移代价；选择哪种书写方案须分别测量学习、检索与传承成本，不能预先宣布越南或韩国“文明完全断代”或“语义系统毁灭”。胡适的拼音化立场见下一节原始文献，不能把他与赵元任合写成已经共同确立“拼音绝不替代汉字”的单一设计团队。  
> 本书保留“高维语义校验”作为消歧类比，要求其接受任务、语境和误解率检验；没有可复核材料前，不报告80%识字率、1200音节或100%丢包率为本案例的实测结果。


<a id="legacy-v11-1-sec-2-4-3"></a>
<a id="sec-2-4-3"></a>

#### 2.4.3 Controlled Inline Assembly: the Systematic Significance of Classical-Culture Organisation

**Normative Spec (规范条文).**

After a new high-level protocol system is established, a mature system architect never adopts a wipe-the-slate-clean nihilism, but uses the new paradigm as a call bus to perform controlled "inline-assembly reverse engineering" on the underlying classical-historical assets. Here "controlled" means explicit call interfaces, versions and retention goals, comparing in stages and retaining correction and rollback paths; at the same time accounting for organisation, maintenance, teaching and conversion costs. This is the book's normative choice, and does not prove that any existing form should be preserved as-is.

> 📜 **【思想史注疏 · 案例 2.4.3-A】（胡适整理国故：新文体对古典资产的再调用）**  
> *原始文献*：胡适以考证方法研究《水浒传》《红楼梦》与中国哲学史。与此同时，他并非笼统反对拼音化：1918年的通信区分以字母拼写汉语与废去汉语，1953年的答问仍提倡拼音字，并指出白话文及新式标点有助于古书传播。整理国故与文字改革不能简化为互斥的两条路线。
> *系统学分析*：这个案例适合说明受控内联汇编（`__asm__`）：新文体可以为旧文献增加可理解、可考证的调用接口。至于任何书写系统改革的迁移成本，须另行比较教育、检索、版本转换与文化传承代价，不能借胡适之名预先宣布结论。
> *核查来源*：[胡适《跋朱我农来信》（1918-10-15，《新青年》5卷4号，原文转录）](https://zh.wikisource.org/zh-hans/跋朱我农来信)；[胡适《提倡拼音字》（1953-01-06，《胡适言论集》乙编，原文转录）](https://zh.wikisource.org/zh-hans/提倡拼音字（《國語日報》歡迎會上答問）)。


<a id="legacy-v11-1-sec-2-5"></a>
<a id="sec-2-5"></a>

### 2.5 Cross-Civilisation Expression and Local-Interpretation Cases

**Four categories of historical comparison and research-question index (analogy does not replace historical causal identification)**

This table only locates comparison questions, and does not list established mechanisms or complete test designs; when entering concrete research, register objects, periods, materials, results and rejection conditions separately.

| Case | Candidate coordination problem | This book's architectural analogy | Question under test |
| :--- | :--- | :--- | :--- |
| 1. Abraham<br>protocol chain | Group boundaries and cross-language propagation | Acts and Pauline epistles each record access questions (see §2.3); fixed canon analogous to text verification | What roles do access rules, language, interpretive authority and political organisation each play? Do not reduce the two religions to a single source-code design |
| 2. Daoism–Buddhism<br>interaction | Doctrinal exchange and local-organisation development | Text absorption and re-editing analogous to adaptation / reverse engineering | How to distinguish the timing and evidence of absorption, competition and independent development? |
| 3. Song-dynasty philosophy<br>reconfiguration | Ethics, mind-nature and argumentative resources | New interpretive framework analogous to standard-library reconfiguration | How to identify the concrete relation with Buddhism, classics and the institutional environment? |
| 4. Tang–Song classical-prose<br>movement | Style, expressive task and propagation audience | De-redundancy analogous to interface simplification | How to compare the comprehension and argumentation cost of different texts? Do not claim a measured low-latency bus |


<a id="legacy-v11-1-sec-2-5-1"></a>
<a id="sec-2-5-1"></a>

#### 2.5.1 Reverse-Engineering Defence and Channel Denoising: Crisis Self-Rescue of Native Systems

**Normative Spec (规范条文).**

Cross-cultural knowledge import may spur competition, borrowing and recombination; formal rhetoric may also increase or decrease comprehension cost. Reverse-Engineered Wrapper and Payload Denoising can be used to raise research hypotheses, but knowledge inheritance, comprehension and task performance must be validated independently; one must not presuppose that a culture must adopt a certain path to survive, nor treat shortening text as automatically lossless compression.

> 📜 **【待补证研究线索与机制比较 · 案例 2.5-A】（道教抗佛逆向工程、宋明理学内核重写与唐宋古文去噪）**  
> *已定位文本与研究线索*：佛道之间的借鉴、竞争与整合须分期研究。[《魏书》卷一一四《释老志》“老”部](https://zh.wikisource.org/wiki/魏書/卷114#老)包含寇谦之的新科与朝廷崇奉叙述；[《梁书》卷五十一《陶弘景传》](https://zh.wikisource.org/wiki/梁書/卷51#陶弘景)记其齐梁时期经历。这里核对的是传世转录中的叙述，不把神异记载当作事件实证，也不据人物传记推出佛教影响或文化防御效果。陆修静经书整理、陶弘景谱系整理的具体年代与文本、道藏及十王观念发展仍保留为待逐项定位的线索；韩愈、柳宗元的文道主张及北宋周敦颐、张载、二程与南宋朱熹的思想关系也须分别补证，不预设“文以载道”为韩柳共同创立的单一口号。上述未补齐部分不登记为已完成的历史实证案例。
> *系统学分析（待检验）*：道教与佛教的借鉴和竞争可借“跨系统协议的兼容层与重构”提出比较问题；唐宋古文运动可借“协议栈去Padding”提出表达资源是否重新配置的假说，不能预定骈文必有冗余或古文必更高效。“释放带宽给政策论辩与哲学思辨”须另以指定文本任务、受众正确率、处理时延及实际论辩表现检验；字数、字节或r的变化都不直接证明认知资源已被释放。此类比不是历史演化的工程还原，也不报告未经测量的压缩率或资源再配置效果。

<!-- SP:END chapter-02 -->
