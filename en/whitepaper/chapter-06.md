> **Translation record**
> - Chinese source: `社会系统协议学白皮书.md`, block `chapter-06` — 55 lines, 7747 bytes, block sha256 `0a717928ca1ffb0b02a47db21c891dfc56f5e7df4e1c227eec50a149abe1b2b355`, taken as the content between the `<!-- SP:BEGIN chapter-06 -->` and `<!-- SP:END chapter-06 -->` markers and reported by `tools/whitepaper_blocks.py list`; whole-file sha256 `d5ffb73e3db73f8bb42a2ecb39871bf6c55eace8bb72111b63a2ee362134d9c8`, 338639 bytes, 2026-11-08
> - Chinese version / release tag: `v11.2-r20261106` (theoretical version remains v11.2)
> - Translation version: `en-v0.1-ch06`
> - Translation date: 2026-11-08
> - Check status: draft; C12 self-check run after write; independent read-only audit to follow; machine and glossary checks only; no independent professional native-speaker review
> - Pending sync: none at present; to be recorded item by item if the Chinese source is updated
> - Status: complete translation of this chapter block, including all 3 case-annotation entries (batch 4, 2026-11-09); nothing inside the block is omitted
> - Authority: the Chinese SSOT is authoritative; this translation does not constitute a separate set of definitions (C2)
> - Note on group name: Proposition Group V's name is consistent throughout the SSOT (chapter title line 1259, the overview tables, the already-landed appendix / chapter-01, and the C12 locked ledger all read "第五组核心命题：传输拓扑与任务反馈" → "Proposition Group V: Transport Topology & Task Feedback"); no internal inconsistency was found.
> - Note on in-block link repointing: the verbatim case block 6.1.2-B contains a repository-relative link `docs/核心案例来源与边界.md`; to resolve under the nested English page it is repointed to `../../docs/核心案例来源与边界.md`, consistent with the cross-chapter link-repointing convention. The Chinese narrative text remains verbatim.

