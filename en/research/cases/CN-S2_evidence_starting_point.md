> **Translation record**
> - Chinese source: `research/cases/CN-S2_证据起点.md` (sha256 `6e0c7f092593e26c0f4bd538f72fa7f03b9bfc8e9ab27748631f7459a0965a69`, `17677` bytes, 2026-11-09)
> - Chinese version / release tag: `v11.2-r20261106` (theoretical version remains v11.2)
> - Translation version: `en-v0.1`
> - Translation date: 2026-11-09
> - Check status: checked sentence by sentence against the Chinese source for claim status, negative guardrails and numbering; machine and glossary checks only; no independent professional native-speaker review
> - Pending sync: pending registration in public-files.json / mkdocs.yml
> - Status: complete translation
> - Authority: the Chinese SSOT is authoritative; this translation does not constitute a separate set of definitions (C2)

# CN-S2 | The Second-Simplification (二简) Draft: First Separate the Fact of Withdrawal from the Explanation of Cause

Version: material trial v0.4 | Date: 2026-10-23 | Language: Chinese original; English translation pending.

This document is the first evidence table, not a case article or a completed study of failure causes. It is executed per the [case comparison method](../case_selection_and_comparison_method.md); the withdrawal and the decision rationale still rely on a single official forwarding-text chain. This round additionally checks the original-paper abstract of an ordinary traditional–simplified study and a publisher's note on a word list; neither is evidence of Second-Simplification effect and neither adds an independent Second-Simplification case count.

## Source and locating

