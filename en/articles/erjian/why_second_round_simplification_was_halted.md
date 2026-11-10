> **Translation record**
> - Chinese source: `articles/erjian/为什么一简字成了_二简字却被叫停.md` (sha256 `b8d27f6aa424907959331b7a0731e3445f5a08ea18ca6b37b9dfe98cb0a7f7d5`, `42138` bytes, 2026-11-10)
> - Chinese version / release tag: `v0.1` (theoretical version remains v11.2)
> - Translation version: `en-v0.1`
> - Translation date: 2026-11-10
> - Check status: checked sentence by sentence against the Chinese source for claim status, negative guardrails and numbering; machine and glossary checks only; no independent professional native-speaker review
> - Pending sync: synchronized in public-files.json and mkdocs.yml
> - Status: complete translation
> - Authority: the Chinese SSOT is authoritative; this translation does not constitute a separate set of definitions (C2)

# Why Did First-Round Simplified Characters Succeed While Second-Round Simplification Was Halted? — "Hash Collisions" and Disambiguation Cost Shifting in Chinese Character Reform

Version: Public Case & Mechanism Exploration Essay v0.1 | Date: 2026-11-10 | Complete English translation of `articles/erjian/为什么一简字成了_二简字却被叫停.md`.

Status: Supported by the [CN-S2 Project & Evidence Starting-Point Card](../../research/cases/CN-S2_evidence_starting_point.md) and [Source Notes & Proposition Testing Receipt](source_notes.md). Serving as a cross-group case study for Proposition Group I ([SP-RFC-001](../../whitepaper/chapter-02.md#sp-rfc-001)) and Proposition Group VI ([SP-RFC-017](../../whitepaper/chapter-07.md#sp-rfc-017)) of *Socio-Protocolics*, this essay examines **how many-to-one glyph merging shifts disambiguation costs** and **how legacy ecosystem lock-in constrains protocol migration**. **Throughout this text, official administrative facts, conditional structural derivations, and engineering analogies are strictly distinguished; unverified recognition-rate percentages are excluded, and the withdrawal of a specific draft scheme is not extrapolated into a blanket failure of character simplification.**

---

Twentieth-century China witnessed two major waves of script simplification that followed strikingly different historical trajectories:

- **First-Round Simplification (commonly called *Yijianzi*, 一简字)**: Promulgated by the State Council in the 1956 *Chinese Character Simplification Scheme* (*Hanzi Jianhua Fang'an*), phased in across primary school textbooks and the *Xinhua Dictionary*, and consolidated into the 1964 *General Table of Simplified Characters* (*Jianhuazi Zongbiao*), it stabilized into the foundational standard written daily by over a billion people today.
- **Second-Round Simplification (commonly called *Erjianzi*, 二简字)**: On December 20, 1977, major national newspapers including the *People's Daily* and *Guangming Daily* published the *Second Chinese Character Simplification Scheme (Draft)* (*Di-er Ci Hanzi Jianhua Fang'an (Cao'an)*), whose "Table 1" (248 characters) was immediately put into trial use in newspapers, books, and textbooks. Yet within a few months—in April and July 1978—the Ministry of Education and the Central Propaganda Department issued notices halting its trial use in textbooks and publications. On June 24, 1986, the State Council formally issued the *Circular Approving and Forwarding the Submission of the State Language Commission on Abolishing the "Second Chinese Character Simplification Scheme (Draft)" and Correcting Social Character-Use Confusion* (**Guofa [1986] No. 64**), officially repealing the draft.[[1]](source_notes.md#historical-sources)

This contrast poses a compelling puzzle for anyone studying language standards, information encoding, and institutional evolution:

**If "fewer strokes = lower writing effort = higher communication efficiency" were a linear law that could be extrapolated indefinitely, why did First-Round Simplification become national infrastructure, whereas Second-Round Simplification—pushing stroke reduction even further—triggered an emergency brake within months and was ultimately repealed?**

If we examine this history through two core systems-engineering concepts from *Socio-Protocolics*—**disambiguation cost shifting under many-to-one mappings, analogized to "Hash Collisions" ([SP-RFC-001](../../whitepaper/chapter-02.md#sp-rfc-001))**, and **legacy ecosystem migration cost accounting ([SP-RFC-017](../../whitepaper/chapter-07.md#sp-rfc-017))**—a fundamental principle emerges: making symbols shorter is never automatically equivalent to making total system communication cheaper.

---

## 1. Saving the Writer's Hand While Taxing the Reader's Brain? Separate "Stroke Reduction" from "Many-to-One Collision"

Before evaluating any script reform, we must untangle a common accounting confusion: **"making a character simpler to write" and "merging several distinct characters into a single glyph" are two fundamentally different operations in information engineering.**

We can classify character modifications into three distinct structural operations:

| Operation Type | Formal Mapping Relation | Impact on Task Distinguishing Capacity |
| :--- | :--- | :--- |
| **① Allograph Consolidation or Pure Visual Simplification** | $f(A_1) = f(A_2) = A'$, where $A'$ does not collide with any other object $B$ that the task must distinguish | **Distinction Preserved**: The writer draws fewer strokes; once the reader learns the new shape $A'$, no semantic boundary is lost. |
| **② High Visual Similarity Across Distinct Objects** | $f(A) = A', f(B) = B'$, where $A' \neq B'$ but their visual features become closely confusable | **Reduced Visual Signal-to-Noise Ratio**: Formal code distinction remains, but misrecognition risk rises under rapid scanning, low-resolution print, or cursive handwriting. |
| **③ Cross-Object Many-to-One Merging (Homophone / Homograph Merger)** | The task requires distinguishing $A \neq B$, but the rewrite maps $f(A) = f(B) = X$ | **Many-to-One Collision**: Given the output symbol $X$ alone, it is impossible to uniquely invert whether the source was $A$ or $B$ without external clues. |

Type ③—merging characters that originally carried distinct semantic roles into a single output glyph $X$—has an intuitive analogy in computer science: a **"Hash Collision."**

> **Boundary of the Engineering Analogy**: We use "Hash Collision" as a heuristic to visualize **how disambiguation costs shift under a many-to-one mapping ($f(A)=f(B)=X$)**. **This does not claim that human reading is mathematically isomorphic to a cryptographic hash function, nor that revising a character table is identical to resizing hash buckets.**[[2]](source_notes.md#competing-explanations)

In a hash table, when two distinct keys (`Key_A` and `Key_B`) map to the same bucket `X`, inspecting bucket `X` alone no longer tells the system which key was inserted. The system must traverse a linked list, compare full key strings, or probe extra slots—incurring a **Collision Resolution Cost**.

The same structural trade-off governs human reading and writing ([SP-RFC-001](../../whitepaper/chapter-02.md#sp-rfc-001)):

- **At the Sender (the Writer)**: Replacing a 15-stroke character with a 4-stroke homophone saves a couple of seconds of physical handwriting effort;
- **At the Receiver (the Reader)**: When multiple distinct common characters are collapsed into the same simplified glyph $X$, the distinguishing information saved by the writer's hand does not vanish—**it is transferred onto the reader's cognitive decoding budget**. The reader is forced to recruit surrounding word compounds, sentence syntax, or domain knowledge to perform real-time "collision resolution" in working memory.

Large-scale psycholinguistic experiments on ordinary simplified and traditional characters confirm that "fewer strokes to write" cannot be equated linearly with "faster or easier to recognize." For example, a lexical-decision megastudy by Tsang et al. (2023/2024) published in the *Quarterly Journal of Experimental Psychology* found a nuanced trade-off even within today's well-established simplified and traditional scripts: while simplified characters reduce stroke complexity and yielded higher lexical-decision accuracy in their sample, their reduced visual distinctiveness was associated with slightly slower reaction times under certain conditions.[[3]](source_notes.md#historical-sources) Although Tsang et al. studied standard simplified characters rather than the 1977 draft, their findings establish a crucial empirical boundary: **reducing physical strokes does not automatically guarantee a monotonic reduction in visual recognition and semantic decoding cost.**

---

## 2. Why Context Saves Full Sentences, But Fails in Short Fields, Personal Names, and Archives

At this point, readers familiar with Chinese script history will immediately raise a sharp counter-observation (which serves as our primary **same-domain counter-evidence**):

> **"Wait a minute! Didn't the 1956 First-Round Simplification (*Yijianzi*) ALSO merge multiple traditional characters into single simplified forms—such as `后 (后/後)`, `发 (發/髮)`, `干 (干/乾/幹)`, and `历 (歷/曆)`? If First-Round Simplification also had many-to-one collisions, why didn't it collapse, whereas Second-Round Simplification was halted?"**

This question goes to the heart of the mechanism.

First, we must state plainly: **the 1956 First-Round Simplification was never a "zero-collision, 100% lossless, automatically reversible" code.** In fact, **Unicode Standard Annex #38 (`UAX #38 §3.7.1`, Revision 41)** explicitly documents the well-known "One-to-Many" mapping problem when converting simplified Chinese back to traditional Chinese, noting that automated systems cannot uniquely recover the original character without contextual analysis.[[4]](source_notes.md#historical-sources)

Why, then, do merges like `发 (發/髮)` and `后 (后/後)` rarely cause confusion in everyday prose?

Immediately preceding that discussion, `UAX #38 §3.4` highlights a vital linguistic fact: **natural reading does not parse isolated characters one by one in a vacuum; it processes compound words and connected sentences.**

In full sentences, modern Chinese carries rich **Contextual Redundancy**:

- When you read *"理发店"* (barbershop, `髮` = hair) versus *"出发点"* (starting point, `發` = depart), the paired morphemes *"理"* and *"出"* lock down the semantic slot so tightly that your brain resolves the collision on *"发"* effortlessly;
- When you read *"皇后"* (empress, `后`) versus *"前后"* (front and back, `後`), the disyllabic word compound acts as a built-in parity check.

**However, the moment we step outside full sentences and fixed disyllabic words into "Restricted-Context Tasks," the hidden cost of many-to-one collisions erupts.**

Compare how the same many-to-one mapping ($f(A)=f(B)=X$) behaves across three tiers of contextual redundancy:

| Communication & Recording Scenario | Contextual Redundancy | Disambiguation Behavior Under $f(A)=f(B)=X$ | Who Bears the Added Cost? |
| :--- | :---: | :--- | :--- |
| **① Full Prose & Fixed Disyllabic Words**<br>(e.g., newspaper articles, everyday dialogue) | **High**<br>(surrounding syntax & word pairs constrain meaning) | As long as two merged characters do not collide in the same part of speech and semantic slot, readers resolve ambiguity via context | Absorbed by the reader's real-time context integration (low marginal cost in fixed compounds) |
| **② Restricted-Context Short Fields**<br>(e.g., personal names, place names, single-character abbreviations, catalog indexes, table headers) | **Near Zero**<br>(only 1–3 characters; no sentence syntax) | **Contextual Disambiguation Fails**: Given the merged glyph $X$ alone, the reader cannot tell whether the source value is $A$ or $B$ | Requires parenthetical notes, verbal clarification (*"which character is your surname?"*), extra database fields, or manual verification |
| **③ Cross-Generational Archives & Single-Record Inversion**<br>(e.g., household register migration, genealogies, historical indexes) | **Broken Across Time**<br>(later generations face static records without the writer present) | **Single Record Is Non-Invertible**: Even knowing the full conversion table only yields a candidate set $\{A, B\}$ for a record written as $X$ | Archival custodians, descendants, dictionary compilers, and individuals bearing misidentification risks |

### Conditional Structural Illustration: When Many-to-One Merging Hits "Surname Short Fields"

Why are personal names the ultimate stress test for character-encoding collisions? Because a Chinese personal name typically consists of just two or three characters, **with no grammatical or syntactic constraints linking the surname to the given name—meaning contextual redundancy is effectively zero.**

Let us walk through a strictly bounded **conditional structural derivation** (per the [CN-S2 Evidence Card](../../research/cases/CN-S2_evidence_starting_point.md), this illustrates conditional structural logic and does not assert nationwide census statistics):

- **Conditional Premise**: Suppose a registration or migration practice records two surnames $A$ and $B$ that the task originally needed to distinguish (such as the conditional illustration of **"戴 / 代" [Dai]**, **"傅 / 付" [Fu]**, or **"萧 / 肖" [Xiao]**) uniformly as a single simpler glyph $X$, and **no "original character field" or migration log is preserved** in the ledger;
- **Necessary Structural Consequence**: Decades later, when an archivist or descendant inspects that single entry written as $X$, **even if they have memorized every rule of the simplification table, they can only deduce that the record originally belonged to candidate set $\{A, B\}$—they can never uniquely recover the ground truth of that standalone record from $X$ alone!**
- **Under What Condition Is Recovery Possible?** Only when the system pays an external preservation cost—such as locating pre-migration household registers, tomb epitaphs, lineage genealogies, or collateral family records.

> **Strict Evidentiary Guardrail**: This conditional derivation demonstrates why context-free short fields lose single-record reversibility under many-to-one mappings. It **does not** claim that all modern bearers of the surnames *Dai (代)*, *Fu (付)*, or *Xiao (肖)* trace their spelling to the 1977 draft (folk variants, dialectal homophone substitutions, and clerical transcription habits predate 1977), nor does it claim that lineage recovery is impossible when corroborating archives exist.[[5]](source_notes.md#historical-sources) (For a concrete catalog of which characters were merged into which target glyphs in Table 1 and Table 2 of the 1977 draft, see the **[Appendix: Three-Category Mapping Catalog of Second-Round Simplified Characters](#erjian-mapping-appendix)** at the end of this essay.)

### Separating Two Layers of Cross-Generational Traceability: Record Reversibility vs. Historical Text Learnability

When accounting for the long-term intertemporal costs of script reform, we must also keep two distinct questions separate (see [CN-S2 Evidence Table](../../research/cases/CN-S2_evidence_starting_point.md)):

1. **Single-Record Reversibility**: Whether a specific migrated entry can be uniquely inverted to its original character (which depends on whether the mapping was many-to-one and whether original fields/logs were kept);
2. **Historical Text Learnability**: How much training, dictionary compilation, and translation investment a society needs so that readers educated in the new script can access historical primary sources.

For instance, the Korean National Institute of Korean History's translation and digitization of the Classical Chinese *Veritable Records of the Joseon Dynasty* (**Source K1**), and the Vietnamese Nôm Preservation Foundation's archival preservation, dictionary compilation, and training programs (**Source V1**), illustrate both the reading barrier faced by general readers after a script transition and the institutional remedies (translation, dictionaries, specialist training) societies deploy to bridge that gap.[[6]](source_notes.md#historical-sources) *Socio-Protocolics* avoids sensationalist claims that a country has fallen into an irreversible "historical amnesia trap"; instead, it asks an accounting question: **when a foundational encoding protocol undergoes an incompatible transition, who pays the ongoing bill for cross-generational translation, dictionary maintenance, and archival preservation?**

---

## 3. Why 1956 Stabilized While 1977 Hit the "System Migration Wall"

With the mechanics of many-to-one collision and contextual boundaries in place, let us return to the historical divergence: why did the 1956 First-Round Simplification cross the adoption threshold and stabilize, whereas the December 1977 Second-Round Draft stalled within months and was formally repealed in 1986?

Reading the full text of **State Council Circular `Guofa [1986] No. 64` (June 24, 1986)** and the attached **Submission of the State Language Commission (May 25, 1986)** (**Source S1**), we can compare the 1956 and 1977 reforms across three systems-engineering dimensions:

### 1. Diminishing Marginal Returns of Compression vs. Rising Collision Density

The 1956 *Chinese Character Simplification Scheme* did not invent a character set out of thin air; to a large extent, it codified vulgar variants (*sutizi*) and cursive-derived forms that had circulated organically in popular writing since the Yuan, Ming, and Qing dynasties. By completing the first round, reformers had already harvested the "low-hanging fruit"—simplifications that cut stroke counts substantially, enjoyed centuries of folk familiarity, and rarely collided within high-frequency core vocabulary.

By 1977, when the *Second Chinese Character Simplification Scheme (Draft)* attempted to **compress already-simplified characters even further—aiming to cap common characters under ten strokes**, the remaining design space was severely constricted. Pushing further required aggressive **homophone merging (many-to-one substitution)** and stripping away distinguishing visual radicals. Section II of the draft's *Explanatory Notes* even explicitly touted that **"in terms of reducing the total number of Chinese characters, the draft eliminated 263 characters"** (by merging two or more homophones into one glyph).[[7]](source_notes.md#historical-sources) Consequently, the marginal writing time saved by shaving off two or three more strokes was tiny, whereas visual unfamiliarity and homograph collision friction in headlines, short fields, and everyday reading spiked sharply.

Even more telling institutional corroboration arrived in 1986: when the State Council repealed the Second-Round Draft via `Guofa [1986] No. 64` and the State Language Commission re-published the 1964 *General Table of Simplified Characters* in October 1986, policymakers did not merely halt the 1977 draft—they also executed **five famous "Collision Rollbacks"** on the 1964 First-Round Table itself! Specifically, the 1986 announcement declared that **“叠 (dié, pile up), 覆 (fù, overturn/cover), 像 (xiàng, portrait/resemble), and 囉 (luo, particle)” would no longer be treated as traditional variants of “迭, 复, 象, 罗,” and that “瞭” when pronounced `liào` (瞭望, look out) would no longer be simplified into “了”** (see [Appendix Table C](#erjian-mapping-appendix)).[[7]](source_notes.md#historical-sources) This demonstrates that even inside the First-Round Simplification, cross-domain many-to-one merges that generated excessive disambiguation friction in practice eventually triggered a system-level rollback.

### 2. Legacy Ecosystem Lock-In and the "Fixed-Mask ROM Chip" Migration Bill (SP-RFC-017)

When evaluating a foundational protocol upgrade, an architect cannot only calculate whether the new syntax is shorter; one must calculate **the total cost of recompiling the entire society's installed base** (Whitepaper Group VI, **[SP-RFC-017 Technical Debt Accounting & Refactoring Migration Cost](../../whitepaper/chapter-07.md#sp-rfc-017)**).

- **In 1956 (Cold Start & Expansion Phase)**: Nationwide mass literacy campaigns, unified national school textbooks, modern dictionary compilation, and lead-type printing standards were in the midst of initial construction—equivalent to adopting a new encoding standard during system cold-start;
- **By 1977–1986 (Installed-Base Lock-In Phase)**: Hundreds of millions of literate citizens, national textbook series, library catalogs, and reference works were already standardized and running on the 1956/1964 simplified character baseline.

Even more strikingly, in **Part 1 of the State Language Commission's May 25, 1986 submission to the State Council (Source S1)**, policymakers recorded a technological constraint that captures the dawn of the information age: alongside noting that the 1977 draft was immature and social character standards needed stability, the submission explicitly pointed out that adding a new batch of simplified characters would impose a heavy conversion burden on **existing dictionaries, reference books, and already-manufactured computer character libraries—specifically citing "fixed-mask chips" (`固定掩膜体芯片`)!**[[1]](source_notes.md#historical-sources)

> **Calibrating Evidentiary Identity**: Under our archival rules, the mention of "fixed-mask chips and reference book conversion burdens" is registered precisely as **an actor's stated decision rationale inside the State Language Commission submission approved by the State Council**. We do not exaggerate it into the sole cause of repeal, nor claim a verified dollar figure for nationwide chip replacement. Yet it vividly illustrates the structural logic of `SP-RFC-017`: **once a character protocol is etched into hundreds of millions of textbooks, dictionaries, and early hardware ROM chips, the ecosystem-wide migration cost of mutating the base character set dwarfs the local savings of writing a few fewer strokes by hand.**

### 3. The Eight-Year "Protocol Split-Brain" of Halted Trial Without Formal Repeal (1978–1986)

The official document chain (`S1`) also highlights an instructive institutional phase between 1978 and 1986:

- **December 20, 1977**: The draft is published and Table 1 enters trial use in publications;
- **April and July 1978**: Relevant ministries issue notices halting trial use in textbooks, newspapers, and books;
- **1978 to June 1986**: For eight years, the Second-Round Simplification remained in a suspended twilight zone—**halted in official textbooks and major press, yet not formally repealed by the State Council!**

In distributed-systems terms, those eight years produced a classic **Protocol Split-Brain** ([SP-RFC-012](../../whitepaper/chapter-05.md#sp-rfc-012) / [SP-RFC-014](../../whitepaper/chapter-05.md#sp-rfc-014)): school textbooks and national newspapers reverted to the 1964 *General Table*, while street signs, mimeographed factory notices, personal letters, and local ledgers continued using—or spontaneously inventing—second-round simplified forms. It was precisely to end this dual-track confusion that the State Language Commission and the State Council issued `Guofa [1986] No. 64` in June 1986, formally abolishing the 1977 draft and re-publishing the 1964 *General Table of Simplified Characters* as the canonical standard.

---

## 4. 🛠️ Takeaway Tool: A 4-Step Checklist for Information Compression & Schema Refactoring

The rise and repeal of the Second-Round Simplification Draft is far more than a chapter of linguistic history.

Today, whether you are a software architect designing microservice APIs or database enums, a manager creating internal corporate abbreviations, or a policymaker streamlining administrative forms, whenever you propose to **"compress a fine-grained encoding scheme into fewer symbols,"** the lessons of `CN-S2` distill into a practical **4-Step Protocol Compression Checklist**:

| Step | Concrete Question You Must Answer Beforehand | Lesson from the Chinese Character Simplification Case |
| :--- | :--- | :--- |
| **1. Separate Mapping Types: Lossless Slimming vs. Many-to-One Collision?** | Does your simplification merely trim redundant strokes/fields, or does it merge distinct semantic states $A$ and $B$ into the same symbol $X$ ($f(A)=f(B)=X$)? | Reducing strokes within a single character lowers writing effort; merging distinct common characters into one glyph creates a many-to-one "hash collision." |
| **2. Stress-Test Zero-Context Short Fields: Will It Fail Outside Long Sentences?** | Never test new abbreviations only inside context-rich paragraphs! If symbol $X$ appears alone in a **2-character personal name, table header, alert code, or catalog index**, can the receiver still uniquely identify it? | Character merges that are easily disambiguated inside full sentences (`UAX #38 §3.4`) lose their disambiguating context inside short fields like personal names and indexes. |
| **3. Trace Cost Shifting: Who Pays for the 2 Seconds Saved by the Sender?** | Did saving the writer 2 seconds force readers, reviewers, or archivists to spend 10x longer guessing, asking, or cross-checking? Did the database preserve an `original_value` field? | Without preserving an original-character field or migration log, a single merged record cannot be uniquely inverted later—leaving only a candidate set $\{A, B\}$. |
| **4. Audit Installed-Base Migration Cost: Does Marginal Gain Beat Ecosystem Recompilation?** | Once the existing standard is embedded in user habits, dictionaries, and hardware firmware, is the Net Present Value ([SP-RFC-017](../../whitepaper/chapter-07.md#sp-rfc-017)) of mutating the base code positive or negative? | The 1986 State Language Commission submission explicitly cited the heavy burden of converting existing reference books and fixed-mask character ROM chips. |

---

## 5. Open Research Invitation: What Is Verified vs. What Awaits Your Contribution

In strict adherence to *Socio-Protocolics*' commitment to **"speaking only in proportion to the evidence,"** this essay does not package the repeal of Second-Round Simplification as a "mathematical proof of a single formula." Instead, we lay both our **verified evidentiary baseline** and our **open empirical gaps** on the table:

1. **Verified Evidentiary Baseline**:
   - The administrative timeline and stated decision rationales in **Source S1** (`Jingzhengfa [1986] No. 107` forwarding State Council `Guofa [1986] No. 64` and the State Language Commission's May 25, 1986 submission: December 1977 draft publication and trial use, April/July 1978 halts in textbooks and press, June 1986 formal repeal, and the explicit mention of scheme immaturity, norm stability, and dictionary / fixed-mask chip conversion burdens);
   - Technical standards on one-to-many simplified-traditional mappings and word-level contextual disambiguation in **Unicode `UAX #38 §3.7.1 & §3.4`**;
   - Empirical psycholinguistic boundaries on speed-accuracy trade-offs in standard simplified vs. traditional word recognition (**Tsang et al., 2023/2024, `R1`**).
2. **Unverified Claims Explicitly Excluded (Not Used as Evidence Here)**:
   - Unverified or conceptually conflated claims circulating in secondary drafts—such as *"Second-Round recognition rates dropped from 83.5%/91.3% to 46.4%/66.9%,"* *"3,500 characters generating 56,008 words proves a 16x morpheme loss amplification,"* or *"merging two characters always loses exactly 1 bit that can never be recovered"*—have been audited and excluded item by item in the [CN-S2 Evidence Starting-Point Card](../../research/cases/CN-S2_evidence_starting_point.md).
3. **Open Research Tasks You Can Claim**:
   - **Primary Archival Scans**: Contribute high-resolution scans of the original December 20, 1977 newspaper publication of the *Second Chinese Character Simplification Scheme (Draft)* and the original texts of the April and July 1978 ministry notices halting trial use;
   - **Restricted-Context Disambiguation Measurement**: Building on [H01 — Expression & Understanding Cost](../../research/H01_expression_and_understanding_cost.md) and the [CN-S2 Evidence Card](../../research/cases/CN-S2_evidence_starting_point.md), construct a per-character mapping table for Table 1 of the 1977 draft and test recognition accuracy and error detection across four context tiers (isolated character, disyllabic word, full sentence, and short personal-name field).
   - If you have access to these archival originals or experimental datasets, we warmly invite you to open an Issue or Pull Request via our [Open Evidence & Material Wishlist](../../research/OPEN_EVIDENCE_WISHLIST.md)!

---

<a id="erjian-mapping-appendix"></a>

## Appendix: What Did Second-Round Simplified Characters Actually Look Like? — A Three-Category Mapping Catalog from Source to Target

Many readers who did not live through the 1977–1978 newspaper trials naturally wonder: **What were the concrete characters in the Second-Round Simplification Draft, and what did they map from and to?**

Published by the Script Reform Committee of China on December 20, 1977, the *Second Chinese Character Simplification Scheme (Draft)* contained a total of 853 simplified characters and 61 simplified components, eliminating 263 characters from the character inventory via homophone mergers. The draft was divided into two distinct tables: **Table 1** (248 characters in total: 172 standalone simplified characters, 21 simplified characters usable as components, and 55 derived characters, **put into immediate trial use in newspapers and books in December 1977**) and **Table 2** (605 characters in total: 269 simplified characters, 16 non-standalone simplified components, and 336 derived characters, **published for public discussion**).[[7]](source_notes.md#historical-sources)

To make the systems-engineering taxonomy from Section 1 concrete, we compile representative examples below from the full public transcription of the 1977 draft and the 1986 re-publication note of the *General Table of Simplified Characters*, organized into **Table A: Cross-Semantic Many-to-One Homophone Merges ($f(A)=f(B)=X$)**, **Table B: Newly Coined Outlines & Component Replacements ($f(A)=A'$)**, and **Table C: Official 1986 Collision Rollbacks** (strictly distinguishing **Table 1 [tried out in 1977]** from **Table 2 [discussion draft]**, with structural descriptions provided for rare Unicode Plane 2/3 characters):

### Table A: Representative Cross-Semantic Many-to-One Homophone Merges ($f(A)=f(B)=X$, the "Hash Collision" Zone)

Rather than creating a new glyph shape, these entries took **an existing high-frequency character $X$ that already possessed its own distinct core meaning (and sometimes a different pronunciation)** and used it to absorb one or more higher-stroke homophones $A, B$—saving strokes for the writer while erasing the semantic boundary between distinct lexemes:

| Original Standard Character ($A / B$) | Target Character ($X$) | Pre-Existing Core Meaning / Pronunciation of $X$ | Exact 1977 Draft Location | Collision Pattern & Restricted-Context (Short Field / Header / Name) Disambiguation Pressure |
| :--- | :---: | :--- | :--- | :--- |
| **副** (*fù*, deputy / vice / auxiliary) | **付** | To pay / hand over; surname *Fu* (`fù`) | **Table 1** (1) Trial | *"副总理 (Vice Premier), 副局长 (Deputy Director), 副食品 (non-staple food)"* became **"付总理, 付局长, 付食品"**; collides directly with *"pay / surname Fu"* in short titles and headers. |
| **蛋** (*dàn*, egg) | **旦** | Dawn / day (*元旦* New Year's Day, *一旦* once); opera role | **Table 1** (1) Trial | *"鸡蛋 (chicken egg), 蛋白质 (protein), 脸蛋 (cheek)"* became **"鸡旦, 旦白质, 脸旦"**; forces *"旦"* to carry two unrelated high-frequency semantic domains (dawn/date vs. egg). |
| **停** (*tíng*, stop / halt) | **仃** | Lonely (*伶仃*, original note: still read `dīng`) | **Table 1** (1) Trial | *"停车 (park/stop a car), 停产 (halt production), 停电 (power outage)"* became **"仃车, 仃产, 仃电"**; both a cross-meaning merge and an artificial polyphone (`tíng / dīng`). |
| **舞** (*wǔ*, dance / inspire) | **午** | Noon / midday (*中午, 午休*) | **Table 1** (1) Trial | *"跳舞 (dance), 歌舞 (song and dance), 鼓舞 (inspire)"* became **"跳午, 歌午, 鼓午"**; outside fixed compounds, creates immediate visual ambiguity with time expressions. |
| **龄** (*líng*, age / years) | **令** | Order / command / season / magistrate | **Table 1** (1) Trial | *"年龄 (age), 工龄 (years of service), 学龄 (school age)"* became **"年令, 工令, 学令"**; *"工令"* (years of work vs. work order) and *"军令"* (years of military service vs. military order) collide head-on. |
| **帮** (*bāng*, help / group / shoe upper) | **邦** | Nation / state / friendly country (*友邦*) | **Table 1** (1) Trial | *"帮忙 (help), 互帮互助 (mutual aid)"* became **"邦忙, 互邦互助"**; blurs *"邻邦 (neighboring country)"* and *"邻帮 (neighboring group/helpers)."* |
| **盒** (*hé*, box / case) | **合** | Close / combine / total | **Table 1** (1) Trial | *"饭盒 (lunchbox), 纸盒 (cardboard box), 一盒火柴 (a box of matches)"* became **"饭合, 纸合, 一合火柴."** |
| **舱** (*cāng*, cabin / hold) | **仓** | Granary / warehouse (*仓库*) | **Table 1** (1) Trial | *"船舱 (ship cabin), 机舱 (aircraft cabin)"* became **"船仓, 机仓"**; erases the written distinction between a land warehouse (*货仓*) and a vessel hold (*货舱*) on shipping manifests. |
| **蓝, 篮** (*lán*, blue; basket) | **兰** | Orchid (*兰花*); surname *Lan* | **Table 1** (1) Trial | **3-into-1 merge** ($f(\text{兰})=f(\text{蓝})=f(\text{篮})=\text{兰}$): *"兰花 (orchid), 蓝天 (blue sky), 竹篮 (bamboo basket), 篮球 (basketball)"* all written as **"兰花, 兰天, 竹兰, 兰球."** |
| **叮, 盯, 钉, 靪** (*dīng/dǐng/dìng*, sting/urge; stare; nail; patch) | **丁** | 4th Heavenly Stem / adult male / cubes; surname *Ding* | **Table 1** (1) Trial | **5-into-1 merge**: *"叮嘱 (urge), 紧盯 (stare closely), 铁钉 (iron nail), 补靪 (patch)"* all collapsed into **"丁"** (*"盯住钉子 [stare at the nail]"* becomes **"丁住丁子"**). |
| **芭, 笆, 粑** (*bā*, plantain; fence; rice cake) | **巴** | Hope / cling / tail; surname *Ba* | **Table 1** (1) Trial | **4-into-1 merge**: *"芭蕉 (plantain), 篱笆 (fence), 糍粑 (glutinous rice cake)"* all written with **"巴."** |
| **葫, 猢, 蝴, 糊** (*hú*, gourd; monkey; butterfly; paste/blurry) | **胡** | Beard / reckless / lane (*胡同*); surname *Hu* | **Table 1** (1) Trial | **5-into-1 merge**: *"葫芦 (gourd), 猢狲 (macaque), 蝴蝶 (butterfly), 糊涂 (muddled)"* all written with **"胡."** |
| **歉** (*qiàn*, apologize / crop failure) | **欠** | Owe / lack / yawn | **Table 1** (1) Trial | *"道歉 (apologize), 抱歉 (sorry), 歉收 (poor harvest)"* became **"道欠, 抱欠, 欠收."** |
| **熄** (*xī*, extinguish) | **息** | Breath / rest / interest / news | **Table 1** (1) Trial | *"熄灭 (extinguish), 熄火 (stall/turn off fire), 熄灯 (lights out)"* became **"息灭, 息火, 息灯."** |
| **圆** (*yuán*, round / circle) | **元** | Primary / first / currency unit | **Table 1** (1) Trial | *"圆形 (circular), 团圆 (reunion), 圆满 (satisfactory)"* became **"元形, 团元, 元满."** |
| **账** (*zhàng*, account / ledger / debt) | **帐** | Mosquito net / tent / canopy | **Table 1** (1) Trial | *"账本 (account book), 算账 (settle accounts)"* merged into **"帐本, 算帐."** |
| **座** (*zuò*, seat / pedestal / classifier) | **坐** | Sit / travel by (verb) | **Table 1** (1) Trial | Noun/classifier *"座位 (seat), 一座山 (a mountain)"* merged into verb **"坐位, 一坐山."** |
| **泰** (*tài*, peace / Mount Tai) | **太** | Too / extreme / highest (*太阳, 太极*) | **Table 1** (1) Trial | *"泰山 (Mount Tai), 国泰民安"* became **"太山, 国太民安."** |
| **煽, 搧** (*shān*, incite; fan) | **扇** | Fan / door leaf | **Table 1** (1) Trial | *"煽动 (incite), 煽风点火"* became **"扇动, 扇风点火."** |
| **预, 豫** (*yù*, prepare/advance; hesitate / Henan abbr.) | **予** | Give / bestow (`yǔ`); literary 1st-person pronoun (`yú`) | **Table 1** (1) Trial | *"预备 (prepare), 预算 (budget), 犹豫 (hesitate), 豫 (Henan province abbreviation)"* all became **"予"**; in single-character province abbreviations, *"豫"* collapses into *"予."* |
| **萧** (*xiāo*, desolate; surname *Xiao*) | **肖** | Resemble (*肖像*); surname *Xiao* (`xiào/xiāo`) | **Table 1** (1) Trial | Merges the common surname and literary word **"萧"** into **"肖"**; loses single-record invertibility in 2–3 character personal-name fields. |
| **嘴 / 遇 / 橘 / 韭** (*zuǐ / yù / jú / jiǔ*) | **咀 / 迂 / 桔 / 艽** | Chew (`jǔ`) / circuitous (`yū`) / Platycodon (`jié`) / Gentiana (`jiāo`) | **Table 1** (1) Trial | Explicit footnotes in the draft kept the old readings (`jǔ, yū, jié, jiāo`) for the original words while adding the new meanings/readings—**artificially creating cross-sound, cross-meaning homographs** (*"嘴巴 [mouth]"* written **"咀巴"**, *"遭遇 [encounter]"* written **"遭迂"**). |
| **戴** (*dài*, wear/respect; surname *Dai*) | **代** | Replace / era / generation; surname *Dai* | **Table 2**·1 Homophone | Proposed merging *"穿戴 (wear), 拥戴 (support)"* and the major surname **"戴"** into **"代"** (Table 2 discussion draft). |
| **傅** (*fù*, tutor/master; surname *Fu*) | **付** | Pay; surname *Fu* (already merged with *副* in Table 1) | **Table 2**·1 Homophone | Following Table 1's `副 → 付`, Table 2 proposed `傅 → 付` (*"师傅"* written **"师付"**), collapsing **付, 副, 傅** into one character. |
| **赣** (*gàn*, Jiangxi province abbr. / Gan River) | **干** | Shield / dry / cadre (already 3-in-1 from 1956) | **Table 2**·1 Homophone | Proposed merging **"赣"** (single-character abbreviation for Jiangxi Province) into **"干"** (which already carried *干/乾/幹* from the First Round). |
| **辩, 辨, 辫** (*biàn*, debate; distinguish; braid) | **弁** | Ancient cap (*皮弁*) / low-ranking officer | **Table 2**·1 Homophone | Collapsed three core characters that rely on their middle radical for disambiguation—*debate (言), distinguish (刀/点), hair braid (纟)*—into the archaic character **"弁."** |
| **鞭 / 陡 / 镰 / 胸 / 颜** | **卞 / 斗 / 连 / 匈 / 彦** | Surname *Bian* / peck or fight / connect / Xiongnu / accomplished | **Table 2**·1 Homophone | Examples: *"皮鞭 (whip) → 皮卞", "陡峭 (steep) → 斗峭", "镰刀 (sickle) → 连刀", "胸怀 (bosom) → 匈怀", "颜色 (color) → 彦色."* |

### Table B: Newly Coined Outlines, Component Replacements & Radical Derivations ($f(A)=A'$, Structural Rewrite & Font-Library Migration Zone)

Instead of borrowing an existing high-frequency word like *"付, 旦, 午, 兰"* for homophone absorption, these entries reduced strokes by **slicing out partial outlines, swapping phonetic/semantic components, regularizing cursive shapes, or coining new associative compounds**. In information-theoretic terms, they are mostly 1-to-1 rewrites (or family derivations) rather than cross-lexeme homophone collisions, yet they **disrupted familiar radical systems and required re-manufacturing print matrices, dictionaries, and early fixed-mask character ROM chips across the entire society** (`SP-RFC-017`):

| Original Standard Character | 1977 Draft Simplified Form (with Component Structure) | Simplification Method & 1977 Table Location | Impact on Reading & Installed-Base Font Ecosystems |
| :--- | :--- | :--- | :--- |
| **餐** (*cān*, meal) | **歺** (top-left component, homographic with archaic *歹/歺 [è]*) | **Table 1** (1) Trial | Cut from 16 strokes to 4 (*"餐厅 [restaurant]"* written **"歺厅"**), stripping away the semantic *"食 (food)"* radical. |
| **街** (*jiē*, street) | **亍** (right-hand component, homographic with *彳亍 [chù]*) | **Table 1** (1) Trial | Cut from 12 strokes to 3 (*"街道 [street]"* written **"亍道"**); visually confusable with *"于, 亏, 丁"* (Type ② visual similarity). |
| **信** (*xìn*, letter / trust) | **伩** (left *"亻"*, right *"文"*) | **Table 1** (1) Trial | Replaced *"言 (speech)"* with 4-stroke *"文"*, breaking the classical associative structure *"person + speech = trust."* |
| **雪** (*xuě*, snow) | **𫜹** (top *"〾"* [rain radical reduced to two dots + hook], bottom *"彐"*) | **Table 1** (1) Trial | Removed the recognizable *"雨 (rain)"* radical at the top, obscuring the meteorological semantic cue. |
| **酒** (*jiǔ*, wine / alcohol) | **氿** (left *"氵"*, right *"九"*) | **Table 1** (1) Trial | Replaced *"酉"* with 2-stroke phonetic *"九"* (colliding with the Jiangsu place-name character *"氿 [guǐ]"*). |
| **算** (*suàn*, calculate) | **祘** (two *"示"* side by side) | **Table 1** (1) Trial | Dropped the bamboo top and revived archaic *"祘"*; Table 2 further proposed merging *"蒜 (garlic)"* into *"祘."* |
| **病** (*bìng*, illness) | **疒** (the sickness radical used standalone as a full character) | **Table 1** (1) Trial | Promoted a non-standalone radical into an independent character, easily confused in handwriting with *"广"* and *"厂."* |
| **部** (*bù*, ministry / department / troops) | **𰆊** (the bottom part of *"节"*, i.e., *"卩"*) | **Table 1** (1) Trial | Reduced the ultra-high-frequency character *"部"* (*部队, 干部, 部门*) to a bare 2-stroke seal radical *"卩."* |
| **道 / 建 / 迎** | **辺 / 迠 / 迊** (*"辶"* walking radical with *"刀 / 占 / 卬"*) | **Table 1** (1) Trial | Simultaneously altered high-frequency walking-radical characters, creating widespread visual unfamiliarity across newspaper pages. |
| **宣 → 演** | **㝉 → 𰛑 (⿰氵㝉)** | **Table 1** (1) Trial | Simplified *"宣"* to *"㝉"* and *"演"* to *"⿰氵㝉"*; Table 2 then merged *"渲"* into *"㝉"* as well. |
| **留 (and 榴, 瘤, 溜)** | **畄** (and **𰗶, 𰣲, 𰜈 [⿰氵畄]**) | **Table 1** (2) Simplifiable Component | Replaced the top of *"留"* with the grass radical *"艹"*, triggering a cascade of derived character rewrites. |
| **展, 辗 (and 碾)** | **𰍰 (⿸尸一)** (and **𰦪 [⿰石𰍰]**) | **Table 1** (2) Simplifiable Component | Left only a single horizontal stroke under *"尸"*, making it visually close to *"尺, 尸, 户"* in newsprint. |
| **面 / 感 / 鼻 / 属** | **𫩑 (⿱丆口) / 𫹯 (⿱干心) / 𢍂 (⿱自廾) / 𰍱 (⿸尸专)** | **Table 1** (2) Simplifiable Component | Core high-frequency characters with component derivation (*缅→𰬄, 撼→𰓭, 憾→𰑞, 嘱→𰇰, 瞩→𰥩*); altering them required rebuilding every dictionary and character ROM chip. |
| **矮 / 寡 / 家** | **仦 (⿰亻小) / 𠆣 (⿱一人) / 𡦼 (⿱宀人)** | **Table 2**·6 Associative Compounds | Newly coined associative forms (*"person + small = short [矮]", "one + person = widow/few [寡]", "roof + person = home [家]"*). |

### Table C: Official 1986 "Collision Rollbacks" When Re-Publishing the *General Table of Simplified Characters*

Perhaps the most compelling proof that high-collision many-to-one merges trigger system pushback is what happened in October 1986: when the State Language Commission abolished the 1977 Second-Round Draft and re-published the **1964 *General Table of Simplified Characters* (the First-Round master table)**, it simultaneously executed **five targeted "Collision Rollbacks"** on the 1964 table itself!

In the *Explanatory Note on Re-Publishing the "General Table of Simplified Characters"* (October 10, 1986, published in *Gazette of the State Council of the PRC*, 1986, Issue No. 29), the State Language Commission formally un-merged five many-to-one simplifications from the 1964 edition[[7]](source_notes.md#historical-sources):

| Original 1964 *General Table* Merge Rule | 1986 Re-Publication Rollback Decision | Why Was It Rolled Back? (Eliminating High-Frequency Semantic Collisions) |
| :--- | :--- | :--- |
| Merged **"叠"** (*dié*, pile up / fold / repeat) into **`迭`** | **Deleted `迭〔叠〕`**, restoring **"叠"** as an independent standard character | Eliminated the collision between *"重叠 (overlap), 折叠 (fold), 层峦叠嶂"* and *"更迭 (alternate), 高潮迭起 (repeatedly arise)."* |
| Merged **"覆"** (*fù*, cover / overturn / capsize) into **`复`** | **Deleted `〔覆〕` under `复`**, restoring **"覆"** as an independent standard character | Eliminated the collision between *"覆盖 (cover), 颠覆 (subvert), 全军覆没 (total rout)"* and *"恢复 (recover), 复习 (review), 往复"* (retaining only *答复/批复*). |
| Merged **"像"** (*xiàng*, portrait / statue / resemble) into **`象`** | **Deleted `象〔像〕`**, restoring **"像"** as an independent standard character | Eliminated the collision between *"画像 (portrait), 肖像, 好像 (seem like)"* and *"大象 (elephant), 现象 (phenomenon), 抽象 (abstract)."* |
| Merged **"囉"** (*luō/luo*, chatter / sentence particle) into **`罗`** | **Deleted `〔囉〕` under `罗`** and simplified it by component derivation into **`啰`** | Re-separated the modal particle / chatter word *"啰唆 (long-winded), 喽啰"* from *"罗网 (net), 星罗棋布, surname Luo (罗)."* |
| Simplified **"瞭"** into **`了`** regardless of whether read `liǎo` or `liào` | Kept **`了`** when read `liǎo` (*了解*, understand), but **restored `瞭` when read `liào` (*瞭望*, look out from a height)** | Eliminated the reading and segmentation collision between *"瞭望哨 (observation post)"* written as *"了望哨"* and the ubiquitous aspect particle *"了 (`le/liǎo`)."* |

> **Appendix Takeaway**: Placing Tables A, B, and C side by side makes the protocol boundary of script simplification crystal clear: **simplifications that trim redundant strokes without creating high-frequency semantic collisions (the bulk of the 1956 First Round and 1-to-1 forms) only face a one-time familiarity and font-conversion threshold; whereas attempts to shrink the character inventory via aggressive "many-to-one homophone merges" (Table A) not only caused the 1977 Second-Round Draft to stall within months, but even forced the 1986 standardizers to roll back five over-merged characters (`叠, 覆, 像, 啰, 瞭`) from the 1964 First-Round Table itself (Table C).**

---

<a id="article-framework"></a>

## Endnote: Which Socio-Protocolics Provisions This Essay Uses, and What It Does Not Claim to Prove

This essay belongs to the cross-group intersection of **Proposition Group I (Channel Capacity & Semantic Boundary)** and **Proposition Group VI (Debt Accounting & Evolutionary Selection)** in the [*Socio-Protocolics Whitepaper v11.2*](../../whitepaper/chapter-01.md):

1. **Postulate Background**: Uses **[SP-POSTULATE-1](../../whitepaper/chapter-01.md#sec-1-5)** (finite cognitive bandwidth and physical resource constraints: both sender handwriting effort and receiver visual/contextual decoding effort are non-zero, and character standards are constrained by physical dictionaries and hardware font memory) and **[SP-POSTULATE-2](../../whitepaper/chapter-01.md#sec-1-5)** (strategic agents with heterogeneous utility weights across writers, readers, typesetters, and lexicographers).
2. **Core Proposition Groups & Normative Rules**:
   - Uses Group I **[SP-RFC-001](../../whitepaper/chapter-02.md#sp-rfc-001)** (physical channel capacity vs. social semantic decoding boundary): treats Second-Round Simplification as a **local reverse-test against the over-strong extrapolation that "fewer strokes / shorter symbols automatically lower comprehension cost,"** separating allograph consolidation from cross-object many-to-one mappings ($f(A)=f(B)=X$);
   - Uses Group II cross-group normative rule **[SP-RFC-007](../../whitepaper/chapter-03.md#sp-rfc-007)**: emphasizes that public encoding standards must balance writer compression against receiver intelligibility, short-field disambiguation, and archival traceability;
   - Uses Group IV **[SP-RFC-012](../../whitepaper/chapter-05.md#sp-rfc-012)** and **[SP-RFC-014](../../whitepaper/chapter-05.md#sp-rfc-014)**: examines the authorization boundary and the 1978–1986 dual-track "protocol split-brain" between halting textbook trials and formal State Council repeal;
   - Uses Group VI **[SP-RFC-017](../../whitepaper/chapter-07.md#sp-rfc-017)** (technical debt and refactoring migration cost accounting): connects the 1986 State Language Commission submission's discussion of reference books and fixed-mask character ROM chips to ecosystem-wide migration accounting.
3. **Epistemic Boundaries & Untested Parts**:
   - The demonstration that a many-to-one mapping $f(A)=f(B)=X$ cannot be uniquely inverted without extra information is a **conditional structural derivation**, not a completed laboratory reaction-time measurement on 1977 draft glyphs;
   - "Hash Collision" is explicitly marked as an **engineering analogy** for disambiguation cost shifting under many-to-one mappings, not a claim of strict mathematical isomorphism to cryptographic hash tables;
   - Surname examples (e.g., *Dai* 代/戴) are strictly bounded as **conditional structural illustrations** of restricted-context fields, not a verified nationwide household-register natural experiment.
4. **Companion Documents**: Full source locations, secondary-draft error exclusions, and the formal Proposition Testing Receipt are in [Source Notes](source_notes.md); drafting and audit logs are in [Revision Notes](revision_notes.md); the underlying evidentiary table is in the [CN-S2 Evidence Starting-Point Card](../../research/cases/CN-S2_evidence_starting_point.md).

