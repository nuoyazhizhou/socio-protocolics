import json
from typing import List, Dict, Any, Optional

class DialogueBus:
    """
    Socio-Engine v2.2/v3.0 微观暗流对话与 P2P 协商总线 (Dialogue & Negotiation Bus)
    在每个季度物理结算前，撮合存在强关系边的微观个体进行端到端对质、密谋、合会商议或道统辩难。
    支持 1~8+ 季度动态演进，杜绝多季度复读静态脚本与认知锚定污染。
    """
    def __init__(self, llm_client: Any = None):
        self.llm_client = llm_client
        self.dialogue_history: List[Dict[str, Any]] = []
        self.last_quarter_encounters: List[Dict[str, Any]] = []

    def get_last_quarter_encounters(self) -> List[Dict[str, Any]]:
        return self.last_quarter_encounters

    def _get_dynamic_cues(self, st: Dict[str, Any], default_cue: str) -> str:
        """根据当前 Agent 最新资产负债表生成动态视觉线索，杜绝资产穿帮"""
        grain = st.get("grain_reserve", 0.0)
        silver = st.get("cash_silver", 0.0)
        status = st.get("survival_status", "ALIVE")
        
        cues = []
        if status in ["FLED", "DEAD"]:
            return "该节点已于此前流亡破产或身故，空留破瓦颓垣。"
        
        if grain <= 0.2:
            cues.append("仓中颗粒无存，面如菜色，眼眶深陷")
        elif grain <= 3.0:
            cues.append("存粮仅余数斗，瓦灶生冷，面带急色")
        elif grain >= 20.0:
            cues.append("仓底老粮尚足，衣着整齐，神色警惕戒备")
            
        if silver <= 0.5:
            cues.append("囊中羞涩无半分碎银，双手因饥寒微颤")
        elif silver >= 5.0:
            cues.append("袖中暗揣完税碎银，步履匆匆唯恐生事")
        elif silver >= 50.0:
            cues.append("锦衣华服，仆役随行，面带从容谋定之色")

        if cues:
            return "；".join(cues) + "。"
        return default_cue

    def _build_encounters_for_tick(
        self,
        tick: int,
        world_state: Dict[str, Any],
        engine: Any
    ) -> List[Dict[str, Any]]:
        """按季度自然节律与制度演化飞轮派发专属剧本"""
        unrest = world_state.get("unrest_risk_score", 0.15)
        abandoned = world_state.get("abandoned_land_mu", 0.0)
        rice_price = world_state.get("rice_price", 1.1)

        # 季度映射: 1=春荒 2=夏熟 3=秋收 4=冬藏
        season_mod = ((tick - 1) % 4) + 1
        year_idx = ((tick - 1) // 4) + 1

        if season_mod == 1:
            # === 第 1 季 / 春荒：青苗贷出与下乡抑配 ===
            return [
                {
                    "id": "OFFICIAL_GENTRY_DEBATE",
                    "speaker_a": "officials_01",
                    "speaker_b": "retired_officials_01",
                    "title": f"【官绅道统较量·第{year_idx}年春荒】祥符知县程元凤 登门拜谒 致仕韩侍郎",
                    "topic": "青苗新法抑配与开封清丈",
                    "script": [
                        ("officials_01", "祥符知县程元凤", "老侍郎容禀：新法乃天子与荆公救弊仁政，年息二分专抑兼并豪强。老侍郎乃三朝耆德，何苦指使族人生员抗拒借贷、阻挠均税？"),
                        ("retired_officials_01", "致仕韩侍郎", "程明府休要欺心！‘散钱收息’名曰惠民，实乃桑弘羊、卢杞聚敛之术！县衙公吏借机逼索火耗，百姓怨声载道，老夫已缮就密折，直递御史台参劾你操切残暴！")
                    ],
                    "impact": "韩侍郎决意发动朝中政治资本发起京控，程知县考核压力与焦躁度剧增！"
                },
                {
                    "id": "OPPORTUNIST_PLOTTING",
                    "speaker_a": "lower_peasants_03",
                    "speaker_b": "lower_peasants_01",
                    "title": f"【游民暗流试探·第{year_idx}年春荒】游民泼皮王二 村头拉拢 佃农陈大",
                    "topic": "官银到手与倒腾私盐试探",
                    "script": [
                        ("lower_peasants_03", "游民泼皮王二", "陈大哥，别愁眉苦脸了！官仓里的青苗银咱已经领出来了。不如听兄弟一句劝：把银子全交给我去汴京倒腾私盐，若赚了平分，若风声紧了，咱哥俩带上盘缠直奔伏牛山入绿林！"),
                        ("lower_peasants_01", "五等佃农陈大", "王二休要胡言！我陈大祖辈本分耕田，宁可全家吃糠咽菜，也绝不干抄家灭族的勾当！你要作死别拉上我和二弟！")
                    ],
                    "impact": "王二见陈大迂腐，暗中下定决心寻找机会卷款潜逃或落草！"
                },
                {
                    "id": "SCHOLAR_MUTUAL_AID",
                    "speaker_a": "middle_peasants_01",
                    "speaker_b": "middle_peasants_02",
                    "title": f"【乡贤自治初议·第{year_idx}年春荒】生员吴秀才 商议 村长自耕农孙老汉",
                    "topic": "创办丰乐乡同心自愿抬会",
                    "script": [
                        ("middle_peasants_01", "丰乐乡生员吴秀才", "孙老叔，公吏下乡强配连坐，分明是拿咱们中农田产给下等穷户垫背！与其坐以待毙，不如咱们三甲合办‘同心抬会’，中农各筹余粮建立社仓，以极低息接济穷邻完税，斩断差役盘剥！"),
                        ("middle_peasants_02", "村长自耕农孙老汉", "秀才公高见！老汉整日提心吊胆，就怕被穷邻连坐破产。若能办起抬会保住全甲不逃荒，老汉第一个出粮支持！")
                    ],
                    "impact": "吴秀才获得乡村老辈支持，正式准备发起民间自治抬会抵御官僚抑配！"
                },
                {
                    "id": "SACRED_KINSHIP",
                    "speaker_a": "lower_peasants_01",
                    "speaker_b": "lower_peasants_02",
                    "title": f"【骨肉手足密语·第{year_idx}年春荒】五等佃农陈大 叮嘱 幼弟陈二",
                    "topic": "断炊绝境下的生存分工",
                    "script": [
                        ("lower_peasants_01", "五等佃农陈大", "二弟，家中就剩这点杂粮糊糊，你全喝了！明日差役下乡催逼利息，我若被锁拿，你千万别冲动，把地窖里的两升杂粮守好，活下去！"),
                        ("lower_peasants_02", "五等佃农陈二", "哥！我不喝！要抓抓我！我怀里揣着磨利的柴刀，公吏要是敢下死手，我跟他拼了！打死一个够本，咱弟兄死也要死在一处！")
                    ],
                    "impact": "陈氏兄弟确立绝对生死同盟，极大推高极端心智抗暴阈值！"
                },
                {
                    "id": "CLERK_EXTORTION_DECEPTION",
                    "speaker_a": "clerks_01",
                    "speaker_b": "lower_peasants_01",
                    "title": f"【胥吏下乡推配·第{year_idx}年春荒】经管钱吏张文远 催逼 佃农陈大",
                    "topic": "青苗官贷强配与折色火耗盘剥",
                    "script": [
                        ("clerks_01", "经管钱吏张文远", "陈大哥，天大的喜事！朝廷推行常平新法，年息只要二分，专为救济尔等穷苦小民！知县相公仁厚，特批本甲五等户借贷三贯！你且速速按下手印画押，立刻领银去买谷种！"),
                        ("lower_peasants_01", "五等佃农陈大", "差爷容禀……小人家中只有两亩薄洼地，秋收就算丰收也卖不出三贯钱。且听说借官银过手要扣头子钱、折色算糙粮，小人万万不敢承领啊！")
                    ],
                    "impact": "张文远以仁政为名行抑配之实，陈大看穿中介掠夺，暗中严防死锁！"
                }
            ]

        elif season_mod == 2:
            # === 第 2 季 / 夏熟：青黄不接与夏税催征 ===
            return [
                {
                    "id": "OFFICIAL_GENTRY_DEBATE",
                    "speaker_a": "retired_officials_01",
                    "speaker_b": "officials_01",
                    "title": f"【官绅公堂质辩·第{year_idx}年夏熟】致仕韩侍郎 公堂质问 祥符知县程元凤",
                    "topic": "夏税火耗浮收与开封清丈冲突",
                    "script": [
                        ("retired_officials_01", "致仕韩侍郎", "程明府！夏粮刚刚过秤，各乡斗级钱吏便浮收火耗至三成以上，青黄不接米价飞涨至一两三钱余！你口称均税，县衙却任由胥吏踢门锁拿，逼得小农卖儿鬻女，这就是你的新法善政？"),
                        ("officials_01", "祥符知县程元凤", "韩老侍郎休要避重就轻！本县正清查城外寄庄隐田，韩府名下三百五十亩良田仅按七十亩纳粮，飞洒诡寄何其猖獗！豪强匿税在先，反诬官府操切，本县绝不退让半步！")
                    ],
                    "impact": "官绅矛盾彻底激化，知县加紧严催夏税，乡绅暗中加快联合弹劾部署！"
                },
                {
                    "id": "OPPORTUNIST_PLOTTING",
                    "speaker_a": "lower_peasants_03",
                    "speaker_b": "middle_peasants_02",
                    "title": f"【游民避役窥伺·第{year_idx}年夏熟】游民王二 探听 村长孙老汉",
                    "topic": "连坐风声与流亡退路",
                    "script": [
                        ("lower_peasants_03", "游民泼皮王二", "保长叔，听说差役今晚要下乡点名抓丁催税？邻县中牟已经闹出人命了。这破地方税比命重，小侄劝你别死撑着当保长了，赶紧分粮防灾吧！"),
                        ("middle_peasants_02", "村长自耕农孙老汉", "畜生休要妖言惑众！官府保甲连坐，你若敢脚底抹油，差役第一个拿我孙老汉抵数！老汉哪怕砸锅卖铁，也绝不容你在本保胡来！")
                    ],
                    "impact": "王二察知保长戒备森严，潜逃决心进一步升级为连夜突袭卷款！"
                },
                {
                    "id": "SCHOLAR_MUTUAL_AID",
                    "speaker_a": "middle_peasants_02",
                    "speaker_b": "middle_peasants_01",
                    "title": f"【乡贤自保决裂·第{year_idx}年夏熟】村长孙老汉 决绝回应 生员吴秀才",
                    "topic": "自家存粮短缺与拒绝代偿自救",
                    "script": [
                        ("middle_peasants_02", "村长自耕农孙老汉", "秀才公休怪老汉心狠！老汉昨夜盘了粮仓，全家存粮离保命还缺三石。眼下差役抓人甚急，我自家税银尚不知能否保全，哪有余粮去接济穷邻办抬会？各人顾各人吧！"),
                        ("middle_peasants_01", "丰乐乡生员吴秀才", "孙老叔糊涂啊！唇亡齿寒，下等户若全部破产逃荒，官差追索欠款必定全落到中农头上！此时不守望相助，明日皆为砧上鱼肉！")
                    ],
                    "impact": "自耕农阶层因自身口粮危机优先选择闭门自保，民间自愿互助网络宣告胎死腹中！"
                },
                {
                    "id": "SACRED_KINSHIP",
                    "speaker_a": "lower_peasants_01",
                    "speaker_b": "lower_peasants_02",
                    "title": f"【骨肉绝粮死守·第{year_idx}年夏熟】佃农陈大 按住 幼弟陈二",
                    "topic": "粮绝门催与死守柴刀",
                    "script": [
                        ("lower_peasants_01", "五等佃农陈大", "二弟把刀放下！仓里最后一升糙米已经见底，差役在村口敲锣，我先去户房向文远差爷磕头求告，求他念在同乡份上宽展由票。千万别动刀！"),
                        ("lower_peasants_02", "五等佃农陈二", "哥！求告有什么用！赵押司带着狼牙棍，进门就要钱！他们不给穷人活路，我绝不看着你被铁索锁走受辱！")
                    ],
                    "impact": "陈大被迫独自走向衙门求怜，陈二极端反抗情绪临界饱和！"
                },
                {
                    "id": "CLERK_EXTORTION_DECEPTION",
                    "speaker_a": "clerks_02",
                    "speaker_b": "lower_peasants_01",
                    "title": f"【公吏踢门催逼·第{year_idx}年夏熟】催征押司赵都头 厉声催迫 佃农陈大",
                    "topic": "夏税火耗即时过秤与铁枷威逼",
                    "script": [
                        ("clerks_02", "催征押司赵都头", "陈大！少在老子面前装穷号丧！知县相公限三日内完纳夏税与借贷火耗，你名下积欠二钱四分碎银，今日交不出，立刻铁枷锁走，送大牢吃杀威棒！"),
                        ("lower_peasants_01", "五等佃农陈大", "赵都头开恩！小人田里夏麦遭了旱，仓底已干涸见石，求宽限十日，待小人去典当行把祖传地契押了换银……")
                    ],
                    "impact": "基层暴力催税将下等农户逼至破产抵押断崖，民怨指数剧烈拉升！"
                }
            ]

        elif season_mod == 3:
            # === 第 3 季 / 秋收：官贷还本加息与连坐逼索 ===
            return [
                {
                    "id": "OFFICIAL_GENTRY_DEBATE",
                    "speaker_a": "upper_gentry_01",
                    "speaker_b": "retired_officials_01",
                    "title": f"【士绅抄底议市·第{year_idx}年秋收】西关典当孙掌柜 密商 致仕韩侍郎",
                    "topic": "小农断贷与折价受田兼并",
                    "script": [
                        ("upper_gentry_01", "西关典当孙掌柜", "老侍郎，眼下秋收催息甚急，五等小农无银还贷，纷纷拿地契来典当换粮。小人打算将折色压低四成，一亩上田只作五斗米折给他们，日后转为韩府佃田，您看如何？"),
                        ("retired_officials_01", "致仕韩侍郎", "在商言商，市易契约愿者上钩，此乃小农自愿质当活命，非兼并也。收下地契后，尽快将田亩挂入韩府义庄，官府清丈便奈何不得。")
                    ],
                    "impact": "士绅中介层通过典当行开启大规模土地兼并，基层产权加速向寡头集中！"
                },
                {
                    "id": "OPPORTUNIST_PLOTTING",
                    "speaker_a": "middle_peasants_02",
                    "speaker_b": "middle_peasants_01",
                    "title": f"【连坐惊惶催命·第{year_idx}年秋收】村长孙老汉 哀诉 生员吴秀才",
                    "topic": "游民逃亡引发保甲连坐代偿",
                    "script": [
                        ("middle_peasants_02", "村长自耕农孙老汉", "秀才公！大祸临头了！下保游民王二卷了借银连夜潜逃入山，差役拿批回封了村口，硬逼老汉与三甲自耕农代偿他欠下的本息火耗！这分明是要榨干老汉骨髓啊！"),
                        ("middle_peasants_01", "丰乐乡生员吴秀才", "岂有此理！官吏抑配在先，逃亡株连在后！孙老叔勿慌，晚生即刻联络开封诸生草拟保甲鸣冤状，直叩按察使行辕！")
                    ],
                    "impact": "保甲连坐直接击中中农资产负债表，自耕农阶层恐慌蔓延，开始动摇对朝廷秩序的信任！"
                },
                {
                    "id": "SCHOLAR_MUTUAL_AID",
                    "speaker_a": "middle_peasants_01",
                    "speaker_b": "lower_peasants_07",
                    "title": f"【诸生联名哭庙·第{year_idx}年秋收】生员吴秀才 发动 佃农李长工",
                    "topic": "联名文庙哭诉与抵制抑配",
                    "script": [
                        ("middle_peasants_01", "丰乐乡生员吴秀才", "李大哥，秋粮全被差役封仓充折火耗，咱们再不争就是饿死！明日随我至县学文庙跪哭先师，向提刑御史呈递万民血书，痛陈新法抑配实情！"),
                        ("lower_peasants_07", "下等佃农李长工", "吴相公，小人一介泥腿子，字都不识，只求能给娃儿留口粗饭。相公若敢领头，小人愿按血手印！")
                    ],
                    "impact": "乡村知识分子与底层佃农结成抗法政治联盟，体制内上访抗争启动！"
                },
                {
                    "id": "SACRED_KINSHIP",
                    "speaker_a": "lower_peasants_01",
                    "speaker_b": "lower_peasants_02",
                    "title": f"【指苗预卖自残·第{year_idx}年秋收】佃农陈大 叹息 幼弟陈二",
                    "topic": "青谷折价套现与断炊死结",
                    "script": [
                        ("lower_peasants_01", "五等佃农陈大", "二弟，秋粮刚熟，县衙就要加息收回青苗银。我私下找孙掌柜‘指苗预卖’，将秋谷折了四成换得现银完税。今年冬天……咱们怕是只能靠挖野菜树皮过冬了。"),
                        ("lower_peasants_02", "五等佃农陈二", "哥！折了四成，那地里辛苦一年全替典当掌柜白干了！这地咱们还种它作甚？不如一把火烧了逃去关外！")
                    ],
                    "impact": "佃农通过金融贴水勉强苟延残喘，但实际卡路里缺口在冬季彻底暴露！"
                },
                {
                    "id": "CLERK_EXTORTION_DECEPTION",
                    "speaker_a": "clerks_01",
                    "speaker_b": "clerks_02",
                    "title": f"【胥吏分赃隐亏·第{year_idx}年秋收】经管钱吏张文远 密语 押司赵都头",
                    "topic": "全县亏空掩盖与死账飞洒",
                    "script": [
                        ("clerks_01", "经管钱吏张文远", "赵兄弟，全县秋粮回笼差着三成，知县考成限期就在眼前。咱们必须把逃亡王二、刘孤儿名下的欠款改注为‘灾伤蠲免’，把平余扣留下来，否则你我都得挨板子！"),
                        ("clerks_02", "催征押司赵都头", "全听文远兄调度！只要底册账目做得圆泛，上头提举官走马观花，查不出这笔烂账！")
                    ],
                    "impact": "胥吏阶层完成技术债掩盖与隐秘寻租联盟，官府数据彻底失真！"
                }
            ]

        else:
            # === 第 4 季 / 严冬：风雪断炊与系统民变临界 ===
            return [
                {
                    "id": "OFFICIAL_GENTRY_DEBATE",
                    "speaker_a": "officials_01",
                    "speaker_b": "retired_officials_01",
                    "title": f"【官绅终局摊牌·第{year_idx}年严冬】祥符知县程元凤 登门怒斥 致仕韩侍郎",
                    "topic": "御史台劾奏与全县考核绝境",
                    "script": [
                        ("officials_01", "祥符知县程元凤", "韩老侍郎好狠的手段！御史台风闻奏事，痛参本县‘抑配激变、民不聊生’，朝廷明旨着本县停职待勘！豪强勾结台谏，活活掐死变法善政！"),
                        ("retired_officials_01", "致仕韩侍郎", "程知县，自作孽不可活！老夫早言聚敛必致祸乱。如今全县逃亡抛荒数十顷，饥民聚于城门，若非老夫施粥弹压，县衙早已被民变踏平！")
                    ],
                    "impact": "知县政治生命濒临破产，行政权威彻底瓦解，地方秩序落入缙绅私家武装之手！"
                },
                {
                    "id": "OPPORTUNIST_PLOTTING",
                    "speaker_a": "lower_peasants_08",
                    "speaker_b": "lower_peasants_09",
                    "title": f"【饥民啸聚抗粮·第{year_idx}年严冬】下等佃农冯破碗 联络 何瘦子",
                    "topic": "风雪绝产与打烂粮仓",
                    "script": [
                        ("lower_peasants_08", "下等佃农冯破碗", "瘦子！仓里最后一捧糠也没了，妻儿冻饿待毙！差役还要来锁人抵债！横竖是死，与其冻死沟壑，不如抄起锄头打进城去抢了粮仓！"),
                        ("lower_peasants_09", "下等佃农何瘦子", "反了！反了！官家逼得人没活路，反了他娘的！谁不让老子活，老子就让谁全家陪葬！")
                    ],
                    "impact": "绝境赤贫阶层触发不可逆暴力相变，全县民变指数逼近爆表极值！"
                },
                {
                    "id": "SCHOLAR_MUTUAL_AID",
                    "speaker_a": "middle_peasants_02",
                    "speaker_b": "middle_peasants_01",
                    "title": f"【中农破产哀歌·第{year_idx}年严冬】村长自耕农孙老汉 泣诉 生员吴秀才",
                    "topic": "积蓄荡尽与自耕农解体",
                    "script": [
                        ("middle_peasants_02", "村长自耕农孙老汉", "秀才公……老汉三代勤俭攒下的二十亩水田，全充了逃户的垫赔和连坐火耗！现银全无，老粮耗尽，老汉明日也要沦为孙掌柜家的佃户了……"),
                        ("middle_peasants_01", "丰乐乡生员吴秀才", "三十年耕读传家，一朝化为乌有！这哪是青苗惠民，分明是吸髓刮骨！晚生无颜再读圣贤之书！")
                    ],
                    "impact": "作为地方财政承重墙的中等自耕农阶层彻底被制度吸干，基层税基全面坍塌！"
                },
                {
                    "id": "SACRED_KINSHIP",
                    "speaker_a": "lower_peasants_01",
                    "speaker_b": "lower_peasants_02",
                    "title": f"【雪夜抛荒逃亡·第{year_idx}年严冬】佃农陈大 背负 幼弟陈二",
                    "topic": "弃田逃荒与落草伏牛山",
                    "script": [
                        ("lower_peasants_01", "五等佃农陈大", "二弟，收拾破席烂锅，咱们连夜走！田契已绝，差役明日又来点卯拿人充军。走！逃出开封府，投伏牛山绿林去！"),
                        ("lower_peasants_02", "五等佃农陈二", "哥！听你的！烧了这间破草房，给那帮狗官留个白地！咱们弟兄上山当好汉去！")
                    ],
                    "impact": "核心农户彻底从体制脱钩流亡，全县抛荒面积与流亡人口跳跃式上升！"
                },
                {
                    "id": "CLERK_EXTORTION_DECEPTION",
                    "speaker_a": "upper_gentry_01",
                    "speaker_b": "clerks_01",
                    "title": f"【豪强收割寡头·第{year_idx}年严冬】西关典当孙掌柜 宴请 钱吏张文远",
                    "topic": "绝田收割与次级垄断均衡落地",
                    "script": [
                        ("upper_gentry_01", "西关典当孙掌柜", "文远老弟，这一年辛苦！全县抛荒的六十顷绝田，契约已尽入我手。官府那头还望兄弟通融，仍按荒地报灾蠲免，日后田租分成，少不了老弟的一成干股！"),
                        ("clerks_01", "经管钱吏张文远", "孙掌柜爽快！只要太仓有银两交账，底册如何填写全在兄弟一笔之间！祝掌柜广置良田、财源茂盛！")
                    ],
                    "impact": "官僚中介与商贾豪强完成闭环分赃，制度演化滑入残酷的寡头兼并终局！"
                }
            ]

    def run_quarterly_dialogues(
        self,
        run_id: str,
        tick: int,
        world_state: Dict[str, Any],
        agents: List[Any],
        engine: Any,
        shocks: Optional[List[Dict[str, Any]]] = None
    ) -> Dict[str, List[str]]:
        """
        运行季度微观对话阶段，返回 {agent_id: [dialogue_transcripts]}
        """
        agent_map = {ag.agent_id: ag for ag in agents}
        dialogues_by_agent: Dict[str, List[str]] = {ag.agent_id: [] for ag in agents}
        self.last_quarter_encounters = []

        encounters = self._build_encounters_for_tick(tick, world_state, engine)

        print(f"\n  💬 ══════════════════════════════════════════════════════════")
        print(f"  💬 [第 {tick:02d} 轮微观暗流对话与私下协商 (Dialogue & Negotiation)]")
        print(f"  💬 ══════════════════════════════════════════════════════════")

        for enc in encounters:
            sp_a = enc["speaker_a"]
            sp_b = enc["speaker_b"]

            # 校验双方是否都在世
            ag_a = agent_map.get(sp_a)
            ag_b = agent_map.get(sp_b)
            if not ag_a or not ag_b:
                continue

            # 检查存活状态与动态资产
            st_a_raw = engine.get_agent_state_json(sp_a)
            st_b_raw = engine.get_agent_state_json(sp_b)
            if not st_a_raw or not st_b_raw:
                continue

            st_a = json.loads(st_a_raw)
            st_b = json.loads(st_b_raw)
            
            # 若任意一方已逃荒或死亡，跳过该特定面对面遭遇
            if st_a.get("survival_status") in ["FLED", "DEAD"] or st_b.get("survival_status") in ["FLED", "DEAD"]:
                continue

            print(f"\n  ▶ {enc['title']}")
            transcript_lines = []
            for sp_id, sp_name, speech in enc["script"]:
                print(f"    🗣️  [{sp_name}]: “{speech}”")
                transcript_lines.append(f"{sp_name}: “{speech}”")

                # 记录入不可篡改 SQLite 账本
                other_id = sp_b if sp_id == sp_a else sp_a
                try:
                    engine.record_dialogue(
                        run_id=run_id,
                        tick_index=tick,
                        speaker_id=sp_id,
                        listener_id=other_id,
                        channel="PRIVATE_WHISPER",
                        prompt=f"Dialogue encounter on {enc['topic']}",
                        response=speech,
                        intent=enc["impact"]
                    )
                except Exception as err:
                    pass

            cue_a = self._get_dynamic_cues(st_a, f"{ag_a.role_name}神色严峻")
            cue_b = self._get_dynamic_cues(st_b, f"{ag_b.role_name}面带谋算")
            cues = {sp_a: cue_a, sp_b: cue_b}
            edge_desc = enc.get("relationship_edge", "地缘宗族与政经交叠网络")
            
            self.last_quarter_encounters.append({
                "id": enc["id"],
                "title": enc["title"],
                "topic": enc["topic"],
                "speaker_a": sp_a,
                "speaker_b": sp_b,
                "name_a": ag_a.role_name,
                "name_b": ag_b.role_name,
                "script": enc["script"],
                "impact": enc["impact"],
                "observable_cues": cues,
                "relationship_edge": edge_desc
            })
            
            # 为 Agent A (sp_a) 构建多维心智感知包
            summary_a = (
                f"【现场对质交涉】{enc['title']}：\n"
                f"  - 交谈对方: {ag_b.role_name} (特权等级: Ring-{ag_b.privilege_ring})\n"
                f"  - 亲眼目睹对方物理状态与神色: {cue_b}\n"
                f"  - 双方历史关系纽带: {edge_desc}\n"
                f"  - 现场往来对话:\n    " + "\n    ".join(transcript_lines) + f"\n"
                f"  - 事件走向与余波: {enc['impact']}\n"
                f"  - 【博弈心智提示】: 察其位、观其行、辨其意！谨记‘说什么、做什么、是什么是三件事’！对方口头言辞可能是声学欺诈，请盯死其特权环与物理做功动机！"
            )
            dialogues_by_agent[sp_a].append(summary_a)

            # 为 Agent B (sp_b) 构建多维心智感知包
            summary_b = (
                f"【现场对质交涉】{enc['title']}：\n"
                f"  - 交谈对方: {ag_a.role_name} (特权等级: Ring-{ag_a.privilege_ring})\n"
                f"  - 亲眼目睹对方物理状态与神色: {cue_a}\n"
                f"  - 双方历史关系纽带: {edge_desc}\n"
                f"  - 现场往来对话:\n    " + "\n    ".join(transcript_lines) + f"\n"
                f"  - 事件走向与余波: {enc['impact']}\n"
                f"  - 【博弈心智提示】: 察其位、观其行、辨其意！谨记‘说什么、做什么、是什么是三件事’！对方口头言辞可能是声学欺诈，请盯死其特权环与物理做功动机！"
            )
            dialogues_by_agent[sp_b].append(summary_b)

        return dialogues_by_agent
