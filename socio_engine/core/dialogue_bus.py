import json
from typing import List, Dict, Any, Optional

class DialogueBus:
    """
    Socio-Engine v2.2/v3.0 微观暗流对话与 P2P 协商总线 (Dialogue & Negotiation Bus)
    在每个季度物理结算前，撮合存在强关系边的微观个体进行端到端对质、密谋、合会商议或道统辩难。
    对话产物将直接沉淀为：
    1. 双方记忆与私有观察 (注入 System 2 Prompt 上下文)
    2. 持久化记录到不可篡改数据库 (dialogue_logs)
    3. 诱发突发行为 (如王二卷款潜逃、吴秀才创办抬会、韩侍郎密折京控)
    """
    def __init__(self, llm_client: Any = None):
        self.llm_client = llm_client
        self.dialogue_history: List[Dict[str, Any]] = []

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

        encounters = [
            # 1. 官绅道统对弈: 程知县 vs 致仕韩侍郎
            {
                "id": "OFFICIAL_GENTRY_DEBATE",
                "speaker_a": "officials_01",
                "speaker_b": "retired_officials_01",
                "title": "【官绅道统较量】祥符知县程元凤 登门拜谒 致仕韩侍郎",
                "topic": "青苗新法抑配与开封清丈",
                "script": [
                    ("officials_01", "祥符知县程元凤", "老侍郎容禀：新法乃天子与荆公救弊仁政，年息二分专抑兼并豪强。老侍郎乃三朝耆德，何苦指使族人生员抗拒借贷、阻挠均税？"),
                    ("retired_officials_01", "致仕韩侍郎", "程明府休要欺心！‘散钱收息’名曰惠民，实乃桑弘羊、卢杞聚敛之术！县衙公吏借机逼索火耗，百姓怨声载道，老夫已缮就密折，直递御史台参劾你操切残暴！")
                ],
                "impact": "韩侍郎决意发动朝中政治资本发起京控，程知县考核压力与焦躁度剧增！"
            },
            # 2. 游民暗流试探: 泼皮王二 vs 佃农伙伴 (陈大或赵瞎子)
            {
                "id": "OPPORTUNIST_PLOTTING",
                "speaker_a": "lower_peasants_03",
                "speaker_b": "lower_peasants_01",
                "title": "【游民暗流密谋】游民泼皮王二 村头拉拢 佃农陈大",
                "topic": "官银到手与卷款潜逃试探",
                "script": [
                    ("lower_peasants_03", "游民泼皮王二", "陈大哥，别愁眉苦脸了！官仓里的青苗银咱已经借出来了，下半年秋粮还要加息归还。不如听兄弟一句劝：把银子全交给我去汴京倒腾私盐，若赚了平分，若风声紧了，咱哥俩带上盘缠直奔伏牛山入绿林！"),
                    ("lower_peasants_01", "五等佃农陈大", "王二，你休要胡言！我陈大祖辈本分耕田，宁可全家吃糠咽菜，也绝不干抄家灭族的勾当！你要作死别拉上我和二弟！")
                ],
                "impact": "王二见陈大迂腐，暗中下定决心：下个季度独自卷走所有拼单本金连夜潜逃！"
            },
            # 3. 乡村知识分子自治: 生员吴秀才 vs 村长自耕农孙老汉
            {
                "id": "SCHOLAR_MUTUAL_AID",
                "speaker_a": "middle_peasants_01",
                "speaker_b": "middle_peasants_02",
                "title": "【乡贤自治议事】生员吴秀才 商议 自耕农孙老汉",
                "topic": "创办丰乐乡同心自愿抬会",
                "script": [
                    ("middle_peasants_01", "丰乐乡生员吴秀才", "孙老叔，县衙公吏下乡强配连坐，分明是拿咱们中农的田产给下等穷户垫背！一旦有人逃荒，官差必查封咱们老粮。与其坐以待毙，不如咱们三甲合办‘同心抬会’，中农各筹二石余粮建立社仓，以极低息接济穷邻完税，斩断差役盘剥！"),
                    ("middle_peasants_02", "村长自耕农孙老汉", "秀才公高见！老汉整日提心吊胆，就怕被穷邻连坐破产。若能办起抬会保住全甲不逃荒，老汉第一个出粮支持！")
                ],
                "impact": "吴秀才获得乡村老辈支持，正式准备发起民间自治抬会抵御官僚抑配！"
            },
            # 4. 生死手足相依: 佃农陈大 vs 陈二
            {
                "id": "SACRED_KINSHIP",
                "speaker_a": "lower_peasants_01",
                "speaker_b": "lower_peasants_02",
                "title": "【骨肉手足密语】五等佃农陈大 叮嘱 幼弟陈二",
                "topic": "断炊绝境下的生存分工",
                "script": [
                    ("lower_peasants_01", "五等佃农陈大", "二弟，家中就剩这半碗高粱糊糊，你全喝了！明日差役下乡催逼利息，我若被锁拿，你千万别冲动，把地窖里的两升杂粮守好，活下去！"),
                    ("lower_peasants_02", "五等佃农陈二", "哥！我不喝！要抓抓我！我怀里揣着磨利的柴刀，公吏要是敢下死手，我跟他拼了！打死一个够本，咱弟兄死也要死在一处！")
                ],
                "impact": "陈氏兄弟确立绝对生死同盟，极大推高极端心智抗暴阈值！"
            }
        ]

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

            # 检查存活状态
            st_a = json.loads(engine.get_agent_state_json(sp_a))
            st_b = json.loads(engine.get_agent_state_json(sp_b))
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
                        channel_type="PRIVATE_WHISPER",
                        raw_prompt=f"Dialogue encounter on {enc['topic']}",
                        raw_response=speech,
                        parsed_intent=enc["impact"]
                    )
                except Exception:
                    pass

            dialogue_summary = f"{enc['title']}：\n" + "\n".join(transcript_lines) + f"\n【后续影响】: {enc['impact']}"
            dialogues_by_agent[sp_a].append(dialogue_summary)
            dialogues_by_agent[sp_b].append(dialogue_summary)

        return dialogues_by_agent

