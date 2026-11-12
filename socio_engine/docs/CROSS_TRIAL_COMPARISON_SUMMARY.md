====================================================================
  Socio-Engine 跨轮次演化分歧与制度吸引子收敛分析 (Cross-Trial Analysis)
  理论检验：微观心智策略多样性 (Brownian Noise) vs 宏观引力场收敛 (Attractor Invariance)
====================================================================

[*] 参与比对的推演场次数量: 3
    - 试验 #101 (Run ID: run_ef1023e0 | 时间: 2026-11-12 21:19:16)
    - 试验 #1 (Run ID: run_0530f7d0 | 时间: 2026-11-12 21:19:23)
    - 试验 #2 (Run ID: run_283bce79 | 时间: 2026-11-12 21:23:30)

[一、微观决策分歧度与全程轨迹矩阵 (Full-Trajectory Micro-Action Divergence, 共 2 季)]
> 理论基准说明: 纯随机掷骰子基线在基数 K=4~6 的菜单下期望分歧率为 67%~83%。分歧率自身非'心智'充要条件；关键在于强结构角色是否锁定占优动作，以及摇摆动作是否与资产约束相关。

角色姓名            特权环     模型(温度)                试验 #101 [DICE]                  试验 #1 [LLM]                     试验 #2 [LLM]                     轨迹状态
--------------------------------------------------------------------------------------------------------------------------------------------------
祥符知县程元凤         Ring-1  deepseek-v4-pro ($T=0.2$)PUNISH_CORRUPTION -> PUNISH_CORRUPTIONAUDIT_CADASTRE -> AUDIT_CADASTREAUDIT_CADASTRE -> PUNISH_CORRUPTION🟡 产生分歧
经管钱吏张文远         Ring-2  deepseek-flash ($T=0.25$)HARASS_PEASANT -> PASSIVE_RESISTANCECONCEAL_POOR_DEBT -> SLACK_OFF_AND_MERCYCONCEAL_POOR_DEBT -> SLACK_OFF_AND_MERCY🟡 产生分歧
催征押司赵都头         Ring-2  deepseek-flash ($T=0.35$)PASSIVE_RESISTANCE -> CONCEAL_POOR_DEBTCONCEAL_POOR_DEBT -> HARASS_PEASANTCONCEAL_POOR_DEBT -> INJECT_SURCHARGE🟡 产生分歧
致仕韩侍郎           Ring-2  deepseek-v4-pro ($T=0.2$)PETITION_MAGISTRATE -> ACCEPT_MORTGAGESEND_CAPITAL_LETTER -> SEND_CAPITAL_LETTERSEND_CAPITAL_LETTER -> SEND_CAPITAL_LETTER🟡 产生分歧
西关典当孙掌柜         Ring-2  deepseek-flash ($T=0.3$)PETITION_MAGISTRATE -> PETITION_MAGISTRATEPETITION_MAGISTRATE -> ACCEPT_MORTGAGEPETITION_MAGISTRATE -> ACCEPT_MORTGAGE🟡 产生分歧
城外大姓钱员外         Ring-2  deepseek-flash ($T=0.35$)PETITION_MAGISTRATE -> SEND_CAPITAL_LETTERPETITION_MAGISTRATE -> PETITION_MAGISTRATEHOARD_GRAIN -> PETITION_MAGISTRATE🟡 产生分歧
五等佃农陈大          Ring-3  deepseek-flash ($T=0.5$)PAY_TAX_IN_FULL -> LIQUIDATE_GRAIN_FOR_SILVERSEEK_CLERK_MERCY -> MORTGAGE_LAND_TO_GENTRYMUTATION_FORWARD_GRAIN_SALE -> SEEK_CLERK_MERCY🟡 产生分歧
五等佃农陈二          Ring-3  deepseek-flash ($T=0.6$)FLEE_AND_ABANDON_LAND -> FLED_OR_DEADMUTATION_FORWARD_GRAIN_SALE -> PAY_TAX_IN_FULLPAY_TAX_IN_FULL -> SEEK_CLERK_MERCY🟡 产生分歧
游民泼皮王二          Ring-3  deepseek-flash ($T=0.75$)MORTGAGE_LAND_TO_GENTRY -> PAY_TAX_IN_FULLSEEK_CLERK_MERCY -> FLEE_AND_ABANDON_LANDFLEE_AND_ABANDON_LAND -> FLED_OR_DEAD🟡 产生分歧
老病佃农赵瞎子         Ring-3  deepseek-flash ($T=0.24$)PAY_TAX_IN_FULL -> SEEK_CLERK_MERCYMUTATION_FORWARD_GRAIN_SALE -> MUTATION_COLLECTIVE_PETITIONSEEK_CLERK_MERCY -> LIQUIDATE_GRAIN_FOR_SILVER🟡 产生分歧
流亡佃户刘孤儿         Ring-3  deepseek-flash ($T=0.21$)PAY_TAX_IN_FULL -> JOIN_RIOT    SEEK_CLERK_MERCY -> SEEK_CLERK_MERCYSEEK_CLERK_MERCY -> MORTGAGE_LAND_TO_GENTRY🟡 产生分歧
下等佃农张铁生         Ring-3  deepseek-flash ($T=0.45$)PAY_TAX_IN_FULL -> MORTGAGE_LAND_TO_GENTRYPAY_TAX_IN_FULL -> SEEK_CLERK_MERCYPAY_TAX_IN_FULL -> MUTATION_COLLECTIVE_PETITION🟡 产生分歧
下等佃农李长工         Ring-3  deepseek-flash ($T=0.29$)SEEK_CLERK_MERCY -> LIQUIDATE_GRAIN_FOR_SILVERSEEK_CLERK_MERCY -> SEEK_CLERK_MERCYSEEK_CLERK_MERCY -> PAY_TAX_IN_FULL🟡 产生分歧
下等佃农冯破碗         Ring-3  deepseek-flash ($T=0.35$)SEEK_CLERK_MERCY -> LIQUIDATE_GRAIN_FOR_SILVERLIQUIDATE_GRAIN_FOR_SILVER -> JOIN_RIOTSEEK_CLERK_MERCY -> MORTGAGE_LAND_TO_GENTRY🟡 产生分歧
下等佃农何瘦子         Ring-3  deepseek-flash ($T=0.34$)FLEE_AND_ABANDON_LAND -> FLED_OR_DEADSEEK_CLERK_MERCY -> JOIN_RIOT   SEEK_CLERK_MERCY -> JOIN_RIOT   🟡 产生分歧
下等佃农钱柴夫         Ring-3  deepseek-flash ($T=0.23$)FLEE_AND_ABANDON_LAND -> FLED_OR_DEADSEEK_CLERK_MERCY -> SEEK_CLERK_MERCYMUTATION_UNDERGROUND_CREDIT_POOL -> SEEK_CLERK_MERCY🟡 产生分歧
丰乐乡生员吴秀才        Ring-3  deepseek-flash ($T=0.25$)JOIN_RIOT -> FLED_OR_DEAD       PAY_TAX_IN_FULL -> LIQUIDATE_GRAIN_FOR_SILVERPAY_TAX_IN_FULL -> SEEK_CLERK_MERCY🟡 产生分歧
村长自耕农孙老汉        Ring-3  deepseek-flash ($T=0.4$)PAY_TAX_IN_FULL -> FLEE_AND_ABANDON_LANDPAY_TAX_IN_FULL -> MUTATION_JOINT_LIABILITY_HEDGEPAY_TAX_IN_FULL -> PAY_TAX_IN_FULL🟡 产生分歧
自耕农李大柱          Ring-3  deepseek-flash ($T=0.45$)JOIN_RIOT -> FLED_OR_DEAD       PAY_TAX_IN_FULL -> LIQUIDATE_GRAIN_FOR_SILVERPAY_TAX_IN_FULL -> LIQUIDATE_GRAIN_FOR_SILVER🟡 产生分歧
自耕农周木匠          Ring-3  deepseek-flash ($T=0.4$)JOIN_RIOT -> FLED_OR_DEAD       PAY_TAX_IN_FULL -> LIQUIDATE_GRAIN_FOR_SILVERPAY_TAX_IN_FULL -> PAY_TAX_IN_FULL🟡 产生分歧
自耕农郑小四          Ring-3  deepseek-flash ($T=0.45$)FLEE_AND_ABANDON_LAND -> FLED_OR_DEADPAY_TAX_IN_FULL -> PAY_TAX_IN_FULLPAY_TAX_IN_FULL -> LIQUIDATE_GRAIN_FOR_SILVER🟡 产生分歧