Source S1: [Beijing Municipal People's Government forwarding notice](https://www.beijing.gov.cn/zhengce/zfwj/zfwj/szfwj/201905/t20190523_71436.html). The page contains the transcription of Jing Zheng Fa [1986] No. 107, Guo Fa [1986] No. 64, and the State Language Commission's request report. The full web page has been read; the first-printing images of each document cited this round have not been obtained, nor have the 1978 two notices' originals been read. The year in the web address does not substitute for the document's drafting date.

## Event and evidence table

| Record | Time and narrow fact | Text locating and evidential identity | What still cannot be inferred |
|---|---|---|---|
| E1 | The request report recalls that the draft was published on 1977-12-20 for comment, and the first table was tried out in publications | First part, opening paragraph of the attached State Language Commission request report; the 1986 official recall, the 1977 original not independently checked | That everyone nationwide, or all fields, had already used it |
| E2 | The same paragraph records that in April and July 1978 relevant departments notified a stop to the trial use in related textbooks and publications | First part, opening paragraph of the request report; the two original notices are to be supplemented, and the specific scope must return to each original | That 1978 had already formally abolished the whole draft |
| E3 | The request report of 1986-05-25 proposed the abolition recommendation | The attached request report's date and first part; the recommendation and rationale the document proposed | That this date is the State Council's abolition date |
| E4 | The State Council notice of 1986-06-24 required the draft to stop being used | Text and date of Guo Fa [1986] No. 64; this round relies on the official transcription | That actual social use went to zero on the same day, or that all glyph shapes never appeared thereafter |
| E5 | Beijing forwarded on 1986-07-30 and required inspection and correction | Web metadata and local body text of Jing Zheng Fa [1986] No. 107 | That the local forwarding date equals the central notice date; that issuing a notice means execution is complete |

## Causes are registered first only as the actors' explanations

The attached request report holds that the scheme was not yet mature, that the norm needed stability, and mentions the conversion burden of existing toolbooks and font libraries. This supports "these reasons appear in the decision material," but does not yet establish the actual magnitude of the burden, which factor was most critical, or that no other political and organisational explanation exists.

The hypothesis that can currently be proposed is: local writing simplification may be accompanied by old–new reading and conversion costs; the overall adoption benefit depends on the audience and supporting measures. This is not an accomplished causal adjudication of the Second-Simplification, nor is the term "technical debt" an explanation of the whole process.

| Item to check | Minimum supplemental evidence | How it could change the judgement |
|---|---|---|
| Scheme maturity and comprehension | Contemporary material on specific glyphs, ambiguity and misreading—not merely a list of strokes | If the alleged comprehension burden is absent, narrow the cognitive-cost explanation |
| Toolbook and font-library conversion | Then-current versions, update arrangements, investment records, and feasible compatibility options | If conversion was actually light, it can no longer be fixed as the principal cause |
| Users' adoption and rejection | Material on teachers, publishers, readers, recording the sample and its denominator | Beneficial adoption or continued use within a field may appear, overturning the blanket "failure" description |
| Authorisation, revision, and policy environment | The 1978 original notices, successive revisions, and contemporaneous dissent | May support alternative explanations such as coordination or goal change |
| Same-field neighbours | The 1956 scheme's phasing and supporting measures, with unified comparison fields | If the same mechanism cannot distinguish different paths, conditions must be added or the explanation admitted insufficient |

## Current adjudication

A formal withdrawal has a locatable administrative text; adoption, comprehension, overall cost, and distributional consequences have not yet been measured. Failure may for the time being refer only to the draft's formal continuous promotion being blocked and its being abolished; it cannot be elevated into an overall failure of Chinese-character simplification, of lowering the barrier, or of the engineering method.

The next deliverable under this project is to supplement the originals and opposing material, marking support, conflict, and omission item by item. An explanation formed solely on S1 must not be written as an already-verified principal cause of failure; when new evidence conflicts with the framework, retain the conflict and then decide the scope of revision.

## Main research question: does merging glyphs transfer the cost of distinguishing information?

Per the maintainer's clarification of 2026-10-23, the main line focuses on "how to disambiguate after the distinctions a task must preserve are merged many-to-one"; the chip remains only as collateral evidence of migration cost, and is not treated as a principal cause or main research variable of this paper.

First separate two kinds of change: the consolidation of allographs of the same task object need not lose the information the task requires; it is only the rewrite that maps different objects a task must distinguish into the same glyph that constitutes the mapping this item tests. A graph becoming simpler, different glyphs becoming similar, and multiple sources being synthesised into one glyph are different treatments and must not be mixed in the accounting.

**Conditional derivation rather than historical measurement:** suppose a task requires distinguishing A and B, but the rewrite satisfies f(A)=f(B)=X. Given only X and no other clue, one cannot guarantee recovering which original item it was. To preserve the original distinction, one must resort to context, annotations, extra fields, source records, or exception rules; if this information already exists, no new cost may be incurred. A word is only one possible disambiguation carrier among others, and increasing word length does not guarantee disambiguation. This structural conclusion does not directly establish that readers react more slowly, that overall net cost rises, or that the Second-Simplification was therefore withdrawn.

The core comparison is: **whether the task's original distinguishing capacity is preserved; if preserved, who bears the added identification, communication, correction, and recording burden.** In particular check short fields, abbreviations, names, and other context-constrained tasks, but each must first verify the real rules and mappings, without assuming all single-character tasks fail. The existing traditional–simplified many-to-one relations may serve as general mechanism background, but must not be blended into Second-Simplification-specific or Second-Simplification-effect data.

The starting point of verification is Unicode [UAX #38 §3.7.1 (Revision 41)](https://www.unicode.org/reports/tr38/tr38-41.html): this round read the traditional–simplified mapping and contextual-disambiguation notes; it supports that general character mapping has a one-to-many reverse selection, but is not the 1977 draft's normative glyph table or a cognitive-cost study. §3.4 also reminds that actual reading cannot be understood as parsing isolated characters one by one. Therefore this mechanism is not called "moving toward an alphabetic language": a change in the ambiguity of writing units does not equal writing being changed to phoneme-based encoding, and Chinese itself does not thereby become another language.

The next minimal material: item by item preserve the draft version / table number / glyph image, the source character, the merged character, the values the original task needed to distinguish, the allowed context, the actual ambiguity, whether it was noticed, the remedy and the investment. The 1977 published draft must not be mixed with earlier drafts / revised drafts; at present this draft-mapping table is not complete, and generalised examples or search snippets must not be filled in as already-checked character cases.

Distinguishable observation: if the merged objects were originally equivalent in that task, the original table still preserves the necessary distinction, existing fields suffice to recover it, or a qualified comparison shows accuracy does not decline and no extra disambiguation burden is needed, then the cost-increase claim for that scenario does not hold or must be narrowed; if only more potential ambiguity is observed, one still cannot directly write it as a measured reading burden. Continue comparing single-character, word-bearing, and full-context conditions separately, without first selecting a window that necessarily supports the claim.

## Cross-generational tracing: separate inability to read the original from inability to recover the record

This is a research direction further proposed by the maintainer, not a newly-added verified historical consequence. The distinctions are as follows:

| Layer | What to check | What cannot be directly inferred |
|---|---|---|
| Reverse recovery of a single record | Whether, after different original values were synthesised into one writing, old originals, original-character fields, migration logs, genealogies, or other corroboration exist | Many-to-one does not automatically mean all evidence is already lost; corroboration may allow recovery |
| Reading ability of historical texts | The training and tools needed by someone who learned only the new system to read old glyphs, old grammar, and specialised literature | A new record cannot uniquely reverse-infer the old character, but that does not mean a person cannot relearn the old system; knowing traditional forms does not equal being able to read all ancient texts |
| Long-term maintenance and distribution | Who preserves originals, trains readers, makes dictionaries/translations, handles misidentification; when costs occur and who pays | One must not pre-assume all costs are delayed or that net cost must be positive; educational and archival support may lower the barrier |

**Surname conditional example, not an already-checked case:** suppose a migration records the originally-distinguished "Dai (代) / Dai (戴)" uniformly as "Dai (代)," with no original character or other distinguishing clue preserved; later generations, relying only on this new record, cannot uniquely judge which character the old record wrote. Even learning all the conversion rules can only list candidates, not recover the record's true value out of thin air. If old household registers, epitaphs, genealogies, collateral records, or migration logs are preserved, further disambiguation may be possible; whether recovery is possible must be checked case by case per lineage.

The above does not equal having verified all origins of the Dai (代) / Dai (戴) surnames, does not equal that people with different writings share one ancestor, and does not equal that all present Dai (代) surnames arose from the Second-Simplification. This round did not obtain the relevant per-person archives nor complete the original-document check of the 1977 published draft's surname-application rules; whether the character Dai was used for pre-existing other records, and when the rewrite occurred, remain evidentiary work.

Therefore the local rejection condition must be concrete: if a real migration preserves the original character, or reliable originals or other fields suffice to match, one cannot call that sample permanently source-lost; if standardised learning material can, at reasonable investment, let the target readers read old texts, one cannot call historical texts unlearnable. Conversely, when all available clues are insufficient to distinguish candidates, one should mark "original character undetermined," and cannot pick an ancestry for the sake of a smooth narrative.

## Korean and Vietnamese material: comparative clues on historical accessibility, not a pre-sealed trap

- K1: [The Veritable Records of the Joseon Dynasty English introduction by the Korean Institute of Korean History](https://sillok.history.go.kr/intro/english.do), the Overview paragraph on Chinese-character originals, ordinary readers, and the Korean translation. Checked 2026-10-23: the project states ordinary readers face a Chinese-character reading barrier, and records that translation and digitisation improve access. This simultaneously supplies both barrier and remedy clues; it does not establish that the barrier is caused solely by script policy, or that Koreans can no longer learn/study their own history.
- V1: [The Nôm Foundation's self-described "Our Work"](https://nomfoundation.org/About-the-Foundation/Misions?uiLang=en), items 2–5 on original preservation, aligned texts, dictionaries, and training. What was read 2026-10-23 is a historical self-description containing early projects and plans; the dated quantities or plans therein are not treated as today's statistics, nor is the institution asserted to still operate per that plan merely because the page is online. The material shows that preservation, transcription, and training work exists; it cannot thereby establish that the Second-Simplification will produce the same consequence or that all Vietnamese cannot read their own historical sources.

The comparable question is "how old-document direct readability, training/transcription, and preservation costs are distributed," not first declaring that some country has fallen into a trap. The objects, languages, education, and historical conditions of Chinese-character, Nôm, Chinese-character simplification, and alphabetic reform differ; whether the same mechanism transfers requires separate argument. The relevant language-policy timelines and surname facts were not comprehensively checked this round.

The next tracing-material table should preserve: `original image and time, original writing, migration rule and scope, new writing, whether original character/log preserved, lineage or document matching basis, candidate count, unknowns, learner background, training and retrieval investment, reading/recovery result`. Count "historical document learnable" and "that piece of information recoverable" as separate results; do not yet claim a completed natural experiment, a cross-generational loss estimate, or a universal law of irreversibility.

## This-round supplemental check: the accurate identity of the chip rationale and the SP-RFC-001 reverse material

Re-read the full text of S1 on 2026-10-23. The first part of the attached State Language Commission request report does contain the expression of a conversion burden from fixed-mask-body chips and the addition of new simplified characters. The location is the **State Council-transmitted State Language Commission request report**, and it must not be labelled an independent technical measurement inside the State Council notice body; the State Council's approving the request report does not produce a second independent source chain.

One may register: the replacement cost of existing font libraries and toolbooks entered the decision rationale. One may not register: that specific equipment costs were verified, that a re-streaming implementation was necessary, that it was the principal cause of abolition, or that the social optimum encoding is entirely determined by hardware distribution. To develop the ROM explanation in engineering terms requires separately checking then-current equipment, font-module implementation, and update/compatibility paths.

This case is formally registered as a **reverse-test candidate material for a partial application of SP-RFC-001**, meaning to check the over-strong extrapolation that "reducing strokes / writing burden necessarily lowers comprehension cost"—not having established that "the Second-Simplification lowered writing cost and raised recognition cost." The actual direction and magnitude still await measurement comparable in character, audience, training, and context. The hardware-replacement cost cross-relates mainly to SP-RFC-017 migration accounting and cannot substitute for the comprehension measurement of SP-RFC-001.

## Item-by-item handling of newly added claims in outside drafts

The following are to-be-checked leads or invalid inferences; they are not treated as this project's measured results; the internal original drafts are not replicated. The publisher and paper original entry points are listed after the table.

| Material/conclusion proposed for inclusion | This-round verification and problems | Handling |
|---|---|---|
| 83.5%/91.3%, 46.4%/66.9% are Second-Simplification recognition rates | The original draft itself lists the objects as cross-glyph recognition of common traditional–simplified characters; the forwarded citations found this round provide no Second-Simplification experiment, and the original experimental method and data for these proportions were not located | Do not admit as Second-Simplification effect evidence; retain the local search lead. Must not be confused with another 800-plus-person study as the same experiment |
| The 800-plus-person study establishes that recognition cost rises monotonically with compression | The Tsang et al. original-paper abstract has been checked: in ordinary simplified–traditional word judgement, simplified is slower but more accurate; one cannot record only the slowness and omit the accuracy, nor was the Second-Simplification studied | As a boundary of SP-RFC-001-related research, not a Second-Simplification effect or causal verification; the full-text method was not rechecked |
| 3500→56008 means the morpheme inventory expanded 16-fold | The publisher confirms 56008 is the number of words collected, not morphemes. Dividing entries of different character lists and word lists is not a generation or loss measurement of the same set | Delete the use of the "16-fold loss/generation" tree as evidence; first distinguish glyph, character, morpheme, word, and word-sense |
| Glyph merging equals deleting morphemes; the Second-Simplification reversed the historical disyllabification | Writing mapping, spoken vocabulary, and word-formation levels differ; merging glyphs does not automatically make word meaning or morphemes disappear | Do not adopt this derivation; separately check ambiguity and recovery conditions in specific contexts |
| The First-Simplification only saved strokes, had no many-to-one, pure benefit and automatically reversible | The draft's own listed traditional–simplified many-to-one examples already conflict with "only moved strokes"; whether recoverable depends on context and added records | Do not adopt the lossless / pure-benefit / universally-reversible claim, nor thereby judge all simplification harmful |
| Total cost must be U-shaped, the First-Simplification sits at the optimum, the Second-Simplification crosses the line | No comparable cost curve, weights, audience, or sample; strokes are not a calibrated unit of writing time or recognition time | Retain only the trade-off question; do not draw it as empirical fitting or announce a threshold found |
| 13.1→6.9 can represent the average performance of two writing systems | The original character-list scope, sample, algorithm, and weighting were not checked; the draft lists only secondary sources | Do not admit the quantitative conclusion; must first clarify whether only simplified characters and frequency weights are counted |
| Fu/Fu (傅/付), Dai/Dai (戴/代) etc. are claimed to show the Second-Simplification caused undetectable identity errors | No per-person original household register, writing prehistory, change time, or correction record; same surname does not equal same origin, different writings not automatically caused by the Second-Simplification | Retain the error-detection / identity-migration research direction; do not write as a verified case or natural experiment |
| Merging two sources must lose 1 bit, unrecoverable at any cost | The 1 bit requires a specific probability setting; recovery also depends on context, backups, and corroboration. Many-to-one only means the output alone may not uniquely reverse-infer | Do not adopt precise loss and absolute unrecoverability; need conditional distribution, auxiliary information, and preservation mechanisms |
| Homography is an exact hash collision; fixing glyphs is hash-table expansion | No specified hash function/table; changing labels, namespaces, and bucket expansion are not the same operation | Retain the clearly-identified many-to-one analogy; do not claim strict technical isomorphism |
| Names must be unique; dictionary variant notes are claimed to show the norm erased error traces | Name and unique-identity key differ; the relevant edition's editorial basis was not read, and deleted notes alone cannot establish intent or full consequences | Do not adopt the uniqueness premise and motive attribution; need separately to check original records and compilation notes |
| The Korean timeline can cross-verify the Second-Simplification and that the adapter is permanently ineliminable | The newly-added K1/V1 only read historical accessibility and a preservation-project self-description, and the original regulation, statistics, and causal process are still unchecked; the policy object differs from the Second-Simplification | Retain the comparison lead; do not adopt the draft's policy-causality / permanence extrapolation; do not treat "multiple sources agree" as independent original verification |

Relevant original entry points:

- R1: Tsang et al., [Comparing word recognition in simplified and traditional Chinese: A megastudy approach](https://journals.sagepub.com/doi/10.1177/17470218231176472), online 2023-05-08, 2024 vol. 77 issue 3 pp. 593–610. Checked the publisher abstract, bibliographic information, and data-availability statement; the full-text method was not obtained, and data were not downloaded/analysed. The abstract reports both speed and accuracy; it must not be retold as a Second-Simplification experiment or a net-cost estimate.
- R2: The Commercial Press, [bibliographic and content-summary page for "Modern Chinese Common Word List" (现代汉语常用词表)](https://www.cp.com.cn/book/91f93016-f.html), 2008-11, ISBN 978-7-100-05655-7. Only the publisher page was read; it supports the word count 56008, and does not establish that 3500 characters generate all entries, nor morpheme count, nor character-merge loss.

## Error detection is worth retaining, but the evidence must be redesigned

One may record task accuracy and "whether the error was noticed" separately: standard answer, reader response, confidence, found/not-found error, correction channel, and correction consequence. The proportion of unnoticed errors requires a known true value and denominator; one cannot infer a real error rate or unrecoverability from a single surname story. Measurement requirements are separately in [H01](../H01_expression_and_understanding_cost.md).

Finding no error does not establish that there is no loss; someone feeling confused also does not establish a wrong answer. Surname migration must also distinguish the person's autonomous choice, historical folk writing, entry error, and policy coercion; one cannot attribute different writings to the Second-Simplification on sight.

## This-round proposition receipts

| Sub-claim | Material and comparison | Current adjudication | Theoretical write-back |
|---|---|---|---|
| The Second-Simplification was formally stopped from use | S1 E4; separated from local forwarding and the earlier trial-stop | Supported by official transcription; this is not used to generalise all social use | Master source unchanged |
| Replacing existing font libraries entered the decision consideration | First part of the request report attached to S1 | Supports the actors' rationale; its actual cost or causal weight not identified | As an SP-RFC-017 cross-issue, cannot fill the SP-RFC-001 measurement |
| Whether glyph simplification or merging transfers the distinguishing burden | First check the task-related many-to-one mapping; R1 and UAX #38 serve only as general research background | Reverse non-uniqueness without added information is conditionally derivable; the Second-Simplification's specific ambiguity, reading effect, and net cost are unmeasured | Do not revise SP-RFC-001 for now; first deliver the draft mapping and the constrained-context task table |
| The Second-Simplification caused silent surname errors | Per-person records and a detection baseline still lacking | A valuable question, not a confirmed consequence or natural experiment | Add detection fields; do not alter the whitepaper / PR-001 prediction |
