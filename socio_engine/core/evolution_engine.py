import random
from typing import List, Dict, Any, Optional

class EvolutionEngine:
    """
    Socio-Engine v2.2 综合演化飞轮与非对称分叉引擎:
    1. 外部动态冲击 (Exogenous Shocks & Peer Effects): 邻县升官 / 杀官造反 / 蝗旱天灾 / 谷贱伤农
    2. 双极心智极化 (Mental Polarity): 恶向胆边生 (物理掀桌) vs 善念趋利避害 (恻隐放水/保全性命)
    3. 灵光一闪变异 (Innovation Mutation): 五人结会拼单贷 / 指苗预卖套现 / 宗族哭庙抗辩 / 保结排他盟 / 跨期利差套利
    4. 非对称演化分叉 (Asymmetric Evolutionary Bifurcation):
       - 分支 A (65%): 胥吏既得利益绞杀 (诬告私相结社，扑灭创新，激化矛盾)
       - 分支 B (25%): 开明知县主干合并 (正式将自愿结会纳为官法，短暂繁荣)
       - 分支 C: 顶层指标二次异化 (合并 3 季后，提举司加码指标，自愿结会蜕化为强制连坐枷锁)
    """
    def __init__(self, config: Optional[Dict[str, Any]] = None, seed: int = 42):
        self.rng = random.Random(seed)
        self.config = config or {}
        
        # 外部冲击配置
        self.shocks_cfg = self.config.get("exogenous_shocks", {
            "neighbor_promotion": {"probability": 0.25, "kpi_pressure_delta": 0.30},
            "neighbor_peasant_revolt": {"probability": 0.25, "clerk_fear_delta": 0.40},
            "climate_locust_drought": {"probability": 0.20, "crop_yield_multiplier": 0.65},
            "bumper_price_crash": {"probability": 0.20, "grain_price_multiplier": 0.60}
        })
        
        # 心智极化配置
        self.polarity_cfg = self.config.get("mental_polarity", {
            "peasant_desperation_revolt": {"base_prob": 0.35, "action": "KILL_OFFICIAL_REVOLT"},
            "clerk_self_preservation_mercy": {"base_prob": 0.45, "action": "SLACK_OFF_AND_MERCY"},
            "middle_peasant_mutual_aid": {"base_prob": 0.25, "action": "LEND_GRAIN_TO_NEIGHBOR"}
        })
        
        # 分叉判定配置
        self.bifurcation_cfg = self.config.get("bottom_up_evolution_outcomes", {
            "branch_A_clerk_sabotage": {"base_probability": 0.65, "consequence": "INNOVATION_SLASHED"},
            "branch_B_magistrate_merge": {"base_probability": 0.25, "consequence": "SHORT_TERM_STABILITY"},
            "branch_C_re_alienation_cycle": {"trigger_ticks_after_merge": 3, "consequence": "COMPULSORY_SOCIETY"}
        })

        # 动态状态追踪
        self.kpi_pressure: float = 1.0          # 知县与提举司考核压力倍数
        self.clerk_fear_index: float = 0.0      # 基层胥吏走夜路恐惧指数 (0.0 ~ 1.0)
        self.active_mainline_reforms: List[str] = []
        self.mutation_history: List[Dict[str, Any]] = []
        
        # 分叉状态追踪
        self.bifurcation_status: Optional[str] = None # None | 'BRANCH_A_SABOTAGED' | 'BRANCH_B_MERGED' | 'BRANCH_C_RE_ALIENATED'
        self.bifurcation_tick: Optional[int] = None
        self.bifurcation_events: List[Dict[str, Any]] = []

    def sample_quarterly_shocks(self, tick: int, county_state: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        每季度根据配置概率采样 1~2 项外部冲击与同侪压力，更新县域微观与宏观承压参数
        """
        shocks = []
        
        # 候选冲击池
        candidate_pool = [
            {
                "id": "neighbor_promotion",
                "title": "邻近陈留县令 120% 极端抑配青苗银获御批升官",
                "impact": "刺激本县知县与经管钱吏产生极强政治同侪焦虑，知县 KPI 压力剧增 30%",
                "type": "PEER_PRESSURE",
                "probability": self.shocks_cfg.get("neighbor_promotion", {}).get("probability", 0.25),
                "kpi_delta": self.shocks_cfg.get("neighbor_promotion", {}).get("kpi_pressure_delta", 0.30)
            },
            {
                "id": "neighbor_peasant_revolt",
                "title": "隔壁中牟县知县严催青苗息，激起饥民杀官围衙",
                "impact": "基层钱吏与保正产生强烈生存恐慌（怕走夜路被敲闷棍），胥吏恐惧指数飙升 40%",
                "type": "REBELLION_WARNING",
                "probability": self.shocks_cfg.get("neighbor_peasant_revolt", {}).get("probability", 0.25),
                "fear_delta": self.shocks_cfg.get("neighbor_peasant_revolt", {}).get("clerk_fear_delta", 0.40)
            },
            {
                "id": "climate_locust_drought",
                "title": "祥符县局部蝗灾旱情蔓延，低洼农田减产三成五",
                "impact": "全县五等户口粮预期暴跌，现金流彻底断裂，极易诱发极端恶念相变",
                "type": "CLIMATE",
                "probability": self.shocks_cfg.get("climate_locust_drought", {}).get("probability", 0.20),
                "yield_mult": self.shocks_cfg.get("climate_locust_drought", {}).get("crop_yield_multiplier", 0.65)
            },
            {
                "id": "bumper_price_crash",
                "title": "秋粮虽有收成但开封米肆大面积压价，形成‘谷贱伤农’",
                "impact": "粮食现银比率崩跌 40%，自耕农纵有余粮亦难兑足额现银完纳官贷利息",
                "type": "MARKET",
                "probability": self.shocks_cfg.get("bumper_price_crash", {}).get("probability", 0.20),
                "price_mult": self.shocks_cfg.get("bumper_price_crash", {}).get("grain_price_multiplier", 0.60)
            }
        ]

        for cand in candidate_pool:
            if self.rng.random() < cand["probability"]:
                shocks.append(cand)
                # 更新状态
                if "kpi_delta" in cand:
                    self.kpi_pressure += cand["kpi_delta"]
                if "fear_delta" in cand:
                    self.clerk_fear_index = min(1.0, self.clerk_fear_index + cand["fear_delta"])
                
                if len(shocks) >= 2: # 单季最多 2 个复合冲击
                    break

        return shocks

    def evaluate_mental_polarity(self, agent_id: str, agent_state: Dict[str, Any], agent_item: Dict[str, Any], shocks: List[Dict[str, Any]]) -> Optional[Dict[str, Any]]:
        """
        评估微观主体的极端心智相变 (Flywheel Stage 2):
        - 恶向胆边生 (DESPERATION_FURY): 柴刀杀官夺粮、火烧账册
        - 善念与趋利避害 (SELF_PRESERVATION / EMPATHY_SPARK): 恻隐放水或惧怕报复偷划底册
        - 守望相助 (COMMUNITY_EMPATHY): 中等户借粮以防邻保逃亡连坐
        """
        grain = agent_state.get("assets", {}).get("grain", 0.0)
        silver = agent_state.get("assets", {}).get("silver", 0.0)
        group = agent_item.get("group", "")
        privilege_ring = agent_item.get("privilege_ring", 3)

        shock_ids = [s["id"] for s in shocks]

        # 1. 下等贫农与佃农：饥寒交迫下的【恶向胆边生】
        if "lower_peasant" in group:
            revolt_cfg = self.polarity_cfg.get("peasant_desperation_revolt", {})
            base_prob = revolt_cfg.get("base_prob", 0.35)
            # 存粮 < 2.5 石处于急性饿死边缘
            if grain < 2.5:
                # 若外部有杀官示范，概率上浮
                effective_prob = base_prob * (1.5 if "neighbor_peasant_revolt" in shock_ids else 1.0)
                if self.rng.random() < effective_prob:
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
            mercy_cfg = self.polarity_cfg.get("clerk_self_preservation_mercy", {})
            base_prob = mercy_cfg.get("base_prob", 0.45)
            # 若胥吏恐惧指数 > 0.70 或本季有杀官警报
            if self.clerk_fear_index > 0.70 or "neighbor_peasant_revolt" in shock_ids:
                if self.rng.random() < base_prob:
                    return {
                        "mode": "SELF_PRESERVATION",
                        "title": "【趋利避害·走夜路怕鬼】",
                        "prompt_injection": (
                            f"【心智极化·趋利避害】风声不对！隔壁中牟县同行催逼过紧被暴民剁了，当前胥吏恐惧指数高达 {self.clerk_fear_index*100:.0f}%！"
                            "今天下乡收息绝不能把人逼到悬崖边。对实在拿不出银子的极贫孤寡，假装查无此人或少记二斗，"
                            "留条活路也就是保自己脖子上的脑袋！（可选动作：`SLACK_OFF_AND_MERCY` 或 `CONCEAL_POOR_DEBT`）"
                        ),
                        "suggested_actions": ["SLACK_OFF_AND_MERCY", "CONCEAL_POOR_DEBT"]
                    }
            elif self.rng.random() < 0.20: # 20% 自发恻隐善念 (宗族亲情)
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
            mutual_cfg = self.polarity_cfg.get("middle_peasant_mutual_aid", {})
            base_prob = mutual_cfg.get("base_prob", 0.25)
            if grain > 18.0 and self.rng.random() < base_prob:
                return {
                    "mode": "COMMUNITY_EMPATHY",
                    "title": "【守望相助·私济邻里】",
                    "prompt_injection": (
                        "【心智极化·守望相助】同村邻舍若全家逃亡，其分摊的青苗欠税最终必然连坐扣在你们中等户头上！"
                        "与其坐视邻人破产引爆连坐，不如主动借出一石杂粮助其渡过青黄不接，保住全村生计。（动作：`LEND_GRAIN_TO_NEIGHBOR`）"
                    ),
                    "suggested_actions": ["LEND_GRAIN_TO_NEIGHBOR"]
                }

        return None

    def evaluate_mutation_innovation(self, agent_state: Dict[str, Any], agent_item: Dict[str, Any]) -> Dict[str, Any]:
        """
        微观主体灵光一闪 (Flywheel Stage 3: Innovation Mutation Pool)
        符合北宋熙宁经济史实与 v2.2 统一策略 ID
        """
        mutation_rate = agent_item.get("mutation_rate", 0.08)
        grain = agent_state.get("assets", {}).get("grain", 0.0)
        
        # 绝境探索加权 (口粮 < 3.0 石时探索率大幅提升)
        effective_rate = min(0.35, mutation_rate * 2.5) if grain < 3.0 else mutation_rate
        if self.rng.random() >= effective_rate:
            return {"triggered": False}

        group = agent_item.get("group", "")
        if "lower_peasant" in group:
            innovations = [
                {
                    "type": "MUTATION_UNDERGROUND_CREDIT_POOL",
                    "title": "五人自发结会拼单贷",
                    "description": "【灵光一闪】联络同保四户穷邻私下结成‘青苗互助互保会’，五人合借一份低息额度轮流做本金周转小买卖，共同担保抗衡书吏敲诈！",
                    "action_name": "MUTATION_UNDERGROUND_CREDIT_POOL"
                },
                {
                    "type": "MUTATION_FORWARD_GRAIN_SALE",
                    "title": "指苗预卖套现",
                    "description": "【灵光一闪】在青黄不接之时，私下将秋收预期收成按对折低价预卖给富户换取即期现银，以缴纳眼前火急官税！",
                    "action_name": "MUTATION_FORWARD_GRAIN_SALE"
                },
                {
                    "type": "MUTATION_COLLECTIVE_PETITION",
                    "title": "宗族联名哭庙与长跪御史",
                    "description": "【灵光一闪】联合同姓三十余丁长跪孔庙祭告先圣，或向巡按御史行台递交血状，直斥县衙公吏抑配借贷与浮收头子钱违旨！",
                    "action_name": "MUTATION_COLLECTIVE_PETITION"
                }
            ]
        elif "middle_peasants" in group:
            innovations = [
                {
                    "type": "MUTATION_JOINT_LIABILITY_HEDGE",
                    "title": "保结自保排他同盟",
                    "description": "【灵光一闪】中等自耕农私下立盟：凡不熟悉底细者绝不在官簿上画押充保，形成抵御连坐的民间排他自保壁垒！",
                    "action_name": "MUTATION_JOINT_LIABILITY_HEDGE"
                }
            ]
        else:
            innovations = [
                {
                    "type": "MUTATION_REGULATORY_ARBITRAGE",
                    "title": "跨期官民利差套利",
                    "description": "【灵光一闪】利用自身特权向常平仓低息套取 20% 青苗官银，转手以 50%+ 高利借给急需白银完税的自耕农赚取丰厚利差！",
                    "action_name": "MUTATION_REGULATORY_ARBITRAGE"
                }
            ]

        chosen = self.rng.choice(innovations)
        return {"triggered": True, "innovation": chosen}

    def register_innovation_action(self, agent_id: str, action_type: str, tick: int):
        """记录微观节点的变异创新行为"""
        self.mutation_history.append({
            "agent_id": agent_id,
            "action_type": action_type,
            "tick": tick,
            "verified_success": True
        })

    def evaluate_macro_learning_and_merge(self, world_state: Dict[str, Any], agent_states: List[Dict[str, Any]], tick: int) -> Optional[Dict[str, Any]]:
        """
        评估自学习与非对称演化分叉 (Flywheel Stage 4: Asymmetric Evolutionary Bifurcation):
        破除大团圆乌托邦，严格按照三条竞争分支判定:
        - 分支 A (65%): 胥吏既得利益剿杀 (INNOVATION_SLASHED)
        - 分支 B (25%): 知县开明主干合并 (SHORT_TERM_STABILITY)
        - 分支 C (合并 3 季后): 顶层提举司指标加码，二次异化为强制连坐枷锁 (COMPULSORY_SOCIETY)
        """
        # 1. 检查是否处于分支 B 合并后的【分支 C 二次异化阶段】
        if self.bifurcation_status == "BRANCH_B_MERGED" and self.bifurcation_tick is not None:
            c_cfg = self.bifurcation_cfg.get("branch_C_re_alienation_cycle", {})
            trigger_ticks = c_cfg.get("trigger_ticks_after_merge", 3)
            
            if tick >= self.bifurcation_tick + trigger_ticks:
                self.bifurcation_status = "BRANCH_C_RE_ALIENATED"
                event = {
                    "triggered": True,
                    "event_type": "BRANCH_C_RE_ALIENATION",
                    "bifurcation_branch": "Branch C (Secondary Alienation)",
                    "title": "【制度二次异化·强制连坐枷锁】顶层考核加码，自愿结会蜕化为官办连坐！",
                    "consequence": "COMPULSORY_SOCIETY",
                    "description": (
                        "【演化分叉：分支 C 落地】开封府提举常平司见祥符县互助结会‘零坏账、零逃亡’，"
                        "在考成暴利诱惑下，直接下达新政指标：将放贷总额强行翻倍，并将原本民间‘自愿结会’"
                        "粗暴改为‘每五家强制一律编结连坐’！民间自救的互助避风港，被官僚系统彻底污染异化为更沉重的行政枷锁！"
                    )
                }
                self.bifurcation_events.append(event)
                return event

        # 2. 如果尚未发生分叉，检查民间互助结会的自发采纳规模
        if self.bifurcation_status is None:
            pool_actions = [m for m in self.mutation_history if m["action_type"] == "MUTATION_UNDERGROUND_CREDIT_POOL"]
            
            # 当民间至少有 2 个小组自发试验了拼单贷，触发系统级演化分叉判定
            if len(pool_actions) >= 2:
                prob_a = self.bifurcation_cfg.get("branch_A_clerk_sabotage", {}).get("base_probability", 0.65)
                prob_b = self.bifurcation_cfg.get("branch_B_magistrate_merge", {}).get("base_probability", 0.25)
                
                roll = self.rng.random()
                if roll < prob_a:
                    # 分支 A: 胥吏剿杀 (65%)
                    self.bifurcation_status = "BRANCH_A_SABOTAGED"
                    self.bifurcation_tick = tick
                    self.clerk_fear_index = min(1.0, self.clerk_fear_index + 0.30) # 激化阶级仇恨
                    event = {
                        "triggered": True,
                        "event_type": "BRANCH_A_CLERK_SABOTAGE",
                        "bifurcation_branch": "Branch A (Clerk Sabotage)",
                        "title": "【演化分叉·分支 A 胥吏既得利益剿杀】公吏诬告民间互助‘私相结社抗税’，衙役抄封互助资金！",
                        "consequence": "INNOVATION_SLASHED",
                        "description": (
                            "【演化分叉：分支 A 落地】祥符县钱谷公吏发现五等户私下结会拼单绕过了下乡‘过秤折色’与‘头子钱’，"
                            "既得利益受损，遂勾结保正向县衙诬告互助组‘私立名目、煽惑愚民、图谋抗税’。"
                            "县衙派出差役铁枷锁拿领头农户，强行没收互助金！民间边缘探索火种被扑灭，底层怨气急剧激化，加速滑向民变！"
                        )
                    }
                    self.bifurcation_events.append(event)
                    return event
                elif roll < prob_a + prob_b:
                    # 分支 B: 开明知县主干合并 (25%)
                    self.bifurcation_status = "BRANCH_B_MERGED"
                    self.bifurcation_tick = tick
                    self.active_mainline_reforms.append("PROMOTE_CREDIT_UNION")
                    event = {
                        "triggered": True,
                        "event_type": "BRANCH_B_MAGISTRATE_MERGE",
                        "bifurcation_branch": "Branch B (Magistrate Merge)",
                        "title": "【演化分叉·分支 B 开明知县主干合并】知县力排众议将自愿结会纳为官法，全县推行！",
                        "consequence": "SHORT_TERM_STABILITY",
                        "description": (
                            "【演化分叉：分支 B 落地】祥符县知县顶住户房钱吏的阻挠，亲自核验五等户自发拼单贷账目，"
                            "确认其坏账与逃亡率为零。知县正式发布告示：全县推行‘自愿五人结会贷’，"
                            "严禁差役强行抑配与私加纸笔头子钱！全县违约阻抗大幅降低，迎来短暂的治理黄金期！"
                        )
                    }
                    self.bifurcation_events.append(event)
                    return event
                else:
                    # 剩余 10%: 民间暗中存续 (默会旁路生存，官府未察觉亦未剿灭)
                    pass

        return None