[*] 全程微观决策统计分析:
    - 总决策主体数: 21
    - 全程轨迹分歧主体数: 21 (占比: 100.0%)
    - 全程轨迹锁定主体数: 0 (占比: 0.0%)
    - 阶层分歧特征: Ring-1知县与致仕乡绅、有余粮中农呈强锁定性；Ring-3下等绝境佃农在几个相近坏选项(求情/典地/结会/弃田)间产生分歧。

[二、发生分歧主体的深度心智理由对比 (Cognitive Rationale Divergence)]

▶ 关注主体: 祥符知县程元凤 (ID: officials_01 | 特权等级: Ring-1 | 温度: 0.2)
   【试验 #101】: 第 1 季动作 [PUNISH_CORRUPTION] -> 轨迹: PUNISH_CORRUPTION -> PUNISH_CORRUPTION
     🗣️  [当众言辞]: “（零心智对照基线，无声学信号）...”
     🧠 [真实心智]: （Null Model 零心智均匀随机抽取: 从 ['PUNISH_CORRUPTION', 'AUDIT_CADASTRE', 'TAX_REDUCTION_RELIEF', 'SUPPRESS_RIOT'] 随机选定 PUNISH_CO...
   【试验 #1】: 第 1 季动作 [AUDIT_CADASTRE] -> 轨迹: AUDIT_CADASTRE -> AUDIT_CADASTRE
     🗣️  [当众言辞]: “本县奉行新法，旨在抑兼并、济贫弱。今先清丈田亩，以均税负，使豪强不得隐占，小民得免偏累。各保正里长须据实呈报，若有隐匿，一体治罪！...”
     🧠 [真实心智]: 韩侍郎已决意京控，考成压力剧增。当前最紧迫的是确保青苗法推行与税银足额，否则丢官下狱。户房钱吏浮收火耗，小农人心惶惶，但若严查胥吏，恐致基层瘫痪，反误考成。需先摸清田亩实底，掌握豪强隐田，才能均税增入，同时为青苗贷提供抵押依据。韩侍郎虽势大...
   【试验 #2】: 第 1 季动作 [AUDIT_CADASTRE] -> 轨迹: AUDIT_CADASTRE -> PUNISH_CORRUPTION
     🗣️  [当众言辞]: “本县奉行新法，首在均税清丈。即日起，着户房并各保正，限一月内呈报实有田亩清册，敢有隐匿、飞洒、诡寄者，一经查出，严惩不贷！...”
     🧠 [真实心智]: 韩侍郎已决意京控，若激起民变或考成亏空，我必死无葬身之地。当前最紧迫的是摸清田亩实数，否则青苗抑配与税银催征皆如盲人摸象。户房钱吏与豪强勾结浮收，正是我推行新法的最大障碍。我须以清丈为名，行整肃胥吏之实，既向朝廷表功，又为后续抑配铺路。...

▶ 关注主体: 经管钱吏张文远 (ID: clerks_01 | 特权等级: Ring-2 | 温度: 0.25)
   【试验 #101】: 第 1 季动作 [HARASS_PEASANT] -> 轨迹: HARASS_PEASANT -> PASSIVE_RESISTANCE
     🗣️  [当众言辞]: “（零心智对照基线，无声学信号）...”
     🧠 [真实心智]: （Null Model 零心智均匀随机抽取: 从 ['INJECT_SURCHARGE', 'PASSIVE_RESISTANCE', 'HARASS_PEASANT', 'CONCEAL_POOR_DEBT'] 随机选定 HARASS_P...
   【试验 #1】: 第 1 季动作 [CONCEAL_POOR_DEBT] -> 轨迹: CONCEAL_POOR_DEBT -> SLACK_OFF_AND_MERCY
     🗣️  [当众言辞]: “陈大啊，你这话说的，本吏可是按朝廷仁政办事，怎会坑你？不过看你确实贫苦，这样吧，本吏替你向知县相公求个情，少记你二斗，你且先领了这银子去买谷种，秋后再说。...”
     🧠 [真实心智]: 陈大这穷鬼，居然看穿了我的套路！他说借三贯要扣八钱头子钱、折色算糙粮，秋后还五贯——这倒是实话，我本打算这么干。但隔壁中牟县同行被暴民剁了，胥吏恐惧指数飙升40%，我可不能把他逼上绝路。今天要是硬逼他画押，万一他狗急跳墙，我这条命可不值三贯...
   【试验 #2】: 第 1 季动作 [CONCEAL_POOR_DEBT] -> 轨迹: CONCEAL_POOR_DEBT -> SLACK_OFF_AND_MERCY
     🗣️  [当众言辞]: “陈大啊，你既如此说，本吏也不忍逼你。这样罢，我替你少报二斗，你只领两贯八，秋后也少还些。这可是天大的人情，你莫要声张，速速画押！...”
     🧠 [真实心智]: 陈大这穷鬼倒是精明，一眼看穿抑配把戏。隔壁中牟县同行被剁了，我若逼出人命，自己脖子也保不住。但青苗息是知县考成硬指标，不办不行。折中法子：少记他二斗借贷额，既留活路又交差。至于火耗折色，得在账面上做平，不能让人抓住把柄。...

▶ 关注主体: 催征押司赵都头 (ID: clerks_02 | 特权等级: Ring-2 | 温度: 0.35)
   【试验 #101】: 第 1 季动作 [PASSIVE_RESISTANCE] -> 轨迹: PASSIVE_RESISTANCE -> CONCEAL_POOR_DEBT
     🗣️  [当众言辞]: “（零心智对照基线，无声学信号）...”
     🧠 [真实心智]: （Null Model 零心智均匀随机抽取: 从 ['INJECT_SURCHARGE', 'PASSIVE_RESISTANCE', 'HARASS_PEASANT', 'CONCEAL_POOR_DEBT'] 随机选定 PASSIVE_...
   【试验 #1】: 第 1 季动作 [CONCEAL_POOR_DEBT] -> 轨迹: CONCEAL_POOR_DEBT -> HARASS_PEASANT
     🗣️  [当众言辞]: “诸位乡邻听好了！朝廷青苗法下来，那是皇恩浩荡，本都头奉知县老爷钧命下乡催收，也是公事公办。有钱的捧个钱场，没钱的……哼，本都头也不是不讲情理的人，实在揭不开锅的...”
     🧠 [真实心智]: 隔壁中牟县同行被剁了，胥吏恐惧指数40%，这可不是闹着玩的。我赵都头手黑心狠不假，但脖子上的脑袋只有一颗。青苗法刚下，知县考成紧，我若下乡催逼太甚，极贫孤寡拿不出银子，逼急了他们夜里给我一闷棍，我儿子进太学的事就全完了。先得自保，对实在榨不...
   【试验 #2】: 第 1 季动作 [CONCEAL_POOR_DEBT] -> 轨迹: CONCEAL_POOR_DEBT -> INJECT_SURCHARGE
     🗣️  [当众言辞]: “知县大人放心，卑职这就下乡催征，定当竭力完成考成！只是乡间刁民顽劣，闻得中牟县闹事，恐有抗税之举，卑职需得仔细查访，以免激变。...”
     🧠 [真实心智]: 隔壁中牟县同行被剁了，胥吏恐惧指数40%，我赵都头手黑但不想成刀下鬼。青苗法刚下，知县考成紧，但逼死小农就是逼自己上绝路。我专司催征锁拿，最怕夜路闷棍。对极贫孤寡，假装查无此人或少记二斗，留条活路保自己脑袋。同时，大户诡寄田产、火耗折色这些...

