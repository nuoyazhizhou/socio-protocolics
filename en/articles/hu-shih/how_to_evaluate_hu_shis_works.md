> **Translation record**
> - Chinese source: `articles/hu-shih/如何评价胡适的作品.md` (sha256 `337c2d879e174a049ccd381fab3861e29d96c7146e7e6c44a80bd06478a9327e`, `33291` bytes, 2026-11-09)
> - Chinese version / release tag: `v11.2-r20261106` (theoretical version remains v11.2)
> - Translation version: `en-v0.1`
> - Translation date: 2026-11-09
> - Check status: checked sentence by sentence against the Chinese source for claim status, negative guardrails and numbering; machine and glossary checks only; no independent professional native-speaker review
> - Pending sync: pending registration in public-files.json / mkdocs.yml
> - Status: complete translation
> - Authority: the Chinese SSOT is authoritative; this translation does not constitute a separate set of definitions (C2)

# How to Evaluate Hu Shi's Works? First Separate "How Well It Is Written" from "What It Changed"

When many people bring up Hu Shi (胡适, 1891–1962, writer and a leading advocate of vernacular Chinese), all that is left in the end is one sentence: "the man who championed vernacular Chinese."

That is not wrong, but it compresses something very difficult into a slogan.

Another kind of assessment starts from Changshi ji (《尝试集》, *Experiments*): these poems may not move readers today, and compared with some famous later works of new poetry they are not mature enough. The conclusion follows: Hu Shi's works are nothing special, and his importance has probably been exaggerated.

What I want to take apart is precisely this leap.

**How well the works are written can of course be assessed; but to judge what a person changed, this one ruler is not enough.**

Below I borrow some engineering concepts to look at the problem in separate pieces. The "protocol", "decoder" and "migration" here are analytical tools: they help us see who can take part, who bears the cost of understanding, and what is allowed into formal settings. They do not replace literary judgement, nor do they automatically prove historical causation.

## 1. First Separate Three Things: Experience, the Value of the Works, Historical Contribution

| Ruler | Question it asks | What it needs |
|---|---|---|
| Experience | Is what I am reading now interesting to me? | The reader's own experience |
| Value of the works | How does it do in language, structure, emotion and invention? | Concrete analysis and comparison of the works |
| Historical contribution | Whose choices did it change, and what did it leave that could be developed further? | Before-and-after materials, comparison with contemporaries, and evidence of influence |

This is not a complete taxonomy of literary evaluation, still less a way of drawing territorial lines between critics and historians. It only prevents us from using the answer to one question as a substitute for another.

"I don't like this poem" does not directly yield "this poem had no historical role". Conversely, "it was pioneering" does not exempt it from aesthetic criticism.

### Take an Example Programmers Know Well

The C language has flaws, and Ritchie knew it himself. In his retrospective "The Development of the C Language" he wrote:

> "C is quirky, flawed, and an enormous success."

Quirky, flawed, and at the same time enormously successful. [1]

His retrospective also records a concrete process: in 1972 Thompson tried to write a system in early C, which did not yet have structures, and later gave up; by the summer of 1973 the language and compiler could already support rewriting the Unix kernel for the PDP-11 in C. [1]

It grew gradually out of concrete needs, failed attempts, tools and implementations. Later standardisation solved another batch of problems.

You may criticise the flaws of the early language, and you may credit the later standardisation work. But from "the later versions are more mature" alone you cannot rank the abilities of the creators against the participants in standardisation, still less erase the contribution of the early work.

**What this example illustrates is a method of evaluation, not using the success of C to testify for the vernacular movement.**

### Back to Changshi ji

If you find some poems in Changshi ji naive, that impression needs no retraction. To argue over whether it, Guo Moruo or Xu Zhimo is better written, you can equally well go piece by piece.

But the next question to ask is: in the process by which new poetry took shape, did these works provide samples that could be discussed, imitated and opposed? What relations did they have with the advocacy, the journals, and the practice of other authors?

Before Changshi ji was collected into a volume, Hu Shi and other authors had already published new poems; it cannot be written up as "not a single sample before it". The safer judgement is: **it preserved a stretch of experimentation in one place, becoming a body of material in the development of new poetry that could be read and evaluated again and again.** [5]

Earlier samples are not the same thing as the sole origin, and later arrivals being more mature is not the same thing as the earlier attempts having had no effect at all.

## 2. Vernacular Chinese Was Not His Invention: the Difficulty Lies in Which Formal Settings It Could Enter

Before Hu Shi, vernacular Chinese had long been used in fiction, drama, recorded sayings, letters and other genres. In "A Historical View of Literature" (《历史的文学观念论》) he himself reviewed these traditions. [3]

