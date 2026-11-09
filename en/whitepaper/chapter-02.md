> **Translation record**
> - Chinese source: `社会系统协议学白皮书.md`, block `chapter-02` — 212 lines, 26501 bytes, block sha256 `852a158084dae15eed299f73fbd99fb6b3275e4283ae5583a5d2082c2a500c15`, taken as the content between the `<!-- SP:BEGIN chapter-02 -->` and `<!-- SP:END chapter-02 -->` markers and reported by `tools/whitepaper_blocks.py list`; whole-file sha256 `d5ffb73e3db73f8bb42a2ecb39871bf6c55eace8bb72111b63a2ee362134d9c8`, 338639 bytes, 2026-11-08
> - Chinese version / release tag: `v11.2-r20261106` (theoretical version remains v11.2)
> - Translation version: `en-v0.1-ch02`
> - Translation date: 2026-11-08
> - Check status: draft; C12 self-check run after write; independent read-only audit to follow; machine and glossary checks only; no independent professional native-speaker review
> - Pending sync: none at present; to be recorded item by item if the Chinese source is updated
> - Status: complete translation of this chapter block, including all 12 case-annotation entries (batch 4, 2026-11-09); nothing inside the block is omitted
> - Authority: the Chinese SSOT is authoritative; this translation does not constitute a separate set of definitions (C2)

**Scope and edition status.** This file is one block of a **phased** translation. As of batch 4 (2026-11-09), this file contains the complete chapter-02 block including the full case-annotation layer: the normative framework text, RFC 2.1–2.3 and the §2.4–§2.5 specifications are translated, and so are all 12 case-annotation entries (cases 2.1-A/B/C, 2.2-A, 2.3-A, 2.4.1-A, 2.4.2-A/B/C/D, 2.4.3-A, 2.5-A); the case-annotation sections retain the source's sharp register. The Chinese master source remains authoritative; this translation does not constitute a separate set of definitions (C2). Completeness of this block does not imply completeness of the edition, and this translation does not elevate any claim to established status. The block itself runs from the `<!-- SP:BEGIN chapter-02 -->` marker to the `<!-- SP:END chapter-02 -->` marker; the translation record, the chapter glossary and the two notes below precede that boundary and are not part of the translated text.

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

> 📜 **[Historical evidence annotation · Case 2.1-A] (The stratification of classical writing and mass comprehension cost)**  
> *Locatable text*: Hu Shi's 《文学改良刍议》 (Essay on Literary Reform, 1917) lists propositions such as “须言之有物” (writing must have substance), “须讲求文法” (grammar must be heeded), “务去滥调套语” (do away with clichés and stock phrases) and “不避俗字俗语” (do not shun vulgar characters and colloquial speech). It can be used to study the expressive norms the author proposed; the author's propositions themselves do not prove that readers' comprehension cost had already fallen. See [the transcribed original](https://zh.wikisource.org/wiki/文學改良芻議).
> *Systematic analysis (candidate mechanism)*: a local hypothesis may be proposed: under a designated decree task, audience training and interpretive resources, requirements on grammar, allusions and terminology may increase comprehension and translation cost; oral retelling, annotation or local practice may also buffer these costs. Using content-comparable texts and audience tasks, comprehension accuracy, latency and execution deviation must be measured separately; from Hu Shi's expressive propositions one does not infer that the grassroots historical effect had already been established.

> 💻 **[Software-engineering isomorphism annotation · Case 2.1-B] (Character sets and interface decoding failure)**  
> **Decoding analogy (not evidence of a social theorem)**: a parser that validates input as ASCII only, on encountering UTF-8 bytes beyond its range, may reject the input, substitute characters, or enter error handling. The outcome depends on the encoding declaration and the checksum and recovery rules; character encoding is not a CPU instruction set, and a decoding mismatch is not equivalent to all logic necessarily failing.