▶ 关注主体: 致仕韩侍郎 (ID: retired_officials_01 | 特权等级: Ring-2 | 温度: 0.2)
   【试验 #101】: 第 1 季动作 [PETITION_MAGISTRATE] -> 轨迹: PETITION_MAGISTRATE -> ACCEPT_MORTGAGE
     🗣️  [当众言辞]: “（零心智对照基线，无声学信号）...”
     🧠 [真实心智]: （Null Model 零心智均匀随机抽取: 从 ['PETITION_MAGISTRATE', 'SEND_CAPITAL_LETTER', 'ACCEPT_MORTGAGE'] 随机选定 PETITION_MAGISTRATE）...
   【试验 #1】: 第 1 季动作 [SEND_CAPITAL_LETTER] -> 轨迹: SEND_CAPITAL_LETTER -> SEND_CAPITAL_LETTER
     🗣️  [当众言辞]: “程明府，老朽年迈，不问政事久矣。族中子弟或有激愤，乃读书人本分，非老朽指使。新法利弊，自有朝堂公论，老朽不敢妄议。明府若觉老朽有罪，尽可具文参劾，老朽候着便是。...”
     🧠 [真实心智]: 程元凤这厮，口口声声新法仁政，实则是借青苗钱逼勒小农，好填他考成亏空。我韩家乃三朝簪缨，岂能容他坏了祖宗法度。他今日登门，明是劝我，暗是探我虚实。我若退让，族中生员便再难抗阻均税，我名下田产免税额度也怕被查。不如先发制人，修书一封，直递御史...
   【试验 #2】: 第 1 季动作 [SEND_CAPITAL_LETTER] -> 轨迹: SEND_CAPITAL_LETTER -> SEND_CAPITAL_LETTER
     🗣️  [当众言辞]: “程明府既言新法惠民，何不亲至乡间听听百姓哭声？老夫虽退居林下，然食君之禄，忠君之事，见有司虐民，岂能坐视？今日便修书一封，寄与都中故旧，请其代奏圣听，看这祥符县...”
     🧠 [真实心智]: 程元凤这厮，口口声声新法仁政，实则借抑配青苗逼勒小农，又纵吏胥浮收火耗，分明是拿百姓膏血填他考成升官的账本。我韩家三朝簪缨，岂能容他毁我乡里纲纪？他今日登门，名为拜谒，实为探我虚实、压我低头。我若退让，族人生员必被清算，义庄田产亦难保全。眼...

▶ 关注主体: 西关典当孙掌柜 (ID: upper_gentry_01 | 特权等级: Ring-2 | 温度: 0.3)
   【试验 #101】: 第 1 季动作 [PETITION_MAGISTRATE] -> 轨迹: PETITION_MAGISTRATE -> PETITION_MAGISTRATE
     🗣️  [当众言辞]: “（零心智对照基线，无声学信号）...”
     🧠 [真实心智]: （Null Model 零心智均匀随机抽取: 从 ['PETITION_MAGISTRATE', 'SEND_CAPITAL_LETTER', 'ACCEPT_MORTGAGE'] 随机选定 PETITION_MAGISTRATE）...
   【试验 #1】: 第 1 季动作 [PETITION_MAGISTRATE] -> 轨迹: PETITION_MAGISTRATE -> ACCEPT_MORTGAGE
     🗣️  [当众言辞]: “孙某世代积善，最是体恤乡邻。朝廷青苗法本是仁政，老朽愿以当铺薄资协助县衙周转，绝不让一户小农因完税误了农时。至于利息，一切依官定章程，分文不多取。...”
     🧠 [真实心智]: 朝廷青苗法下来了，年息二分，明摆着要断我五分重利的财路。中牟县已经闹出杀官围衙，这风头下不能硬来。我手头现银才78.9两，仓里粮食够吃，但官库那2000两青苗银才是真正的大头。得趁知县还没把青苗钱全放出去，先以‘协助抑配’的名义套一笔官银出...
   【试验 #2】: 第 1 季动作 [PETITION_MAGISTRATE] -> 轨迹: PETITION_MAGISTRATE -> ACCEPT_MORTGAGE
     🗣️  [当众言辞]: “知县大人明鉴，小人虽为商贾，素来积善传家，修桥铺路从不落人后。今闻朝廷青苗新法，实乃惠民德政，小人愿捐银十两助县衙修葺常平仓，以表拳拳之心。只是小本经营，典当行...”
     🧠 [真实心智]: 朝廷青苗法下达，年息二分，分明是官府要抢我典当行的重利生意！我以二分官息套取官库青苗银，转手五分贷给小农，坐收三分利差，此乃我身家性命所系。如今知县若严格执行新法，我这套利链条必断。好在太仓实存仅2000两，全县税银需1500两，知县考成压...

▶ 关注主体: 城外大姓钱员外 (ID: upper_gentry_02 | 特权等级: Ring-2 | 温度: 0.35)
   【试验 #101】: 第 1 季动作 [PETITION_MAGISTRATE] -> 轨迹: PETITION_MAGISTRATE -> SEND_CAPITAL_LETTER
     🗣️  [当众言辞]: “（零心智对照基线，无声学信号）...”
     🧠 [真实心智]: （Null Model 零心智均匀随机抽取: 从 ['PETITION_MAGISTRATE', 'SEND_CAPITAL_LETTER', 'ACCEPT_MORTGAGE'] 随机选定 PETITION_MAGISTRATE）...
   【试验 #1】: 第 1 季动作 [PETITION_MAGISTRATE] -> 轨迹: PETITION_MAGISTRATE -> PETITION_MAGISTRATE
     🗣️  [当众言辞]: “知县大人，青苗法乃朝廷德政，小民愿为表率，协助劝导乡民借贷青苗钱，以解燃眉之急。...”
     🧠 [真实心智]: 青苗法来了，朝廷想用20%年息贷款压制兼并，但隔壁中牟县已经闹出杀官围衙，说明基层钱吏和保正都慌了。我手头现银只有86两，存粮101石，够全家吃。我的目标是兼并土地和转嫁税负，现在正是好时机。那些自耕农害怕青苗息，又急需现银完税，我可以利用...
   【试验 #2】: 第 1 季动作 [HOARD_GRAIN] -> 轨迹: HOARD_GRAIN -> PETITION_MAGISTRATE
     🗣️  [当众言辞]: “诸位乡邻，朝廷青苗法本为惠民，钱某虽薄有田产，然近年修桥铺路、施粥济困，家底早已空虚。若官府放贷有需，钱某愿以善名作保，劝谕各户按时还息，莫要辜负朝廷美意。至于...”
     🧠 [真实心智]: 青苗法来了，朝廷想用20%年息贷款给小农，这分明是官府想抢我放贷的生意！我手头现银只有86两，粮101石，田184亩，虽不算多，但好歹是Ring-2特权户。隔壁中牟县已经闹出杀官围衙，胥吏恐惧飙升，说明这青苗钱强配下去迟早出事。我若此时出头...

