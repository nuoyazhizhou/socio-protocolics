> **Translation record**
> - Chinese source: `articles/hai-rui/来源说明.md` (sha256 `e6038fcdfd498510748b50e5c9cf7b0b322d18c7a23d9df9b150e1fe4546ca68`, `13878` bytes, 2026-11-10)
> - Chinese version / release tag: `v0.1` (theoretical version remains v11.2)
> - Translation version: `en-v0.1`
> - Translation date: 2026-11-10
> - Check status: checked sentence by sentence against the Chinese source for claim status, negative guardrails and numbering; machine and glossary checks only; no independent professional native-speaker review
> - Pending sync: synchronized in public-files.json and mkdocs.yml
> - Status: complete translation
> - Authority: the Chinese SSOT is authoritative; this translation does not constitute a separate set of definitions (C2)

# Hai Rui & Ming Fiscal Intermediaries: Source Notes, Sandbox Boundaries, and Proposition Testing Receipt

Version: v0.1 | Date: 2026-11-10 | Companion to [*Why Couldn't Even Hai Rui Defeat the County Clerks?*](why_hai_rui_could_not_defeat_county_clerks.md); complete English translation of `articles/hai-rui/来源说明.md`.

Compiled under [Case-Driven Writing and Proposition Testing](../../CASE_DRIVEN_TESTING.md) and [AGENTS.md Red Lines 8 & 9](../../AGENTS.md), this document provides the provenance of historical sources cited in the main text, competing historiographical explanations, reproducible pointers for the Socio-Engine sandbox runs, and the mandatory Proposition Testing Receipt.

---

<a id="historical-sources"></a>

## 1. External Historical Sources & Evidence Boundaries

| Main Text Section | Source, Edition & Location | Substantiated Historical Scope | Prohibited Extrapolation Boundary |
| :--- | :--- | :--- | :--- |
| **§1. The 1577 "Book of Silk" Dispute** | 1. Cheng Renqing (ed.), *The Book of Silk* (*Sijuan Quanshu*, Ming Wanli woodblock edition, 16 vols., preserving all official dispatches, plaints, and ledger audits of the 1577 Shexian silk tax dispute);<br>2. Ray Huang (1974), *Taxation and Governmental Finance in Sixteenth-Century Ming China* (Cambridge University Press), Ch. 3;<br>3. Ray Huang, *1587, A Year of No Significance*, Ch. 5 ("Hai Rui: The Eccentric Model Official") and related notes. | Huizhou Prefecture owed an annual quota of 8,780 bolts of "head-tax silk" to the Nanjing Ministry of Revenue (commuted at 0.7 taels per bolt, totaling 6,145.3 taels of silver); this burden was borne solely by Shexian for decades; in 1577 (Wanli 5), licentiate Shuai Jiamo cross-checked the *Da Ming Huidian* and old gazetteers, exposed the allocation error, and petitioned higher authorities, resulting in partial relief, inter-county reallocation, and the printing of *The Book of Silk*. | Shuai Jiamo audited macro inter-county quota allocation, not a plot-by-plot resurvey of every household; printing *The Book of Silk* publicized the macro dispute but did not eradicate micro-level *feisa* tax scattering inside rural *lijia* units. |
| **§1. Shexian Cadastral Survey & Single-Whip Tax Slips** | 1. Wanli *Shexian Gazetteer* (*Shexian Zhi*, 1612 edition, Vol. 4 *Fiscal Monograph*);<br>2. Chinese Academy of Social Sciences (CASS) Institute of History archival original: 1588 (Wanli 16) *Shexian Single-Whip Tax Slip* (*Tiaobian Youpiao*);<br>3. Liang Fangzhong, *Dynastic Land Tax and Household Statistics in China*, and Luan Chengxian, *A Study of Ming Yellow Registers*; summarized in [HISTORICAL_BASELINE.md](../../../socio_engine/docs/HISTORICAL_BASELINE.md). | Prior to Zhang Juzheng's 1581 (Wanli 9) survey, Shexian's registered land stood at ~420,000 *mu*; post-survey measured land reached 587,400 *mu* (+38%); the 1588 tax slip records statutory silver rates of 0.0801 taels/*mu* for paddy, 0.0474 for dry land, and 0.0331 for hills. | Newly surveyed acreage includes converted hill land and unit standardization, so the 167,400-*mu* increase cannot be attributed 100% to single-clerk embezzlement; high-resolution scans of the original woodblock pages remain open for collection on the [Open Evidence Wishlist](../../research/OPEN_EVIDENCE_WISHLIST.md). |
| **§2. Hai Rui's Reforms as Magistrate of Chun'an (1558–1562)** | 1. *Collected Works of Hai Rui* (*Hai Rui Ji*, Zhonghua Book Company punctuated edition, ed. Chen Yizhong, 1962/1981), Part I *Chun'an Administration* (*Xingge Tiaoli*, *Liangtian Zeli*);<br>2. *History of Ming* (*Ming Shi*), Vol. 226 *Biography of Hai Rui*. | As Magistrate of Chun'an, Hai Rui abolished customary meltage fees, brought his own dry rations on rural inspections, and enacted the *Rules for Land Measurement* (*Liangtian Zeli*) to personally supervise land surveys and deliver tax slips directly to *lijia* households. | Chun'an was a small, mountainous county in western Zhejiang; Hai Rui's local dis-intermediation achieved through extraordinary personal exertion cannot be extrapolated as a low-cost template for major Jiangnan fiscal prefectures. |
| **§2. Hai Rui's Stalled Governorship in Yingtian (1569–1570)** | 1. *Hai Rui Ji*, Part I *Governor Administration* (*Dufu Tiaoyue*);<br>2. *Ming Shi*, Vol. 226 *Biography of Hai Rui*;<br>3. Ray Huang, *1587*, Ch. 5. | As Governor of Yingtian (overseeing ten Jiangnan prefectures), Hai Rui issued the *Dufu Tiaoyue* ordering gentry to return encroached lands, prompting thousands of daily petitions and passive resistance from gentry and clerks; impeached by Censor Dai Fengxiang after eight months and transferred out, with his land-return orders collapsing. | Serves as the core **real same-case counter-observation**: proves that without a scalable technical bureaucracy and public accounting infrastructure, relying on executive willpower alone to shock entrenched intermediary networks triggers severe administrative overload and systemic pushback. |

---

<a id="competing-explanations"></a>

## 2. Real Counter-Evidence & Competing Academic Explanations

| Explanatory Lens | Representative Scholarship | Core Argument | How This Study Incorporates & Distinguishes It |
| :--- | :--- | :--- | :--- |
| **Competing Explanation A: Lack of Numerical Management** | Ray Huang (1974, 1981) | Ming fiscal disorder stemmed from the empire's lack of modern currency, banking, commercial law, and statistical survey capacity, leading the state to substitute moral exhortation for technical management. | Fully endorsed as the macro institutional backdrop; protocolics further decomposes this into an operational micro-mechanism: where macro statistical infrastructure is absent, grassroots administration inevitably evolves privatized `O4 Middleware` (clerk secret books) to bridge the translation gap. |
| **Competing Explanation B: Starvation Wages & Office Budget Compensation (Key Counter-Constraint)** | Ming-Qing fiscal and sub-bureaucracy scholarship (e.g., Miao Quanji, *Ming Clerks*; Zhou Baoming on county public expenses; Qing Yongzheng *Huohao Guigong* archives) | Ming officials received minimal statutory pay, clerks were unranked and virtually unpaid, and the central treasury did not fund local paper, ink, runners, or silver transport. Thus, a substantial portion of local *huohao* meltage fees actually funded **essential county office operations**. | Directly constrains the application boundary of `SP-RFC-004`: **one cannot treat 100% of meltage fees as pure parasitic loss**. If a reformer bans surcharges to zero without providing legitimate budgetary replacement (such as Qing Yongzheng's *Huohao Guigong & Yanglian Silver*), normal administrative translation inevitably stalls. |

---

<a id="sandbox-boundary"></a>

## 3. Socio-Engine Sandbox Parameters & Epistemic Demarcation

The four multi-agent experimental runs cited in the main text are stored in the repository's open-source `socio_engine/database/socio_sim.db` (SQLite WAL ledger). Any researcher can run `python socio_engine/scripts/inspect_hai_rui.py` or `query_experiments.py` to independently verify them:

| Experiment Label | Database `Run ID` | Configuration File | Epistemic Status & Strict Limits |
| :--- | :--- | :--- | :--- |
| **Exp A (Contradictory Bureaucratic Mandate)** | `run_52ed940d` | `sim_config_mandate_conflict.yaml` | **Counterfactual Computational Simulation**: Simulates a standard magistrate demanding full quota delivery while nominally banning surcharges, illustrating *feisa* burden-shifting and high peasant flight (40.0%). |
| **Exp B (Hai Rui Baseline Purge)** | `run_2df8b194` | `sim_config_hai_rui.yaml` | **Counterfactual Computational Simulation**: Simulates abolishing surcharges + granary relief, illustrating the Q2–Q3 clerk work-to-rule strike response. |
| **Exp C (Hai Rui Dis-intermediation Breakthrough)** | `run_e422c3a8` / `run_cf7532c3` | `sim_config_hai_rui.yaml` | **Counterfactual Computational Simulation**: Simulates triggering `RECRUIT_NEW_CLERKS` in Q4 (recruiting poor scholars to take over bookkeeping) and confiscating prior illicit surcharge rents in Q5–Q6, demonstrating how alternative routing + rent recovery raises treasury silver to 2,201.1 taels with 0% flight. |
| **Exp D (Anonymized Empire Ablation)** | `run_360a05ed` | `sim_config_anonymized.yaml` | **Counterfactual Computational Simulation (Ablation Test)**: Strips all historical semantic labels ("Ming, Hai Rui, Huizhou"), yielding final treasury silver of 2,051.6 taels, 0.0 *mu* abandoned land, 0.0% flight (with tailwater peasant bankrupt and two households reduced to zero cash), 45.0% unrest risk, and 1.43 institutional entropy, while intermediary nodes (`clerk_qian` 270.0 taels, `clerk_crime_ma` 185.0 taels) spontaneously extract heavy rents—verifying that dynamics are driven by underlying Rust privilege rings and double-entry conservation rather than LLM historical memorization. |

> **Iron Rule Reaffirmed**: Historically, Hai Rui never served as Magistrate of Shexian. Placing Hai Rui's strategies into the 1575 Shexian cadastral baseline is a **counterfactual institutional stress test**. Silver figures, flight rates, and entropy scores produced by the sandbox are model demonstrations and **never constitute empirical Ming historical data**.

---

<a id="whitepaper-mapping"></a>

## 4. Itemized Correspondence with *Socio-Protocolics Whitepaper v11.2*

| Whitepaper Entry | How Used in This Essay | Epistemic Identity | Untested or Uncovered Aspects |
| :--- | :--- | :--- | :--- |
| **[SP-POSTULATE-1](../../whitepaper/chapter-01.md#sec-1-5)** / **[SP-POSTULATE-2](../../whitepaper/chapter-01.md#sec-1-5)** | The magistrate has finite cognitive bandwidth (cannot manually compute 26,800 household accounts); clerks, gentry, and village heads optimize private utilities $U_i$. | First-Order Postulates (Modelling Background) | Does not directly test mathematical existence or convergence of P3 belief distributions. |
| **[O4 Middleware](../../whitepaper/chapter-01.md#-04-协议学核心对象模型与公理体系layer-2-theoretical-primitive-spec)** | Maps county revenue clerks as translation and certification intermediaries between the court/magistrate and rural households. | Core Object Primitive | Acknowledges that clerks also possess lineage and marriage network ties, not reducing them to stateless software. |
| **[SP-RFC-004](../../whitepaper/chapter-03.md#sp-rfc-004)** | Tests its applicability condition: because clerks perform essential silver-conversion and register-compilation services (productive contribution), one cannot naively apply a pure-loss "fewer layers is always better" deduction. | Conditional Proposition | Does not fit historical data to the exponential attenuation parameter $\eta_k$. |
| **[SP-RFC-005](../../whitepaper/chapter-03.md#sp-rfc-005)** | Analyzes how clerks manufacture interpretive monopoly and extract rents via complex conversion categories (*feisa*, *guiji*, private ledgers). | Empirical Mechanism Hypothesis | Qualitative process tracing and sandbox mechanism demonstration only; no cross-county econometric regression. |
| **[SP-RFC-007](../../whitepaper/chapter-03.md#sp-rfc-007)** | Derives the "5-Step Checklist": before stripping rent-seeking power, one must specify who takes over productive work and how essential office costs are funded. | Cross-Group Normative Rule | Normative operational guideline, not an objective physical law. |
| **[SP-RFC-011](../../whitepaper/chapter-05.md#sp-rfc-011)** / **[SP-RFC-014](../../whitepaper/chapter-05.md#sp-rfc-014)** | Analyzes Shuai Jiamo's "bypass verification" via the *Da Ming Huidian* and "ledger split-brain" caused by distorted official registers. | Group IV Conditional Proposition / Mechanism Hypothesis | Does not test modern cryptographic certificate revocation or multi-sig mechanisms. |
| **[SP-RFC-017](../../whitepaper/chapter-07.md#sp-rfc-017)** | Highlights transition costs of replacing bookkeeping staff, resurveying land, and printing tax slips. | Group VI Accounting Definition | Does not compute a monetized lifecycle Net Present Value (NPV) for the 1581 cadastral survey. |

---

<a id="proposition-receipt"></a>

## 5. Proposition Testing Receipt

In accordance with [Case-Driven Writing and Proposition Testing](../../CASE_DRIVEN_TESTING.md), the verdict and the separate checks for **necessity, sufficiency, and minimality** are registered below:

| Sub-Claim & SSOT Location | Supporting & Counter-Evidence, Location | Competing Explanations & Differentiation | Verdict & Boundaries (Necessity / Sufficiency / Minimality) | Intended Write-Back or Reason for No Change |
| :--- | :--- | :--- | :--- | :--- |
| **Sub-Claim**: When a grassroots intermediary (`O4`) combines productive accounting services with exclusive ledger interpretation power, relying solely on bans/punishments without alternative bookkeepers and public ledger interfaces (dis-intermediation) causes administrative paralysis or burden shifting; coupling alternative routing with public verification is required to suppress rent-seeking.<br>**SSOT Location**: [SP-RFC-004](../../whitepaper/chapter-03.md#sp-rfc-004), [SP-RFC-005](../../whitepaper/chapter-03.md#sp-rfc-005), [SP-RFC-007](../../whitepaper/chapter-03.md#sp-rfc-007) | **Supporting Evidence**:<br>1. Shuai Jiamo cross-checking the public *Da Ming Huidian* exposed the 6,145-tael inter-county silk tax error hidden by clerks for decades (HF-01~03);<br>2. Hai Rui personally supervising land measurement and issuing direct *youpiao* slips in small Chun'an County succeeded locally (HF-04);<br>3. Zhang Juzheng's 1581 survey rebuilding Fish-Scale registers and issuing *Single-Whip Youpiao* uncovered 38% hidden land in Shexian (HF-06).<br>**Counter / Limiting Evidence**:<br>1. As Governor of Yingtian across ten prefectures, lacking a scalable technical bureaucracy, Hai Rui's land-return orders triggered thousands of daily plaints, administrative overload, and removal after eight months (HF-05);<br>2. Ming meltage fees partially funded essential local office and transport costs left unpaid by the central budget (Competing Explanation B). | 1. **Ray Huang's "Lack of Numerical Management"**: Highly compatible; this study operationalizes it into "privatized state tables + absence of terminal verification interfaces";<br>2. **Fiscal History "Office Expense Compensation"**: Corrects the naive tendency to treat 100% of meltage fees as pure corruption, forcing dis-intermediation designs to include legitimate operational funding (Step 3 of Checklist). | **Overall Verdict**: **Partially Supported (subject to strict scale and budgetary boundaries)**.<br>- **Necessity (Checked)**: Where ledgers are complex and monopolized by clerks, providing an independent accounting team or public verification interface (*youpiao* / statutory cross-check) is a **necessary condition** to break informational hostage-taking (corroborated negatively by the Yingtian overload and Q2–Q3 sandbox strike);<br>- **Sufficiency (Checked & Unconditional Sufficiency Rejected)**: Executive iron willpower or a one-off survey is **not a sufficient condition**—if jurisdiction scale exceeds alternative staffing capacity (Yingtian case) or legitimate office expenses remain unfunded, reform stalls or rebounds;<br>- **Minimality (Pending Cross-Period Test)**: Whether directly replacing clerks (Hai Rui's Chun'an model) or retaining clerks while formalizing gray surcharges into statutory budgets (Qing Yongzheng's *Huohao Guigong & Yanglian Silver* model) incurs lower transition cost awaits comparative testing in task [`W-SIM-03`](../../research/OPEN_EVIDENCE_WISHLIST.md). | **No change to Whitepaper main text**.<br>Reason: Whitepaper v11.2's definition of `O4` and `SP-RFC-004/005/007` already distinguish productive coordination contributions from exclusive rent-seeking and incorporate transition-cost constraints (`RFC-017`). This case study substantiates and illustrates those boundaries without requiring changes to the canonical axioms. |