> 📐 **[Candidate-model annotation · Case 2.1-C] (Conditional trade-off between serial payload throughput and decoding cost)**  
> *Model setting*: fix the task, the proposition set and the encoding scheme; I denotes the number of payload-coded bits of the chosen payload, not directly called a measured “semantic bit”. Let the compression rate r>0 (bits/symbol), the transmission rate B>0 (symbols/second), and the independently measured average decoding latency d>0 (seconds/symbol) for this audience and task; the number of symbols is N=I/r. Assume transmission and decoding do not overlap, there is no packet-loss retry, and comprehension accuracy is fixed; the timing and accuracy scopes follow Model 2.1-1, and source-side encoding and prior-learning costs are not counted.  
> *Conditional algebra*: $T_{\mathrm{total}}=N/B+Nd$, hence $\Phi_{\mathrm{payload}}=I/T_{\mathrm{total}}=rB/(1+Bd)$. Only the algebraic relation under this set of assumptions is demonstrated here; if the stage pipelines overlap, a separate bottleneck model is required, and the terms can no longer be added directly.
> *Testable boundary*: when B is very small, throughput is approximately rB; when B is very large, it tends to r/d. Comparing literary styles must simultaneously compare r, d and comprehension accuracy; one cannot judge either side the winner by the “Classical Chinese/vernacular” label alone. Parameterising d as the ratio of cognitive difficulty to processing rate must also be independently calibrated; years of education or readability grade indices cannot directly substitute for these two physical units.  
> *Literature and evidence status*: Smith and Levy (2013) study the logarithmic relation between word predictability and reading time in specific corpora; Brothers and Kuperberg (2021) report a linear relation in other designs. The divergence between the two concerns the functional form relating predictability to processing time; it cannot be merged into one universal function for all audiences and styles, nor can their estimates be directly converted into the d of this model. The payload-throughput formula comes from adding latencies under explicitly stated assumptions; it is not a social conclusion delivered directly by these reading studies or by physical capacity theorems.
> *Verification sources*: [Smith & Levy (2013), original paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC3709001/); [Brothers & Kuperberg (2021), original paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC7584137/).


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