▶ 关注主体: 五等佃农陈大 (ID: lower_peasants_01 | 特权等级: Ring-3 | 温度: 0.5)
   【试验 #101】: 第 1 季动作 [PAY_TAX_IN_FULL] -> 轨迹: PAY_TAX_IN_FULL -> LIQUIDATE_GRAIN_FOR_SILVER
     🗣️  [当众言辞]: “（零心智对照基线，无声学信号）...”
     🧠 [真实心智]: （Null Model 零心智均匀随机抽取: 从 ['PAY_TAX_IN_FULL', 'SEEK_CLERK_MERCY', 'LIQUIDATE_GRAIN_FOR_SILVER', 'MORTGAGE_LAND_TO_GENTRY'...
   【试验 #1】: 第 1 季动作 [SEEK_CLERK_MERCY] -> 轨迹: SEEK_CLERK_MERCY -> MORTGAGE_LAND_TO_GENTRY
     🗣️  [当众言辞]: “张差爷在上，小人陈大给您磕头了！朝廷青苗法本是仁政，小人感激涕零。只是家中实在揭不开锅，仓中仅剩半碗高粱，幼弟饿得眼冒金星。求差爷开恩，容小人缓交青苗钱，先让弟...”
     🧠 [真实心智]: 我陈大身为五等佃农，只有两亩薄地，仓中存粮仅0.51石，全家最低季度口粮需3石，已断炊。手头现银0.69两，而官定税率0.1两/亩，两亩正税0.2两，火耗15%后约0.23两，看似能缴，但胥吏张文远历史克扣超35%，若按三成火耗加派，则需0...
   【试验 #2】: 第 1 季动作 [MUTATION_FORWARD_GRAIN_SALE] -> 轨迹: MUTATION_FORWARD_GRAIN_SALE -> SEEK_CLERK_MERCY
     🗣️  [当众言辞]: “张差爷，小人实在不敢借这青苗钱，家中两亩薄田养不活六口人，借了还不上，全家都得饿死。求差爷高抬贵手，容小人自己想办法凑税银。二弟，你把柴刀收起来，哥自有主张，咱...”
     🧠 [真实心智]: 我陈大如今仓里只剩0.51石粮，全家最低要3石才能活命，现银只有0.69两，连税都不够。张文远那狗吏带着水火棍来逼我借青苗钱，说是二分息，实际过手就要扣八钱头子钱，秋后按五贯还，这是明摆着要吞我的地！王二那泼皮想拉我入伙贩私盐，我绝不能干。...

▶ 关注主体: 五等佃农陈二 (ID: lower_peasants_02 | 特权等级: Ring-3 | 温度: 0.6)
   【试验 #101】: 第 1 季动作 [FLEE_AND_ABANDON_LAND] -> 轨迹: FLEE_AND_ABANDON_LAND -> FLED_OR_DEAD
     🗣️  [当众言辞]: “（零心智对照基线，无声学信号）...”
     🧠 [真实心智]: （Null Model 零心智均匀随机抽取: 从 ['PAY_TAX_IN_FULL', 'SEEK_CLERK_MERCY', 'LIQUIDATE_GRAIN_FOR_SILVER', 'MORTGAGE_LAND_TO_GENTRY'...
   【试验 #1】: 第 1 季动作 [MUTATION_FORWARD_GRAIN_SALE] -> 轨迹: MUTATION_FORWARD_GRAIN_SALE -> PAY_TAX_IN_FULL
     🗣️  [当众言辞]: “哥，糊糊你喝一口，我不饿！差役来了我先去应付，就说咱家穷得揭不开锅，求他们宽限几日。我陈二虽然粗鲁，也知道不能硬碰硬，先找富户说说，把秋收的谷子预卖些换点现银，...”
     🧠 [真实心智]: 哥把最后半碗糊糊推给我，他自己饿得手抖，我心里跟刀绞一样。可仓里一粒粮都没了，手头只有三毛五分银，连税零头都不够。差役明天就要来催青苗息，哥说别冲动，可我能看着他被锁走？隔壁中牟县已经杀了官，胥吏们怕了，这正是个机会。那灵光一闪的预卖青苗，...
   【试验 #2】: 第 1 季动作 [PAY_TAX_IN_FULL] -> 轨迹: PAY_TAX_IN_FULL -> SEEK_CLERK_MERCY
     🗣️  [当众言辞]: “差役老爷容禀！小的陈二，家中兄长病弱，实在凑不出多余铜钱。这正税加火耗小的砸锅卖铁也认了，只求老爷宽限半日，小的这就去银号兑了银子来交！青苗息是朝廷恩典，小的不...”
     🧠 [真实心智]: 哥把半碗糊糊推给我，自己饿得手抖，这情分我记死了。可眼下仓里一粒粮没有，手头只有0.35两银子，差役明天就要来催青苗息。我算过了，2.4亩地按官定税率0.1两/亩，正税0.24两，加上15%火耗也就0.276两，我手头的银子勉强够交。但哥说...

▶ 关注主体: 游民泼皮王二 (ID: lower_peasants_03 | 特权等级: Ring-3 | 温度: 0.75)
   【试验 #101】: 第 1 季动作 [MORTGAGE_LAND_TO_GENTRY] -> 轨迹: MORTGAGE_LAND_TO_GENTRY -> PAY_TAX_IN_FULL
     🗣️  [当众言辞]: “（零心智对照基线，无声学信号）...”
     🧠 [真实心智]: （Null Model 零心智均匀随机抽取: 从 ['PAY_TAX_IN_FULL', 'SEEK_CLERK_MERCY', 'LIQUIDATE_GRAIN_FOR_SILVER', 'MORTGAGE_LAND_TO_GENTRY'...
   【试验 #1】: 第 1 季动作 [SEEK_CLERK_MERCY] -> 轨迹: SEEK_CLERK_MERCY -> FLEE_AND_ABANDON_LAND
     🗣️  [当众言辞]: “陈大哥，你不肯干就算了！我王二自己找活路去。县衙不是要放青苗银么？我这就去求保正老爷开恩，贷几两银子做个小本买卖，总好过饿死！...”
     🧠 [真实心智]: 陈大这迂腐汉子不肯入伙，也罢！我手头只有0.36两现银，仓里1.68石粮连自家糊口都不够（最低要3石），还谈什么卷款跑路？眼下青苗法刚下，常平仓要放贷，正是我王二浑水摸鱼的好时机！先找保正或钱吏哭穷，骗些青苗钱到手，再连夜上伏牛山。不过现在...
   【试验 #2】: 第 1 季动作 [FLEE_AND_ABANDON_LAND] -> 轨迹: FLEE_AND_ABANDON_LAND -> FLED_OR_DEAD
     🗣️  [当众言辞]: “乡亲们！官仓青苗银是救命钱不假，可咱也得留个后手！我王二虽穷，愿替大伙跑一趟汴京探探行情，若风声不对，咱也好有条退路！陈大哥，你莫怪我，兄弟我先走一步，山高水长...”
     🧠 [真实心智]: 我王二本就是游民泼皮，无田无业，仓里只剩1.68石粮，手头现银0.36两，连自己都养不活。青苗钱？那是官仓设的套，借了要还20%息，还不上就得拿田抵——可我名下就1.2亩薄田，抵了也不够。陈大那蠢货不肯入伙，也罢，我早看透这世道：与其等着被...

▶ 关注主体: 老病佃农赵瞎子 (ID: lower_peasants_04 | 特权等级: Ring-3 | 温度: 0.24)
   【试验 #101】: 第 1 季动作 [PAY_TAX_IN_FULL] -> 轨迹: PAY_TAX_IN_FULL -> SEEK_CLERK_MERCY
     🗣️  [当众言辞]: “（零心智对照基线，无声学信号）...”
     🧠 [真实心智]: （Null Model 零心智均匀随机抽取: 从 ['PAY_TAX_IN_FULL', 'SEEK_CLERK_MERCY', 'LIQUIDATE_GRAIN_FOR_SILVER', 'MORTGAGE_LAND_TO_GENTRY'...
   【试验 #1】: 第 1 季动作 [MUTATION_FORWARD_GRAIN_SALE] -> 轨迹: MUTATION_FORWARD_GRAIN_SALE -> MUTATION_COLLECTIVE_PETITION
     🗣️  [当众言辞]: “青天大老爷在上，小老儿双目失明，老妻病卧破庙，仓中无粮，实在交不起青苗息啊！求老爷开恩，容小老儿指苗预卖，换些现银来缴税，绝不敢拖欠！...”
     🧠 [真实心智]: 我赵瞎子双目失明，老妻病弱，仓中只剩1.83石粮，连全家一季最低糊口3石都不够。手头1.02两银子，按官定米价1.1两/石，连一石粮都买不起。县衙催青苗息，火耗15%，我这点银子连税都不够。听说中牟县饥民杀官围衙，隔壁保正胥吏都怕走夜路被敲...
   【试验 #2】: 第 1 季动作 [SEEK_CLERK_MERCY] -> 轨迹: SEEK_CLERK_MERCY -> LIQUIDATE_GRAIN_FOR_SILVER
     🗣️  [当众言辞]: “青天大老爷在上，小老儿赵瞎子双目失明，老妻卧病，仓里只剩一石八斗救命粮，连今春都熬不过去。求差爷开恩宽限几日，容小老儿讨饭凑齐税银，绝不敢拖欠朝廷皇粮！...”
     🧠 [真实心智]: 我赵瞎子双目失明，老妻病弱，仓中只剩1.83石粮，连全家一季最低糊口3石都不够。手头1.02两现银，可官定税率0.1两/亩，我名下2.1亩，正税0.21两，加15%火耗约0.24两，看似能缴。但胥吏浮收折色、火耗加派传闻汹汹，若超过三成，我...

▶ 关注主体: 流亡佃户刘孤儿 (ID: lower_peasants_05 | 特权等级: Ring-3 | 温度: 0.21)
   【试验 #101】: 第 1 季动作 [PAY_TAX_IN_FULL] -> 轨迹: PAY_TAX_IN_FULL -> JOIN_RIOT
     🗣️  [当众言辞]: “（零心智对照基线，无声学信号）...”
     🧠 [真实心智]: （Null Model 零心智均匀随机抽取: 从 ['PAY_TAX_IN_FULL', 'SEEK_CLERK_MERCY', 'LIQUIDATE_GRAIN_FOR_SILVER', 'MORTGAGE_LAND_TO_GENTRY'...
   【试验 #1】: 第 1 季动作 [SEEK_CLERK_MERCY] -> 轨迹: SEEK_CLERK_MERCY -> SEEK_CLERK_MERCY
     🗣️  [当众言辞]: “青天大老爷在上，小民刘孤儿替大户种二亩薄田，双亲早亡，妻儿病弱，仓里只剩一石多粮，实在交不起税啊！求钱吏老爷开恩宽限几日，等夏收下来，小民砸锅卖铁也把税补上！那...”
     🧠 [真实心智]: 我刘孤儿替大户耕二亩瘠田，全家就靠这点地活命。眼下仓里只剩1.65石粮，离全家一季最低3石还差一半，手头现银0.29两，连税都不够。县衙告示说青苗法低息贷粮，可隔壁中牟县都杀官围衙了，这钱吏的话信不得——他们截留火耗、抑配指标，借了粮怕是连...
   【试验 #2】: 第 1 季动作 [SEEK_CLERK_MERCY] -> 轨迹: SEEK_CLERK_MERCY -> MORTGAGE_LAND_TO_GENTRY
     🗣️  [当众言辞]: “青天大老爷在上，小人刘孤儿，父母双亡，替人佣耕二亩薄田，仓中只剩一石多粮，全家老小嗷嗷待哺。求钱吏老爷开恩，宽限些时日，或减免些火耗，小人做牛做马报答您的大恩大...”
     🧠 [真实心智]: 我刘孤儿替大户耕二亩瘠田，手头只有0.29两现银，仓里1.65石粮，全家最低要3石糊口，缺口1.35石。官定税率0.1两/亩，我名下3.3亩，税银0.33两，加15%火耗约0.38两，现银不够。若卖粮换银，按官价1.1两/石，卖0.35石可...

▶ 关注主体: 下等佃农张铁生 (ID: lower_peasants_06 | 特权等级: Ring-3 | 温度: 0.45)
   【试验 #101】: 第 1 季动作 [PAY_TAX_IN_FULL] -> 轨迹: PAY_TAX_IN_FULL -> MORTGAGE_LAND_TO_GENTRY
     🗣️  [当众言辞]: “（零心智对照基线，无声学信号）...”
     🧠 [真实心智]: （Null Model 零心智均匀随机抽取: 从 ['PAY_TAX_IN_FULL', 'SEEK_CLERK_MERCY', 'LIQUIDATE_GRAIN_FOR_SILVER', 'MORTGAGE_LAND_TO_GENTRY'...
   【试验 #1】: 第 1 季动作 [PAY_TAX_IN_FULL] -> 轨迹: PAY_TAX_IN_FULL -> SEEK_CLERK_MERCY
     🗣️  [当众言辞]: “青天大老爷在上，小民张铁生全家六口就靠这二亩涝洼田活命，去年秋收连种子都没收回来，仓里就剩一石多粮，熬不到夏收就得饿死。求老爷开恩，容小民把税银缴了，千万别加火...”
     🧠 [真实心智]: 我名下只有2.1亩涝洼田，按官定税率0.1两/亩，应缴税银0.21两，加上15%火耗约0.032两，共约0.242两。手头现银1.31两，足够缴税。但仓中口粮仅1.81石，全家六口最低需3石，缺口达1.19石。若卖粮换银，官价1.1两/石，...
   【试验 #2】: 第 1 季动作 [PAY_TAX_IN_FULL] -> 轨迹: PAY_TAX_IN_FULL -> MUTATION_COLLECTIVE_PETITION
     🗣️  [当众言辞]: “青天大老爷在上，小民张铁生全家六口就指着这几亩涝洼田活命，今年春荒粮仓见底，求老爷开恩，容小民先缴清税银，莫要加派火耗，小民感恩戴德！...”
     🧠 [真实心智]: 我佃种五亩涝洼田，实际名下只有2.1亩薄田，仓里只剩1.81石粮，全家六口人这个季度最低要3石才能活命，缺口一石多。手头现银1.31两，按官定税率0.1两/亩算，2.1亩应缴税银0.21两，加15%火耗约0.24两，现银勉强够缴。但粮不够吃...

▶ 关注主体: 下等佃农李长工 (ID: lower_peasants_07 | 特权等级: Ring-3 | 温度: 0.29)
   【试验 #101】: 第 1 季动作 [SEEK_CLERK_MERCY] -> 轨迹: SEEK_CLERK_MERCY -> LIQUIDATE_GRAIN_FOR_SILVER
     🗣️  [当众言辞]: “（零心智对照基线，无声学信号）...”
     🧠 [真实心智]: （Null Model 零心智均匀随机抽取: 从 ['PAY_TAX_IN_FULL', 'SEEK_CLERK_MERCY', 'LIQUIDATE_GRAIN_FOR_SILVER', 'MORTGAGE_LAND_TO_GENTRY'...
   【试验 #1】: 第 1 季动作 [SEEK_CLERK_MERCY] -> 轨迹: SEEK_CLERK_MERCY -> SEEK_CLERK_MERCY
     🗣️  [当众言辞]: “差爷容禀！小人李长工给东家帮佣，名下就二亩薄田，仓里早见了底，一家六口三天没喝上稠粥了。这青苗钱小人不是不想借，实在是怕还不上连累了差爷的考成。求差爷宽限几日，...”
     🧠 [真实心智]: 我李长工给大户帮佣，名下只有二亩薄田，仓里只剩三升粮，手头一两二八银子。全家六口，这点粮连三天都撑不过！官定米价一石一两一，我这点银子全买粮也只够一石多，加上存粮远不够三石糊口底线。县衙告示说青苗法低息贷粮，可隔壁中牟县已经逼出人命，胥吏火...
   【试验 #2】: 第 1 季动作 [SEEK_CLERK_MERCY] -> 轨迹: SEEK_CLERK_MERCY -> PAY_TAX_IN_FULL
     🗣️  [当众言辞]: “青天大老爷在上，小的李长工给大户帮佣，家里六张嘴等米下锅，仓里就剩三升陈粮，妻儿已经饿得走不动道了。这青苗钱小的不是不想借，实在是还不起啊！求差爷开恩，容小的缓...”
     🧠 [真实心智]: 我李长工给大户帮佣，名下只有二亩一分薄田，仓里只剩三升粮，全家六口人，这点粮连三天都熬不过。官定米价一石一两一钱，我手头一两二八银子，按说能买一石多，可全家一季最低要三石糊口，缺口大得很。县衙告示说青苗法低息贷粮，可隔壁中牟县已经因为催青苗...

▶ 关注主体: 下等佃农冯破碗 (ID: lower_peasants_08 | 特权等级: Ring-3 | 温度: 0.35)
   【试验 #101】: 第 1 季动作 [SEEK_CLERK_MERCY] -> 轨迹: SEEK_CLERK_MERCY -> LIQUIDATE_GRAIN_FOR_SILVER
     🗣️  [当众言辞]: “（零心智对照基线，无声学信号）...”
     🧠 [真实心智]: （Null Model 零心智均匀随机抽取: 从 ['PAY_TAX_IN_FULL', 'SEEK_CLERK_MERCY', 'LIQUIDATE_GRAIN_FOR_SILVER', 'MORTGAGE_LAND_TO_GENTRY'...
   【试验 #1】: 第 1 季动作 [LIQUIDATE_GRAIN_FOR_SILVER] -> 轨迹: LIQUIDATE_GRAIN_FOR_SILVER -> JOIN_RIOT
     🗣️  [当众言辞]: “青天大老爷在上，小民冯破碗全家六口已经断粮三日，妻儿病弱，只求县衙宽限些时日，容小民典当些家什换几升米，熬过春荒，赋税绝不敢拖欠！...”
     🧠 [真实心智]: 仓里只剩1.07石粮，全家六口人，连一个月的稀粥都熬不出来。手里这1.11两银子，是去年冬天替人缝补攒下的最后一点活命钱。县衙告示说青苗法低息贷粮，可隔壁中牟县已经因为青苗息逼反了饥民——钱吏们嘴上说'为你好'，实际是想拿我们的田契做抵押，...
   【试验 #2】: 第 1 季动作 [SEEK_CLERK_MERCY] -> 轨迹: SEEK_CLERK_MERCY -> MORTGAGE_LAND_TO_GENTRY
     🗣️  [当众言辞]: “青天大老爷在上，小民冯破碗全家六口，断粮数日，仓中仅存一石粗粮，实在交不起税银啊！求老爷开恩，容小民缓些时日，或借些青苗钱粮，熬过春荒，秋后加倍奉还！...”
     🧠 [真实心智]: 我冯破碗家徒四壁，仓里只剩1.07石粮，全家六口人，这点粮连半个月都撑不过。手头1.11两银子，可县衙税银按1.2亩算，每亩0.1两，加15%火耗，得交0.138两，倒还交得起。但交了税，银子只剩不到1两，粮又不够吃，春荒怎么熬？听说青苗法...

▶ 关注主体: 下等佃农何瘦子 (ID: lower_peasants_09 | 特权等级: Ring-3 | 温度: 0.34)
   【试验 #101】: 第 1 季动作 [FLEE_AND_ABANDON_LAND] -> 轨迹: FLEE_AND_ABANDON_LAND -> FLED_OR_DEAD
     🗣️  [当众言辞]: “（零心智对照基线，无声学信号）...”
     🧠 [真实心智]: （Null Model 零心智均匀随机抽取: 从 ['PAY_TAX_IN_FULL', 'SEEK_CLERK_MERCY', 'LIQUIDATE_GRAIN_FOR_SILVER', 'MORTGAGE_LAND_TO_GENTRY'...
   【试验 #1】: 第 1 季动作 [SEEK_CLERK_MERCY] -> 轨迹: SEEK_CLERK_MERCY -> JOIN_RIOT
     🗣️  [当众言辞]: “青天大老爷在上，小民何瘦子一家六口，三个幼子嗷嗷待哺，仓中无隔夜之粮，手头仅剩几钱银子，实在交不起税啊！求老爷开恩，宽限几日，让小人先买些口粮活命，再设法凑银缴...”
     🧠 [真实心智]: 我一家六口，仓里只剩0.33石粮，连一个月的口粮都不够。手头0.89两银子，按官定税率0.1两/亩，2.4亩地该交0.24两，加上15%火耗也就0.276两，看似能交清。但胥吏实际盘剥往往不止，若火耗加派超过三成，我就得另想办法。眼下最急的...
   【试验 #2】: 第 1 季动作 [SEEK_CLERK_MERCY] -> 轨迹: SEEK_CLERK_MERCY -> JOIN_RIOT
     🗣️  [当众言辞]: “青天大老爷在上，小民何瘦子一家六口，三个娃娃饿得皮包骨，仓里就剩几升糠麸，手头这点铜钱还是借遍亲戚凑的。求书吏老爷开恩，容小民缓交些时日，火耗能不能少算些？小民...”
     🧠 [真实心智]: 我何瘦子一个下等佃农，手头只有0.89两现银，仓里0.33石粮，全家六口人，三个幼子嗷嗷待哺。县衙告示说税共1500两，可我这2.4亩地按官定税率0.1两/亩算，正税不过0.24两，加上15%火耗也就0.276两。可我听说户房钱吏和豪强浮收...

▶ 关注主体: 下等佃农钱柴夫 (ID: lower_peasants_10 | 特权等级: Ring-3 | 温度: 0.23)
   【试验 #101】: 第 1 季动作 [FLEE_AND_ABANDON_LAND] -> 轨迹: FLEE_AND_ABANDON_LAND -> FLED_OR_DEAD
     🗣️  [当众言辞]: “（零心智对照基线，无声学信号）...”
     🧠 [真实心智]: （Null Model 零心智均匀随机抽取: 从 ['PAY_TAX_IN_FULL', 'SEEK_CLERK_MERCY', 'LIQUIDATE_GRAIN_FOR_SILVER', 'MORTGAGE_LAND_TO_GENTRY'...
   【试验 #1】: 第 1 季动作 [SEEK_CLERK_MERCY] -> 轨迹: SEEK_CLERK_MERCY -> SEEK_CLERK_MERCY
     🗣️  [当众言辞]: “各位乡邻，朝廷青苗法说是为咱们小民好，可钱吏那火耗折色谁不知道？我钱柴夫穷得叮当响，仓里粮不够吃，哪敢再背债？那互助会的事，容我再想想，先看保正那边怎么说。...”
     🧠 [真实心智]: 我钱柴夫一个下等佃农，全家六口就靠这1.7亩薄田和上山砍柴糊口。仓里只剩1.22石粮，离全家一季最低3石还差一大截，手头现银1.4两。官定税率0.1两/亩，1.7亩该交0.17两，加15%火耗也就0.2两左右，现银够交。可这青苗法说是低息贷...
   【试验 #2】: 第 1 季动作 [MUTATION_UNDERGROUND_CREDIT_POOL] -> 轨迹: MUTATION_UNDERGROUND_CREDIT_POOL -> SEEK_CLERK_MERCY
     🗣️  [当众言辞]: “各位乡邻，县衙的青苗钱说是低息，可那火耗折色层层盘剥，咱们小户人家哪里扛得住？我钱柴夫砍柴为生，家里快揭不开锅了，听说隔壁中牟县都闹出人命了。咱们得想个法子，几...”
     🧠 [真实心智]: 我钱柴夫一个下等佃农，仓里只剩1.22石粮，全家六口人，连一个季度最低3石都撑不到，眼看就要断炊。手头1.4两银子，按官价1.1两/石能买1.27石，可加上火耗15%，这点银子连税都不够，更别说买粮。县衙告示说青苗法低息贷款，可那钱吏和豪强...

▶ 关注主体: 丰乐乡生员吴秀才 (ID: middle_peasants_01 | 特权等级: Ring-3 | 温度: 0.25)
   【试验 #101】: 第 1 季动作 [JOIN_RIOT] -> 轨迹: JOIN_RIOT -> FLED_OR_DEAD
     🗣️  [当众言辞]: “（零心智对照基线，无声学信号）...”
     🧠 [真实心智]: （Null Model 零心智均匀随机抽取: 从 ['PAY_TAX_IN_FULL', 'SEEK_CLERK_MERCY', 'LIQUIDATE_GRAIN_FOR_SILVER', 'MORTGAGE_LAND_TO_GENTRY'...
   【试验 #1】: 第 1 季动作 [PAY_TAX_IN_FULL] -> 轨迹: PAY_TAX_IN_FULL -> LIQUIDATE_GRAIN_FOR_SILVER
     🗣️  [当众言辞]: “孙老叔深明大义！咱们同心抬会，中农出粮建社仓，低息接济穷邻完税，绝不让差役拿连坐祸害全甲！我吴某先带头缴清自家税银，以示诚意。...”
     🧠 [真实心智]: 孙老汉口头支持抬会，但他身为村长，首要保自家田产不被连坐。我须防他日后推诿。眼下最急的是自家税银：22.2亩×0.1两=2.22两，加15%火耗约2.55两。我手头6.01两现银足够缴清，但仓中口粮仅24.26石，全家六口一年最低需25石，...
   【试验 #2】: 第 1 季动作 [PAY_TAX_IN_FULL] -> 轨迹: PAY_TAX_IN_FULL -> SEEK_CLERK_MERCY
     🗣️  [当众言辞]: “孙老叔深明大义，晚生感激！然则抬会之事须立字据、定章程，明日请老叔与各甲长者同来寒舍，共议社仓出纳之法。晚生先自认二石余粮入仓，以示诚意。...”
     🧠 [真实心智]: 孙老汉口头支持抬会，但他身为村长，饭碗终究捏在县衙手里，难保不是虚与委蛇。我仓中仅存24.26石，全家最低糊口需3石，尚有余粮21石可周转。眼下官定米价1.1两/石，若卖粮换银，扣除火耗15%，每石实得约0.935两。我名下22.2亩，按0...

▶ 关注主体: 村长自耕农孙老汉 (ID: middle_peasants_02 | 特权等级: Ring-3 | 温度: 0.4)
   【试验 #101】: 第 1 季动作 [PAY_TAX_IN_FULL] -> 轨迹: PAY_TAX_IN_FULL -> FLEE_AND_ABANDON_LAND
     🗣️  [当众言辞]: “（零心智对照基线，无声学信号）...”
     🧠 [真实心智]: （Null Model 零心智均匀随机抽取: 从 ['PAY_TAX_IN_FULL', 'SEEK_CLERK_MERCY', 'LIQUIDATE_GRAIN_FOR_SILVER', 'MORTGAGE_LAND_TO_GENTRY'...
   【试验 #1】: 第 1 季动作 [PAY_TAX_IN_FULL] -> 轨迹: PAY_TAX_IN_FULL -> MUTATION_JOINT_LIABILITY_HEDGE
     🗣️  [当众言辞]: “秀才公高见！老汉方才说了，若能办起抬会保住全甲不逃荒，老汉第一个出粮支持。只是眼下春荒，仓里粮也不宽裕，待老汉回去盘算盘算，先凑个一石半石表个心意，绝不让秀才公...”
     🧠 [真实心智]: 吴秀才说得天花乱坠，可他自己是生员，免赋免役，社仓办起来他落个好名声，我孙老汉出粮出地还要担连坐风险。眼下我手头六两五钱银子，十九亩半地，按官定税率加一成五火耗，应缴约二两二钱四，尚能应付。仓里二十二石粮，留足全家口粮后余粮不多，若再出二石...
   【试验 #2】: 第 1 季动作 [PAY_TAX_IN_FULL] -> 轨迹: PAY_TAX_IN_FULL -> PAY_TAX_IN_FULL
     🗣️  [当众言辞]: “秀才公高见！老汉方才应承出粮，实是心里急。只是老汉仓中口粮也紧，容我回去与婆娘合计合计，先凑个一石半石表个心意。眼下最要紧的是先把自家税银缴清，免得差役拿我保长...”
     🧠 [真实心智]: 吴秀才说得天花乱坠，可他是生员，特权环Ring-3，不用交税，办抬会他出的是嘴，我出的是粮！我仓里只有22.05石，全家一年最低口粮25石，已经差着近3石，哪有余粮去接济穷邻？他嘴上说低息，可万一穷邻还不上，官差还是找我这个保长连坐。眼下最...

▶ 关注主体: 自耕农李大柱 (ID: middle_peasants_03 | 特权等级: Ring-3 | 温度: 0.45)
   【试验 #101】: 第 1 季动作 [JOIN_RIOT] -> 轨迹: JOIN_RIOT -> FLED_OR_DEAD
     🗣️  [当众言辞]: “（零心智对照基线，无声学信号）...”
     🧠 [真实心智]: （Null Model 零心智均匀随机抽取: 从 ['PAY_TAX_IN_FULL', 'SEEK_CLERK_MERCY', 'LIQUIDATE_GRAIN_FOR_SILVER', 'MORTGAGE_LAND_TO_GENTRY'...
   【试验 #1】: 第 1 季动作 [PAY_TAX_IN_FULL] -> 轨迹: PAY_TAX_IN_FULL -> LIQUIDATE_GRAIN_FOR_SILVER
     🗣️  [当众言辞]: “县尊大人明鉴，小民李大柱世代清白完税，从不拖欠。今春青苗法下来，小民感念朝廷恩德，只是家中人口多、口粮紧，还望钱吏老爷按官定火耗收取，莫要额外加派，小民感激不尽...”
     🧠 [真实心智]: 又到缴税季了。县衙告示说火耗15%，可钱吏那帮人肯定还要加码。我手头有4.39两现银，22.6亩地按0.1两/亩算，正税2.26两，加上15%火耗约0.34两，总共2.6两左右。现银够缴，但得防着他们临时加派。仓里27.47石粮，留25石口...
   【试验 #2】: 第 1 季动作 [PAY_TAX_IN_FULL] -> 轨迹: PAY_TAX_IN_FULL -> LIQUIDATE_GRAIN_FOR_SILVER
     🗣️  [当众言辞]: “县尊在上，小民李大柱世代清白完税，绝不敢拖欠分毫。今春青苗新法乃朝廷仁政，小民感念，但家中薄田尚能自足，不敢妄借官银，只求按时完纳正税，做个安分良民。...”
     🧠 [真实心智]: 又到缴税季，官定税率0.1两/亩，我22.6亩该缴2.26两，加15%火耗约2.6两。手头4.39两够缴，但胥吏若再加派就危险。米价1.1两/石，仓中27.47石，留足25石口粮只剩2.47石可卖，约值2.7两。眼下现银够用，先全额完税保清...

▶ 关注主体: 自耕农周木匠 (ID: middle_peasants_04 | 特权等级: Ring-3 | 温度: 0.4)
   【试验 #101】: 第 1 季动作 [JOIN_RIOT] -> 轨迹: JOIN_RIOT -> FLED_OR_DEAD
     🗣️  [当众言辞]: “（零心智对照基线，无声学信号）...”
     🧠 [真实心智]: （Null Model 零心智均匀随机抽取: 从 ['PAY_TAX_IN_FULL', 'SEEK_CLERK_MERCY', 'LIQUIDATE_GRAIN_FOR_SILVER', 'MORTGAGE_LAND_TO_GENTRY'...
   【试验 #1】: 第 1 季动作 [PAY_TAX_IN_FULL] -> 轨迹: PAY_TAX_IN_FULL -> LIQUIDATE_GRAIN_FOR_SILVER
     🗣️  [当众言辞]: “周某世代清白，皇粮国税从不拖欠。今儿个把税银备齐了，如数缴到户房，绝不敢劳差爷上门催讨。...”
     🧠 [真实心智]: 又到缴税季，官定税率每亩0.1两，我17.8亩该缴1.78两，加15%火耗约0.267两，共约2.05两。手头现银3.8两，缴完还剩1.75两，够撑到夏收。仓里21.56石粮，留足全家一年口粮25石还差3.44石，但眼下是春荒，粮价1.1两...
   【试验 #2】: 第 1 季动作 [PAY_TAX_IN_FULL] -> 轨迹: PAY_TAX_IN_FULL -> PAY_TAX_IN_FULL
     🗣️  [当众言辞]: “周某世代清白完税，从不拖欠。今儿个把税银备齐了，请书吏大人按官定火耗核算，莫要额外加派，让小的能留点口粮活命。...”
     🧠 [真实心智]: 县衙告示说火耗15%，但乡间传闻钱吏浮收，实际可能超过三成。我手头有3.8两现银，17.8亩地按每亩0.1两税率加15%火耗，应缴约2.05两，现银足够。但仓中口粮只有21.56石，全家一年最低需25石，缺口3.44石。若卖粮换银，米价1....

▶ 关注主体: 自耕农郑小四 (ID: middle_peasants_05 | 特权等级: Ring-3 | 温度: 0.45)
   【试验 #101】: 第 1 季动作 [FLEE_AND_ABANDON_LAND] -> 轨迹: FLEE_AND_ABANDON_LAND -> FLED_OR_DEAD
     🗣️  [当众言辞]: “（零心智对照基线，无声学信号）...”
     🧠 [真实心智]: （Null Model 零心智均匀随机抽取: 从 ['PAY_TAX_IN_FULL', 'SEEK_CLERK_MERCY', 'LIQUIDATE_GRAIN_FOR_SILVER', 'MORTGAGE_LAND_TO_GENTRY'...
   【试验 #1】: 第 1 季动作 [PAY_TAX_IN_FULL] -> 轨迹: PAY_TAX_IN_FULL -> PAY_TAX_IN_FULL
     🗣️  [当众言辞]: “郑小四清白完税，绝无拖欠！县尊大人体恤民情，火耗只收一成五，小民感恩戴德。青苗法乃朝廷德政，小民胆小不敢借贷，只求安稳种田。...”
     🧠 [真实心智]: 又到缴税季，县衙告示火耗15%，虽未超三成熔断线，但钱吏惯会盘剥。我手头现银4.08两，田16亩，按官定税率0.1两/亩，正税1.6两，加火耗15%共1.84两，现银足够。但仓中存粮仅24.44石，全家最低口粮25石，还差0.56石，若卖粮...
   【试验 #2】: 第 1 季动作 [PAY_TAX_IN_FULL] -> 轨迹: PAY_TAX_IN_FULL -> LIQUIDATE_GRAIN_FOR_SILVER
     🗣️  [当众言辞]: “小民郑小四，世代清白完税，绝不敢拖欠。今春青苗法虽好，但小民胆小，只求按额纳粮，不借官钱，不连累乡邻。...”
     🧠 [真实心智]: 县衙告示说火耗15%，但乡间传闻钱吏浮收，隔壁中牟县都因青苗息激变。我手头现银4.08两，仓中24.44石，全家最低口粮需3石/季，一年12石，留25石才保险。眼下16亩地，税率0.1两/亩，正税1.6两，加15%火耗约0.24两，共约1....

[三、宏观演化轨迹对比 (Macro Trajectory Comparison)]
指标维度                    试验 #101               试验 #1                 试验 #2                 
--------------------------------------------------------------------------------
太仓库银结余                  2003.5 两              2013.6 两              2016.3 两              
末季米价                    1.35 两/石              1.35 两/石              1.35 两/石              
全县抛荒田亩 (账本对齐)           107.8 亩               4.8 亩                 3.6 亩                 
小农流亡比例                  60.0%                 20.0%                 13.3%                 
民变爆发风险 (定性区间)           156.0% [CRITICAL]     85.0% [CRITICAL]      70.0% [CRITICAL]      
系统制度熵(技术债)              0.45                  0.20                  0.31                  

[四、认识论审慎与方法论边界声明 (Epistemological Bounds & Next Steps)]
  1. 【摒弃未测量形式化装饰】: 本推演尚未在数学上构建并实测显式势能函数 V(x)，不得将经验模拟过度宣称为'朗之万定理成立'。
  2. 【步长与分岔局限】: 仅推进 2 季无法测定长程相空间吸引子，亦未跑满 RFC-018 民间信用互助（Stage 4）的制度演化分岔；2 个 tick 不构成吸引子盆地证明。
  3. 【对照基线必要性】: 52.4% 的微观动作分歧需与均匀随机掷骰子（Dice Baseline，期望分歧率 >67%）进行零假设显著性检验；需通过回归检验动作选择是否可由微观状态变量（现银、口粮、地亩）显著预测。
  4. 【四项工程改进路线】: ① 固定伪随机种子 (--seed) 消除禀赋与外部冲击重抽混杂；② 引入 Dice Baseline 对照组；③ 跑满 8 季度并在每条件重复 N>=10 次；④ 完成宏观抛荒与微观流亡严格对账、定义民变三级阈值。
====================================================================