So I will no longer summarise it as "having run for six hundred years". The number of years you get depends on whether you take the Tang–Song, the Yuan, or the Ming–Qing fiction as the starting point; and these genres were not a single, unchanging set of language norms either.

What is really worth pressing is:

> **When an expression is already in use, why is it still necessary to fight for "orthodox" status?**

The engineering term "formal protocol" can be borrowed here, but the object must be stated precisely. "Formal" is not one switch shared by the whole country: recognition by literary journals, admission into school curricula, examination requirements and the conventions of administrative documents are different interfaces.

That vernacular fiction could become popular does not mean some school was willing to teach the national language with it; that one journal accepted vernacular does not mean all official documents had changed. Conversely, not being adopted by some institution does not mean vernacular Chinese had no norms, no tradition, no social standing.

In engineering terms, the question is not "is there code", but also: **who allows it to be plugged in, which settings accept it, and which people are willing to invest in it.**

### A Concrete Interface Change

Order No. 4 of the Jingshi Education Affairs Bureau, dated 23 January 1920 — "in pursuance of Ministry of Education Order No. 12" (verified as No. 12 against the OCR transcription of the scanned issue from the same period and the numbering system of Ministry of Education orders) — concerned switching guowen (national-language) instruction in grades one and two of national schools (国民学校) to the colloquial written style (yuti wen) from the autumn of that year. [6]

Three boundaries apply here:

- 23 January is the date of this local forwarding order and cannot be taken directly as the date of the central ministry's order.
- It concerns specific schools, grades and a course, and cannot be expanded into "all government documents nationwide in vernacular".
- It establishes that the rule had been laid down; it does not establish that schools in every locality actually completed the switch on the same day.

The matter still matters. Changing textbooks, curricula and teaching requirements changes the choices facing authors, publishers, teachers and students. Only — **issuing the rule and completing the migration must be entered in separate accounts.**

From the 1917 advocacy to this 1920 regulation one can observe several years of institutional advance; on that basis one cannot claim that "four years refactored the nation's social operating system".

## 3. See Language as an Assembly Line: Count Not Only the Characters but Who Has to Understand

"Classical Chinese is more condensed" and "vernacular Chinese spreads more easily" are not necessarily in conflict.

What you save may be length; what is paid may be the reader's time to fill in background, resolve references and parse allusions. But this account cannot be filled in from impressions, still less settled by sticking a permanent performance label on each style.

| Layer of observation | What to ask | What to avoid |
|---|---|---|
| Carrier | What are the costs of length, paper, printing and circulation? | Assigning Classical Chinese only to bamboo strips and vernacular only to letterpress |
| Expression | Is the same content more compact, more explicit? | Comparing word counts without checking the content is equivalent |
| Reading | Which kinds of readers read faster, understand more accurately? | Taking the author's own impressions as a universal result |
| Transmission | Is it sound, script or semantic understanding being compared? | Plugging speech information rates directly into tables of written reading |
| Learning | How much prior knowledge and special training is required? | Treating differences in education as fixed "hardware tiers" |
| Adoption | Who can use it in which settings, and who is willing to adopt it? | Treating the language form as the only barrier |

The original draft once filled "about 39 bit/s" in under both Classical and vernacular Chinese. That was inappropriate. The relevant study compared speech information rates across seventeen languages; it did not measure the written comprehension costs of Classical versus vernacular Chinese, and cannot be used to declare the two "even" at this layer. [8]

Nor is saving length the only thing about Classical Chinese worth examining. As a shared written tradition, it may have supported written communication across dialect regions, the continuity of canonical texts across eras, and coordination among those with the relevant training. What is described here are potential functions; they cannot in turn be inflated into "anyone can directly read texts from two thousand years ago".

**To evaluate a style, one must first specify the task, the readers and the setting; one may not pick a single dimension oneself and then declare total victory or defeat on it.**

### An Analogy: a Small File Does Not Mean Every Device Plays It Well

Video coding is well suited to helping one grasp this variable. When comparing H.264, H.265 and AV1, besides compression efficiency one must look at the specific content, the encoding settings, the implementation, hardware support and power consumption. That one software decoder struggles on some build does not mean a device with a dedicated decoder struggles by the same factor.

The original draft's claim that "AV1 hardware decoding is supported only by flagship chips from 2021 onward" also needs correction: MediaTek announced AV1 hardware decoding support for the Dimensity 1000 series as early as April 2020. [7]

**What is borrowed here is a trade-off: resources the sender saves may cost the receiver extra.** From video coding one cannot directly compute how many times easier vernacular is than Classical Chinese.

