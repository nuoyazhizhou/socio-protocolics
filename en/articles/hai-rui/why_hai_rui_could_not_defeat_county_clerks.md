> **Translation record**
> - Chinese source: `articles/hai-rui/为什么海瑞斗不过县衙老吏.md` (sha256 `12916ead49c343123983c35bf1bdd94b400d9e298d19ecd8881c8b82737e4c2f`, `23793` bytes, 2026-11-10)
> - Chinese version / release tag: `v0.1` (theoretical version remains v11.2)
> - Translation version: `en-v0.1`
> - Translation date: 2026-11-10
> - Check status: checked sentence by sentence against the Chinese source for claim status, negative guardrails and numbering; machine and glossary checks only; no independent professional native-speaker review
> - Pending sync: synchronized in public-files.json and mkdocs.yml
> - Status: complete translation
> - Authority: the Chinese SSOT is authoritative; this translation does not constitute a separate set of definitions (C2)

# Why Couldn't Even Hai Rui Defeat the County Clerks? — From the 1577 "Book of Silk" Tax Dispute to "Dis-intermediation" in a Rust + AI Sandbox

Version: Public Case & Sandbox Essay v0.1 | Date: 2026-11-10 | Complete English translation of `articles/hai-rui/为什么海瑞斗不过县衙老吏.md`.

Status: Supported by the [Project Registration & Proposition Testing Card](../../research/cases/II-CN-C_ming_huizhou_silk_tax_and_hai_rui_card.md) and [Sources & Epistemic Boundaries](source_notes.md). This essay takes the 1577 Huizhou "Head-Tax Silk" dispute and Hai Rui's local fiscal reforms in Ming China as its real historical backbone, paired with counterfactual mechanism simulations from our open-source [Socio-Engine Multi-Agent Sandbox](../../socio_engine/README.md). **All historical records and computational sandbox figures are explicitly separated; sandbox outputs are never presented as empirical historical measurements.**

---

There is a thousand-year-old proverb in Chinese bureaucratic history: **"The county yamen (office) is cast in iron; the magistrates flow like water."**

In Ming Dynasty China (1368–1644), a County Magistrate (*Zhixian*, seventh rank) was an elite scholar who had triumphed in the imperial civil service examinations, holding imperial commission as chief judge, tax collector, and administrator of 150,000+ subjects. By contrast, the revenue clerks (*Hufang Shuli*) working inside his yamen were unranked sub-bureaucrats barred from the civil service career path and forbidden even to wear official robes.

On paper, a magistrate disciplining a few county clerks should have been as effortless as a root administrator revoking a rogue user account.

