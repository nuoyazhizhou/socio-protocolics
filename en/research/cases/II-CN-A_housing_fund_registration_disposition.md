> **Translation record**
> - Chinese source: `research/cases/II-CN-A_住房公积金登记工作去向.md` (sha256 `d9d1de2e850bf5e10d80f6fe2425a87cfa983cb43546a27e04f583bfc69caea8`, `7459` bytes, 2026-11-09)
> - Chinese version / release tag: `v11.2-r20261106` (theoretical version remains v11.2)
> - Translation version: `en-v0.1`
> - Translation date: 2026-11-09
> - Check status: checked sentence by sentence against the Chinese source for claim status, negative guardrails and numbering; machine and glossary checks only; no independent professional native-speaker review
> - Pending sync: pending registration in public-files.json / mkdocs.yml
> - Status: complete translation
> - Authority: the Chinese SSOT is authoritative; this translation does not constitute a separate set of definitions (C2)

# II-CN-A: The Disposition of New-Employer Housing-Provident-Fund Contribution Registration

Version: material table v0.1 | Date: 2026-10-23 | Chinese original; English translation pending.

Identity: a retrospective collation of institutional texts, not a field investigation, an estimate of reform effect, or a pre-registration. The result status is "the integration arrangement is checkable, but actual cost and effect are undetermined." To avoid blending different cities into one, this round does not fill in the actual number of in-person trips for the whole of Zhejiang; the next actual operation must select one city and a window for which records can be obtained.

## I. Fixed object

| Item | Scope this round |
|---|---|
| Matter | New-employer housing-provident-fund contribution registration, item 4 of the first batch of the 2017 integration list |
| Institutional window | The provincial design effective 2017-07-01; the old side takes the regulation's Articles 13 and 14 as carried in State Council Decree No. 350 as the normative baseline |
| End point | The employer's registration information is claimed, recorded, and checkable by the competent agency; the specific business-system status name is to be supplemented |
| Exclusion | Do not count the employee's individual account opening, actual payment, withdrawal, loan, or other certificate matters as this matter's completion |
| Population / denominator | In future should cover all newly-established employers within the same service scope that meet the applicable conditions, and distinguish attempt, registration, completion, and exit; this round has no quantity data |
| Selection rationale | The matter is locatable in the original appendix and conveniently exposes the judgement risk that "front-end integration ≠ all back-office business completed"; the reform direction is known, not a blind pick |

## II. Source chain and versions