If you must use the 286, the Pentium or Centrino as analogies, they can only stand for different conditions of prior knowledge and training, not rank human beings. People learn, refuse, modify ways of expression, and can choose not to use something when the payoff is insufficient; they are not devices waiting to be flashed with new firmware.

The analogy leaves three useful questions:

**First, why might the two-track arrangement persist?** When old and new expressions coexist, this may involve reader training, the supply of teaching materials, formal requirements and existing habits. It is not an inevitable outcome decided by "a hardware generation change" alone.

**Second, whom does the middleware save trouble for?** Translation, annotation, teachers and editors may lower comprehension costs, and may also add filtering and dependence. Their concrete net contribution should be compared, rather than prophesying that they will exist forever or are bound to be parasitic.

**Third, does lowering the threshold damage the quality of the task?** If the goal is public education, accessibility is an important metric; if the goal is professional derivation, precision must also be guaranteed. Engineering requires specifying the scope of support and a resource budget, not unconditionally "designing for the lowest device".

### Why One Cannot Say "Classical Chinese Lost to the Printing Press"

Printing, the press and education enlarged the opportunities to use different modes of expression. But Classical Chinese could also be printed, could appear in newspapers, could enter modern communication; these carriers do not automatically select vernacular.

The end of the imperial examination system, changes in schools and curricula, political and cultural movements, the publishing market, and the organisation and creative work of participants all belong in the explanation. How large a role each played requires comparison of historical materials; a single engineering analogy cannot rank a unique prime cause.

The judgement that can be kept is: **once the conditions of dissemination and education change, the costs and benefits of the styles change too; which expressions gain formal position still depends on institutions and actors.**

### Making Structure Explicit Is Not Accomplished by Renaming

Borrow one more analogy programmers know. HTML writes certain structures as tags, so that programs following the relevant rules can process them. But HTML itself is also stored as text; code, configuration and Markdown can equally have explicit structure, and one cannot say "plain text can only be guessed at by humans; machines cannot read it". [10]

What is genuinely worth borrowing is: **writing relations out explicitly may spare some readers inference, and may at the same time add notation, rules and learning burden.**

This is not a one-way staircase from Classical to vernacular. Everyday vernacular is not rigorous argument; scientific vernacular needs terminology, structure and training; Classical Chinese too has rules that can be taught — it does not run on nothing but mysterious linguistic intuition.

Therefore "lowering the threshold" must be pinned down: **whose threshold for which task is lowered, and who bears the cost?**

### "Fit" Cannot Serve as an After-the-Fact Universal Explanation

H.265/AV1, VHS/Betamax, FireWire/USB are all technical cases that can be studied further, but one may not first pick a performance metric, crown it "technically stronger", and then attribute the market outcome to that same cause.

Compression, picture quality, recording duration, cost, licensing and ecosystem were never one and the same metric. They can remind us to check trade-offs; together they cannot serve as independent validation of the vernacular movement.

Still less can one derive from this that "success is logically unpredictable, and only failure can be predicted". Success and failure may both be affected by unknown conditions; whether conditional prediction is possible depends on the specific model and tests, and half the testing obligation cannot be waived in advance.

**If an explanation can only say "it fit the environment best" after the winner has appeared, that ruler has no graduations yet.**

## 4. Three Essays: How Claim, Status and Practice Connect

Putting Hu Shi's three essays side by side lets one see work more concrete than "advocating vernacular". That said, what follows is today's analytical arrangement; it does not say Hu Shi had already written a modern protocol migration specification.

| Essay | Date | The question this article focuses on |
|---|---|---|
| "A Preliminary Discussion of Literary Reform" (文学改良刍议) | January 1917 | What is the claim about writing? |
| "A Historical View of Literature" (历史的文学观念论) | May 1917 | Why fight for orthodox status in literature? |
| "Constructive Literary Revolution" (建设的文学革命论) | April 1918 | How to build a new literature through works, tools and methods? |

### The First Essay: Writing the Claim Down

The "eight matters" of "A Preliminary Discussion of Literary Reform" include: there must be substance in the words; do not imitate the ancients; grammar must be attended to; no moaning without illness; hackneyed phrases and stock expressions must be banished; do not use allusions; do not attend to parallelism; do not shun vulgar words and colloquialisms. [2]

Among them, "do not use allusions", "grammar must be attended to" and "do not shun vulgar words and colloquialisms" may suggest to an engineer lowering background dependence, making expression explicit, and reusing knowledge readers already have.

But not every one of the "eight matters" lowers decoding costs. Emotion, thought, invention and literary form have their own aims. And "grammar" certainly cannot be equated straightaway with adding punctuation.