> 📰 **[Real-world case annotation · Case 2.2-A] (Evolution of the “sexual harassment” concept and the taking shape of an institutional interface)**  
> *Case and bibliographic positioning*: in 1977 the United States Court of Appeals for the District of Columbia Circuit, in [Barnes v. Costle, 561 F.2d 983](https://openjurist.org/561/f2d/983/barnes-v-m-costle), held that — for the plaintiff's alleged adverse workplace treatment after refusing her supervisor's sexual demands — her claim could fall under the Title VII prohibition of sex discrimination, and vacated the lower court's summary judgment. MacKinnon's 1979 monograph 《职场女性的性骚扰》 (*Sexual Harassment of Working Women: A Case of Sex Discrimination*; see [the Yale University Press record](https://yalebooks.yale.edu/book/9780300022995/sexual-harassment-of-working-women/)) marked sex discrimination as the object of its argument in the subtitle; what is checked here is the bibliographic record, which does not substitute for studying the book's contents. The two materials can order the judgment and the monograph in time; from this one cannot conclude that the case occurred before the concept was named, nor separately identify the net effect of naming on remedies.
> *Systematic analysis*: concept naming can provide a communication tool of “API encapsulation and interface declaration”; whether it lowers routing friction, and whether it creates a new interpretive monopoly, should be examined against actual cases, procedures and competitive mechanisms — naming itself must not be treated as a coordination gain that has already been measured. What this example delimits is the claim that “judicial remedies had to wait for that monograph's publication”; it is not a positive-effect test of the naming gain, nor an independent proof that remedies were available without naming.


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

> 📜 **[Textual witness and pending leads annotation · Case 2.3-A] (The account of the Jerusalem council and the problem of canonical versions)**  
> *Textual witness*: [Acts 15:19—29](https://www.biblegateway.com/passage/?search=Acts%2015&version=NRSVUE) records the decision concerning Gentile believers: circumcision was not required of them, but several prohibitions were retained; it cannot be generalised as cancelling all norms. [Galatians 2](https://www.biblegateway.com/passage/?search=Galatians%202&version=NRSVUE) contains Paul's account of the dispute over acceptance and table fellowship. What is checked here is the transmitted scriptural text in translation, not independent council minutes, and no causal effect of propagation expansion has been identified on that basis.
> *This book's mechanism explanation and gap*: the materials above can be used to raise the interface question of membership conditions and cross-group access, but they cannot prove that some single rule adjustment alone drove propagation across the Greco-Roman world. The Quran's revelation, collection, standardisation, translation status and local interpretation must be studied by stage, tradition and task; this section has not yet provided locatable historical sources, and the matter is retained for now as a lead for canon research — “textual locking” is not used to prove long-run consistency of practice or semantics.


<a id="legacy-v11-1-sec-2-4"></a>
<a id="sec-2-4"></a>

### 2.4 Language-Reform Interfaces, Samples and Compatibility Cases


<a id="legacy-v11-1-sec-2-4-1"></a>
<a id="sec-2-4-1"></a>

#### 2.4.1 Language as I/O and Compiler: the leap from Assembly (Classical Chinese) to C (Vernacular)

**Normative Spec (规范条文).**

In this book's engineering mapping, literary styles can be analogised to Serialization Protocol and Language Spec, literary-reform proposals to a Linter, and new punctuation to the boundary hints of a Lexer. They are used to raise questions of comprehension, translation and adoption cost; they do not imply that natural language equals programming language, nor that Hu Shi alone devised all the grammar or punctuation of modern Chinese. "Assembly → C" is an analogy aimed at the audience, and cannot replace the historical explanation of literature, aesthetics, education and political communication.

> 📜 **[Sources and mechanism hypothesis annotation · Case 2.4.1-A] (Classical-Chinese mathematical texts and beginners' comprehension cost)**  
> *Locatable historical source*: the [preface](https://zh.wikisource.org/wiki/代微積拾級/序) of Li Shanlan and Alexander Wylie's 《代微积拾级》 (an 1859 Chinese translation of a calculus textbook) discusses algebra, differentiation, integration and substitution into formulas. It can serve as textual material for comparing modes of expression; this case raises the comparison question between modes of expression and audiences' comprehension cost; the actual difference must still be measured with parallel propositions and behavioural tasks.  
> *Systematic analysis*: classical-Chinese segmentation, word senses and terminology thresholds may add to beginners' decoding burden; whether vernacular textbooks lower comprehension cost, and how much they affect different audiences and engineering education, must be tested with reproducible tasks, corpora, audience backgrounds and controlled designs. What is offered here is only a mechanism explanation; unmeasured ratios of cognitive compute, reading rates, or reductions in training cycles are not reported. For candidate comparisons on parallel corpora see §8.5.2; the specific textbooks, tasks, audiences and sampling must still be pre-specified. If Model 2.1-1 is applied, r, d and accuracy must be measured separately; LLM perplexity cannot directly substitute for human decoding latency.


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

> 📜 **[Historical evidence annotation · Case 2.4.2-A] (Systematic mounting and institutional evolution of the pre-Qin Confucian draft)**  
> *Note on historical sources*: this book takes Confucius and later Confucianism as a research case of norm formation. The closing “appreciation” (赞) of [《汉书》 (*Book of Han*) Book 6, "Annals of Emperor Wu" (武帝纪)](https://zh.wikisource.org/wiki/漢書/卷006#〖贊〗) contains the summaries “罢黜百家，表章六经” (dismiss the hundred schools, exalt the Six Classics) and the founding of the Imperial Academy; this is a historian's evaluation, not a single administrative edict on which dating can be based or which can be quoted verbatim. The concrete institutions of Erudite appointments, education and talent selection, their chronology and scope of implementation must still be checked separately; one passage of appreciation does not prove the entire institutionalisation process.
> *Systematic analysis*: the pre-Qin Confucian texts, through later organisation, interpretation and Han-dynasty institutional adoption, formed a multi-stage authority-and-governance interface. This book uses this to compare the relation between norms and authorisation; it does not assume that Confucius single-handedly drafted a complete state protocol, nor treat institutionalisation as a single instant merge into the trunk.

> 💻 **[Software-engineering isomorphism annotation · Case 2.4.2-B] (Dennis Ritchie and the historical non-substitutability of the C specification)**  
> Dennis Ritchie's contributions to the C language and early UNIX provided an important foundation for the portability of system software. On this basis the book analogises Hu Shi's interface-organisation and propagation work to the niche of “father of the C language + part-time free-software advocate”; this is a comparison of contributions, not the historical counterfactual proof that “without some particular individual, no open-source alternative could possibly have appeared”.

> 📊 **[Quantitative political-science and media-history annotation · Case 2.4.2-C] (Scott's “state legibility” and the measured expansion of the European movable-type printing network)**  
> *Classic monograph anchor*: the political anthropologist James C. Scott, in 《国家的视角》 (*Seeing Like a State*, 1998), explored how states use instruments such as standardised weights and measures, fixed surnames and cadastral registers to convert complex heterogeneous local customs into “**legibility**” interfaces that facilitate governance and taxation; this top-down standardisation aims to reshape the state's governance perspective, is not equivalent to the masses' spontaneous comprehension of norms, and may also rearrange intermediary power structures.  
> *Quantitative study and boundary of applicability*: Dittmar (2011, *Quarterly Journal of Economics*) used European city population data to test the relation between early printing-technology adoption and city growth, using multivariate regression, generalised difference-in-differences, and estimation with distance from Mainz as an instrument. The 202 cities in the paper form a balanced panel; other specifications use larger samples; the main outcome variable is log growth of city population. The study supports that cities adopting printing early grew faster over 1500–1600, but the figures must be reported together with table numbers, sample and growth scope; they should not be generalised into uniformly 30%–60% higher economic size, nor do they by themselves prove that communication bandwidth has a decisive cross-contextual role. The IV interpretation rests on identification assumptions such as instrument relevance and that, under the listed controls, distance from Mainz does not affect city growth through other channels; the samples and variable scopes of different specifications must be checked separately. This book cites the study's conditional interpretation, has not independently replicated its estimates, and does not register the exclusion restrictions as verified by this book.
> *Verification sources*: [Dittmar (2011), Information Technology and Economic Change: The Impact of the Printing Press](https://people.bu.edu/chamley/764-23/Dittmar.pdf); [Dittmar (2011), journal publication page](https://doi.org/10.1093/qje/qjr035).

> 📜 **[Protocol-engineering comparison annotation · Case 2.4.2-D] (Characters, speech and migration: the boundary of the Soft Fork analogy)**  
> *Engineering explanation and evidence boundary*: character recognition, speech understanding and access to historical texts are different tasks. Using deliberately constructed homophone texts such as 《施氏食狮史》 (“Lion-Eating Poet in the Stone Den”) as stress tests can raise disambiguation questions for particular encodings and contexts; one cannot infer from extreme classical samples that everyday vernacular speech approaches 100% decoding failure, nor equate Chinese characters directly with cryptographic hashes or collision-free check codes.  
> *Systematic analysis*: Soft Fork / Hard Fork can help compare the migration costs of character-set conversion, polyphonic words, contextual redundancy, and textbook and classical-text retrieval; choosing a writing scheme requires measuring learning, retrieval and transmission costs separately, and one cannot pre-announce “complete civilisational rupture” or “destruction of the semantic system” for Vietnam or Korea. Hu Shi's romanisation stance appears in the primary sources of the next section; he must not be co-written with Zhao Yuanren into a single design team that had already jointly established “romanisation will never replace Chinese characters”.  
> This book retains “high-dimensional semantic verification” as a disambiguation analogy and requires it to undergo tests of task, context and misunderstanding rate; until verifiable materials exist, 80% literacy, 1200 syllables or 100% packet loss are not reported as measured results of this case.


<a id="legacy-v11-1-sec-2-4-3"></a>
<a id="sec-2-4-3"></a>

#### 2.4.3 Controlled Inline Assembly: the Systematic Significance of Classical-Culture Organisation

**Normative Spec (规范条文).**

After a new high-level protocol system is established, a mature system architect never adopts a wipe-the-slate-clean nihilism, but uses the new paradigm as a call bus to perform controlled "inline-assembly reverse engineering" on the underlying classical-historical assets. Here "controlled" means explicit call interfaces, versions and retention goals, comparing in stages and retaining correction and rollback paths; at the same time accounting for organisation, maintenance, teaching and conversion costs. This is the book's normative choice, and does not prove that any existing form should be preserved as-is.

> 📜 **[Intellectual-history annotation · Case 2.4.3-A] (Hu Shi's reorganisation of the national heritage: the new vernacular style re-invoking classical assets)**  
> *Primary sources*: Hu Shi studied 《水浒传》 (*Water Margin*), 《红楼梦》 (*Dream of the Red Chamber*) and the history of Chinese philosophy with evidential-research methods. At the same time he was not opposed to romanisation across the board: his 1918 correspondence distinguished spelling Chinese with letters from abolishing Chinese, and his 1953 reply still advocated a phonetic script, noting that the vernacular written language and new punctuation helped the dissemination of old books. Reorganising the national heritage and script reform cannot be simplified into two mutually exclusive routes.
> *Systematic analysis*: this case suits illustrating controlled inline assembly (`__asm__`): the new vernacular style can add comprehensible, verifiable call interfaces to old documents. As for the migration cost of any writing-system reform, the costs of education, retrieval, version conversion and cultural transmission must be compared separately; conclusions must not be pre-announced in Hu Shi's name.
> *Verification sources*: [Hu Shi, "Postscript to Zhu Wonong's Letter" (《跋朱我农来信》, 1918-10-15, 《新青年》 (*New Youth*) vol. 5 no. 4, transcribed original)](https://zh.wikisource.org/zh-hans/跋朱我农来信); [Hu Shi, "Advocating a Phonetic Script" (《提倡拼音字》, 1953-01-06, 《胡适言论集》 (*Collected Hu Shi Discourses*) series B, transcribed original)](https://zh.wikisource.org/zh-hans/提倡拼音字（《國語日報》歡迎會上答問）).


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

> 📜 **[Pending-evidence research leads and mechanism comparison annotation · Case 2.5-A] (Daoist reverse-engineering against Buddhism, Song–Ming Neo-Confucian kernel rewriting, and Tang–Song classical-prose denoising)**  
> *Located texts and research leads*: borrowing, competition and integration between Buddhism and Daoism must be studied by period. [《魏书》 (*Book of Wei*) Book 114, "Lao" (老) section of the "Treatise on Buddhism and Daoism" (释老志)](https://zh.wikisource.org/wiki/魏書/卷114#老) contains the narrative of Kou Qianzhi's new statutes and the court's veneration; [《梁书》 (*Book of Liang*) Book 51, "Biography of Tao Hongjing" (陶弘景传)](https://zh.wikisource.org/wiki/梁書/卷51#陶弘景) records his experiences in the Qi and Liang periods. What is checked here is the narrative in transmitted transcriptions; miraculous records are not treated as event evidence, nor are effects of Buddhist influence or cultural defence inferred from biographies. The dates and texts of Lu Xiujing's scripture organisation and Tao Hongjing's lineage organisation, the Daoist Canon and the development of the Ten Kings conception remain leads to be located item by item; Han Yu's and Liu Zongyuan's propositions on wen and the Way, and the intellectual relations among Zhou Dunyi, Zhang Zai and the Cheng brothers of the Northern Song and Zhu Xi of the Southern Song, must also be supplemented with evidence separately — “文以载道” (writing as the vehicle of the Way) is not presupposed to be a single slogan co-founded by Han and Liu. The unsupplemented portions above are not registered as completed historical-evidence cases.
> *Systematic analysis (awaiting test)*: borrowing and competition between Daoism and Buddhism can raise comparison questions via “the compatibility layer and refactoring of cross-system protocols”; the Tang–Song classical-prose movement can raise, via “protocol-stack padding removal”, the hypothesis of whether expressive resources were reallocated — one cannot presuppose that parallel prose necessarily carries redundancy or that classical prose is necessarily more efficient. “Freeing bandwidth for policy debate and philosophical speculation” must be tested separately with designated text tasks, audience accuracy, processing latency and actual debate performance; changes in character counts, bytes or r do not directly prove that cognitive resources were released. This analogy is not an engineering reduction of historical evolution, and unmeasured compression rates or resource-reallocation effects are not reported.

<!-- SP:END chapter-02 -->
