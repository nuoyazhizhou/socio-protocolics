> **Translation record**
> - Chinese source: `research/cases/II-INT_审计与驾照研究核对.md` (sha256 `56a0db61f205f48f139f4085fdf8bbeb6e1da758c634aa60d34b55f65bee8f8c`, `5124` bytes, 2026-11-09)
> - Chinese version / release tag: `v11.2-r20261106` (theoretical version remains v11.2)
> - Translation version: `en-v0.1`
> - Translation date: 2026-11-09
> - Check status: checked sentence by sentence against the Chinese source for claim status, negative guardrails and numbering; machine and glossary checks only; no independent professional native-speaker review
> - Pending sync: pending registration in public-files.json / mkdocs.yml
> - Status: complete translation
> - Authority: the Chinese SSOT is authoritative; this translation does not constitute a separate set of definitions (C2)

# Group II Foreign-Research Check: Audit and Driver's-License Agency

Version: material table v0.1 | Date: 2026-10-23 | Chinese original; English translation pending.

This is a check of passages from two published papers, not a replication, a systematic review, or a re-analysis of the original data. The two cases differ in task and result and cannot be merged into an "average intermediary effect," nor are they a causal control for the Zhejiang reform.

## I. II-INT-A: Olken's Indonesian road audit study

**Version and locating.** Benjamin A. Olken, 2007, *Monitoring Corruption: Evidence from a Field Experiment in Indonesia*, *Journal of Political Economy* 115(2):200–249, DOI 10.1086/517935. [The published version preserved by the author's university](https://economics.mit.edu/sites/default/files/publications/Monitoring%20Corruption%20Evidence%20from%20a%20Field.pdf). This round read the abstract and pp. 200–203, 217–220 (Table 4 and result notes), 240–242 (§VI, Table 13). The 2005 NBER working paper 11753 is only a version predecessor; figures are not spliced from the two versions.

**Usable results and limits.** The study covers 608 village projects; the audit intervention raised the probability of an announced audit and was actually carried out. Missing expenditure is compared between declared values and independent engineering estimates, and the indicator may contain non-theft loss. Table 4 road main-project row N=477, no fixed-effects estimate −0.085, p=0.058; stratified fixed-effects −0.048, p=0.123. One cannot write that all specifications are significant at the 5% level. The net benefit in §VI depends on additional assumptions.

**Role in this project.** As material testing the unconditional claim that "adding a layer only harms results." If the object of study has a supervision benefit, then the SP-RFC-004 premise of "no added output / recovery" is not met; this cannot be interpreted as the multiplicative arithmetic being overturned by experiment, still less that it verifies this book's loss parameters.

**Next take-up check.** Column by column check the randomisation level, clustered standard errors, missing samples, and engineering-estimate calibration, then separately check cost–benefit sensitivity. Do not use the initial 608 in place of all analysis-row sample sizes, and do not translate missing expenditure directly into a net loss of social resources. Analysis data and code have not been obtained this round, and no coefficient has been re-estimated.

## II. II-INT-B: Bertrand et al.'s Delhi driver's-license study

**Version and locating.** Marianne Bertrand, Simeon Djankov, Rema Hanna, Sendhil Mullainathan, 2007, *Obtaining a Driver's License in India: An Experimental Approach to Studying Corruption*, *The Quarterly Journal of Economics* 122(4):1639–1676, DOI 10.1162/qjec.2007.122.4.1639. [The published version linked from the authors' page](https://sendhil.org/wp-content/uploads/2019/08/Publication-44.pdf). Checked the paper's first page, §III recruitment/grouping passages (pp. 1643–1645), §IV main results and Table III (pp. 1651–1655), §V and Tables V–VII (pp. 1661–1669), and §VI related explanations (pp. 1669–1671); the full text was not read through and statistics were not re-run. The 2006 NBER 12274 titled *Does Corruption Produce Unsafe Drivers?* is not treated as the 2007 publication.

**Usable results and limits.** The initial 822 participants were assigned by fast-license reward, driving course, and comparison group; whether agent use was non-randomly assigned is not. Table V's agent-use comparison is a correlation analysis; §V.B separately uses scripted audit visits, recording the agent's promises and quotes, which is not the same as actually obtaining a license case by case. The Table VII on artificially creating red tape and §V.C rely on descriptive evidence and cannot be elevated into an identified complete causal feedback.

**Role in this project.** Record the parties' convenience, qualification quality, authority, and payment separately; one cannot use licensing speed as the sole success criterion. It is not a conclusion about all agent occupations, nor does it directly estimate all mechanisms of this book's SP-RFC-005.

**Next take-up check.** Label each conclusion clearly as random intervention, post-selection descriptive comparison, or audit-script evidence, and record denominator, attrition, and tracking window item by item. First explain why different tables do not share the initial sample size, then consider whether the related design can be used for other administrative flows.

## III. How the two cases participate in the comparison

| Analysis question | This-round arrangement | Boundary that cannot be crossed |
|---|---|---|
| Whether supervision has only cost | Use the audit case to bound the unconditional "one more layer must be bad" judgement | Do not transfer the road-project effect to all approvals or meetings |
| Whether party convenience equals total benefit | Use the license case to require separately recording qualification and service indicators | Do not rename the correlation table as a randomised experiment on agent use |
| What the framework adds | Use O4 and the SP-RFC-004/005 boundaries to organise the questions, compared with an ordinary cost list | The original studies already exist; renaming is not a mechanism finding |
| How to revise the whitepaper | Current material reminds one to retain conditions such as productive benefit, separation of service and authority, and independent measurement | These limits already exist in the master source; this round does not re-add a theorem, nor claims the whole group is verified |

Another Chinese candidate — the national pipeline-network meeting burden — currently has only [item 3 of part 2 of a 2024 official reprint notice](https://lzw.cmc.gov.cn/pgt/art/2024/art_e7bb5788c0d94bed97af2f705c81e076.html) as checkable. It is registered only as "a notice lead that a coordination-burden problem exists"; the meeting output, man-hours, and post-cancellation results have not been obtained, and it is not counted as evidence of equal weight with the two experiments. This round did not independently verify that candidate's continuous change across 2022–2024.

Main-text entry: [Removed Two Approval Steps — Did the Work Really Decrease?](../../articles/intermediary/two_approvals_removed.md). The to-be-tested questions in methodological expression are separately in [OP-001](../OP-001/question_card.md).