**Scope and edition status.** This file is one block of a **phased** translation. As of batch 4 (2026-11-09), this file contains the complete chapter-06 block including the full case-annotation layer: the normative framework text, RFC 6.1, the §6.1.1 / §6.1.2 normative specs and the Performative-ACK coding constraint are translated, and so are all 3 case-annotation entries (cases 6.1.1-A, 6.1.2-A, 6.1.2-B); the case-annotation sections retain the source's sharp register. The Chinese master source remains authoritative; this translation does not constitute a separate set of definitions (C2). Completeness of this block does not imply completeness of the edition, and this translation does not elevate any claim to established status. The block itself runs from the `<!-- SP:BEGIN chapter-06 -->` marker to the `<!-- SP:END chapter-06 -->` marker; the translation record, the chapter glossary and the two notes below precede that boundary and are not part of the translated text.

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
**Generation and evidence card:** [G016](appendix.md#rfc-evidence-016).

#### 6.1.1 TCP Architecture: Connection-Oriented Reliable Collaborative Network

**Normative Spec (规范条文).**
TCP provides a connection-oriented, reliable, ordered byte stream and can be used to analogise acknowledgement and feedback within organisations; organisational resilience depends on application-layer responsibility tracking, resource replenishment, and fault recovery, and cannot be inferred from the transport-protocol name or the number of ACKs. Reliable mechanisms can also be built atop UDP — see QUIC (RFC 9000).

> 📜 **[Historical evidence annotation · Case 6.1.1-A] (The slow-and-steady Slow Start algorithm)**  
> *Citation of historical sources*: [《明史》 (*History of Ming*) Book 136, "Biography of Zhu Sheng" (朱升传)](https://zh.wikisource.org/wiki/明史/卷136#朱升) records Zhu Sheng's reply “高筑墙，广积粮，缓称王” (“build high walls, stockpile grain widely, delay claiming kingship”), and says Taizu “善之” (“approved of it”). This supports that the official history contains a record of the advice; it does not by itself prove the intensity of its execution, the number of years it lasted, or its causal contribution to victory; the narrative of the Qing-compiled official history still requires cross-corroboration.
> *Systematic analysis*: Zhu Yuanzhang's strategy can be analogised to feedback-driven gradual capacity expansion (Slow Start), but it was not the actual adoption of the TCP algorithm. How wall-building, grain stockpiling and organisation-building affected battlefield outcomes still requires judgement combined with manpower, finance, military technology and the opponent's conditions.

> **Coding constraint guarding against "performative acknowledgement (Performative ACK)":** Meyer and Rowan (1977, AJS 83(2):340–363) discuss how formal structure and actual activity can decouple, which offers a theoretical clue for examining superficial compliance but does not directly prove that any specific organisation sends false acknowledgements at high frequency. Building on this, this book proposes an exploratory measurement coding convention (see §8.3.4 and [G016](appendix.md#rfc-evidence-016)): a mere textual statement, or a receipt unaccompanied by verifiable resource/state delivery, is recorded only as a syntactic-layer receipt (`Syntactic_ACK`, weighted 0 in $B_{\text{TCP}}$); only closed-loop feedback accompanied by independent third-party sampling verification, physical delivery, or traceable accountability records may be counted into the effective $B_{\text{TCP}}$. This is a coding choice of this book; its measurability and validity must be tested separately and are not auto-derived from the classic literature.

#### 6.1.2 UDP Analogy: Unidirectional Diffusion's Mobilisation Advantage and Governance Boundary

**Normative Spec (规范条文).**
UDP provides connectionless datagram transmission and by itself guarantees no reliable delivery, ordering, or congestion control; it is not equivalent to broadcast, and reliable mechanisms can also be provided by upper-layer protocols. The "UDP broadcast" in this section only analogises unidirectional diffusion and does not directly map a transport protocol onto an organisational type. When moving into complex governance, one should test whether expropriation and resupply, responsibility tracking, negotiated acknowledgement, and fault-recovery capacity can bear the added load; if these capacities remain persistently insufficient, rapid mobilisation may expose governance fragility. If the organisation compensates through layered coordination, existing administrative networks, or other feedback mechanisms, the risk inference must be narrowed or withdrawn — one cannot predict collapse merely from the mode of dissemination. Organisational-level "congestion collapse" is here a mechanism analogy awaiting testing, not a direct corollary of a network theorem.

> 📜 **[Historical-material and mechanism annotation · Case 6.1.2-A] (The gap between slogan broadcasting and the governance interface)**  
> *Citation of historical sources*: [《明史》 (*History of Ming*) Book 309, "Biography of Li Zicheng" (李自成传)](https://zh.wikisource.org/wiki/明史/卷309) records the mobilisation slogan “迎闯王，不纳粮” (“Welcome the Chuang King; he will not take grain”), and at the same time records that Dashun set up six ministries and local officials, that after entering the capital it tortured former officials to extort wealth, and that it withdrew from Beijing after the defeat at Shanhai Pass. Given the records of official appointments, one cannot say its administrative structure was “completely absent”; given the wealth-extraction behaviour, one cannot directly infer that it had no source of revenue whatsoever. The book is a Qing-compiled official history, and its narrative and attributions still require cross-corroboration with other materials.
> *Systematic analysis*: a slogan is not a treasury, and taking a city gate is not the same as hooking up the tax, supply and administrative interfaces. “不纳粮” (“no grain levy”) can serve as a slice of low-complexity mobilisation information; one cannot encode an entire regime into a single bit, nor infer in reverse from the slogan that it had no organisational capability. The candidate mechanism this book proposes is: the tension among mobilisation promises, sustained resource extraction and administrative execution may weaken governance resilience; this explanation must be compared with military defeat, external pressure, social support and the degree of continuity of the existing administrative network. If the materials show that finance and administration could keep operating while the rout is mainly explained by military shock, then it cannot be attributed to an endogenous deadlock of “UDP-to-governance”. This case is used to demonstrate mechanism comparison, not as evidence of an identified causal effect or predictive capability.

> 📊 **[Quantitative computational-sociology and political-science annotation · Case 6.1.2-B] (Tufekci's discussion of the “tactical freeze” mechanism and the measured MIT information-cascade dynamics)**  
> *Classic monograph anchor*: in 《推特与催泪瓦斯》 (*Twitter and Tear Gas*, 2017), Tufekci discusses the “tactical freeze” that can arise in networked movements. This book analogises rapid broadcasting to UDP, and sustained negotiation, acknowledgement and logistical break-in to TCP; this is an engineering explanatory framework, not a proof that the two transport protocols decide political success or failure. Rapid assembly may bypass part of organisational-capacity building; whether negotiation, strategy adjustment or governance can follow depends further on the participants, resources, opponents and error-correction mechanisms, and must be examined with comparative materials.
> *Review of external empirical research*: the study by the MIT team of Vosoughi, Roy and Aral, published in *Science* (2018), tracked roughly 126,000 rumour-diffusion cascades involving about 3 million users between 2006–2017 (covering true, false and mixed categories; the number of cascades does not equal the number of non-duplicated news stories). The study found that false news spread significantly deeper, wider and faster than true rumours; the model-estimated retweeting odds ratio (Odds Ratio about 1.7, colloquially often called 70% more likely to be retweeted) represents the ratio of occurrence odds p/(1-p) between the two groups under specific control conditions; it cannot be understood as an increase of 70% at any baseline probability, nor directly equated with a causal-manipulation effect of emotional arousal. The study's object of measurement is message diffusion; it did not directly examine the governance capability or survival span of substantive organisations.
> *Mechanism hypothesis and research-card specification (avoiding post-hoc circular definition)*: this book proposes a task-mechanism hypothesis awaiting test: when mobilisation shifts into governance tasks such as sustained resource allocation, negotiation and execution, while the organisation's responsibility tracking, coordination, resource supply or fault-recovery capability remains persistently insufficient to bear the added load, task mismatch may appear. The observation window and the insufficiency criterion must be fixed in advance, and four candidate dimensions recorded independently: （1）capability, including dedicated communication nodes, two-way acknowledgement rules, responsibility records, logistical supply and recovery arrangements; （2）task load, including concurrent transactions, external conflict and peaks of resource calls; （3）duration, recorded as time series; （4）outcome state, distinguishing institutionalised compromise, orderly downsizing, schism and collapse. The four dimensions are not the only qualified design, and listing them in full does not complete causal identification. If layered coordination, existing administrative networks or other mechanisms compensate for the capability, the corresponding risk inference must be narrowed or withdrawn; compensated acknowledgement and feedback by themselves do not guarantee organisational stability. Testing must compare explanations such as task load, external shocks and pre-existing organisational capability, and retain methods such as process tracing, comparative studies and — where event definitions are clear — organisational survival analysis (Survival Analysis); one cannot stick the “UDP” label on an organisation in reverse on the basis of its final failure, nor infer organisational success or failure from message truth or diffusion speed.
> *Verification sources*: [Vosoughi, Roy and Aral (2018), authors' paper page](https://www.media.mit.edu/publications/the-spread-of-true-and-false-news-online/). The odds ratio of about 1.7 corresponds to Fig. 4B of the original paper; it is not a fixed 70% increase at any baseline probability. For variables, samples, estimation scope and the non-replicated scope, see uniformly the [source ledger](../case_sources_and_boundaries.md).

<!-- SP:END chapter-06 -->