Part of it can be read as a checklist for expression; the whole literary programme cannot be shrunk into a performance-optimisation list.

### The Second Essay: Why the Fight for "Orthodoxy" Was Unavoidable

The most noteworthy thing in "A Historical View of Literature" is that Hu Shi explicitly links status with investment: if vernacular literature keeps being regarded as a petty byway, men of letters may refuse to commit themselves to it. [3]

In today's analytical language, one can put forward this mechanism hypothesis:

> **Recognition rules change → actors' assessments of benefit and risk change → the investment and adoption of some people change.**

That is one step more than "good things spread naturally", and one layer of autonomous choice more than "the top gives the order and those below execute".

However, the text can establish, first, only this: Hu Shi made such a mechanism judgement. It cannot yet independently establish how many people changed their behaviour because of it, still less establish that without formal recognition no one would have invested. The earlier vernacular authors he himself mentions already warn us not to state this mechanism as an absolutely necessary condition.

He likewise kept open the possibility of failure: whether valuable vernacular literature could be produced in the future still depended on the practice of literary writers. [3]

**That boundary is worth inheriting: a claim needs works and action to cash it out; the claim itself cannot serve as proof of success.**

### The Third Essay: How Documents, Works and Use Shape One Another

"Constructive Literary Revolution" put forward "a literature in the national language, a national language of literature", emphasising the role of literary works in the formation and development of language. [4]

He did not say dictionaries and textbooks are useless. The text explicitly acknowledges their importance; what it opposes is the idea that the national language could be created by such things alone. He also advocated reading more existing vernacular works, practising in settings such as correspondence, writing poetry and translating books, and discussed the methods creation requires. [4]

An engineer can see in this a feedback relation: **the claim guides attempts, works expose problems, use accumulates expressions, and systematisation in turn shapes later writing.**

This is not "the specification document doesn't count; running code decides everything". Software also needs documentation, standards, maintenance and interoperability; literary practice even less can be judged solely by whether the program runs.

Hu Shi's three essays supply analytical material supporting our inquiry into the relations among expression, status and practice. How large a role these relations actually played in the movement still requires materials on other actors and on actual adoption.

## 5. Changshi ji Is a Sample, but a Sample Is Not an Inspection Exemption

Engineers readily understand what a demo does: a sentence of "this can be done" and an artefact one can inspect, imitate and modify are not the same thing.

Seen from this angle, one importance of Changshi ji lies in leaving the experiments on paper. People could endorse, criticise and surpass it, instead of having to guess from a manifesto alone what the finished product looked like.

But three places call for restraint here.

### First, It Was Not the Only Sample Before It

Before the collection was assembled there was already a publishing practice; other authors did not wait for a volume of poems to appear before starting to write. One cannot write "the specification sat unacted upon for half a year, and once the sample appeared everyone fell in line", still less infer from publication order alone that the later must have been caused by the earlier. [5]

Demonstrating exemplary influence requires cross-checking authors' own accounts, correspondence, editorial records, relations among works, and other sources.

### Second, Immaturity Is Not Deliberately Designed Immaturity

The preface to the fourth edition of Changshi ji reviews the works' changes with the image of "shoe patterns for unbound feet", and states explicitly that keeping some of the old poems may have historical use. This helps readers see how the author assessed his own experimentation and why he kept some works. [5]

It cannot establish that Hu Shi could have written polished works but deliberately left flaws in them for others to imitate. Preserving existing traces and pre-manufacturing defects are two different things.

One may say: **these works preserve the traces of an evolution.** There is no need to add "only half-finished products could let others walk this path". Excellent works can equally provide learnable models.

### Third, "Others Wrote Better" Cannot Directly Erase Earlier Contributions

Comparing works with The Goddesses (《女神》) or "A Madman's Diary" (《狂人日记》) can yield concrete gains; using the later arrivals' artistic achievement to infer that the early explorers do not matter still lacks an influence analysis.

Conversely, one cannot book Lu Xun's and Guo Moruo's works entirely as the result of Hu Shi "building the platform". Creators, editors, journals, readers, intellectual resources and historical circumstances jointly took part in the development of the new literature.

**A work's artistic achievement and its role in changing the conditions of creation can be studied at the same time.** There is no need to belittle the later arrivals in order to credit Hu Shi, nor to erase the earlier attempts in order to admire the later ones.

## 6. Scientific Writing: Terminology, Notation and Proposition Formulation Must Be Separated

The 1859 Daiweiji shiji (《代微积拾级》) had already translated and expounded calculus in Chinese. That fact by itself suffices to oppose the claim that "without modern vernacular, higher mathematics could not have been transmitted in". [9]

