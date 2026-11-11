> **Translation record**
> - Chinese source: `articles/erjian/为什么一简字成了_二简字却被叫停.md` (sha256 `f6d528230330e5e30346693ca7e654ca71b1df8647555020ace0cc9d90971487`, `37085` bytes, 2026-11-11)
> - Chinese version / release tag: `v0.1` (theoretical version remains v11.2)
> - Translation version: `en-v0.1`
> - Translation date: 2026-11-11
> - Check status: checked sentence by sentence against the Chinese source for claim status, negative guardrails and numbering; machine and glossary checks only; no independent professional native-speaker review
> - Pending sync: synchronized in public-files.json and mkdocs.yml
> - Status: complete translation
> - Authority: the Chinese SSOT is authoritative; this translation does not constitute a separate set of definitions (C2)

# Why Did First-Round Simplified Characters Succeed While Second-Round Simplification Was Halted? — "Hash Collisions" and Disambiguation Cost Shifting in Chinese Character Reform

Twentieth-century China witnessed two major waves of script simplification that followed strikingly different historical trajectories:

- **First-Round Simplification (commonly called *Yijianzi*, 一简字)**: In 1956, the State Council promulgated the *Chinese Character Simplification Scheme*. It was phased in across primary school textbooks and dictionaries, and consolidated into the 1964 *General Table of Simplified Characters*. Today, it forms the foundational standard written daily by over a billion people.
- **Second-Round Simplification (commonly called *Erjianzi*, 二简字)**: On December 20, 1977, national newspapers published the *Second Chinese Character Simplification Scheme (Draft)*. Its "Table 1" (248 characters) was immediately put into trial use in newspapers and textbooks. Yet within a few months—in April and July 1978—the Ministry of Education and other departments issued notices halting its trial use. On June 24, 1986, the State Council formally issued Circular Guofa [1986] No. 64, officially repealing the draft.[[1]](source_notes.md#historical-sources)

This contrast leaves a compelling question for anyone studying language standards, information encoding, and institutional evolution:

If "fewer strokes = lower writing effort = higher communication efficiency" were a universal law, why did Second-Round Simplification trigger an emergency brake within months? Why did First-Round Simplification become national infrastructure, while Second-Round Simplification was officially abandoned?

Through two core systems-engineering concepts—disambiguation cost shifting under many-to-one mappings (analogized to "Hash Collisions") and legacy ecosystem migration cost accounting—the reason becomes clear: **making symbols shorter never automatically equals making total system communication cheaper.**

---

## 1. Saving the Writer's Hand While Taxing the Reader's Brain? Separate "Stroke Reduction" from "Many-to-One Collision"

Before discussing script simplification, we must correct a common accounting misconception: making a character simpler to write, and merging several distinct characters into one glyph, are two completely different operations in information engineering.

We can classify character adjustments into three distinct operations:

| Operation Type | Formal Mapping Relation | Impact on Task Distinguishing Capacity |
| :--- | :--- | :--- |
| ① Allograph consolidation or pure visual reduction | $f(A_1) = f(A_2) = A'$, where $A'$ does not collide with other objects | Distinction preserved: The writer draws fewer strokes; once the reader learns the new shape, semantic boundaries remain intact. |
| ② Visual similarity across distinct objects | $f(A) = A', f(B) = B'$, where $A'$ and $B'$ have closely similar visual features | Reduced visual signal-to-noise ratio: Code distinction remains, but misrecognition risk rises under rapid scanning, low resolution, or cursive writing. |
| ③ Cross-semantic many-to-one merging (homophone / homograph merger) | The task requires distinguishing $A \neq B$, but rewrite maps $f(A) = f(B) = X$ | Many-to-one collision occurs: Given output $X$ alone, it is impossible to invert whether the source was $A$ or $B$ without external clues. |

Type ③—merging characters that originally carried different semantic roles into a single output glyph $X$—has an intuitive analogy in computer science: **Hash Collision**.

> **Engineering Analogy Boundary Note**: We use "Hash Collision" as an intuitive analogy for disambiguation cost shifting under many-to-one mappings ($f(A)=f(B)=X$). This does not claim that human reading is mathematically identical to cryptographic hash functions, nor that modifying character tables is hash bucket expansion.[[2]](source_notes.md#competing-explanations)

In computer systems, when two distinct keys (`Key_A` and `Key_B`) map to the same bucket `X`, inspecting bucket `X` alone cannot identify the key. The system must maintain linked lists, compare full key fields, or execute open-address probing—incurring collision resolution costs.

The same logic applies to written communication ([SP-RFC-001](../../whitepaper/chapter-02.md#sp-rfc-001)):

- **Sender (the writer)**: Replacing a 15-stroke character with a 4-stroke homophone saves two seconds of physical writing effort;
- **Receiver (the reader)**: When multiple common characters are merged into one glyph, the saved information does not vanish—it is **transferred onto the reader's cognitive decoding budget**. Readers must recruit surrounding phrases, full-sentence context, or domain knowledge to resolve conflicts in working memory.

Psycholinguistic experiments on ordinary simplified and traditional character recognition confirm this trade-off. For example, a megastudy by Tsang et al. (2023/2024) in the *Quarterly Journal of Experimental Psychology* examined standard simplified versus traditional characters. While simplified characters reduced stroke burden and yielded higher accuracy, their reduced visual distinctiveness was associated with slightly slower reaction times under certain conditions.[[3]](source_notes.md#historical-sources)

Although that study examined standard simplified characters rather than the 1977 draft, it establishes a clear scientific boundary: **fewer strokes do not automatically guarantee a monotonic reduction in visual recognition and semantic decoding costs.**

---

## 2. Why Context Saves Full Sentences, But Fails in Short Fields, Personal Names, and Archives

At this point, readers familiar with Chinese script history will raise a sharp question (which serves as key same-domain counter-evidence):

> "Wait a minute! Didn't the 1956 First-Round Simplification also include many-to-one merges—such as `后 (后/後)`, `发 (發/髮)`, `干 (干/乾/幹)`, and `历 (歷/曆)`? If First-Round Simplification had collisions too, why did it succeed while Second-Round Simplification was halted?"

This question touches the core mechanism.

First, we must acknowledge: the 1956 First-Round Simplification was never a zero-collision, 100% lossless code. In Unicode Standard Annex #38 (`UAX #38 §3.7.1`, Revision 41), technical specifications explicitly document the one-to-many mapping problem when converting simplified characters back to traditional forms, noting that automated systems cannot uniquely recover the original character without context.[[4]](source_notes.md#historical-sources)

Why, then, do merges like `发 (發/髮)` and `后 (后/後)` rarely create confusion in daily reading?

`UAX #38 §3.4` provides a crucial explanation: **natural reading does not decode isolated single characters in a vacuum; it processes compound words and full sentences.**

In everyday sentences, Chinese possesses abundant contextual redundancy:

- When reading "理发店" (barbershop) versus "出发点" (starting point), "理" and "出" provide strong constraints. The brain resolves ambiguity effortlessly;
- When reading "皇后" (empress) versus "前后" (front and back), disyllabic word compounds serve as natural parity checks.

**However, once we leave full sentences and common compounds and enter restricted-context short fields, the cost of many-to-one collisions erupts.**

Compare how many-to-one merging ($f(A)=f(B)=X$) behaves across three contextual tiers:

| Scenario | Contextual Redundancy | Disambiguation Behavior Under $f(A)=f(B)=X$ | Who Bears the Added Cost? |
| :--- | :---: | :--- | :--- |
| ① Full prose & fixed disyllabic words<br>(e.g., newspaper articles, daily dialogue) | High<br>(surrounding phrases provide strong constraints) | As long as high-frequency clashes in the same semantic slot are avoided, readers resolve ambiguity automatically | Readers' instantaneous context integration (low marginal cost in fixed compounds) |
| ② Restricted-context short fields<br>(e.g., personal names, place names, abbreviations, table headers) | Near zero<br>(only 1–3 characters, no sentence syntax) | Contextual disambiguation fails: Given merged character $X$ alone, impossible to determine if source was $A$ or $B$ | Requires parenthetical notes, verbal explanations, extra fields, or manual verification |
| ③ Intertemporal archives & single-record inversion<br>(e.g., household registers, genealogies, historical indexes) | Intertemporal fracture<br>(later generations face static records without original writer) | Single record cannot be uniquely inverted: Even knowing full conversion tables only yields candidate set $\{A, B\}$ | Archival custodians, descendants, scholars, and individuals bearing misidentification risks |

### Conditional Derivation: When Many-to-One Merges Hit "Surname Short Fields"

Why are personal names the ultimate stress test for character-encoding collisions? Because names typically contain only two or three characters, without grammatical constraints linking surname to given name. Contextual redundancy is near zero.

Consider a controlled conditional derivation (per [CN-S2 Evidence Card](../../research/cases/CN-S2_evidence_starting_point.md), this illustrates conditional logic and does not assert nationwide statistics):

- **Conditional Premise**: Suppose a registration rule merges two distinct surnames $A$ and $B$ (such as "戴/代", "傅/付", or "萧/肖") uniformly into simplified glyph $X$, without preserving an original-character field or migration log;
- **Structural Consequence**: Decades later, an archivist inspecting that entry written as $X$ can only know "this could originally be $A$ or $B$," even if knowing the full table by heart. The system cannot recover the truth value from $X$ alone.
- **Recovery Condition**: Only when the system expends extra preservation costs—such as locating pre-migration original registers, genealogies, or collateral records—can intertemporal disambiguation succeed.

> **Strict Evidentiary Boundary**: This derivation illustrates that context-free short fields lose single-record reversibility under many-to-one mappings. It does not claim that all modern bearers of surnames "代, 付, 肖" originate from the 1977 draft (folk variants and homophone substitutions existed earlier), nor that lineage is impossible to trace when collateral evidence exists.[[5]](source_notes.md#historical-sources) (See the [Appendix](#erjian-mapping-appendix) for specific merged character lists.)

### Separating Two Layers of Intertemporal Traceability: Record Reversibility vs. Historical Text Learnability

In evaluating the long-term cost of script reform, we must separate two distinct questions (see [CN-S2 Evidence Table](../../research/cases/CN-S2_evidence_starting_point.md)):

1. **Single-Record Reversibility**: Whether a single migrated entry can be uniquely inverted (depending on whether mapping was many-to-one and whether original logs were preserved);
2. **Historical Text Learnability**: How much training, dictionary compilation, and translation investment society requires so that new readers can comprehend historical sources.

For example, South Korea undertook translation and digitization of the Classical Chinese *Veritable Records of the Joseon Dynasty* (Source K1). Vietnam has historical preservation and training programs for Chữ Nôm manuscripts (Source V1). These projects show both the barrier to reading original manuscripts after script transitions and the institutional costs society pays to restore access.[[6]](source_notes.md#historical-sources)

Socio-Protocolics avoids exaggerated claims that a society has lost its historical memory. Instead, it asks: **when foundational encoding undergoes an incompatible shift, who pays the ongoing bill for cross-generational translation, dictionary maintenance, and archival preservation?**

---

## 3. Why 1956 Stabilized While 1977 Hit the "System Migration Wall"

Understanding many-to-one collisions and contextual boundaries brings us back to the historical record: why did the 1956 First-Round Simplification cross the migration threshold to become a stable standard, while the late-1977 Second-Round Draft quickly met resistance and was repealed in 1986?

On June 24, 1986, the State Council issued Circular Guofa [1986] No. 64, approving the State Language Commission's submission on repealing the draft (Source S1). Examining this document reveals three key engineering dimensions:

### 1. Diminishing Marginal Returns of Compression vs. Spiking Collision Density

The 1956 scheme did not create characters out of nothing. It largely codified vulgar variants and cursive-derived forms that had circulated organically for centuries. The first round had already harvested the low-hanging fruit: characters that cut stroke counts significantly, enjoyed high social familiarity, and rarely broke high-frequency disambiguation.

By the 1977 draft, attempting to push common characters under ten strokes left minimal design room. The scheme had to rely heavily on homophone merging and radical stripping. The draft's Explanatory Notes explicitly celebrated "eliminating 263 characters" (compressing the character inventory via homophone mergers) as an achievement.[[7]](source_notes.md#historical-sources)

As a result, saving one or two more strokes yielded negligible marginal benefit, while visual estrangement and collision friction in headlines and short fields spiked sharply.

Even clearer institutional corroboration arrived in 1986. When the State Council repealed the draft via Guofa [1986] No. 64 and the State Language Commission re-issued the *General Table of Simplified Characters* in October, authorities not only abolished Second-Round characters, but also executed five targeted "Collision Rollbacks" on the 1964 First-Round table itself. Authorities formally declared: "叠, 覆, 像, 囉" would no longer be treated as variants of "迭, 复, 象, 罗"; "瞭" read `liào` (look out) would no longer be simplified to "了" (see [Appendix Table C](#erjian-mapping-appendix)).[[7]](source_notes.md#historical-sources)

This proves that even within First-Round Simplification, any cross-domain many-to-one merge that created excessive friction in practice eventually triggered a system rollback.

### 2. Installed-Base Ecosystem Lock-In and the "Fixed-Mask ROM Chip" Migration Bill (SP-RFC-017)

Any foundational protocol upgrade must calculate not only whether the new syntax is easier to write, but also **the total cost of recompiling society's installed base** ([SP-RFC-017 Technical Debt & Refactoring Migration Cost](../../whitepaper/chapter-07.md#sp-rfc-017)).

- **In 1956 (Cold-Start Phase)**: Mass literacy campaigns, national unified textbooks, dictionary compilation, and lead-type printing were being newly established—switching encoding during system build-out;
- **By 1977–1986 (Installed-Base Phase)**: Hundreds of millions of literate citizens, textbooks, library catalogs, and reference tools were stably operating on the 1956/1964 baseline.

More notably, in Part 1 of the State Language Commission's 1986 submission (Source S1), policymakers recorded a striking technological reason: beyond scheme immaturity and the need for standard stability, promoting new characters would impose heavy replacement burdens on **existing dictionaries, reference books, and already-manufactured computer Chinese character libraries (specifically citing "fixed-mask chips")!**[[1]](source_notes.md#historical-sources)

> **Evidentiary Identity Calibration**: Under our source standards, "fixed-mask chips and reference book conversion burdens" is recorded as an actor's decision rationale in the State Council-approved submission. We do not claim it was the sole cause of repeal, nor assert an exact nationwide chip cost figure. Yet it vividly illustrates the core mechanism of SP-RFC-017: **when a character protocol is etched into society's textbooks, dictionaries, and hardware ROM chips, the ecosystem-wide migration cost of mutating the character set dwarfs the local benefit of writing a few fewer strokes by hand.**

### 3. The 1978–1986 "Protocol Split-Brain" of Halted Trial Without Formal Repeal (SP-RFC-012 / 014)

The official document chain (S1) reveals an often-overlooked institutional phase:

- December 20, 1977: Draft published; Table 1 enters trial use in publications;
- April and July 1978: Relevant departments notify halting trial use in textbooks and publications;
- 1978 to June 1986: For eight years, Second-Round characters remained suspended—halted in official publications, yet not formally repealed by the State Council.

In protocol terms, these eight years produced a classic **Protocol Split-Brain**: school textbooks and major newspapers reverted to the 1964 table, while street signs, mimeographs, and personal letters continued using or inventing second-round forms. This ongoing dual-track confusion led the State Council to issue Guofa [1986] No. 64 in 1986, formally repealing the draft and re-issuing the 1964 table as the sole authoritative standard.

---

## 4. 🛠️ Takeaway Tool: A 4-Step Checklist for Information Compression & Schema Refactoring

The history of Second-Round Simplification extends far beyond linguistics.

Whether you design microservice APIs, establish corporate reporting standards, or draft public administrative forms, whenever you compress a fine-grained encoding scheme into fewer symbols, the lessons distill into this 4-step checklist:

| Step | Concrete Question You Must Answer Beforehand | Lesson from Character Simplification Case |
| :--- | :--- | :--- |
| 1. Dissect mapping type: Lossless slimming vs. many-to-one collision? | Does your simplification merely trim redundant decoration, or does it merge distinct meanings $A$ and $B$ into one symbol $X$ ($f(A)=f(B)=X$)? | Reducing strokes within a single character lowers writing effort; merging distinct common characters into one glyph creates a "hash collision." |
| 2. Stress-test zero-context short fields: Will it fail outside long prose? | Do not test abbreviations only in context-rich text! If it appears alone in a personal name, table header, alert code, or index, can the receiver uniquely identify it? | Merged characters disambiguated in full sentences (`UAX #38 §3.4`) lose contextual clues in names, titles, and indexes. |
| 3. Trace cost shifting: Who pays for the 2 seconds saved by the sender? | Did saving the writer effort force readers, auditors, or archivists to spend 10x more time guessing and verifying? Did the database retain an original value field? | Without preserving original character fields or migration logs, single merged records cannot be uniquely inverted later. |
| 4. Audit ecosystem migration: Does marginal gain beat recompilation cost? | When an existing standard is embedded in habits, dictionaries, and hardware firmware, is the Net Present Value ([SP-RFC-017](../../whitepaper/chapter-07.md#sp-rfc-017)) of mutating the base code positive or negative? | The 1986 submission explicitly cited the conversion burden on existing reference books and fixed-mask character ROM chips. |

---

## 5. Open Research Invitation: What Is Verified vs. What Awaits Your Contribution

Adhering to *Socio-Protocolics*' standard of "speaking strictly in proportion to evidence," this essay does not treat the repeal as proof of a single formula, but openly presents verified facts and open gaps:

1. **Verified Evidentiary Chain**:
   - The administrative decision chain from December 1977 trial publication, April/July 1978 trial halt, to May 1986 State Language Commission submission and June 1986 State Council Guofa [1986] No. 64 repeal, including the official rationale citing scheme immaturity, norm stability, and dictionary / fixed-mask chip conversion burdens ([Source S1](source_notes.md#historical-sources));
   - Technical standards on one-to-many simplified-traditional mappings and word-level contextual disambiguation in Unicode `UAX #38 §3.7.1 & §3.4`;
   - Experimental psycholinguistic boundaries on speed-accuracy trade-offs in standard simplified vs. traditional word recognition (Tsang et al., 2023/2024).
2. **Excluded Unverified Rumors (Not Used as Evidence Here)**:
   - Rumors circulating in secondary drafts—such as "Second-Round recognition dropped from 83.5%/91.3% to 46.4%/66.9%," "3,500 characters generating 56,008 words equals 16x morpheme loss amplification," or "merging two characters always loses 1 bit permanently"—have been audited and excluded in the [CN-S2 Evidence Starting-Point Card](../../research/cases/CN-S2_evidence_starting_point.md).
3. **Open Research Tasks You Can Claim**:
   - **Contribute primary scans**: Collect high-resolution scans of the December 20, 1977 newspaper publication of the draft, and original notices from April and July 1978 halting trial use;
   - **Construct restricted-context mapping tables**: Following [H01 Research Design](../../research/H01_expression_and_understanding_cost.md) and the [CN-S2 Evidence Table](../../research/cases/CN-S2_evidence_starting_point.md), measure disambiguation and misreading across four context tiers (single character, disyllabic word, full sentence, personal name field) for Table 1 characters.
   - If you have access to archives or experimental data, submit an Issue or Pull Request via our [Open Evidence Wishlist](../../research/OPEN_EVIDENCE_WISHLIST.md)!

---

<a id="erjian-mapping-appendix"></a>

## Appendix: What Did Second-Round Simplified Characters Actually Look Like? — A Three-Category Mapping Catalog

Many readers who did not experience the 1977–1978 newspaper trials ask: What characters were actually in the Second-Round Simplification Draft, and how did they map from source to target?

On December 20, 1977, the Script Reform Committee of China published the *Second Chinese Character Simplification Scheme (Draft)* (containing 853 simplified characters and 61 simplified components, eliminating 263 characters via homophone mergers). The draft was divided into two parts: **Table 1** (248 characters: 172 standalone simplified characters, 21 simplified components, 55 derived characters, put into trial use in newspapers and books from December 1977) and **Table 2** (605 characters: 269 simplified characters, 16 non-standalone components, 336 derived characters, published for public discussion).[[7]](source_notes.md#historical-sources)

To illustrate the mechanisms discussed above, representative characters from the 1977 draft and 1986 explanations are organized into Table A (cross-semantic many-to-one homophone merges), Table B (newly coined outlines and component replacements), and Table C (1986 official collision rollbacks):

### Table A: Representative Cross-Semantic Many-to-One Homophone Merges ($f(A)=f(B)=X$, "Hash Collision" Zone)

Rather than creating a new glyph shape, these operations took an existing character $X$ with its own high-frequency meaning (and sometimes distinct pronunciation) to absorb one or more homophones $A, B$:

| Original Standard Character ($A / B$) | Target Character ($X$) | Pre-Existing Core Meaning / Pronunciation of $X$ | Exact 1977 Draft Location | Collision Pattern & Restricted-Context Disambiguation Pressure |
| :--- | :---: | :--- | :--- | :--- |
| 副 | 付 | To pay / deliver; surname Fu | Table 1 (1) Trial | "副总理, 副局长, 副食品" written as "付总理, 付局长, 付食品"; collides with "pay / surname Fu" in job titles and short labels. |
| 蛋 | 旦 | Dawn / day (*元旦, 一旦*); opera role | Table 1 (1) Trial | "鸡蛋, 蛋白质, 脸蛋" written as "鸡旦, 旦白质, 脸旦"; forces "旦" to carry two unrelated high-frequency semantic domains (dawn vs. egg). |
| 停 | 仃 | Lonely (*伶仃*, note: still read `dīng`) | Table 1 (1) Trial | "停车, 停产, 停电" written as "仃车, 仃产, 仃电"; cross-meaning merge that burdens "仃" with two pronunciations (`tíng / dīng`). |
| 舞 | 午 | Noon / midday (*中午, 午休*) | Table 1 (1) Trial | "跳舞, 歌舞, 鼓舞" written as "跳午, 歌午, 鼓午"; outside fixed compounds, easily produces visual ambiguity with time expressions. |
| 龄 | 令 | Order / command / season / magistrate | Table 1 (1) Trial | "年龄, 工龄, 学龄前" written as "年令, 工令, 学令前"; "工令" (years of work vs. work order) and "军令" (military seniority vs. military order) collide. |
| 帮 | 邦 | Nation / state / friendly country (*友邦*) | Table 1 (1) Trial | "帮忙, 互帮互助, 鞋帮" written as "邦忙, 互邦互助, 鞋邦"; blurs "邻邦" (neighboring country) and "邻帮" (neighboring group/helpers). |
| 盒 | 合 | Close / combine / total | Table 1 (1) Trial | "饭盒, 纸盒, 一盒火柴" written as "饭合, 纸合, 一合火柴"; classifier "一合" collides with verb "一合". |
| 舱 | 仓 | Granary / warehouse (*仓库*) | Table 1 (1) Trial | "船舱, 机舱, 客舱" written as "船仓, 机仓, 客仓"; erases distinction between land warehouse (*货仓*) and vessel hold (*货舱*). |
| 蓝, 篮 | 兰 | Orchid (*兰花*); surname Lan | Table 1 (1) Trial | 3-into-1 merge ($f(\text{兰})=f(\text{蓝})=f(\text{篮})=\text{兰}$): "兰花, 蓝天, 竹篮, 篮球" all written as "兰花, 兰天, 竹兰, 兰球". |
| 叮, 盯, 钉, 靪 | 丁 | 4th Heavenly Stem / adult male / cubes; surname Ding | Table 1 (1) Trial | 5-into-1 merge: "叮嘱, 紧盯, 铁钉, 补靪" all written as "丁嘱, 紧丁, 铁丁, 补丁" ("盯住钉子" becomes "丁住丁子"). |
| 芭, 笆, 粑 | 巴 | Hope / cling / tail; surname Ba | Table 1 (1) Trial | 4-into-1 merge: "芭蕉, 篱笆, 糍粑" all written as "巴蕉, 篱巴, 糍巴". |
| 葫, 猢, 蝴, 糊 | 胡 | Beard / alley / lute; surname Hu | Table 1 (1) Trial | 5-into-1 merge: "葫芦, 猢狲, 蝴蝶, 糊涂/面糊" all written as "胡芦, 胡狲, 胡蝶, 胡涂/面胡". |
| 歉 | 欠 | Owe debt / lack / yawn | Table 1 (1) Trial | "抱歉, 道歉, 歉收" written as "抱欠, 道欠, 欠收". |
| 熄 | 息 | Rest / interest / news / breath | Table 1 (1) Trial | "熄灭, 熄火, 熄灯" written as "息灭, 息火, 息灯". |
| 圆 | 元 | New Year / first / currency unit | Table 1 (1) Trial | "圆形, 团圆, 圆满" written as "元形, 团元, 元满". |
| 账 | 帐 | Mosquito net / tent | Table 1 (1) Trial | "账本, 算账, 报账" written as "帐本, 算帐, 报帐" (lingering confusion persists in common usage). |
| 座 | 坐 | Sit / take transport (verb) | Table 1 (1) Trial | "座位, 茶座, 一座桥" written as "坐位, 茶坐, 一坐桥". |
| 泰 | 太 | Sun / extreme / grand | Table 1 (1) Trial | "泰山, 国泰民安, 泰然" written as "太山, 国太民安, 太然". |
| 煽, 搧 | 扇 | Fan / door leaf | Table 1 (1) Trial | "煽动, 煽风点火, 搧扇子" written as "扇动, 扇风点火, 扇扇子". |
| 预, 豫 | 予 | Give / grant; classical 1st person | Table 1 (1) Trial | "预备, 预算, 犹豫, 豫 (Henan abbreviation)" written as "予备, 予算, 犹予, 予"; "豫剧" becomes "予剧". |
| 萧 | 肖 | Resemble / likeness; surname Xiao | Table 1 (1) Trial | "萧条, 风萧萧" and surname "萧" merged into "肖"; loses single-record reversibility in personal names. |
| 嘴 / 遇 / 橘 / 韭 | 咀 / 迂 / 桔 / 艽 | 咀嚼 (`jǔ`) / 迂回 (`yū`) / 桔梗 (`jié`) / 秦艽 (`jiāo`) | Table 1 (1) Trial | Draft note kept original pronunciation for compounds, creating cross-sound/meaning polyphones ("嘴巴" written "咀巴", "遭遇" written "遭迂"). |
| 戴 | 代 | Replace / era / represent; surname Dai | Table 2·1 Homophone Substitution | Merged "穿戴, 爱戴" and surname "戴" into "代" (Table 2 discussion draft). |
| 傅 | 付 | Pay; surname Fu (Table 1 already merged 副) | Table 2·1 Homophone Substitution | Following Table 1 `副 → 付`, Table 2 proposed `傅 → 付` ("师傅" written "师付"), making "付, 副, 傅" three-into-one. |
| 赣 | 干 | Shield / dry / cadre (already 3-in-1 in 1st round) | Table 2·1 Homophone Substitution | Proposed merging Jiangxi abbreviation "赣" into "干" (which already carried three meanings). |
| 辩, 辨, 辫 | 弁 | Ancient cap / military officer | Table 2·1 Homophone Substitution | Merged "辩论, 辨别, 发辫" into rare ancient character "弁". |
| 鞭 / 陡 / 镰 / 胸 / 颜 | 卞 / 斗 / 连 / 匈 / 彦 | Surname Bian / peck, struggle / connect / Xiongnu / talent | Table 2·1 Homophone Substitution | "皮鞭→皮卞", "陡峭→斗峭", "镰刀→连刀", "胸怀→匈怀", "颜色→彦色". |

### Table B: Newly Coined Outlines, Component Replacements & Derivations ($f(A)=A'$)

These characters did not borrow existing high-frequency characters for homophone mergers, but reduced strokes by trimming outlines, replacing phonetics/radicals, or coining ideograms. They represent one-to-one rewrites, but broke familiar structural patterns and forced fonts, dictionaries, and early character ROM chips to be remanufactured (`SP-RFC-017`):

| Original Standard Character | 1977 Draft Simplified Shape (with structure note) | Simplification Method & Table Location | Impact on Recognition & Legacy Font Ecosystem |
| :--- | :--- | :--- | :--- |
| 餐 | 歺 (upper-left component, homograph of ancient "歹/歺") | Table 1 (1) Trial | 16 strokes reduced to 4 ("餐厅" written "歺厅"), losing the "食" (food) semantic radical. |
| 街 | 亍 (right part, homograph of "亍" in "彳亍") | Table 1 (1) Trial | 12 strokes reduced to 3 ("街道" written "亍道"), visually close to "于, 亏, 丁". |
| 信 | 伩 (left "亻", right "文") | Table 1 (1) Trial | Replaced right "言" with 4-stroke "文", breaking the traditional associative structure. |
| 雪 | 𫜹 (upper simplified rain radical, lower "彐") | Table 1 (1) Trial | Stripped traditional rain head, making weather association difficult for general readers. |
| 酒 | 氿 (left "氵", right "九") | Table 1 (1) Trial | Replaced "酉" with 2-stroke "九" (colliding with place name character "氿 [`guǐ`]"); also simplified "酿 → 𰼃". |
| 算 | 祘 (two parallel "示" components) | Table 1 (1) Trial | Removed bamboo radical, using ancient form "祘"; Table 2 further proposed merging "蒜" into "祘". |
| 病 | 疒 (sickness radical used standalone) | Table 1 (1) Trial | Promoted a non-standalone radical into a full character, easily confused in handwriting with "广, 厂". |
| 部 | 𰆊 (bottom part of "节", i.e., "卩") | Table 1 (1) Trial | Reduced high-frequency "部" ("部队, 干部, 部门") to single seal radical "卩", lowering distinctiveness. |
| 道 / 建 / 迎 | 辺 / 迠 / 迊 (walking radical with "刀 / 占 / 卬") | Table 1 (1) Trial | Simultaneously altered high-frequency walking-radical characters, creating visual unfamiliarity in press. |
| 宣 → 演 | 㝉 → 𰛑 (⿰氵㝉) | Table 1 (1) Trial | "宣" simplified to "㝉", "演" to "⿰氵㝉"; Table 2 also merged "渲" into "㝉". |
| 留 (and 榴, 瘤, 溜) | 畄 (and 𰗶, 𰣲, 𰜈 [⿰氵畄]) | Table 1 (2) Simplifiable Component | Replaced top with grass radical "艹", triggering cascading derived character rewrites. |
| 展, 辗 (and 碾) | 𰍰 (⿸尸一) (and 𰦪 [⿰石𰍰]) | Table 1 (2) Simplifiable Component | Left only single stroke under "尸", visually close to "尺, 尸, 户" in low resolution. |
| 面 / 感 / 鼻 / 属 | 𫩑 (⿱丆口) / 𫹯 (⿱干心) / 𢍂 (⿱自廾) / 𰍱 (⿸尸专) | Table 1 (2) Simplifiable Component | Core high-frequency characters with derived forms (*缅→𰬄, 撼→𰓭, 憾→𰑞, 嘱→𰇰, 瞩→𰥩*); altering them required rebuilding dictionaries and ROM chips. |
| 矮 / 寡 / 家 | 仦 (⿰亻小) / 𠆣 (⿱一人) / 𡦼 (⿱宀人) | Table 2·6 Ideograms | Newly coined ideograms ("person + small = short", "one + person = widow/few", "roof + person = home"), detached from established habits. |

### Table C: Official 1986 "Collision Rollbacks" When Re-Publishing the *General Table of Simplified Characters*

The clearest proof that high-collision many-to-one merges trigger system pushback is that in October 1986, when abolishing the 1977 draft and re-issuing the 1964 First-Round table, the State Language Commission executed five targeted "Collision Rollbacks" on the 1964 table itself!

In the *Explanatory Note on Re-Publishing the "General Table of Simplified Characters"* (October 10, 1986, *Gazette of the State Council*, 1986, Issue No. 29), authorities formally un-merged five many-to-one simplifications[[7]](source_notes.md#historical-sources):

| Original 1964 Merge Rule | 1986 Re-Publication Rollback Decision | Why Rolled Back? (Eliminating High-Frequency Semantic Collisions) |
| :--- | :--- | :--- |
| Merged “叠” into `迭` as traditional variant | Deleted `迭〔叠〕`, restored “叠” as independent standard character | Eliminated collision between "重叠, 折叠, 层峦叠嶂" and "更迭, 交替, 高潮迭起". |
| Merged “覆” into `复` as traditional variant | Deleted `〔覆〕` under `复`, restored “覆” as independent standard character | Eliminated collision between "覆盖, 颠覆, 全军覆没" and "恢复, 复习, 往复" (retaining only 答复/批复). |
| Merged “像” into `象` as traditional variant | Deleted `象〔像〕`, restored “像” as independent standard character | Eliminated collision between "画像, 肖像, 好像" and "大象, 现象, 抽象". |
| Merged “囉” into `罗` as traditional variant | Deleted `〔囉〕` under `罗`, simplified via component derivation into `啰` | Separated modal particle "啰唆, 喽啰, 好啰" from "罗网, 星罗棋布, surname Luo (罗)". |
| Simplified “瞭” to `了` whether read `liǎo` or `liào` | Kept `了` when read `liǎo` (*了解*); restored `瞭` when read `liào` (*瞭望*, look out) | Eliminated reading and segmentation collision between "瞭望哨" written as "了望哨" and aspect particle "了 (`le/liǎo`)". |

> **Appendix Takeaway**: Placing Tables A, B, and C side by side clarifies the protocol boundary of script simplification: **simplifications that trim redundant strokes without creating high-frequency semantic collisions (Table B and First-Round core) face only initial familiarity and font conversion thresholds; whereas attempts to shrink the character inventory via aggressive many-to-one homophone merges (Table A) not only caused the 1977 Second-Round Draft to stall, but even forced the 1986 standardizers to roll back five over-merged characters from the 1964 First-Round Table itself (Table C).**

---

<a id="article-framework"></a>

## Endnote: Which Socio-Protocolics Provisions This Essay Uses, and What It Does Not Claim to Prove

> **Sources & Boundaries**: This essay belongs to Proposition Group I (SP-RFC-001) and Group VI (SP-RFC-017) of the *Socio-Protocolics Whitepaper v11.2*, grounded in SP-POSTULATE-1/2, guided by SP-RFC-007, with authorization boundary analysis from SP-RFC-012/014. The historical backbone comprises the 1956 First-Round Simplification and the 1977–1986 Second-Round Simplification trajectory, cited in [1]–[7] and companion source notes. Focus is placed on many-to-one disambiguation costs and ecosystem migration costs, distinguishing administrative records from engineering analogies. Unverified percentages are excluded, and withdrawal of a draft is not extrapolated into blanket failure. Full registration and version records are preserved in the repository.

1. **Postulate Background**: Uses **[SP-POSTULATE-1](../../whitepaper/chapter-01.md#sec-1-5)** (finite cognitive bandwidth and physical resource constraints: both sender handwriting effort and receiver visual/contextual decoding effort are non-zero, and character standards are constrained by physical dictionaries and hardware font memory) and **[SP-POSTULATE-2](../../whitepaper/chapter-01.md#sec-1-5)** (strategic agents with heterogeneous utility weights across writers, readers, typesetters, and lexicographers).
2. **Core Proposition Groups & Normative Rules**:
   - Uses Group I **[SP-RFC-001](../../whitepaper/chapter-02.md#sp-rfc-001)** (physical channel capacity vs. social semantic decoding boundary): treats Second-Round Simplification as a local reverse-test against the over-strong extrapolation that "fewer strokes / shorter symbols automatically lower comprehension cost," separating allograph consolidation from cross-object many-to-one mappings ($f(A)=f(B)=X$);
   - Uses Group II cross-group normative rule **[SP-RFC-007](../../whitepaper/chapter-03.md#sp-rfc-007)**: emphasizes that public encoding standards must balance writer compression against receiver intelligibility, short-field disambiguation, and archival traceability;
   - Uses Group IV **[SP-RFC-012](../../whitepaper/chapter-05.md#sp-rfc-012)** and **[SP-RFC-014](../../whitepaper/chapter-05.md#sp-rfc-014)**: examines the authorization boundary and the 1978–1986 dual-track "protocol split-brain" between halting textbook trials and formal State Council repeal;
   - Uses Group VI **[SP-RFC-017](../../whitepaper/chapter-07.md#sp-rfc-017)** (technical debt and refactoring migration cost accounting): connects the 1986 State Language Commission submission's discussion of reference books and fixed-mask character ROM chips to ecosystem-wide migration accounting.
3. **Epistemic Boundaries & Untested Parts**:
   - The demonstration that a many-to-one mapping $f(A)=f(B)=X$ cannot be uniquely inverted without extra information is a conditional structural derivation, not a completed laboratory reaction-time measurement on 1977 draft glyphs;
   - "Hash Collision" is explicitly marked as an engineering analogy for disambiguation cost shifting under many-to-one mappings, not a claim of strict mathematical isomorphism to cryptographic hash tables;
   - Surname examples (e.g., *Dai* 代/戴) are strictly bounded as conditional structural illustrations of restricted-context fields, not a verified nationwide household-register natural experiment.
4. **Companion Documents**: Full source locations, secondary-draft error exclusions, and the formal Proposition Testing Receipt are in [Source Notes](source_notes.md); drafting and audit logs are in [Revision Notes](revision_notes.md); the underlying evidentiary table is in the [CN-S2 Evidence Starting-Point Card](../../research/cases/CN-S2_evidence_starting_point.md).
