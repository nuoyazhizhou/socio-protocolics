> **Translation record**
> - Chinese source: `research/PR-001_Agent协作规模.md` (sha256 `2480e274b0d992c41aefb60518d75980f02ddc1fc7e991e535cb28feb2b497c8`, `12397` bytes, 2026-11-09)
> - Chinese version / release tag: `v11.2-r20261106` (theoretical version remains v11.2)
> - Translation version: `en-v0.1`
> - Translation date: 2026-11-09
> - Check status: checked sentence by sentence against the Chinese source for claim status, negative guardrails and numbering; machine and glossary checks only; no independent professional native-speaker review
> - Pending sync: pending registration in public-files.json / mkdocs.yml
> - Status: complete translation
> - Authority: the Chinese SSOT is authoritative; this translation does not constitute a separate set of definitions (C2)

# PR-001 | If access is easier, will the optimal collaboration scale be larger?

**Status: an open-for-review research design draft, v0.2. Not yet formally pre-registered; no experiment has been run under this protocol; there are no results.**

Compiled: 2026-10-22. Planned review point: 2027-01-22; even if there are no results by then, progress and reasons will be recorded, and it will not be back-filled as though a completed test had been done. The responsible person, frozen version, and external registration record will be filled in after the design is completed.

`PR-001` is only a problem identifier; it is not a registration credential. The H1a, H1b and H2 in this document are local research hypotheses, not the whitepaper's three postulates or core propositions. The two predictions on the original desktop card have here been split apart and revised into a discussable design.

## I. What we want to test

That "more people or agents can gain access" and "a larger team can collaborate effectively" are two different matters. This card asks: **does lowering the access cost raise actual participation, yet not markedly change the best-performing collaboration scale under a given task and resource budget?**

The tentative object of study is an AI agent collaboration system. Even if supported, it cannot be directly generalised to human willingness, Wikipedia contributors, all social organisations, or the loosely termed "emergence of collective intelligence".

Three judgements pending test:

- **H1a: lowering the access cost raises the actual participation rate.** It must exceed the minimum meaningful gain specified before launch; it cannot rest on a significance label alone.
- **H1b: after lowering the access cost, the change in the optimal configuration scale falls within a preset equivalence range.** It does not predict strict mathematical invariance, nor does it describe this as already-proven variable orthogonality or statistical independence.
- **H2: beyond the identifiable optimal scale, more active participants coincide with more concentrated qualified contributions.** One cannot simply count the added empty seats as concentrated output.

The original main prediction was counted as locally supported only when both H1a and H1b were supported, forming these two parts together. If any one is contradicted by the results, the corresponding hypothesis should be revised; it is not automatically interpreted as "the framework is stronger".

## II. First, separate scale, cost and performance

| Symbol | Definition in this card | Easily confused with |
|---|---|---|
| N | the number of accessible seats to which a task assignment is issued and invitations sent, assigned by the experiment | a denominator adjusted afterwards by the active count; the total platform user count |
| A | the number of agents that explicitly joined and actually entered the collaboration phase, A≤N; those with zero contribution after joining are still counted | whether a qualified contribution was produced, or merely the number started |
| R=A/N | the actual participation rate, with the denominator retaining all assigned seats | the proportion only among successful producers |
| c | the assigned high/low access-cost condition, manipulated via tool round-trips, waiting, and resource-consumption checks | the Beta-distribution shape parameter, model diversity |
| Q(N,c) | the expected proportion of final answers passing fixed acceptance, under a predetermined task distribution and fixed collaboration budget | total word count, call count, per-capita output, or cost efficiency |
| B, T | the total resource budget and wall-clock time limit for the collaboration phase of each task, including coordination overhead | giving each agent the same budget and then stacking without bound |

The optimal configuration scale in the main question is defined as:

$$N^*(c)=\min\operatorname*{arg\,max}_{n\in\mathcal G}Q(n,c)$$

where the scale grid $\mathcal G$ is locked before the formal study; if several scales are genuinely tied for optimal, the smallest scale is used as the tie-breaking rule by definition. This rule does not mean estimation error can be ignored: the entire performance curve, the near-optimal range, and the uncertainty should all be reported together.

**Here N\* is the configuration upper bound under a given grid, task and budget — not a universally "optimal number of active participants" whose existence has been proven.** If performance keeps rising up to the largest tested scale, one can only say that the region beyond the upper bound remains unknown; one cannot announce that an interior peak has been found. If the curve is too flat or the interval too wide, N\* cannot be reliably identified, and the H1b and corresponding H2 intervals are recorded as undetermined.

## III. How to operationalise access cost, with a feasibility check first

The candidate manipulation is: with task information, model, reward, or goal description held constant, vary the required registration tool round-trips or waiting steps before joining. The low-cost condition reduces these steps, the high-cost condition retains them; record the actual time and consumption, and do not merely label the two groups "high" and "low".

