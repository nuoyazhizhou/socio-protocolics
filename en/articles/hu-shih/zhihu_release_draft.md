> **Translation record**
> - Chinese source: `articles/hu-shih/知乎发布稿.md` (sha256 `817e4353eded5f15267a005f784c794e82bdeb04f441e11a24675aac177a99dd`, `21309` bytes, 2026-11-09)
> - Chinese version / release tag: `v11.2-r20261106` (theoretical version remains v11.2)
> - Translation version: `en-v0.1`
> - Translation date: 2026-11-09
> - Check status: checked sentence by sentence against the Chinese source for claim status, negative guardrails and numbering; machine and glossary checks only; no independent professional native-speaker review
> - Pending sync: pending registration in public-files.json / mkdocs.yml
> - Status: complete translation
> - Authority: the Chinese SSOT is authoritative; this translation does not constitute a separate set of definitions (C2)

# How to Evaluate Hu Shi's Works? Do Not Mix "How Well It Is Written" and "What It Changed" into One Question

When many people bring up Hu Shi (胡适, 1891–1962, writer and a leading advocate of vernacular Chinese), all that is left in the end is one sentence: the man who championed vernacular Chinese.

Get a bit more specific, and you open Changshi ji (《尝试集》, *Experiments*): this counts as a good poem?

That question is entirely fair to ask. If some poems do not move you today, there is no need to force yourself through a round of being moved out of respect for history.

But the next step should be taken slowly: **the poems are not well enough written, so Hu Shi's contribution amounts to no more than this.**

Once you step across, the evaluation of the works quietly turns into a different question.

I want to borrow a few concepts programmers know well to take this question apart. First, how this article uses them: "protocol" refers to traceable rules and conventions, "interface" refers to the admission and usage requirements of a concrete setting, and "decoding" refers to the work a reader does to complete understanding. The technical analogies that follow help make the variables visible; historical judgement still has to return to historical materials.

## 1. First Separate Three Things: Experience, Value, Contribution

To read a work, you need at least three rulers.

**Experience: do I enjoy reading it?**

**Value: how does it do on language, emotion, structure and invention?**

**Contribution: whose choices did it change, and what did it leave that could be developed further?**

The three are related, but they cannot answer for one another.

"I don't like it" is not the same as "no contribution"; "it was pioneering" cannot automatically turn the mediocre into a masterpiece.

### Take an Example Programmers Know Well

Early C was of course imperfect.

Ritchie himself wrote in his retrospective:

> C is quirky, flawed, and an enormous success.

Quirky, flawed, and at the same time enormously successful.