But having terminology does not make a textbook easy; unfamiliar notation does not mean all the difficulty comes from notation. At least three layers must be separated here:

| Layer | What it is concerned with |
|---|---|
| Terminology | What a concept is called; is the definition clear? |
| Notation | What signs are used; are readers familiar with them; can they be operated reliably? |
| Proposition formulation | How do conditions, references and inferential steps connect? |

**A well-named variable is not readable control flow.** This remains a useful engineering analogy.

At the same time, that the old notation later fell out of use is not enough to judge that it "did it wrong" at the time; a more explicit formulation of propositions is not necessarily more efficient for every reader with the relevant training. Concrete tasks must be compared.

### Three Ways of Reading, Not a Completed Controlled Experiment

Below is an excerpt from Li Shanlan's preface, transcribed into simplified characters, with punctuation and symbol spacing modernised; it does not preserve the original edition's layout verbatim. [9]

**A | Excerpt with the original terminology and notation retained**

> 凡同类诸题，皆有一公式，而每题又各有一本式。公式中恒兼有天地，或兼有彳天彳地，但求得本式中天与彳天之同数，或地与彳地之同数以代之，乃求其积分，即得本题之全积，是谓积分术。

**B | Only some of the notation in this passage replaced with forms familiar to modern readers**

> 凡同类诸题，皆有一公式，而每题又各有一本式。公式中恒兼有 x、y，或兼有 dx、dy，但求得本式中 x 与 dx 之同数，或 y 与 dy 之同数以代之，乃求其积分，即得本题之全积，是谓积分术。

Reading up to here, you may have recognised the symbols, yet still not know the exact usage here of "公式" (formula), "本式" (the base expression) or "同数" (the same value), nor what "以代之" (to substitute for it) specifically refers to.

**C | First list the questions, then give structural hints**

One can first divide the sentence into parts — "the general form for problems of the same class — the specific form of one problem — substitution — integration — result" — and then interrogate each item: what is substituted into what? Does "同数" (the same value) refer to a value, a relation, or a concept specific to the original book? What is the scope of "全积" (the whole area)?

This step does not pretend the original has already been translated correctly. To write a reliable modern paraphrase one would still need checking against the history of mathematics and the original book's context; one cannot casually swap "同数" for "corresponding value" and then treat that as completed terminology control.

The use of the three versions is to let the reader see: **recognising symbols, understanding terminology, and tracking relations are not the same task.**

They cannot establish how much difficulty each of the three contributes. C has already added hints; the reading order also brings a familiarity effect; and the author's own sense of difficulty is not a randomised-group measurement.

From this the original draft concluded that "notation contributes little, terminology less, and grammar is the main source" — the evidence is insufficient. That ordering is withdrawn here, and the testable question is retained: [Once content and background are controlled, how much comprehension cost can explicit expression reduce?](../../research/H01_expression_and_understanding_cost.md)

### Scientific Vernacular Also Has to Be Learned

Modern everyday speech does not automatically supply rigorous argument. Terminology, mathematical notation, long sentences, conditional qualifiers and discourse structure all require training; scientific expression is not naturally unambiguous, nor naturally "lossless".

The closeness of vernacular to readers' spoken experience may lower part of the entry burden, but that is not the same as literacy, written expression and professional reasoning being "installed at the factory". Thresholds remain between different dialects, educational histories and professional backgrounds.

This also reminds us not to book scientific education and industrialisation entirely to one literary advocate. Textbooks, translation, teachers, school organisation, resources and the industrial system are all in the chain.

<a id="reform-scope"></a>

## 7. How to Separate Long-Term Goals from Current Deliverables

In talking about reform it is easy to compare only whose slogan is grander, more thorough. The engineer will also press: **what does this version solve first, which changes must be done together, and which can be tried separately?** "Version" is borrowed here to discuss scope of implementation; it does not say the historical actors managed their project like software.

Vernacular writing, simplification of character forms, building a standard language and a phonetic script are related to one another yet are not one task. Fewer strokes, ease of learning, accurate recognition and compatibility with old documents are not guaranteed to improve simultaneously. The trade-offs among the goals must be stated first; one cannot count only the single indicator easiest to tabulate.

When Hu Shi discussed the national language and literature in 1918, he argued there was no need to wait for the standard national language to be fully formed: one could start creating with existing vernacular works, the expressions of the day, and necessary Classical supplements. This provides a checkable arrangement: building the language and creating works can advance each other, without taking the full determination of the standard as a precondition for starting to write. [4]