The agent must have a clear record of joining, declining, timing out, or failing to complete access. **If the framework offers no join/decline choice and records all auto-starts directly as participation, R is mechanically equal to 1, and H1a is not testable in that system.** A separate study of "start-up success rate / access latency" may be opened, but it cannot be renamed and then claimed to support the autonomous-participation prediction.

This candidate manipulation has not yet been verified as feasible and requires a pilot check:

1. The cost is genuinely different, and task knowledge, available tools, and collaboration opportunities have not been unintentionally altered.
2. The access phase and the collaboration phase are accounted for separately; the collaboration budget B and T are fixed, and end-to-end total cost and total latency are reported separately. Under this accounting, N\* is not the end-to-end cost-optimal scale; if instead the total budget is fixed, that is a different comparison that needs to be locked down separately.
3. The decline rule cannot be hand-set by the researcher to the participation rate they hope to observe. If a threshold can only be specified within a simulation, the conclusion belongs only to that simulation setting and is not treated as a real-system finding.

The threshold-distribution parameter α may be used for a separate behavioural-model study, but it cannot be equated with external access cost without calibration. Model/sampling diversity changes a different variable and is likewise not a substitute when c cannot be measured.

## IV. How to form a fair comparison

The candidate structure is a grouped comparison of "access-cost condition × configuration scale". Tasks, model versions, prompts, communication topology, tools, coordinator, and acceptance rules are fixed; conditions are assigned by task block, and repeated runs are arranged at each scale and cost.

A task family may be stratified, but favourable tasks must not be picked as the main result after seeing the outcomes. The task or team run is the unit of analysis; messages, tool calls, and multiple agents within the same task cannot be treated as mutually independent samples.

Final answers are scored by fixed tests or rules; when human scoring is genuinely needed, the condition should be hidden as far as possible and scoring disagreements recorded. Pilot material and the formal test are kept separate, and the data already viewed, the number of tests, and their influence on the plan must be disclosed.

When N\* is chosen using the data, and "beyond N\*" is then analysed, a selection error is present. Before freezing, an independent calibration/validation sample split must be selected, or a calibrated full-pipeline resampling method used, so that the peak-selection error is counted into the interval; one cannot treat the highest point in the same batch of data as an error-free constant.

## V. How to compute contribution concentration

First determine acceptable, attributable contribution units, such as accepted independent sub-problem solutions, and record how de-duplication, joint contributions, and coordination work are scored. Let agent i's qualified contribution be $q_i\ge0$. Output word count cannot be used directly to represent effective contribution, nor can a coordinator with no submission record be automatically scored as zero.

The main concentration measure uses the finite-population-normalised Gini among active participants:

$$G_A=\frac{\sum_{i=1}^{A}\sum_{j=1}^{A}|q_i-q_j|}{2(A-1)\sum_{i=1}^{A}q_i}$$

Defined only when A≥2 and the total qualified contribution is greater than 0. When effective contribution is missing or there is only one person, record it as "not applicable", and also report its frequency, without filling in zero. The contribution score here is an operational indicator; it does not equal each person's true causal credit.

Also report the all-seat concentration including un-joined seats, together with A and R, to avoid mistaking concentration caused by added non-access as concentration internal to active members. The original "top-1% share" is not used as the primary metric for small teams; teams of fewer than 100 people in particular need to handle rounding and scale comparability, and cannot quietly substitute the "top-1% share".

If a credible, non-negative and consistent attribution rule for qualified contributions cannot be established, H2 is not launched for the time being; only the system's overall performance is recorded.

## VI. How support, opposition and undetermined are divided

The following is a **verdict structure pending freezing**. The effect thresholds and interval algorithms are not yet determined, so the conditions for a formal launch are not yet in place. All intervals must use a method compatible with the data hierarchy, and address the simultaneous-comparison problem when needed.

| Hypothesis | Support | Oppose | Undetermined |
|---|---|---|---|
| H1a | under the predetermined scale weights, the participation-rate difference ΔR between low and high cost has an interval lower bound greater than the preset minimum gain δR | the interval upper bound is below δR, i.e. it excludes the promised meaningful gain; if the whole is below 0, note additionally that the direction is reversed | the interval straddles δR, or the cost manipulation / participation identification failed |
| H1b | define D=log₂[N\*(low cost)/N\*(high cost)]; its interval falls entirely within the preset equivalence range (-δN, δN) | the interval lies entirely outside one side of the equivalence range; both positive and negative changes can oppose "essentially unchanged" | the interval cannot be adjudicated, the scale peak is unidentifiable, or the test range is insufficient |
| H2 | in a pre-specified and identifiable beyond-peak interval, A's scale trend exceeds δA, and the main concentration trend exceeds δG | sufficiently precise data rule out at least one promised trend; a flat or declining trend can serve as opposing evidence | any necessary interval cannot be adjudicated, or contribution attribution is not credible, or there is no analysable beyond-peak interval |

