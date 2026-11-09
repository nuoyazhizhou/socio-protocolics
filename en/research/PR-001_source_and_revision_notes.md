> **Translation record**
> - Chinese source: `research/PR-001_来源与修订说明.md` (sha256 `3af4ae20c4d0fe422684199215797699f6a8e28f9484cf01b252843812be0254`, `5622` bytes, 2026-11-09)
> - Chinese version / release tag: `v11.2-r20261106` (theoretical version remains v11.2)
> - Translation version: `en-v0.1`
> - Translation date: 2026-11-09
> - Check status: checked sentence by sentence against the Chinese source for claim status, negative guardrails and numbering; machine and glossary checks only; no independent professional native-speaker review
> - Pending sync: pending registration in public-files.json / mkdocs.yml
> - Status: complete translation
> - Authority: the Chinese SSOT is authoritative; this translation does not constitute a separate set of definitions (C2)

# PR-001 | Sources and revision notes

Corresponding to the [design draft v0.2](PR-001_agent_collaboration_scale.md), 2026-10-22. This document is an editorial and methodological verification record, not an independent peer review; no experiment has been run nor formal pre-registration completed.

## Sources read and scope of use

| Source | What was actually verified this round | What this card retains | What is not claimed on this basis |
|---|---|---|---|
| Kim et al., [*Towards a Science of Scaling Agent Systems*, arXiv:2512.08296v3](https://arxiv.org/abs/2512.08296v3) (revised 2026-04-08) | the arXiv title, version and abstract; the abstract reports architecture matching and coordination overhead under multiple configurations and tasks. No table-by-table check, no code or data reproduction | that task, architecture and budget need to be controlled, and it is an existing study worth comparing against | that all systems have a unique interior N\*; that lowering access cost does not change N\*; that all percentages in the original card have been re-verified |
| Fontanari, [*Exact Solution of Granovetter's Threshold Model for a Finite Population*, arXiv:2606.25921v1](https://arxiv.org/abs/2606.25921v1) (2026-06-24); the page lists *Mathematics* 14 (2026) 2620 | title, version, journal information and abstract; threshold heterogeneity is modelled with a Beta distribution, and the abstract distinguishes the infinite-population limit from different β conditions | α is the threshold-distribution parameter in this model and may inspire a separate model study | that α is the real access cost; that α=1 can directly predict this experiment's collaboration quality or optimal scale; that the threshold model equals LLM autonomous choice |
| Lakens, [*Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses* (2017)](https://doi.org/10.1177/1948550617697177); [author's collected paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC5502906/) | the abstract and the equivalence-method section returned by search, covering preset equivalence bounds and "non-significant does not equal no effect"; opening the full text directly hit an access check, so it was not treated as a close full-text read | the preset minimum meaningful difference, and the distinction between supporting equivalence and an undetermined result | that a simple t-test or TOST can be applied without argument to the discrete N\*; that this card's sample size and interval algorithms are already fully designed |
| [OSF registration guidance](https://help.osf.io/article/330-welcome-to-registrations) | the passages on definitions and on a research plan needing explicit variables, analyses, exclusions and deviations | the distinction among draft, frozen plan, execution and post-hoc exploration | that writing a date means registration is complete, or that this card already has a registration link |
| [Git commit documentation](https://git-scm.com/docs/git-commit) | the project had previously verified the date-specifiable documentation; this round follows the version-tracking boundary | that Git records the content version; the public registration record is kept separately | that a commit date is naturally unalterable or carries an independently credible time certification |

Both arXiv papers could be located and should no longer be loosely labelled "the whole paper does not exist / nothing was verified". Likewise, locating the abstract does not equal confirming all values and extrapolations. The Kim-related benefit figures in the original card, and the Vals AI / Anthropic cost and Fable scale claims, were not used as the basis for this card's predictions; the latter two have not yet been located item by item in the original material, so they are not assumed to be fictional.

The original card's claim about the Kittur and Ortega studies — "one measures participation rate, the other measures concentration, therefore both are right" — was not re-checked item by item this round against the same time, language, editor definitions and contribution scope, so the definitive reconciliation conclusion is withdrawn. Even if the agent experiment supports H2, it cannot by itself resolve the disagreements among Wikipedia studies.

## Substantive differences from the original card to v0.2

| Original treatment | v0.2 treatment |
|---|---|
| "registered, not yet launched" | an open-for-review draft; no external registration credential, and the registrant is not back-filled |
| the title claimed access cost and scale were orthogonal | changed into a question; H1b only predicts substantive equivalence under specified conditions, which is not the same as independence |
| the original P1 combined participation growth with unchanged N\* | split into H1a and H1b, to avoid confusion with the whitepaper's P1 (postulate 1, resource background), and adjudicated separately |
| N\* undefined | defined as the in-grid optimal configuration upper bound under a fixed collaboration budget and task, distinguishing the active count and boundary truncation |
| p>0.05 treated as no change | a preset equivalence range; insufficient evidence is separated from equivalence support |
| listed only α's positive correlation with N\* as refutation | α is no longer used to replace cost; both meaningful positive and negative changes in N\* can oppose H1b |
| when the threshold could not be measured, diversity was switched to instead | neither can directly replace access cost; when not identifiable, the corresponding hypothesis test is not launched |
| auto-runs could also be discussed as participation rate | requires identifiable join/decline and real access, otherwise study start-up or latency separately |
| non-zero output was required for participation | participation and qualified contribution are separated, to avoid defining the denominator by the result |
| choose either Gini or top-1% | the active-member-normalised Gini is primary; the all-seat metric is reported separately, and small teams do not use top-1% directly |
| post-hoc selection of the best point and beyond-peak interval | requires handling peak-selection error, interval selection and hierarchical dependence before freezing |
| an R² threshold and zero-crossing uniformly judged as undetermined | adjudicated by each hypothesis's effect threshold, equivalence range and identifiability |
| overturning P1 means the framework is stronger | overturning the corresponding local prediction; any alternative explanation requires separate testing |
| unchecked numbers treated as a prior for N\*'s necessary existence | returned to source clues, specifying neither a statistical prior nor a preset interior peak |
| any post-launch modification invalidated the whole card | retain the frozen original and publish deviations, specifically judging which analyses become exploratory |
| Git timestamps are tamper-proof | version records and independent registration time are kept separate |
| after three months, must fill in "established" or "overturned" | the review may record "not yet executed", "unidentifiable" or "undetermined"; it does not manufacture results |

## Relationship with the whitepaper

This round did not modify the [whitepaper text](../../社会系统协议学白皮书.md) or the [CheatSheet](../CHEATSHEET.md). Limited resources, autonomous agents, expectation and feedback are the source of the questions, and the H1a/H1b/H2 of this card cannot be derived directly from these postulates. New results should first be compared with existing architecture, organisation and collaboration explanations; whether the whitepaper needs revision is adjudicated separately on the basis of concrete evidence.

What needs collaboration first is not producing significant results, but filling in the [card's items to be locked](PR-001_agent_collaboration_scale.md#vii-items-that-must-be-completed-before-a-formal-launch) — in particular whether access cost is operational, whether contributions are attributable, and how to compare an uncertain optimal scale.