But this cannot be used to cast him as an opponent of simplified characters or of a phonetic script. In 1953, in his answers in the Mandarin Daily (《国语日报》), he endorsed simplified characters and advocated a phonetic script; on simplified characters he stressed gradual recognition, on extending the national language he did not demand excessive speed, and he opposed forbidding children to speak their dialects. This helps in studying his implementation attitude, but cannot be run backwards to recover all of his 1917 motives. [11]

Likewise, although Lu Xun used fierce wording about the Chinese script in 1934, he also distinguished the conditions for spreading Latinisation from the research, trial writing and plain vernacular that could be done at the time; another piece of his proposed starting experiments from mixed use of Chinese characters and Latin spelling. Qian Xuantong's radical 1918 position also listed transitional measures. **A radical long-term position does not mean implementation has no steps at all; mild wording cannot substitute for costs and outcomes either.** Evaluating such arrangements requires reading the implementation steps, not stopping at slogans. [12][13][14]

The Second Simplification of Chinese Characters (erjian) supplies the questioning of another period. A 1986 official document reviews: after the 1977 draft was published, the first table was tried out in publications; in 1978 the relevant textbooks and publications stopped the trial, while the draft had not yet been rescinded; only in 1986 was discontinuation formally required. Trial use, stopping the trial, and rescission are different decisions. [15]

This outcome cannot directly establish who was more restrained, but it obliges us to take "simplification" apart: **if it merely saves a few strokes, do the distinctions the original task needs still exist? If different sources are merged into one written form, what restores the distinctions, and who bears the work of recognition, error-correction and preserving the original records?** Documents currently available can explain the decisions and some of the reasons; they cannot substitute for measuring the second scheme's comprehension effects or historical losses; for specific materials and gaps see the [Second Simplification evidence table](../../research/cases/CN-S2_evidence_starting_point.md).

Returning to the vernacular movement, a counterfactual question can be raised: if spreading vernacular had to wait for character forms, a standard language and a spelling system to be all ready, would it have delayed some benefits that could have been obtained earlier? Conversely, might advancing the pieces together have lowered repeated conversion costs? Both directions should be examined. We have no evidence to fill in the delay as 1927, nor can we derive from it a shortage of technical or administrative talent; schools, funding, teachers, textbooks and social demand all remain on the causal chain.

**To evaluate a reform one should also look at how it arranges the dependencies among goals: which benefits can be delivered first, which changes need trials, which distinctions and historical records must be preserved.** This ruler must measure Hu Shi, Lu Xun, Qian Xuantong and the other reformers alike; one cannot award a prize to someone first and then find the reasons for him.

## 8. What Remains Is Not "Hu Shi Won" but Several Questions That Keep Working

To evaluate Hu Shi one may read his poems, and one may also study how his essays took part in changing the conditions of creation and education. The two need not cancel each other.

This article borrows "protocol migration" in order to pose a set of questions:

- On which tasks can old and new expressions be translated into each other? Where does meaning get lost or usage change?
- Who is building the bridge, and who bears the bridge's cost?
- Which goals must be achieved together, which benefits can be delivered first, and which distinctions and records must be preserved?
- Which institution recognised what, and how far has actual adoption gone?
- Why are authors and users willing to invest, and why might they refuse?

"Mutual translatability" helps in studying compatibility and gradual migration, but on this item alone one cannot divide "protocol revolution" and "paradigm revolution" into two mutually incompatible classes. Nor do we have materials to assert that none of the participants had an epiphany or a conceptual conversion. This framework must face complex materials; it should not first trim the materials into the shape it wants.

**If after reading you are left only with "Hu Shi matters", this article has done half its job.** What I would rather leave you is: when evaluating a change, look not only at the finished product but also at the conditions of participation, the costs of understanding, the incentives to adopt, and the path of migration.

This is also what Socio-Protocolics (《社会系统协议学》), which I am assembling, wants to do: put some scattered questions into comparable engineering formulations, then let concrete materials correct those formulations. It inherits questions already present in the study of language understanding, institutions and organisations; whether it adds anything must be settled by comparison, not by the word "-ology" in its name.

This article has not demonstrated the six core proposition groups, nor has it measured any operating indicators of society. What it provides is a case that can be taken apart and examined.

If you work on linguistics, literary history, the history of education, institutions or human–computer interaction, the following three items are all ready to take up:

1. [Check comprehension costs](../../research/H01_expression_and_understanding_cost.md): how to build equivalence-preserving texts and separate the effects of notation, terminology, added explanation and syntax?
2. [Examine status and adoption](../../research/H02_formal_status_and_adoption.md): can actors' talk of "orthodoxy" be matched against actual changes in investment? Is there contrary material?
3. [Trace rules and migration](../../research/H03_rules_and_actual_migration.md): from an official order to a textbook to classroom use, which evidence is still missing in between?