δR is measured in participation-rate percentage points, and δN in the log₂ of the scale ratio; H2's δA and δG correspond to the pre-specified trend scale for changes in log₂N. For H2, which cost condition, which interval estimate, and which trend model is used as the main analysis must all be frozen; the two cost conditions cannot be mixed, nor can a segment be picked after seeing the curve.

The original card's generic rule "R²<0.3 or interval crossing zero means undetermined" is deleted. Different hypotheses face different boundaries: an interval that crosses zero but falls entirely within the equivalence range can precisely support H1b. A mere p>0.05 does not establish the absence of a meaningful change. For the equivalence approach, see [Lakens (2017), *Equivalence Tests: A Practical Primer for t Tests, Correlations, and Meta-Analyses*](https://doi.org/10.1177/1948550617697177); its simple test cannot be applied without argument to the discrete, peak-selected N\*. [Source and revision notes](PR-001_source_and_revision_notes.md) records the scope of what was read.

## VII. Items that must be completed before a formal launch

| Item to be locked | Current status |
|---|---|
| Access flow, join/decline rules, and manipulation-check thresholds | pending feasibility pilot |
| Task list, stratification, and scale grid | pending material check |
| Model / coordinator version, prompts, and tool snapshot | to be provided |
| Collaboration budget B, time limit T, access window, and complete cost scope | pending resource estimation |
| Contribution units, de-duplication, shared attribution, and coordination-work scoring | pending domain review |
| δR, δN, δA, δG, and the near-optimal range | pending a practical meaning in task or resource terms; must not be set to favour the results |
| Sample size, number of repeats, interval level/algorithm, peak-selection error, and multiple-comparison handling | pending precision or power planning |
| Beyond-peak interval, H2 cost condition, trend model, and robustness analysis | pending locking |
| Failures, timeouts, API errors, empty outputs, missing data, and exclusion rules | pending itemisation by error type; cannot keep only successful runs |
| Responsible person, actually accessible data, existing analyses, budget ceiling, and stopping rule | to be filled in |
| Frozen document, code/material hashes, external registration link and date | none yet |

This draft may now be made public to solicit design feedback; the empty items cannot be treated as a completed design. 2027-01-22 is a review point, not a date that guarantees a conclusion by then; if unfinished, it is published as unfinished.

## VIII. Three things easiest to take up

1. **Engineering feasibility**: submit a minimal procedure that records joining, declining, timeout and cost, and check whether H1a is actually identifiable; do not run an effect experiment first.
2. **Measurement and statistics**: design a contribution score sheet for a small task, point out the situations in which the Gini, budget, or N\* estimate would be distorted, and suggest a practical basis for the equivalence range.
3. **Literature check**: locate the task, scale, architecture, budget and measurement scope of existing studies, and show whether they already answer the same question, rather than merely all mentioning "multi-agent".

The minimum fields to submit are: version, task ID, run ID, cost condition, N, join status, A, final acceptance result, per-agent contribution and attribution basis, access and collaboration cost/latency, model and prompt version, random-assignment record, and error type. Raw-log access and public permissions are recorded separately; at present there is no set of downloadable real run data.

## IX. Results and version record

**Result status: none yet; guesses must not be filled in below.**

| Item | Backfill content |
|---|---|
| Frozen / registered version, link, date | not registered |
| Execution time, task/run counts, exclusions and missing data | not executed |
| H1a estimate, interval, and verdict | not tested |
| H1b curve, N\* range, D interval, and verdict | not tested |
| H2 analysable interval, A and G trends, not-applicable proportion, and verdict | not tested |
| Deviations, exploratory analyses, and unexpected findings | no execution record |

The draft may be revised before formal freezing, but the date and reason are kept; after freezing, the original version is retained and deviations and their impact recorded separately. Affected analyses are switched to exploratory or pre-registered separately; a single correction does not erase all old records, nor is the original prediction overwritten.

Git is used for version tracking and does not by itself serve as an unalterable registration timestamp. For formal pre-registration, see the [OSF registration guidance](https://help.osf.io/article/330-welcome-to-registrations); additionally keep an independently checkable registration record.

This card does not presuppose that an optimal scale necessarily exists, does not use agent experiments to reconcile Wikipedia studies, and does not claim that "both results validate protocolics". For existing studies, source verification and the changes in this round, see [source and revision notes](PR-001_source_and_revision_notes.md). This card takes up the questions in the [whitepaper](../../社会系统协议学白皮书.md) concerning limited resources, autonomous agents and feedback; the specific hypotheses still require independent testing.
