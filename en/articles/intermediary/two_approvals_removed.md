> **Translation record**
> - Chinese source: `articles/intermediary/删掉两道审批_工作真的少了吗.md` (sha256 `fb7215978bc581a2b4982051d9d820fd1f4eb752cf2b6b332624062f43d6d767`, `12268` bytes, 2026-11-09)
> - Chinese version / release tag: `v11.2-r20261106` (theoretical version remains v11.2)
> - Translation version: `en-v0.1`
> - Translation date: 2026-11-09
> - Check status: checked sentence by sentence against the Chinese source for claim status, negative guardrails and numbering; machine and glossary checks only; no independent professional native-speaker review
> - Pending sync: pending registration in public-files.json / mkdocs.yml
> - Status: complete translation
> - Authority: the Chinese SSOT is authoritative; this translation does not constitute a separate set of definitions (C2)

# Two approvals deleted — is the work really less?

Version: conceptual sample chapter v0.3 | Date: 2026-10-23 | English translation pending.

Status: pending reconstruction with a real case; T3 case-article acceptance not passed. The existing institutional material and paper citations have not yet been developed into a complete real mainline; evidence is to be supplemented and the piece reconstructed per the [case-first rules](../../CASE_DRIVEN_TESTING.md); the text is kept for now, and this round's status correction is not written up as the case study being complete.

A form travels from Desk A to Desk B, and back from Desk B to Desk A. A says a stamp is missing; B says the version is wrong. By the time you have fixed the version, C tells you: the old stamp can't be used — you have to get it stamped again.

At this point someone proposes: remove the two desks in the middle — wouldn't that be faster?

In a different setting you might hesitate. Before software goes live, testing turns up intermittent data overwrites; before release, the backups are confirmed impossible to restore at all. The steps that were slowing things down were, it turns out, shielding the people downstream.

All of the above are scenarios constructed for discussion, not a survey of any particular organisation. The question they raise is very concrete: **after a step is deleted, does the original work disappear, get transferred, or simply go undone?**

Counting desks won't answer it.

## Behind the service window, who else is doing the work

Start from a real document. In 2017 Zhejiang pushed the "multiple certificates merged into one, one licence with one unified code" (多证合一、一照一码) reform, listing "housing provident fund deposit registration" among the first batch of consolidated items. Here we look only at this registration for newly established units — withdrawals and loans are not discussed, and an employee's account opening and actual deposits are not counted together as completion. [2017 document, Annex 1, item 4](https://zjjcmspublic.oss-cn-hangzhou-zwynet-d01-a.internet.cloud.zj.gov.cn/jcms_files/jcms1/web3096/site/zfxxgkold/170713100118017.pdf#page=7)