His account also records a process: in 1972 Thompson tried to write a system in early C, which did not yet have structures, and gave up; by the summer of 1973 the language and compiler could already support rewriting the Unix kernel for the PDP-11 in C. [〔1〕](https://www.nokia.com/bell-labs/about/dennis-m-ritchie/chist.html)

The early flaws were real, and the later maturing was real too. But you cannot take the maturity of the later versions and run it backwards to conclude that the early work was worthless.

What is borrowed here is a method of evaluation. The success of C does not testify for vernacular Chinese.

Returning to Hu Shi, you may criticise Changshi ji poem by poem, and you may also ask: how did this batch of works enter the discussion of new poetry — how were they read, revised and opposed?

**A work's degree of finish and the possibilities it helped open should be studied separately.**

## 2. Vernacular Chinese Was Not His Invention; the Difficulty Is Which Doors It Could Enter

Vernacular Chinese existed before Hu Shi. Fiction, drama, recorded sayings, letters — Hu Shi himself listed a string of such traditions in "A Historical View of Literature" (《历史的文学观念论》). [〔3〕](https://zh.wikisource.org/wiki/歷史的文學觀念論)

So writing him up as "the inventor of vernacular writing" actually makes his work smaller than it was.

What is more worth pressing is:

**Everyone was already using it — why still fight to make it the "orthodoxy" of literature?**

For an engineer there is a familiar distinction here: having a program does not mean it has been wired into production.

Fiction can become popular while schools may still be unwilling to teach the national language in that style; journals can accept the new way of writing while examinations and administrative documents may not change in step. Every door has its own usage requirements and its own gatekeepers.

As for "upgrading it to a formal protocol", brought down to history one must state precisely: **who recognised what, which requirement changed, and who actually began using it.**

There is one node that can be pinned down on paper.

On 23 January 1920, Order No. 4 of the Jingshi Education Affairs Bureau — "in pursuance of Ministry of Education Order No. 12" (verified as No. 12 against the OCR transcription of the scanned issue from the same period and the numbering system of Ministry of Education orders) — concerned switching guowen (national-language) instruction in grades one and two of the people's schools to the colloquial written style (yuti wen) from the autumn of that year. [〔6〕](https://upload.wikimedia.org/wikipedia/commons/6/6e/NLC404-01J002135-24988_%E4%BA%AC%E5%B8%AB%E5%AD%B8%E5%8B%99%E5%B1%80%E6%95%99%E8%82%B2%E8%A1%8C%E6%94%BF%E6%9C%88%E5%88%8A_1920%E5%B9%B41%E5%8D%B77%E6%9C%9F.pdf#page=8)

This is a regulation for a specific school stage, grade and course. 23 January is the date of local forwarding; a regulation being issued does not mean classrooms everywhere completed the switch that day.

But the change was not small. It altered part of the textbooks and teaching requirements, and the choices facing authors, publishers, teachers and students changed with it.

**Issuing the rule and completing the migration are two separate accounts. Omit the second and you exaggerate success; miss the first and you underestimate the change.**

## 3. Why It Is Hard: Look at Language as an Assembly Line

Classical Chinese is more condensed — why still need vernacular?

Do not rush to argue which is "more advanced". Take the communication apart and see where the money goes.

| Layer | The account to compute |
|---|---|
| ① Carrier | Writing, printing, storage, circulation — how many resources? |
| ② Expression | How much length does the same content take, and what is omitted? |
| ③ Reading | Who can read it, how fast, and where do errors arise? |
| ④ Transmission | Sound, script and understanding — what does each measure? |
| ⑤ Learning | How much knowledge and training must the reader acquire first? |
| ⑥ Adoption | Which settings accept it, and who gets the chance to use it? |

This is a table of questions, not a performance leaderboard with the scores already filled in.

Nor is length the only thing about Classical Chinese worth examining. A shared written tradition may also have supported communication across dialects, the continuity of old documents, and collaboration among trained groups. These functions likewise depend on specific populations and materials; one cannot criticise its high threshold on one side while forgetting what it once solved on the other.

### The File Is Small, but the Player May Not Cope

An analogy: you send a friend a video; you are quite satisfied with the file size, but on their end it stutters.

What he cares about is not your compression report. He cares whether he can watch it.

H.264, H.265 and AV1 can help one understand this account: comparing codecs requires looking beyond file size at content, settings, implementation, devices and hardware decoding support. For example, MediaTek announced in April 2020 that the Dimensity 1000 series supports AV1 hardware decoding; dedicated decoding support is a condition that needs its own check when comparing devices. [〔7〕](https://www.mediatek.com/zh-tw/press-room/mediatek-to-enable-cutting-edge-av1-video-codec-technology-on-android-smartphones)

**Resources saved on the sending side sometimes turn into work on the receiving side.**

Carried over to language, the question is: what must readers supply to make up for the characters this sentence left out? Context? Allusions? Specialist knowledge? Or a teacher's explanation?

It may also not have increased the comprehension burden at all. Readers familiar with the rules sometimes find the condensed expression clearer because it is condensed. To compare, you must find equivalent content, target readers and concrete tasks; you cannot convert a Classical-versus-vernacular reading ratio straight from video.

If the knowledge readers already have is likened to a player's specifications, then the allusions, terminology and syntax rules still to be learned are like support that has to be added. Analogies such as the 286, the Pentium or Centrino are only good for reminding us to check prerequisites. Human capability changes, and people cannot be tiered by model number; people also question, and can decide it is "not worth learning" and walk away.

When a program refuses to run, you check compatibility; when people refuse to use it, you still have to check benefits, habits and the right to choose.

### HTML Again: Explicit Structure Has a Cost Too

HTML writes part of the structure as tags, making it convenient for rule-following programs to process. It is itself text; "plain text" and "structured" cannot be treated as antonyms. [〔10〕](https://html.spec.whatwg.org/multipage/syntax.html)

What makes this analogy useful: writing the relations out may spare readers some guessing; the price is writing more and learning more rules.

Scientific vernacular is the same. Closeness to everyday speech may reduce part of the entry burden; terminology, conditions, inference and discourse structure still have to be learned.

**Between "the reader recognises every character" and "the reader understands this proposition" there still lies a stretch of engineering.**

Hence, for comparisons like VHS/Betamax and FireWire/USB, if you really want to study them, you must examine costs, licensing, compatibility, performance and ecosystem separately; you cannot first pick a winner and then invent the single reason it won.

Returning to Classical and vernacular: the printing press does not automatically choose the style. Classical Chinese could equally be printed and run in newspapers. Schools, curricula, publishing, political and cultural movements, and the participants' practice all need to enter the explanation.

A usable ruler should press: **for whom, for which task, under which conditions it fits better, and what was sacrificed?**

To say only "the winner fit the environment" after the result is out does not finish the question.

## 4. Three Essays: Connecting Claim, Status and Practice

Read together, Hu Shi's three essays are far more concrete than the one phrase "championed vernacular".

| Essay | The question this article cares about |
|---|---|
| 1917, "A Preliminary Discussion of Literary Reform" (文学改良刍议) | How to write? |
| 1917, "A Historical View of Literature" (历史的文学观念论) | Why is it worth writing in earnest? |
| 1918, "Constructive Literary Revolution" (建设的文学革命论) | On what does it keep growing? |

This is today's analytical arrangement; it does not say he was managing history by software-project rules at the time.

### 4.1 First Write the Claim Down as Items That Can Be Argued

"A Preliminary Discussion of Literary Reform" lists the "eight matters". Among them, "do not use allusions", "grammar must be attended to" and "do not shun vulgar words and colloquialisms" readily suggest to an engineer reducing implicit dependencies, making relations explicit, and reusing readers' existing experience. [〔2〕](https://zh.wikisource.org/wiki/文學改良芻議)

But "there must be substance in the words" and "no moaning without illness" also involve thought, emotion and literary aims; you cannot stuff all eight items into the single drawer of "decoding cost".

What matters is that the claim now has content that can be argued item by item. Which item you endorse, which you oppose, which you revise — that gives more places to get a grip than shouting "literature must be reformed".

### 4.2 Why the Fight for "Orthodoxy" Was Unavoidable

"A Historical View of Literature" makes a very practical judgement: if vernacular literature keeps being regarded as a petty byway, men of letters may refuse to commit their full effort. [〔3〕](https://zh.wikisource.org/wiki/歷史的文學觀念論)

In today's words: **the rules of recognition may change people's judgement of whether the investment is worth it.**

Vernacular's earlier works also form a piece of contrary material: without having obtained the orthodox status being fought for, some people were still writing in earnest. Hu Shi himself cited such authors.

So what this explanation must ask is "whose investment did status change", not announce "without formal recognition, absolutely nobody would have worked".

More worth keeping is that he did not treat the claim as the result: whether future vernacular literature could have value still had to be cashed out by writing.

### 4.3 Documents and Works Must Be Able to Correct Each Other

"Constructive Literary Revolution" puts forward "a literature in the national language, a national language with a literature". It opposes waiting until the standard national language is fully in place before writing, acknowledges that dictionaries and textbooks matter, and stresses the relations among works, use and building the language. [〔4〕](https://zh.wikisource.org/wiki/建設的文學革命論)

An engineer can borrow from this a feedback process: the claim guides attempts, works expose problems, use accumulates expressions, and systematisation in turn shapes later writing.

Documents need to land in practice, and practice needs rules that can be argued over.

### 4.4 "Reform" and "Revolution": Why the Two Could Talk to Each Other

In 1917 Hu Shi's title used "literary reform" (文学改良); Chen Duxiu then wrote "literary revolution" (文学革命), explicitly backing Hu Shi. In 1918, Hu Shi's own essay title also used "literary revolution". [〔16〕](https://zh.wikisource.org/wiki/文學革命論)[〔4〕](https://zh.wikisource.org/wiki/建設的文學革命論)

They look like a few names; what really needs reading is what they point at. Hu Shi's eight matters and Chen Duxiu's three-point programme overlap, and also differ in organisation and aims; they cannot be treated as one specification with a changed title.

**The same name does not guarantee the same meaning, and different names do not prevent an explicit reply.**

Whether a name is useful cannot be measured by counting how many people chant along; one must also see whether it lets people know more precisely which thing we agree on and which thing we are contesting.

There are already textual threads of cross-author reply here. How much communication cost the naming itself saved needs separate checking; it cannot be computed straight from three essay titles.

## 5. Changshi ji Is That Demo, but a Demo Has to Take Criticism Too

Engineers know this distinction well: a statement of "this can be done" and an artefact that can be inspected and modified are not the same.

Read from this angle, Changshi ji left behind a batch of visible experiments. Before the collection, there were already new-poetry practices by Hu Shi and other authors; it was not one volume of poems suddenly switching on a blank world.

Here there is a stretch of material far more interesting than "the pioneers were always great".

In the preface to the fourth edition, Hu Shi compared his own poems to "shoe patterns for unbound feet": the old habits were still on, some steps had been taken, but the walking was not yet clean. He re-selected and cut, keeping part of the old poems on the view that they still had historical use. [〔5〕](https://simplelits.com/books/classical/classical-10463-%E8%87%AA%E7%94%B1%E4%BA%BA%E7%94%9F/22)

This was not deliberately leaving flaws at the time of writing; it was looking back and choosing which traces deserved to be kept.

The same preface also records concrete revisions.

He asked friends including Ren Shuyong, Chen Shafei, Lu Xun, Zhou Zuoren and Yu Pingbo to take part in cutting the poems. Some suggestions he accepted; some he did not.

"A Smile" (《一笑》) contains the line:

> 那个人不知后来怎样了。

Jiang Baili suggested changing it to:

> 那个人后来不知怎样了。

Hu Shi adopted it. (The change moves 后来, "later", from its place after 不知 to before it.)

In "You Must Not Forget" (《你莫忘记》), Kang Baiqing suggested adding a "了" character. Hu Shi solemnly recorded revisions as small as this. [〔5〕](https://simplelits.com/books/classical/classical-10463-%E8%87%AA%E7%94%B1%E4%BA%BA%E7%94%9F/22)

Now there is a sense of being in the room: the man championing vernacular was still racking his brains over the word order of a sentence and where one character should land; friends could point out problems, the author could revise, and he could also explain why he kept something as it was.

**"Everyone can talk" did not automatically solve "how to write well".**

This is a revision record the author left behind, enough to observe one concrete instance of writing collaboration. It is still not enough to compute a demonstration effect for the whole new-literature movement, but it is already firmer than "half-finished products necessarily attract successors".

Admiring The Goddesses (《女神》) and "A Madman's Diary" (《狂人日记》) does not conflict with studying the role of Changshi ji. Who wrote better can be read concretely; who influenced whom requires finding concrete links. Lu Xun, Guo Moruo and the other authors were not accessory plugins on somebody's platform.

Crediting the early exploration does not require belittling those who came later; and those who came later going further does not automatically zero out the early exploration.

## 6. Scientific Writing: Giving a Concept a Good Name Is Not Yet Explaining It

The 1859 Daiweiji shiji (《代微积拾级》) had already translated and expounded calculus in Chinese. It constrains by itself one overreaching claim: without modern vernacular, higher mathematics could not have been transmitted in. [〔9〕](https://zh.wikisource.org/wiki/代微積拾級/序)

But that a book exists, and for which kinds of students it is easy to understand, are again two different questions.

At least three layers must be separated here:

**Terminology: what is this thing called?**

**Notation: what signs represent it?**

**Propositions: what relations hold among these things, and under what conditions?**

Look at a passage of the original. The following is arranged from a public transcription into simplified characters with modern punctuation:

> 凡同类诸题，皆有一公式，而每题又各有一本式。公式中恒兼有天地，或兼有彳天彳地，但求得本式中天与彳天之同数，或地与彳地之同数以代之，乃求其积分，即得本题之全积，是谓积分术。

A modern reader may stall on the old notation, may stall on the historical usage of "公式" (formula), "本式" (the base expression) and "同数" (the same value), or may simply never have studied the mathematics this passage involves.

Replacing "天、地" (tian, di) with familiar letters helps with recognising the signs; it does not automatically explain "同数". Add one more sentence of explanation and it may read more easily, but that has already added information and cannot pass itself off as a controlled experiment that changed only the style.

This material can help set exam questions; it cannot directly rank Classical against vernacular by efficiency.

The more practical question: **where exactly does a reader with the relevant mathematical training stall? What do changing the notation, glossing the terminology, and restructuring the syntax each solve?**

Scientific expression needs precise relations, and it also needs trained readers. Vernacular is not an automatic compiler of thought; and Classical-Chinese translators were not standing on the opposite side of science communication either.

To hand knowledge to more people, textbooks, annotation, teachers, schools and linguistic expression are all in the chain. The credit for this chain cannot all be hung under one person's name.

## 7. Leave Behind One Question You Can Carry Away: What Exactly Are You Optimising?

Ask again now: how should one evaluate Hu Shi's works?

You may read his poems, and you may also watch how he raised demands, fought for status, delivered works and accepted revisions. Each item needs its own evidence.

With this method, looking at reform, one can press one step further:

**What does this version solve first? Which goals must be completed together, and which can be tried separately?**

Vernacular writing, simplification of character forms, building a standard language and a phonetic script are different but related tasks. They cannot be bundled into one package that must be delivered simultaneously just because they are all called "language and script reform".

Hu Shi's 1918 arrangement was that one need not wait for the standard to be fully settled before creating. But that is not the same as opposing simplified characters or a phonetic script. His 1953 answers still endorsed the relevant reforms, and spoke of gradualism and tolerating dialects. [〔4〕](https://zh.wikisource.org/wiki/建設的文學革命論)[〔11〕](https://zh.wikisource.org/wiki/提倡拼音字（《國語日報》歡迎會上答問）)

Among Lu Xun's fierce 1934 positions there were likewise arrangements for trial writing now, plain vernacular and mixed script; Qian Xuantong's 1918 position also discussed transitional measures. On a slogan alone you cannot line these people up into "restrained" and "unrestrained" teams. [〔12〕](https://zh.wikisource.org/zh-hant/答曹聚仁先生信)[〔13〕](https://zh.wikisource.org/zh-hant/漢字和拉丁化)[〔14〕](https://zh.wikisource.org/zh-hans/中國今後之文字問題)

To evaluate an arrangement, look at what it demands, what it preserves, and how it allows trial and error.

This also brings us to the next piece: the Second Simplification of Chinese Characters (erjian).

A 1986 official document reviews: the 1977 draft was published and the first table tried out; in 1978 the relevant textbooks and publications stopped the trial; only in 1986 was use formally discontinued. [〔15〕](https://www.beijing.gov.cn/zhengce/zfwj/zfwj/szfwj/201905/t20190523_71436.html)

The process leaves behind a question worth studying on its own:

**If writing saves a few strokes, do reading, recognition, archive retrieval and error correction run up an extra bill?**

If a task originally needed to distinguish two sources and the new writing merges them into one, the new writing by itself cannot uniquely reconstruct them. Context, extra fields, a lookup table or the original records — how much can they recover, and who maintains them?

What the next piece has to check is what exactly the character tables merged, which tasks depend on those distinctions, and whether the original records were kept. Only with such materials can losses and gains be discussed; the fact that the draft was withdrawn is not enough to pre-fill the answers.

**Writing the optimisation target as "simpler" is not enough. You must say plainly whose work is saved, and whose trouble is left behind.**

This is what I want to carry away from the Hu Shi case: a few rulers that can be taken to check the next thing, not just a yes vote for a historical figure.

---

### What Framework This Article Borrows, and Whom It Invites to Join

This article uses Socio-Protocolics (《社会系统协议学》), which I am revising. It tries to put rules, interfaces, comprehension costs and feedback into one comparable analytical language, while submitting to the test of existing explanations in linguistics, literary history, and institutional and organisational research.

The three modelling starting points can first be noted in plain words: **resources are limited; participants have their own goals; rules influence choices through expectations.** The framework is organised as "3 postulates → 6 core proposition groups → 19 valid RFC items"; the arrows denote modelling dependency, not a completed proof chain.

This piece mainly borrows two questions from Group 1: **RFC-001 asks about the costs and boundaries of understanding; RFC-002 asks how names and definitions help shared identification.** Educational admission is additionally mapped functionally onto RFC-014, and migration and trial works are linked qualitatively to 017/018. Weighting intelligibility and error correction is a normative objective this article publicly chooses, not a command smuggled in on the authority of physical theorems. For the concrete definitions see the [whitepaper](../../whitepaper/chapter-01.md); for the actual scope of use see [sources and receipts](source_notes.md#zhihu-receipt).

The existing materials support concrete texts, rules and revision processes; they have not yet identified comprehension-cost effects of the vernacular movement, nor obtained proof of the six proposition groups. This article is a retrospective exploratory essay, not an ex-ante prediction or a completed-acceptance theoretical validation.

If you work on language, literary history or the history of education, or you are at home with experiments and data, the following three questions are all ready for hands-on work:

1. **How can the cost of understanding be compared fairly?** Take a stretch of real textbook, verify equivalence first, then separate the effects of notation, terminology, explanation and syntax. For the design starting point see [H01](../../research/H01_expression_and_understanding_cost.md).
2. **How do names help people pick up each other's thread?** Trace the item-by-item replies across "reform/revolution", and also look for misunderstandings and successful collaboration under different names; do not just count slogans. A [preliminary comparison table](../../research/cases/CN-HU_naming_and_response_mapping.md) already exists.
3. **How does an official order get into the classroom?** Add textbooks, schools and records of actual use, and also look for material where the regulation was not carried out. Starting point: [H03](../../research/H03_rules_and_actual_migration.md).

Project entry point: [nuoyazhizhou/socio-protocolics](https://github.com/nuoyazhizhou/socio-protocolics). The repository versions corresponding to this article and its companion materials have been pushed, and the reading site is live and can provide navigation; this does not mean the article has been published on external platforms such as Zhihu. When citing, verify that the article, the whitepaper and the receipts can all be found from the entry point.

Counterexamples, existing research, or one concrete revision that can be carried out are all welcome. You do not have to accept the whole framework first.

**For this ruler to be any use, others must be allowed to point out: this graduation is mis-cut.**

### Sources and Reading Notes

This article: Chinese dissemination candidate draft v0.1, 2026-10-23; English translation pending, not yet released externally. The numeric labels follow the [shared source table](source_notes.md) and are therefore not continuous. The links support the corresponding facts; they do not testify for the author's mapping. The technical analogies and textual illustrations did not serve as measurements of historical effects; the scope of the 1920 regulation, the limits on naming effects and on textbook comparison are explained in the relevant paragraphs.

The primary sources are Hu Shi's three essays, the prefaces to Changshi ji and the specific education documents; the web transcriptions have not yet all been collated against images of the original printings. The longer item-by-item scope and adjudications of claims are in [sources and receipts](source_notes.md#zhihu-receipt). To compare degrees of expansion, read the [research draft v0.5](how_to_evaluate_hu_shis_works.md); the two drafts differ in depth of expression, with the same boundaries of fact and conclusion.