Counterexamples, existing research, better explanations, or one exact line of revision are all welcome. You do not have to accept the whole framework first.

**Whether a new ruler is any good requires letting others pick it up and measure with it, and letting them point out: this graduation is mis-cut.**

---

<a id="article-framework"></a>

### On the Framework and Clauses This Article Uses

This article is a case article of Socio-Protocolics. This still-under-revision research framework tries to use engineering concepts such as protocol, interface, middleware, compatibility and feedback to compare collaboration problems across fields.

The framework is organised as "3 postulates → 6 core proposition groups → 19 valid RFC items (including the 007 rule; version cross-references listed separately)". The arrows denote modelling dependency and clause ownership; they cannot substitute for proof. This article uses only part of it; the [complete index of topics and clauses](../../framework_and_case_index.md) lists other topics and gaps.

The three modelling starting points this article uses are:

1. **P1: Resources are limited, and collaboration has costs.** Time, attention, learning and information transmission are constrained; concrete social comprehension costs require independent definition and measurement.
2. **P2: Participants have their own goals and choices.** Under the same set of rules, different agents may adopt different strategies.
3. **P3: Rules influence action through expectations.** Assessments of recognition, benefit, risk and performance may influence an agent's investment and cooperation. This article treats recognition–expectation–action as a candidate mechanism and does not infer from it that an equilibrium exists or converges.