Under the regulation text in force beforehand, a newly established unit had to go to the housing provident fund management centre to complete deposit registration; unit registration and the setting up of employee accounts were separate procedures. This is what the rules required; it cannot yet tell us how many trips applicants in a given city actually made at the time. [Text as carried in State Council Decree No. 350, Articles 13 and 14](https://www.shanghai.gov.cn/nw4544/20200905/0001-4544_302.html)

Zhejiang's new arrangement proposes unified acceptance, data entry and data sharing, while keeping the relevant departments' responsibilities for claiming data and supervising it. [Reform notice, part three and Annex 2](https://www.ndrc.gov.cn/xwdt/ztzl/gdqjcbzc/zejiang/201807/t20180704_1209490.html)

On this design, what changes is possibly how firms interact with departments: part of the repeated submission and relaying work is shifted to cooperation between the service window, the platform and the back office. One fewer interface on the firm's side; the back office still has work.

This is much like wrapping an interface in software: the user need not know how many services are called behind it, which does not mean those services are not running. **This is the author's functional analogy, used to raise questions to check — not evidence that the reform works.**

How much time the reform actually saved still requires checking processing records, correction-and-return cycles, data matching, back-office hours, and the people who never entered registration. What a document says should be done and what actually gets done are two different kinds of material. At present we have only the process starting point at the institutional level, and cannot write "total cost has already fallen". [Table of where the work went and what is missing](../../research/cases/II-CN-A_housing_fund_registration_disposition.md)

## Removing a post is not removing the work

Imagine a data-lookup system. In the middle sits a person whose job is to nail things down: from which date does the period run? Is the amount in yuan or in fen? Does "last year" mean the calendar year or the fiscal year?

Delete that box from the org chart and the two ends connect directly. The dates, units and fields do not vanish with it. The explaining work may be spread across every applicant, or may turn into the back office returning forms again and again to be refilled.

Validation in software also helps make sense of this. JSON Schema can constrain required fields and types, but "age is an integer" and "this age is true" are still two different things. Technical validation has its own boundary; it cannot substitute for fact-checking. [The type and required entries of the structural validation spec](https://json-schema.org/draft/2020-12/json-schema-validation)

Let's work a small exercise. **All of the following numbers are fictional set-ups authored for this piece, not field measurements from Zhejiang or any institution.** The same 100 applications; both methods eventually complete all 100, with acceptance, accessibility and review conditions held identical by stipulation.

| Per batch of 100 applications | The two ends process directly | With a translation layer added |
|---|---:|---:|
| Total person-minutes for first-time processing | 800 | 500, translation staff included |
| First-pass error count | 20 | 5 |
| Extra rework person-minutes per error | 10 | 10 |
| Recurring total person-minutes | **1000** | **550** |

One person working ten minutes, or two people each working five minutes, both count as ten person-minutes. That is labour input, not the applicant's waiting time on the calendar.

In this exercise, adding a layer actually uses 450 person-minutes less. If the first switchover costs another 120 person-minutes, the first-batch investment is 670 — still 330 less than direct connection. The answer holds only inside the stipulations; the real-world translation gains, maintenance costs and errors have to be measured separately.

That intermediaries or organisations may economise on coordination costs has long had research precursors. When Coase discussed why firms exist, he already brought the cost of using the price mechanism into the explanation. Renaming it "middleware" does not automatically add a discovery. [Coase, 1937, the original paper](https://msuweb.montclair.edu/~lebelp/coasenatfirmec1937.pdf)

If the engineering representation has added value, it should show up as readers finding omissions more easily and making fewer accounting mistakes — not merely sounding more impressive after a change of vocabulary.

## Providing a service does not mean you may monopolise the gate

Imagine two arrangements. One publishes the format, letting applicants fill it in themselves and letting others offer translation services; the other hides the format, rejects submissions without specific reasons, and forbids changing the handler.

Both may contain real labour. But the second also controls a gate: who qualifies to move to the next step is explained by him.

**Service function, control rights and where the money flows should be recorded separately.** The same intermediary can provide a useful service while using exclusive power to add burdens. High fees, a high position or centrality in the organisation cannot, on their own, complete a rent-seeking determination.

The Indian driving-licence study offers a concrete reminder: ease of obtaining the document and driving competence cannot be recorded as one item. Its agent-use analysis carries correlational evidence, with separate random incentives and audit visits; the several designs cannot be blended into "randomising people into using agents". [Bertrand et al., 2007, published version §IV–V](https://sendhil.org/wp-content/uploads/2019/08/Publication-44.pdf)

This makes us ask one more question: whom does an arrangement let get what, faster, and on whom does it leave the risk? That sentence is this article's analytical question, not a general conclusion generalised from that study.

The money also has to be put on separate ledgers. What an applicant pays the service provider is not the same thing as everyone concerned squandering an equal amount of resources for nothing. Service labour, transfer payments, waiting and risk each need their own records; fees cannot all be counted as losses, nor can unfairness and behavioural distortion be ignored just because the money merely changes hands.

## Some checks are worth keeping; some burdens need to be taken apart

A randomised-audit study of Indonesian road projects shows that added oversight is not bound to be pure loss. It also reminds us that converting oversight results into net gains takes additional assumptions. [Olken, 2007, research design and §VI](https://economics.mit.edu/sites/default/files/publications/Monitoring%20Corruption%20Evidence%20from%20a%20Field.pdf)

This does not endorse every check. It demands that before deletion we first ask what the check provides. The positioning of the study's results and limits is in the [foreign-study check table](../../research/cases/II-INT_audit_and_driving_license_research_check.md).

Another piece of Chinese material comes from a 2024 public notification, concerning PipeChina's insufficient meeting coordination and the burden of attending and sitting through meetings. It supplies a question worth investigating, not a set of work-hour data from which net loss could be directly computed. [Item 3 of part two of the officially reposted monthly report](https://lzw.cmc.gov.cn/pgt/art/2024/art_e7bb5788c0d94bed97af2f705c81e076.html)

So one can neither declare all meetings useful, nor multiply every meeting-hour by wages and call it waste. One still has to check duplicated coordination, effective decisions, follow-through, and whether more rework appears after cancellation.

Now the second **fictional exercise**: 100 applications originally took 600 person-minutes in total, 200 of them spent on repeated signatures. The stipulation is explicit: removing that signature loses no exclusive information or accountability, other checks and remedies remain, and the retooling costs 50 person-minutes once. Then the first batch is 450, and each batch thereafter 400.

Under these conditions, deletion has grounds. The hardest part in reality is precisely verifying those conditions — not computing 600 minus 200.

That a backup has never restored data to date does not prove it useless; that a gatekeeper claims to prevent disasters does not buy unlimited exemption from checks. Low-frequency losses, recovery capability and the people affected must enter the comparison. Protection conditions that cannot reasonably be converted into money can be listed separately as constraints.

## The prettiest optimisation may happen in the denominator

The third exercise is likewise a **fictional set-up**.

| Two batches | Before the change | After the change |
|---|---:|---:|
| Attempted applications | 100 people | 100 people |
| Entered registration | 100 people | 60 people |
| Completed on time and qualified | 90 items | 54 items |
| Total relevant labour of those registered | 900 person-minutes | 360 person-minutes |

The report can declare: after registration the qualification rate is 90% in both cases, and the input per registered application has fallen from 9 to 6 person-minutes.

But counting from the people who attempted, the share completing on time and qualified falls from 90% to 54%. Whether the other 40 met the criteria, where they dropped out, and how much time they spent is currently unknown; the migration cost is unrecorded too.

These numbers are not enough to determine the full net consequences of the change, still less to identify a causal effect. But they are already enough to stop us from declaring an overall efficiency gain on the strength of the registration report.

What some processes are best at optimising is optimising troublesome people out of the statistical scope. To judge whether a given reform did that, one still has to trace where those people went; a snappy one-liner cannot substitute for evidence.

## Put this checklist on the scale too

When you meet a suspicious gate, you can start by writing down six things:

- What it is doing; if it were deleted, who would take over, or why it would no longer be needed.
- On whom the inputs and the benefits each land.
- Who can refuse, interpret and change the rules, and how to exit or appeal.
- Besides keeping and demolishing, which other feasible alternatives exist.
- Whether the comparison covers the same needs, quality, period and recovery conditions.
- Which information is unknown; what evidence would make the writer change their verdict.

These questions also apply to this engineering vocabulary itself. If the word "middleware" makes it easier for readers to curse someone yet harder to see the work someone else carries, that expression needs repair.

To that end we provide the [OP-001 question card](../../research/OP-001/question_card.md): compare the engineering checklist against ordinary cost and process checklists carrying the same information, and see whether readers really make fewer mistakes. At present there is only the design and publicly disclosed fictional material; **there are no experimental results, and no formal pre-registration**.

You can do just one small thing: point out which condition an exercise is missing; supply an equivalent or better existing study; or contribute a historical record that can trace where registration work went. Null results, counterexamples and factual corrections can all change later versions — you do not have to subscribe to "Socio-Protocolics" first.

<a id="article-framework"></a>

## Endnote: which principles this article uses, and what it does not prove

This article belongs to the second group's themes in the [Socio-Protocolics Whitepaper v11.2](../../whitepaper/chapter-01.md). **P1** supplies the finite-resource background; **P2** reminds us participants have their own goals; P3's belief updating or equilibrium is not tested in this article. **O4 Middleware** is used to distinguish translation, certification and oversight functions from exclusive control.

The main use is the applicability boundary of [SP-RFC-004](../../whitepaper/chapter-03.md#sp-rfc-004): where new services or recovery gains exist, a serial-loss formula cannot be applied by layer count alone; the person-minute exercises in this article plug nothing into that formula. [SP-RFC-005](../../whitepaper/chapter-03.md#sp-rfc-005) supplies the to-be-tested risk questions of service, authority and rent; this article has not identified the causal feedback of "complexity and rent-seeking reinforcing each other".

[SP-RFC-007](../../whitepaper/chapter-03.md#sp-rfc-007) states the normative objective chosen by this article: reduce useless burden, protect rights and keep error correction. [SP-RFC-017](../../whitepaper/chapter-07.md#sp-rfc-017) is used to distinguish switching from continuing investment; no net-present-value accounting of a real process has been completed. The stage paths of the candidate process diagram (non-numbered material), 005's long-run closure and 006's deadline mismatch have not been tested by this article, and the other proposition groups cannot be counted as proven on that account either.

The existing literature supports each of its own narrow claims; the author's mapping of where the work went onto interfaces and middleware is an analytical arrangement. **This article shows how to raise questions; OP-001 tests whether this way of expressing them has any local use; neither can substitute for testing the framework as a whole.** For source versions, reading scope and item-by-item correspondences see the [source notes](source_notes.md), and for this round's changes the [revision notes](revision_notes.md). Chinese first; the English version has not yet been produced.