Yet actual history ran in the opposite direction: most magistrates arriving at their posts dared not touch the veteran clerks and had to rely on them for daily operations. Even **Hai Rui (1514–1587)**—the Ming Empire's most famously incorruptible and fearless reformer—managed to hold his ground only through grueling personal exertion when governing tiny Chun'an County; when promoted to Governor of Yingtian (overseeing the empire's wealthiest Jiangnan region) and attempting to overhaul land and tax abuses at scale, he was bogged down by administrative overload and impeached within just eight months.

Why couldn't chief executives holding formal supreme authority defeat unranked grassroots clerks?

If we step outside the moral drama of "loyal officials vs. wicked clerks" and examine the system through the engineering primitives of *Socio-Protocolics*—**Middleware (`O4`), Ledger Split-Brain, Privilege Ring Isolation (`Ring-0~3`), and Dis-intermediation**—we uncover a classic architectural deadlock in distributed systems.

---

## 1. The Ledger the Magistrate Couldn't Read: The 1577 "Book of Silk" Dispute

Let us first return to Shexian County in Huizhou Prefecture during the fifth year of the Wanli Emperor (1577).

That year, Huizhou erupted in a massive tax protest known to historians as the **"Head-Tax Silk Dispute" (*Rending Sijuan An*)**. The complete official dispatches, plaints, and audit calculations of this conflict were compiled by Ming local scholar Cheng Renqing into a sixteen-volume work, *The Book of Silk* (*Sijuan Quanshu*), and analyzed in detail by historian Ray Huang in *Taxation and Governmental Finance in Sixteenth-Century Ming China* and *1587, A Year of No Significance*.[〔1〕](source_notes.md#historical-sources)

The origin of the dispute was straightforward: according to the imperial statutory code (*Collected Statutes of the Ming Dynasty* / *Da Ming Huidian*), Huizhou Prefecture—comprising six counties (Shexian, Xiuning, Wuyuan, Qimen, Yixian, and Jixi)—was required to deliver **8,780 bolts of "head-tax silk"** annually to the Nanjing Ministry of Revenue (commuted at 0.7 taels of silver per bolt, totaling **6,145.3 taels of silver**).

By statute, this burden was to be shared across all six counties according to registered male taxpayers. Yet for decades, when prefectural and county clerks compiled the decennial *Yellow Registers* (*Huangce*), they buried this 6,145-tael obligation inside a maze of complex conversion formulas and quietly **dumped the entire छह-county bill onto Shexian County alone**!

Then came the most astonishing fact: **for decades, neither the successive Prefects of Huizhou, nor the Magistrates of Shexian, nor the gentry and commoners of Shexian realized that the ledger had been rigged!**

Why did no one notice? Because Ming local tax books had long been turned by revenue clerks into a **proprietary black-box protocol** that outsiders could not decode:

1. **Nested Surcharges and Conversions**: Land was divided into upper, middle, and lower grades across paddy fields, dry land, hills, and ponds; taxes included summer wheat, autumn rice, horse fodder, and mulberry silk, split into in-kind (*bense*) and silver-commuted (*zhese*) rates, topped with "meltage fees" (*huohao*, charged for melting fractional silver into standard ingots) and "porterage/facilitation fees" (*pudian*);
2. **Fraudulent Registration (*Guiji*) and Tax Scattering (*Feisa*)**: Wealthy landowners registered their prime paddy fields under the names of tax-exempt degree-holders (*guiji*), or bribed clerks to alter "fertile paddy" to "barren hill" on the *Fish-Scale Map-Registers* (*Yulin Tuce*). How did the clerks plug the resulting tax shortfall? They sliced the missing quota into dozens of tiny fractions and silently scattered them (*feisa*) onto illiterate poor peasants and rotating village heads (*lizhang*).

In systems architecture terms:
- **The Imperial Court (`Ring-0`)** only issued macro county-wide quotas ("Shexian must remit 20,000 taels this year") and had no direct read/write channel to individual household land plots;
- **The County Magistrate (`Ring-1`)** served a three-to-six-year term, did not speak the local Huizhou dialect, and could not untangle a century of accumulated conversion formulas;
- **The Revenue Clerks (`Ring-2`, acting as `O4 Middleware`)** stayed in the yamen across generations, clutching the secret private ledgers (*miben*) that alone could execute the tax collection routine.

This produced severe **Ledger Split-Brain**: the official public registers (*Yellow Registers* and *Fish-Scale Map-Registers*) diverged wildly from physical reality. When Grand Secretary Zhang Juzheng ordered a national cadastral resurvey in 1581 (Wanli 9), Shexian's official pre-survey book listed **420,000 *mu*** of land, whereas the physical measurement uncovered **587,400 *mu***—a **38% ledger distortion rate** (+167,400 hidden *mu*)![〔2〕](../../../socio_engine/docs/HISTORICAL_BASELINE.md)

How was the 1577 silk tax discrepancy finally exposed?

It was uncovered neither by a Prefect nor by an Imperial Censor, but by **Shuai Jiamo**, a local Shexian licentiate (*shengyuan*) skilled in mathematics. Happening upon a printed copy of the imperial *Da Ming Huidian*, Shuai cross-checked its macro statutory quotas line by line against historical gazetteers and tax rolls, isolated the 6,145-tael inter-county accounting discrepancy from tens of thousands of numbers, and bypassed the county/prefectural clerks to petition the provincial governor and central ministry directly!

In computer engineering, what Shuai Jiamo executed is called **Bypass Verification**: when an intermediary layer monopolizes data interpretation, the only way to expose it is to obtain the top-level specification (*Da Ming Huidian*) and terminal collection records, recomputing the state outside the black box.

---

## 2. Why Simply Purging "Corrupt Clerks" Causes the System to Crash

If the clerks were so manipulative, why couldn't a newly arrived magistrate simply arrest all veteran clerks on day one and ban every single cent of "meltage fees" (*huohao*)?

That is the illusion popularized by costume dramas—and the exact analytical trap warned against by Proposition Group II ([SP-RFC-004](../../whitepaper/chapter-03.md#sp-rfc-004) and [SP-RFC-005](../../whitepaper/chapter-03.md#sp-rfc-005)) of *Socio-Protocolics*:

> **The same intermediary layer (`Middleware`) frequently bundles "indispensable productive translation services" together with "exclusive rent-seeking privileges."**

Under the Ming fiscal regime, county revenue clerks performed two fundamentally different functions at once:

| Dual Attributes of County Clerks | Concrete Actions | Engineering Protocol Nature |
| :--- | :--- | :--- |
| **① Productive Service Function** | Decomposing macro imperial tax quotas across 26,800 households and hundreds of thousands of plots; issuing notices, assaying silver, compiling registers, and organizing transport. | **Essential protocol translation & routing** (without which macro commands cannot be executed at the micro level) |
| **② Exclusive Rent-Seeking Power** | Hiding true ledgers at home; granting tax shelters (*guiji*) to those who paid bribes; scattering deficits (*feisa*) onto the powerless; levying arbitrary meltage surcharges (*huohao*). | **Parasitic rent extraction via exclusive interpretive monopoly** (manufacturing complexity to lock in irreplaceability) |

Even more critically, fiscal historians highlight a vital **countervailing institutional constraint**: Ming statutory salaries for magistrates and clerks were near starvation levels, and the central government **did not allocate adequate operational budgets for local county offices** (paper, ink, runners' rations, silver smelting loss, and armed escort costs all had to be raised locally).[〔3〕](source_notes.md#competing-explanations)

What did this mean? It meant that within the clerks' *huohao* surcharge, **one portion was actually the physical fuel keeping the yamen running (productive cost compensation), while the other portion was extortionate private rent**.

Now, suppose a righteous new magistrate arrives. Without securing a new operational budget or training an alternative bookkeeping team, he simply issues a blanket decree: **"Meltage fees are reduced to zero! Anyone collecting an extra copper coin will be prosecuted!"**

What happens next?

1. **Immediate Interface Paralysis (Work-to-Rule Strike)**: Veteran clerks rarely rebel openly; instead, they feign illness and stage a work-to-rule strike. They dump the tangled, century-old Fish-Scale registers onto the magistrate's desk: *"Your Honor is incorruptible; we humble clerks dare not touch the silver. Please calculate the silver conversions for all 26,800 households yourself!"* Even if the magistrate worked sleeplessly, one person could never compute 26,000 household accounts before the treasury deadline.
2. **How Did the Historical Hai Rui Respond?**
   - **In 1558 (Jiajing 37), Hai Rui became Magistrate of Chun'an County in Zhejiang**. Chun'an was a small, mountainous county. Hai Rui not only issued the *Regulations for Reform* (*Xingge Tiaoli*) abolishing customary meltage fees and bringing his own dry rations to the countryside, but crucially enacted the ***Rules for Land Measurement* (*Liangtian Zeli*)**—personally leading teams to survey plots, drawing simplified maps, and writing exact tax liabilities onto public slips (*youpiao*) delivered directly to *lijia* households.[〔4〕](source_notes.md#historical-sources) In short, Hai Rui avoided being hollowed out in Chun'an because he used extraordinary personal exertion to **act as an alternative accounting engine himself, achieving small-scale "dis-intermediation."**
   - **Yet in 1569 (Longqing 3), Hai Rui was promoted to Governor of Yingtian (overseeing ten major prefectures in Jiangnan, including Suzhou, Songjiang, Changzhou, and Huizhou)**. Facing Jiangnan's massive fiscal volume and deeply entrenched gentry-clerk networks, Hai Rui again tried to rely on executive iron willpower, issuing the *Governor's Statutes* (*Dufu Tiaoyue*) to force powerful families to return encroached lands. Immediately, three to four thousand petitions flooded his office every day; clerks and gentry staged coordinated strikes, and Hai Rui possessed no scalable technical bureaucracy capable of auditing tens of millions of *mu* across Jiangnan. Within eight months, Censor Dai Fengxiang impeached him for "abetting wicked commoners and persecuting the gentry." Hai Rui was transferred out, and his land-return orders collapsed immediately.[〔5〕](source_notes.md#historical-sources)

Hai Rui's local success in tiny Chun'an versus his eight-month deadlock in vast Yingtian forms a **real historical positive-and-negative comparison** within the career of a single reformer: **when system scale expands, unless the accounting and verification capacity monopolized by old intermediaries is extracted into a public, replaceable institutional interface, relying on a chief executive's personal morality and iron fist will inevitably be overwhelmed by middleware sabotage and information overload.**

---

## 3. Putting Hai Rui into a Rust + LLM Sandbox: Four Counterfactual Experiments

To visualize the mechanism bifurcation between "moral purge alone" and "purge coupled with dis-intermediation," we ran a controlled set of **counterfactual computational simulations** in our open-source **[Socio-Engine](../../socio_engine/README.md)** sandbox.

> ⚠️ **Epistemic Boundary Statement (Mandatory Reading)**:
> 1. Historically, Hai Rui never served as Magistrate of Shexian. Placing "Hai Rui-style governance strategies" into the authentic 1575 Shexian household, land-grade, and tax-rate baseline (see [HISTORICAL_BASELINE.md](../../../socio_engine/docs/HISTORICAL_BASELINE.md)) is a **counterfactual institutional stress test**;
> 2. The sandbox's physical core is enforced by native Rust (`socio_core`) with strict double-entry conservation (silver, grain, land) and `Ring-0~3` privilege ring gates, while the cognitive layer uses LLMs to drive multi-agent games among the Magistrate, Revenue Clerk Qian, Pawnshop Gentry Sun, Scholar-Candidate Household Wu, Rotating Village Head Zhao, and Tailwater Poor Peasant Li;
> 3. **All numerical results below are sandbox simulation outputs (fully reproducible via `Run ID` in `socio_engine/database/socio_sim.db`) designed to illustrate internal model causality, and must never be treated as empirical Ming historical measurements.**

Under identical initial physical resource pools (2,000 taels base treasury, identical statutory tax quotas, and identical drought shocks), we executed four 8-quarter (two-year term) comparative runs:

### 1. End-of-Term Macro Metrics Across the Four Experimental Runs

| Experiment Group & `Run ID` | Magistrate Strategy & Protocol Intervention | Final Treasury Silver | Official Land Abandonment (*mu*) | Peasant Flight Rate | Civil Unrest Risk Index | Qualitative Mechanism Outcome |
| :--- | :--- | :---: | :---: | :---: | :---: | :--- |
| **Exp A: Compromised Bureaucrat & Contradictory Mandate**<br>(`run_52ed940d`) | Issues contradictory orders ("meet full quota on time, yet nominally ban surcharges"), relying entirely on old clerks | 2,034.7 taels | 13.0 *mu* | **40.0%** | **83.0%** | **Grassroots Collapse**: Clerks scatter tax shortfalls onto village heads and poor peasants, triggering chain bankruptcies and riots |
| **Exp B: Hai Rui Iron-Fist Purge (Baseline)**<br>(`run_2df8b194`) | Q1 zero-surtax mandate + clerk audit + granary relief for drought victims | 2,170.3 taels | 0.0 *mu* | 0.0% | 19.0% | **Stabilized Base, Administrative Friction**: Cutting surcharges saves peasants, but triggers a clerk work-to-rule strike in Q2–Q3 |
| **Exp C: Hai Rui Dis-intermediation Breakthrough**<br>(`run_e422c3a8` / `cf7532c3`) | Zero-surtax + **Q4 recruiting poor scholars to take over bookkeeping (`RECRUIT_NEW_CLERKS`)** + Q5–Q6 confiscating illicit clerk/pawnshop rents | **2,201.1 taels** | **0.0 *mu*** | **0.0%** | **19.0%** | **Protocol Refactoring Success**: Alternative bookkeepers break clerk monopoly; illicit rents are recovered (Clerk Qian left with 6.24 taels) with zero flight |
| **Exp D: Anonymized Empire Ablation Test**<br>(`run_360a05ed`) | Strips all historical labels ("Ming / Hai Rui / Huizhou / Clerks"), keeping only abstract `Ring-0~3` and double-entry physics (standard governor without dis-intermediation) | 2,051.6 taels | 0.0 *mu* | 0.0%<br>(1 bankrupt / 2 cash-zero) | **45.0%** | **Ablation Verified**: Without historical prompts, intermediaries still spontaneously extract high rents (Clerk Qian amasses 270.0 taels, Clerk Ma 185.0 taels) and drive peasant bankruptcy, proving dynamics are driven by privilege ring topology |

### 2. Inside the Sandbox Logs: The Q2–Q4 "Clerk Strike" and Hai Rui's Breakthrough

In the execution logs of **Experiment C (`run_e422c3a8`)**, the interaction between the LLM agents and the Rust state machine captures a striking institutional game sequence:

- **Quarter 1 (Issuing `ZERO_SURTAX_POLICY`)**:
  The Hai Rui agent records in its internal reasoning log: *"Meltage surcharges scrape the marrow from the people's bones... Effective today, all meltage surcharges are abolished; anyone collecting a single extra copper coin shall be prosecuted without mercy."*
- **Quarters 2–3 (Middleware Counter-Attack: Six-Office Clerk Strike)**:
  Once meltage fees are forced to zero, Revenue Clerk Qian (`clerk_qian`) and Judicial Clerk Ma immediately trigger a passive sabotage strategy—halting ledger updates under the pretext of illness so that autumn tax collection will suffer a cliff-edge deficit in Q4, aiming to use the imperial *Kaocheng* (performance evaluation) law to oust Hai Rui.
- **Quarter 4 (The Turning Point: `RECRUIT_NEW_CLERKS` Dis-intermediation)**:
  Facing a paralyzed yamen, Hai Rui neither capitulates to the old clerks nor stops at verbal fury; instead, he invokes an institutional refactoring action:
  > **[Tick 4 Hai Rui Cognitive Log]**: *"The clerks of the Six Offices have collectively feigned illness to stall work, attempting to hold this magistrate hostage by paralyzing tax collection. I shall never compromise with corrupt clerks! I shall immediately recruit upright, impoverished licentiates from the county school and honest village elders as new clerks, personally instruct them in bookkeeping, and rebuild the administrative staff so that county finances and justice can no longer be hijacked."*
- **Quarters 5–6 (Liquidating the Rent-Seeking Coalition)**:
  Once the newly recruited student-bookkeepers restore basic ledger throughput, in Q5 and Q6 Hai Rui executes targeted asset forfeitures (`PURGE_CLERKS`) against "Revenue Clerk Qian and Pawnshop Gentry Sun" for proven prior surcharge embezzlement, returning hidden land and illicit silver to the public treasury. This preserves all five grassroots households from flight (**0.0%** flight rate) while raising final treasury silver to **2,201.1 taels**.

---

## 4. What Do Existing Historical Explanations Already Cover, and What Does Protocolics Add?

In accordance with our epistemic honesty rules, we must ask: **historians and economists have studied Ming clerks and Hai Rui for decades; does introducing the engineering vocabulary of *Socio-Protocolics* actually add analytical value?**

Let us first place the two classic historiographical explanations on the table:

1. **Ray Huang's "Lack of Numerical Management" Thesis**: The Ming state centralized power prematurely without modern banking, statistics, insurance, or commercial law, forcing it to substitute moral exhortation for technical administration (*1587, A Year of No Significance*).
2. **The Fiscal History "Starvation Wage & Office Budget Deficit" Thesis**: By barring clerks from regular civil service promotion and starving local yamens of statutory operating funds, the Ming fiscal system structurally forced counties to rely on informal *huohao* surcharges to pay for paper, runners, and silver transport—a deadlock only partially resolved in the Qing Dynasty when the Yongzheng Emperor enacted ***Huohao Guigong* (formalizing meltage fees into public revenue to fund statutory *Yanglian* anti-corruption stipends)** in 1724.

**So what does mapping this phenomenon onto `O4 Middleware` and `Ring-0~3` Privilege Rings add?**

Simply renaming "county clerk" to `Middleware` would be a zero-gain word game. The true analytical gain of the engineering protocol lens is that it enforces an **operational, auditable, anti-omission "Dis-intermediation Engineering Checklist."**

Whether you are analyzing an ancient fiscal reform, merging two departments in a modern tech company, or cutting approval windows in a municipal government, whenever you touch an intermediary layer, this framework forces you to complete the following **Five-Step Diagnostic Table** first:

### 🛠️ Actionable Tool: The 5-Step Middleware Reform Checklist

| Diagnostic Step | Concrete Question You Must Answer | Corresponding Lesson from Ming Fiscal Reform |
| :--- | :--- | :--- |
| **1. Unbundle Service from Privilege** | Beyond rent-seeking at the chokepoint, what **real data translation, validation, and logistics work** does this intermediary currently perform? | Although clerks embezzled meltage fees, they also performed the real arithmetic of decomposing quotas across 26,800 households. |
| **2. Build Alternative Routing** | Once you remove or bypass the intermediary, **who takes over the productive bookkeeping, and do they have sufficient compute/staffing capacity?** | In tiny Chun'an, Hai Rui could calculate ledgers himself and recruit local students; across ten Jiangnan prefectures in Yingtian, lacking a scalable alternative team meant drowning in thousands of daily petitions. |
| **3. Fund the Physical Fuel** | Did part of the informal fee actually subsidize **essential operating costs** of the system? | Banning surcharges to zero without providing statutory office funding starves the yamen of paper and transport funds (which Qing Yongzheng later addressed via *Yanglian* stipends). |
| **4. Open Terminal Verification Interfaces** | Can terminal users (`Ring-3`) independently verify rules and bills without going through the intermediary? | Shuai Jiamo cross-checking the public *Da Ming Huidian* and Zhang Juzheng issuing direct *Single-Whip Youpiao* slips to households both opened terminal verification interfaces. |
| **5. Watch for Burden Shifting** | After the reform, did the terminal user's total burden (money + time + rejection risk) genuinely fall, or merely change disguises? | If old clerks are replaced by new land surveyors who demand a "measurement fee," the reform fails the net burden test ([SP-RFC-017](../../whitepaper/chapter-07.md#sp-rfc-017)). |

---

## 5. Join the Experiment: Run the Sandbox, Critique the Claims, or Contribute Archives

This essay is not an announcement that "we have proved Ming history with a computer." Instead, it lays **historical archives, protocol models, and a runnable code sandbox** openly on the table, inviting you to test, critique, and extend them:

1. **Want to modify Hai Rui's decrees yourself, or simulate Wang Anshi's Song Dynasty reforms?**
   - Clone our open-source [Socio-Engine Simulation Sandbox](../../socio_engine/README.md) and edit `socio_engine/roles/magistrate_hai/system_prompt.md` or the YAML configs;
   - Or use our [Universal Scenario Prompt Template](../../../socio_engine/docs/UNIVERSAL_SCENARIO_PROMPT_TEMPLATE.md) to compile **Northern Song Wang Anshi's Green Sprouts Law (`W-SIM-01`)**, **Tang Dynasty Yang Yan's Two-Tax Law (`W-SIM-02`)**, or **Qing Dynasty Yongzheng's *Huohao Guigong* (`W-SIM-03`)** into a runnable multi-agent sandbox!
2. **Have access to Ming local gazetteers, Yellow Registers, or original woodblock scans of *The Book of Silk*?**
   - Visit our [Open Evidence & Material Wishlist](../../research/OPEN_EVIDENCE_WISHLIST.md) to claim an archival task or point out any historical inaccuracies in this essay. Every verified correction or counterexample will be credited by name in the whitepaper and revision logs.

---

<a id="article-framework"></a>

## Endnote: Which Socio-Protocolics Provisions This Essay Uses—and What It Does Not Prove

This essay belongs to the cross-group special topic linking **Group II (Intermediary Parasitism & Compatibility Decay)** and **Group IV (Privilege Ring Isolation & Split-Brain Contagion)** of the [*Socio-Protocolics Whitepaper v11.2*](../../whitepaper/chapter-01.md):

1. **Postulate Background**: Uses **[SP-POSTULATE-1](../../whitepaper/chapter-01.md#sec-1-5)** (finite cognitive bandwidth and administrative resource bounds: a magistrate cannot manually compute tens of thousands of household accounts alone) and **[SP-POSTULATE-2](../../whitepaper/chapter-01.md#sec-1-5)** (self-gaming agents: clerks, gentry, and village heads pursue private utilities $U_i$ and survival thresholds).
2. **Core Primitives & Propositions**:
   - Uses **[O4 Middleware](../../whitepaper/chapter-01.md#-04-协议学核心对象模型与公理体系layer-2-theoretical-primitive-spec)**, **[SP-RFC-004](../../whitepaper/chapter-03.md#sp-rfc-004)**, and **[SP-RFC-005](../../whitepaper/chapter-03.md#sp-rfc-005)** to separate the clerks' "productive bookkeeping translation service" from "exclusive ledger interpretation rent-seeking";
   - Uses **[SP-RFC-007](../../whitepaper/chapter-03.md#sp-rfc-007)** (cross-group normative rule) to formulate the architectural guideline that stripping exclusive monopoly requires building alternative routing and compensating necessary operating costs;
   - Uses **[SP-RFC-011](../../whitepaper/chapter-05.md#sp-rfc-011)** and **[SP-RFC-014](../../whitepaper/chapter-05.md#sp-rfc-014)** to analyze Shuai Jiamo's "bypass verification" via the *Da Ming Huidian* and "ledger split-brain" caused by register distortion;
   - Uses **[SP-RFC-017](../../whitepaper/chapter-07.md#sp-rfc-017)** to highlight transition costs during cadastral surveys and staff replacement.
3. **Epistemic Boundaries & Untested Items**:
   - Historical sources substantiate the 1577 Shexian silk tax dispute and the contrasting outcomes of Hai Rui's Chun'an magistracy versus his Yingtian governorship;
   - The four `Socio-Engine` experimental runs are **counterfactual multi-agent simulations** calibrated on historical baseline parameters, illustrating internal model logic rather than econometric causal identification of Ming macro-history;
   - This essay does not fit historical parameters to the exponential attenuation formula of `SP-RFC-004`, nor does it claim that all provisions of Groups II and IV are empirically proved.
4. **Companion Files**: Full archival citations, sandbox `Run ID` parameters, and the Proposition Testing Receipt are documented in [Sources & Boundaries](source_notes.md), version history in [Revision Notes](revision_notes.md), and the project registration card in [II-CN-C Project Card](../../research/cases/II-CN-C_ming_huizhou_silk_tax_and_hai_rui_card.md).