These are summaries; for the [postulates and object definitions](../../whitepaper/chapter-01.md#-04-协议学核心对象模型与公理体系layer-2-theoretical-primitive-spec) the authority is whitepaper §1.5. This article also uses O1 agent, O2 protocol, O3 expectation and O4 intermediary to organise its objects, and does not judge the mere existence of teachers or editors to be parasitic.

The specific clauses participate in this article as follows:

| Reference | What this article uses it to discuss | Scope of use |
|---|---|---|
| Group 1 · [SP-RFC-001](../../whitepaper/chapter-02.md#sp-rfc-001) | Background supplementation, decoding and comprehension costs in §3 and §6 | Main conceptual reference; no Shannon capacity or throughput formulas were used to compute historical effects |
| Group 4 · [SP-RFC-014](../../whitepaper/chapter-05.md#sp-rfc-014) | The authorisation gateway of the education system in §2 | Main functional mapping; regulation, textbooks and actual adoption remain separate |
| The normative rule of Group 2 · [SP-RFC-007](../../whitepaper/chapter-03.md#sp-rfc-007) | Weighting the intelligibility of expression, public participation and error correction | A normative objective this article makes public; it does not follow automatically from the physical postulates |
| Group 6 · [SP-RFC-017](../../whitepaper/chapter-07.md#sp-rfc-017), [SP-RFC-018](../../whitepaper/chapter-07.md#sp-rfc-018) | Old–new compatibility, migration, trial works and feedback in §3, §4, §5, §7–8 | Qualitative extension; no net-present-value accounting of migration was done, and neither independent-branch probabilities nor feedback windows were tested |

This article does not develop Group 3's intertemporal performance model or Group 5's sustained-mobilisation model, and does not test Group 2's serial-decay and rent-seeking mechanisms. The expectation language of P3 does not mean proof has already been obtained for Group 3's propositions; a work's providing a sample does not mean the 018 model has passed testing.

In the Hu Shi case this article further proposes: expression thresholds, formal recognition and imitable works may jointly influence the adoption of a way of writing. This is a candidate explanation requiring comparative material to test; this article does not strictly derive historical conclusions from the three postulates, nor does it use one case to validate the six core proposition groups.

The public entry point for whitepaper v11.2 and open research: [nuoyazhizhou/socio-protocolics](https://github.com/nuoyazhizhou/socio-protocolics). The repository version corresponding to this article has been pushed; the entry point and the reading site can provide navigation; publication in the repository and on the website does not mean this article has been published on external platforms such as Zhihu. In the repository you can read directly the [authoritative whitepaper](../../whitepaper/chapter-01.md) and [open questions](../../research/README.md); for item-by-item boundaries of concepts and sources see the [source notes](source_notes.md).

Counterexamples, existing research and concrete revisions are welcome. Later materials and research results will be used to revise the framework's scope of application and its predictions.

This article: Chinese v0.5, 2026-10-23; English translation pending. For item-by-item usage locations, external sources and questions awaiting verification see the [source notes](source_notes.md); for changes see the [revision notes](revision_notes.md).

### Main Sources

The numbers correspond to the body text; for full locations, reading scope and limitations see the [source notes](source_notes.md).

1. Dennis M. Ritchie, [The Development of the C Language](https://www.nokia.com/bell-labs/about/dennis-m-ritchie/chist.html), 1993; especially Portability, the closing retrospective and Acknowledgments.
2. Hu Shi, ["A Preliminary Discussion of Literary Reform" (《文學改良芻議》)](https://zh.wikisource.org/wiki/文學改良芻議), 1917; the "eight matters" and related discussion.
3. Hu Shi, ["A Historical View of Literature" (《歷史的文學觀念論》)](https://zh.wikisource.org/wiki/歷史的文學觀念論), 1917; passages on the vernacular tradition, orthodox status, investment and the conditions of practice.
4. Hu Shi, ["Constructive Literary Revolution" (《建設的文學革命論》)](https://zh.wikisource.org/wiki/建設的文學革命論), 1918; especially sections 3 and 4.
5. Hu Shi, [Preface to Changshi ji (《尝试集》自序)](https://zh.wikisource.org/wiki/《尝试集》自序), [Preface to the Fourth Edition of Changshi ji (《尝试集》四版自序)](https://simplelits.com/books/classical/classical-10463-%E8%87%AA%E7%94%B1%E4%BA%BA%E7%94%9F/22). What was checked here is the author's own account; literary evaluation and influence still require the works themselves and other materials of the period.
6. [Jingshi Education Affairs Bureau Educational Administration Monthly, 1920, vol. 1, no. 7, scanned page 8](https://upload.wikimedia.org/wikipedia/commons/6/6e/NLC404-01J002135-24988_%E4%BA%AC%E5%B8%AB%E5%AD%B8%E5%8B%99%E5%B1%80%E6%95%99%E8%82%B2%E8%A1%8C%E6%94%BF%E6%9C%88%E5%88%8A_1920%E5%B9%B41%E5%8D%B77%E6%9C%9F.pdf#page=8): Order No. 4 of the Jingshi Education Affairs Bureau, "in pursuance of Ministry of Education Order No. 12" (verified as No. 12 against the OCR transcription of the scanned issue from the same period and the numbering system of Ministry of Education orders).
7. MediaTek, [AV1 hardware decoding for the Dimensity 1000 series](https://www.mediatek.com/zh-tw/press-room/mediatek-to-enable-cutting-edge-av1-video-codec-technology-on-android-smartphones), 28 April 2020.
8. Coupé et al., [Different languages, similar encoding efficiency](https://pmc.ncbi.nlm.nih.gov/articles/PMC6984970/), 2019. This item is used to clarify the research scope the original draft misused; it is not evidence for a Classical-versus-vernacular reading comparison.
9. Li Shanlan and Alexander Wylie, [Preface to Daiweiji shiji (《代微積拾級》序)](https://zh.wikisource.org/wiki/代微積拾級/序), 1859.

10. WHATWG, [HTML syntax](https://html.spec.whatwg.org/multipage/syntax.html), used for the discussion of the relation between text and structure in §3.
11. Hu Shi, ["Advocating a Phonetic Script — Answers at the Welcome Meeting of the Mandarin Daily" (《提倡拼音字——〈國語日報〉歡迎會上答問》)](https://zh.wikisource.org/wiki/提倡拼音字（《國語日報》歡迎會上答問）), 6 January 1953; the question-and-answer items on simplified characters, phonetic script, dialects and extending the national language.
12. Lu Xun, ["Letter in Reply to Mr. Cao Juren" (《答曹聚仁先生信》)](https://zh.wikisource.org/zh-hant/答曹聚仁先生信), 2 August 1934; point three and what could be done at the time.
13. Lu Xun, ["Chinese Characters and Latinisation" (《漢字和拉丁化》)](https://zh.wikisource.org/zh-hant/漢字和拉丁化), 23 August 1934; the passages on experiments and mixed writing.
14. Qian Xuantong, ["The Problem of Chinese Writing Hereafter" (《中國今後之文字問題》)](https://zh.wikisource.org/zh-hans/中國今後之文字問題), letter dated 14 March 1918, published 15 April of the same year; focused on transitional measures; Chen Duxiu's reply is listed separately, and the authors are not conflated.
15. [Beijing Municipal Government forwarding of 国发〔1986〕64号 with the attached request of the State Language Commission](https://www.beijing.gov.cn/zhengce/zfwj/zfwj/szfwj/201905/t20190523_71436.html), distinguishing the 1977 trial, the 1978 stoppage of the trial and the 1986 discontinuation; for the actual reading and boundaries see the [Second Simplification evidence table](../../research/cases/CN-S2_evidence_starting_point.md).
