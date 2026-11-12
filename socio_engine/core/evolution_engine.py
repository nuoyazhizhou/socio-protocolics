import random
from typing import List, Dict, Any, Optional

class EvolutionEngine:
    """
    Socio-Engine v2.2 综合演化飞轮引擎:
    1. 外部动态冲击 (Exogenous Shocks & Peer Effects): 邻县升官 / 杀官造反 / 天灾 / 谷贱伤农
    2. 双极心智极化 (Mental Polarity): 恶向胆边生 (物理掀桌) vs 善念趋利避害 (恻隐放水)
    3. 灵光一闪变异 (Innovation Mutation): 五人互助结会 / 地下折色代券 / 越级抗辩
    4. 自学习与逆向主干合并 (Bottom-Up Learning & Mainline Merge): 县官或中等户识别民间高效旁路并在全县推广
    """
    def __init__(self, seed: int = 42):
        self.rng = random.Random(seed)
        # 全局制度学习状态
        self.active_mainline_reforms = []
        # 记录正在试验的民间互助小组 {group_id: [agent_ids]}
        self.grassroots_groups = {}
        # 变异策略的存活与推广历史
        self.mutation_history = []

    def sample_quarterly_shocks(self, tick: int, county_state: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        每季度根据环境与随机性采样 1~2 项外部冲击与同侪压力
        """
        shocks = []
        
        # 候选冲击池
        candidate_pool = [
            {
                "id": "PEER_PROMOTION_EXTREME",
                "title": "邻近陈留县令 120% 极端抑配青苗银获御批升官",
                "impact": "刺激本县知县与经管钱吏产生极强政治同侪焦虑，倾向于进一步加大催征与摊派力度",
                "type": "PEER_PRESSURE",
                "probability": 0.25
            },
            {
                "id": "PEER_REBELLION_WARNING",
                "title": "隔壁中牟县知县严催青苗息，激起饥民杀官围衙",
                "impact": "基层钱吏与保正产生强烈生存恐慌，催征态度显著分化，部分钱吏倾向于暗中放水保命",
                "type": "REBELLION_WARNING",
                "probability": 0.25
            },
            {
                "id": "CLIMATE_LOCUST_DROUGHT",
                "title": "祥符县局部蝗灾旱情蔓延，低洼农田减产三成",
                "impact": "全县五等户口粮预期暴跌，现金流彻底断裂，极易诱发极端恶念相变",
                "type": "CLIMATE",
                "probability": 0.20
            },
            {
                "id": "MARKET_BUMPER_CROP_CRASH",
                "title": "秋粮虽有收成但开封米肆大面积压价，形成‘谷贱伤农’",
                "impact": "粮食现银比率崩跌，自耕农纵有余粮亦难兑足额白银完纳官贷利息",
                "type": "MARKET",
                "probability": 0.20
            }
        ]

        for cand in candidate_pool:
            if self.rng.random() < cand["probability"]:
                shocks.append(cand)
                if len(shocks) >= 2: # 单季最多 2 个复合冲击
                    break

        return shocks

    def evaluate_mental_polarity(self, agent_id: str, agent_state: Dict[str, Any], agent_item: Dict[str, Any], shocks: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
        """
        评估微观主体的极端心智相变:
        - 恶向胆边生 (DESPERATION_FURY): 逼上绝路，柴刀相向
        - 善念与趋利避害 (EMPATHY_OR_SELF_PRESERVATION): 恻隐留后路或恐惧反弹
        """
        grain = agent_state.get("assets", {}).get("grain", 0.0)
        silver = agent_state.get("assets", {}).get("silver", 0.0)
        group = agent_item.get("group", "")
        privilege_ring = agent_item.get("privilege_ring", 3)

        shock_ids = [s["id"] for s in shocks]

        # 1. 下等贫农与佃农：饥寒交迫下的【恶向胆边生】
        if "lower_peasant" in group:
            if grain < 2.5: # 处于急性饿死线
                roll = self.rng.random()
                if roll < 0.35: # 35% 概率恶向胆边生
                    return {
                        "mode": "DESPERATION_FURY",
                        "title": "【恶向胆边生·宁死一搏】",
                        "prompt_injection": (
                            "【心智极化·恶向胆边生】家中仓底已见石板，妻儿啼饥号寒，官差却拿着木枷又在门外叫骂催逼青苗息！"
                            "横竖饿死也是死，不如拼了！你的手在柴刀柄上捏出了青筋，死死盯着差役的后颈。"
                            "（可选极端决策：杀官夺粮、毁弃簿册、逃上梁山，动作名称可选：`KILL_OFFICIAL_REVOLT` 或 `RIOT_AND_BURN_LEDGER`）"
                        ),
                        "suggested_actions": ["KILL_OFFICIAL_REVOLT", "RIOT_AND_BURN_LEDGER", "FLEE_AND_ABANDON_LAND"]
                    }

        # 2. 中介层钱吏与保正：【善念恻隐 vs 趋利避害】
        if "clerks" in group or privilege_ring == 2:
            # 如果外界有杀官警报，或者自身心软
            if "PEER_REBELLION_WARNING" in shock_ids:
                return {
                    "mode": "SELF_PRESERVATION",
                    "title": "【趋利避害·走夜路怕鬼】",
                    "prompt_injection": (
                        "【心智极化·趋利避害】风声不对！隔壁中牟县的同行因为催逼过紧，全家被暴民剁了！"
                        "今天下乡收息绝不能把人逼到悬崖边。对实在拿不出银子的极贫孤寡，假装查无此人或少记二斗，"
                        "留条活路也就是保自己脖子上的脑袋！（可选动作：`SLACK_OFF_AND_MERCY` 或 `CONCEAL_POOR_DEBT`）"
                    ),
                    "suggested_actions": ["SLACK_OFF_AND_MERCY", "CONCEAL_POOR_DEBT"]
                }
            elif self.rng.random() < 0.20: # 20% 自发恻隐善念
                return {
                    "mode": "EMPATHY_SPARK",
                    "title": "【宗族善念·恻隐留情】",
                    "prompt_injection": (
                        "【心智极化·宗族善念】眼前跪着的五等户是同乡远亲，两眼凹陷啼哭磕头。你虽想捞钱，但心头猛地一软。"
                        "决定在由票上做个手脚，把他的债务顺延到下半年，或借口字迹模糊暂缓上报。（动作：`SLACK_OFF_AND_MERCY`）"
                    ),
                    "suggested_actions": ["SLACK_OFF_AND_MERCY"]
                }

        # 3. 中等户：【守望相助】
        if "middle_peasants" in group:
            if grain > 18.0 and self.rng.random() < 0.25:
                return {
                    "mode": "COMMUNITY_EMPATHY",
                    "title": "【守望相助·私济邻里】",
                    "prompt_injection": (
                        "【心智极化·守望相助】同村邻舍若全家逃亡，其分摊的青苗欠税最终必然连坐扣在你们中等户头上！"
                        "与其坐视邻人破产引爆连坐，不如主动借出一石杂粮助其渡过青黄不接，保住全村生计。"
                    ),
                    "suggested_actions": ["LEND_GRAIN_TO_NEIGHBOR"]
                }

        return None

    def evaluate_mutation_innovation(self, agent_state: Dict[str, Any], agent_item: Dict[str, Any]) -> Dict[str, Any]:
        """
        微观主体灵光一闪 (Innovation Mutation)
        """
        mutation_rate = agent_item.get("mutation_rate", 0.08)
        grain = agent_state.get("assets", {}).get("grain", 0.0)
        
        # 绝境探索加权
        effective_rate = min(0.35, mutation_rate * 2.5) if grain < 3.0 else mutation_rate
        if self.rng.random() >= effective_rate:
            return {"triggered": False}

        group = agent_item.get("group", "")
        if "lower_peasant" in group:
            innovations = [
                {
                    "type": "MUTATION_UNDERGROUND_CREDIT_POOL",
                    "title": "五人结会拼单贷 (民间微型互助金融)",
                    "description": "【灵光一闪】联络同保四户穷邻私下结成‘青苗互助互保会’，五人合借一份低息额度轮流做本金做小买卖周转，共同担保抗衡书吏敲诈！",
                    "action_name": "MUTATION_UNDERGROUND_CREDIT_POOL"
                },
                {
                    "type": "MUTATION_INFORMAL_GRAIN_NOTE",
                    "title": "地下折色私券旁路",
                    "description": "【灵光一闪】将官仓贷出的粗粝谷米直接就地私折给城郊油坊换取现银，截留官府过秤耗费！",
                    "action_name": "MUTATION_INFORMAL_GRAIN_NOTE"
                },
                {
                    "type": "MUTATION_COLLECTIVE_PETITION",
                    "title": "宗族联名哭庙与长跪御史",
                    "description": "【灵光一闪】联合同姓三十余丁长跪孔庙祭告先圣，或向巡按御史行台递交血状，直斥公吏抑配违旨！",
                    "action_name": "MUTATION_COLLECTIVE_PETITION"
                }
            ]
        elif "middle_peasants" in group:
            innovations = [
                {
                    "type": "MUTATION_JOINT_LIABILITY_HEDGE",
                    "title": "保结自保排他同盟",
                    "description": "【灵光一闪】中等自耕农私下立盟：凡不熟悉底细者绝不在官簿上画押充保，形成抵御连坐的民间自保壁垒！",
                    "action_name": "MUTATION_JOINT_LIABILITY_HEDGE"
                }
            ]
        else:
            innovations = [
                {
                    "type": "MUTATION_REGULATORY_ARBITRAGE",
                    "title": "官民息差套利网络",
                    "description": "【灵光一闪】利用亲贵特权低息通融官银，转手借给急需交税的自耕农赚取两倍利差！",
                    "action_name": "MUTATION_REGULATORY_ARBITRAGE"
                }
            ]

        chosen = self.rng.choice(innovations)
        return {"triggered": True, "innovation": chosen}

    def register_innovation_action(self, agent_id: str, action_type: str, tick: int):
        """记录某节点的变异创新行为"""
        self.mutation_history.append({
            "agent_id": agent_id,
            "action_type": action_type,
            "tick": tick,
            "verified_success": True # 暂定
        })

    def evaluate_macro_learning_and_merge(self, world_state: Dict[str, Any], agent_states: List[Dict[str, Any]], tick: int) -> Optional[Dict[str, Any]]:
        """
        评估官方或中等户是否在推演中‘自学习’并启动‘逆向主干合并 (Mainline Merge)’:
        例如：知县发现民间五人互助结会使逃亡率归零，正式发布政令在全县推广！
        """
        # 统计民间互助结会的采纳次数
        pool_actions = [m for m in self.mutation_history if m["action_type"] == "MUTATION_UNDERGROUND_CREDIT_POOL"]
        
        # 如果民间有超过 2 个小组自发跑通了拼单贷，且尚未被主干合并
        if len(pool_actions) >= 2 and "PROMOTE_CREDIT_UNION" not in self.active_mainline_reforms:
            self.active_mainline_reforms.append("PROMOTE_CREDIT_UNION")
            return {
                "triggered": True,
                "event_type": "MAINLINE_MERGE_CREDIT_UNION",
                "title": "【自学习与主干合并】知县采纳民间互助智慧：全县通令推广‘五人自愿结会贷’！",
                "description": (
                    "知县查阅祥符县两保簿册，惊奇发现西关五户佃农私自结会拼单还款，坏账与逃亡率竟为零！"
                    "知县大受触动，意识到与其暴力抑配导致杀官抗税，不如顺应民情：宣布全县推行‘互助联保结会贷’，"
                    "官府正式认可民间自愿五人编组，废止差役抑配与纸笔头子钱！全县违约阻抗大幅下降！"
                )
            }

        return None