- **Z1: The 2017 provincial original PDF.** [Zhejiang Zheng Ban Fa [2017] No. 53](https://zjjcmspublic.oss-cn-hangzhou-zwynet-d01-a.internet.cloud.zj.gov.cn/jcms_files/jcms1/web3096/site/zfxxgkold/170713100118017.pdf), tool report 12 pages. The extractable notice body and Appendix 1 item 4 (PDF p. 7) have been read; Appendix 2 operational procedures were checked this round via Z2. The original body is dated 2017-06-16; Z2's operational procedures separately list 2017-06-20, the original's final-page issuance column was not independently eye-checked, and the two are not to be conflated with the web publication date. Subsequent direct download and screenshot timed out; no claim is made of a complete page-by-page verification of the original images.
- **Z2: A same-text reprint.** [National Development and Reform Commission reprint page](https://www.ndrc.gov.cn/xwdt/ztzl/gdqjcbzc/zejiang/201807/t20180704_1209490.html), web-published 2018-07-04; the body and operational procedures have been read. It and Z1 are one document source chain and do not count as independent effect evidence. The page does not expand Appendix 1's table, so item 4 cannot be confirmed from that page alone.
- **Z3: The old-norm text.** [The State Council Decree No. 350 "Housing Provident Fund Management Regulation" as carried on the Shanghai Municipal Government website](https://www.shanghai.gov.cn/nw4544/20200905/0001-4544_302.html); the title and Articles 12–15, 34–36 have been checked. Its Article 14 still contains the expression that, holding the management-centre review document, one goes to the entrusted bank to handle the employee account; it is used only as a source for the 2002 revised text, and the reprint-page date is not used to call it a 2020 newly-added institution. This table discusses historical design, not a current business-handling guide.

## III. Item-by-item facts and explanations

| Code | Checkable narrow claim | Location | Identity and limits |
|---|---|---|---|
| ZF1 | The new-employer registration matter is listed in the first integration batch | Z1 Appendix 1 item 4 | Institutional scope, not that every employer actually completed it |
| ZF2 | The reform design is window acceptance, data flow, departmental claiming, and supervision | Z1 Part III (2)(3), Appendix 2; Z2 same passages | A provision, not a back-office man-hour measurement |
| ZF3 | The old text distinguishes the employer registration from the employee-account procedures | Z3 Articles 13, 14 | Normative baseline, insufficient to reconstruct some city's old-window material list, online channels, and number of trips |
| ZF4 | The operational procedures provide for material correction, non-conforming feedback, and change/cancellation handling | Z1 Appendix 2 | An exception-handling design exists; actual return and correction effect to be checked |
| ZM1 | The change can be expressed as front-end interface integration and back-office work reallocation | This table's explanation of ZF1–4 | The author's engineering mapping; an existing process analysis could also express it, not an independent finding |

## IV. Old and new flows: draw only the known parts

The old side has only normative requirements:

```text
Newly-established employer → handles unit contribution registration at the provident-fund management centre
             └→ employee-account-related procedures are separate (not counted by this table as unit registration)
The specific city's acceptance channels, materials, round trips, internal handling, and exception flow: to be supplemented
```

The new side is the 2017 provincial design, not an execution log:

```text
Applicant declares per the list → comprehensive/industry-and-commerce window accepts, reviews, and enters
                     ↓
               Information-sharing platform → relevant departments claim and handle per their duties
                     ↓
               Confirmation of actual completion of the provident-fund registration business: municipal procedures and records to be supplemented
Material correction, feedback, update, and legacy-record linking: check separately
```

One must not auto-encode "data has been pushed" as "registration completed," nor treat the provincial reform's start date as all municipal systems having simultaneously completed go-live verification.

| Work to trace | Old side known/unknown | New side known/unknown | What is needed to compare |
|---|---|---|---|
| Information provision and duplicate filling | Old application fields and labour unknown | Unified-declaration design checkable; actual fields and re-filling unknown | Same-city before/after guides, forms, and de-identified application records |
| Transcription and matching | Bearer and errors unknown | Window, platform, and claiming duties checkable; actual interface and manual re-entry unknown | Field dictionary, claiming status, and failure-retry records |
| Review and protection | Normative duties checkable; actual execution unknown | Supervision not cancelled; actual inspection quality unknown | Acceptance rules, error and missed-registration review records |
| Change/cancellation and exception items | Same-city old flow unknown | Provincial operational procedures have arrangements; business-linkage effect unknown | Actual handling trails of change/cancellation/duplicate-name/field-mismatch etc. |
| Migration and maintenance | Persistent old burden unknown | One-time retrofitting, training, dual-track, and maintenance investment unknown | Man-hours and spending apportioned by agent, with clear shared-cost allocation |
| People who never entered registration | Need, validity unknown | Unregistered, exited, and barriers unknown | Same-service-scope population and traceable exit reasons; unknowns not counted as zero |

## V. Opposing material and competing explanations

This round obtained no field material confirming that this matter's burden rose, nor independent records confirming that net burden fell. The two absences cannot be offset against each other or used as favourable evidence.

Subsequently proactively seek three kinds of material that would force a narrowing of the judgement: data-claiming failure causing a second submission; window reduction but back-office rework or increased burden on disadvantaged applicants; the original flow already providing an approximately convenient function. Correspondingly, if same-calibre total investment falls while quality, accessibility, and correction are maintained, that supports a local improvement of this matter, not directly "fewer intermediaries is always better."

Competing explanations include unified identification, shared data, personnel training, online handling, contemporaneous demand structure, and other reforms. These may act together. From a single document containing multiple measures one cannot separate their respective effects, nor attribute all results to "protocol change."

## VI. The first deliverable that can be submitted

Select one Zhejiang city for which historical procedures can be obtained, and supplement the three materials "pre-reform guide — 2017 municipal implementation procedure — result-status definition" with their versions and sources; do not estimate savings for the time being. If no usable historical material exists, simply return the gap and the access result; do not pass off today's handling guide as the 2017 flow.

Minimum fields to collect: matter / city / rule version, anonymised business number, applicable eligibility, first attempt / registration / completion time, per-agent handling and rework person-minutes, correction reason, claiming/matching status, exit reason, quality review, and one-time migration investment. The above are field specifications, not an already-existing open dataset, and no acquisition is promised.

The link to the [article](../../articles/intermediary/two_approvals_removed.md) is a disposition; the link to [OP-001](../OP-001/question_card.md) is a judgement omission. This case was not used to estimate the SP-RFC-004 loss rate, the SP-RFC-005 rent, or the SP-RFC-017 net present value.
