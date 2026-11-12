import random
from typing import List, Dict, Any

class SwarmPopulationGenerator:
    """
    Socio-Engine v2.0 群体规模化与微观参数扰动生成器
    负责根据 YAML 中的阶级原型配置 (Archetypes)，生成具备统计物理特性的多智能体群落
    """
    def __init__(self, seed: int = 42):
        self.rng = random.Random(seed)

    def generate_population(self, archetypes_config: Dict[str, Any]) -> List[Dict[str, Any]]:
        """
        根据声明式阶级原型生成群体列表
        """
        population = []

        for group_name, group_cfg in archetypes_config.items():
            role_type = group_cfg.get("role_type", group_name)
            base_name = group_cfg.get("base_name", group_name)
            count = group_cfg.get("count", 1)
            privilege_ring = group_cfg.get("privilege_ring", 3)
            asset_dist = group_cfg.get("assets_distribution", {})
            traits_pool = group_cfg.get("traits_pool", ["NORMAL"])
            background_template = group_cfg.get("background_template", "")
            objective_function = group_cfg.get("objective_function", "")
            mutation_rate = group_cfg.get("mutation_rate", 0.08)

            for i in range(1, count + 1):
                agent_id = f"{group_name}_{i:02d}"
                name = f"{base_name}_{i:02d}号"
                
                # 资产微扰采样
                silver = self._sample_value(asset_dist.get("silver", {"type": "fixed", "val": 1.0}))
                grain = self._sample_value(asset_dist.get("grain", {"type": "fixed", "val": 2.0}))
                land = self._sample_value(asset_dist.get("land", {"type": "fixed", "val": 0.0}))
                
                # 性情特质采样
                trait = self.rng.choice(traits_pool)
                
                # 认知温度微扰 (0.1 ~ 0.5)
                temp = round(self.rng.uniform(0.15, 0.45), 2)
                
                bg = background_template.format(index=i, land=land, silver=silver, grain=grain)

                agent_item = {
                    "id": agent_id,
                    "name": name,
                    "group": group_name,
                    "role_type": role_type,
                    "privilege_ring": privilege_ring,
                    "model": group_cfg.get("model", "deepseek-flash"),
                    "temperature": temp,
                    "trait": trait,
                    "objective_function": objective_function,
                    "mutation_rate": mutation_rate,
                    "background": bg,
                    "initial_assets": {
                        "silver": round(silver, 2),
                        "grain": round(grain, 2),
                        "land": round(land, 2)
                    }
                }
                population.append(agent_item)

        return population

    def _sample_value(self, dist_spec: Dict[str, Any]) -> float:
        dtype = dist_spec.get("type", "fixed")
        if dtype == "fixed":
            return float(dist_spec.get("val", 0.0))
        elif dtype == "uniform":
            min_v = dist_spec.get("min", 0.0)
            max_v = dist_spec.get("max", 10.0)
            return self.rng.uniform(min_v, max_v)
        elif dtype == "normal":
            mean = dist_spec.get("mean", 5.0)
            std = dist_spec.get("std", 1.0)
            return max(0.0, self.rng.gauss(mean, std))
        return 0.0


class MutationEngine:
    """
    Socio-Engine v2.0 灵光一闪 (Innovation Mutation) 算子
    根据微观主体处境与探索概率 epsilon，在常规动作空间外注入自发创新的边缘解
    """
    def __init__(self, rng: random.Random = None):
        self.rng = rng or random.Random(42)

    def evaluate_mutation(self, agent_state: Dict[str, Any], agent_item: Dict[str, Any]) -> Dict[str, Any]:
        """
        判断是否触发灵光一闪，并返回变异策略
        """
        mutation_rate = agent_item.get("mutation_rate", 0.08)
        
        # 绝境加权：当粮食低于保命线时，灵光一闪的紧迫性倍增
        grain = agent_state.get("assets", {}).get("grain", 0.0)
        silver = agent_state.get("assets", {}).get("silver", 0.0)
        
        effective_rate = mutation_rate
        if grain < 3.0: # 饥馑边缘
            effective_rate = min(0.35, mutation_rate * 2.5)

        roll = self.rng.random()
        is_mutated = roll < effective_rate

        if not is_mutated:
            return {"triggered": False}

        # 随机从策略创新池中选择一个灵光一闪方案
        group = agent_item.get("group", "")
        if "lower_peasant" in group:
            innovations = [
                {
                    "type": "MUTATION_UNDERGROUND_CREDIT_POOL",
                    "title": "民间地下拼单借贷互助",
                    "description": "【灵光一闪】私下联络同甲三户穷邻，合并借贷以抗衡大户兼并，轮流使用本金贩卖农副产品周转现金流",
                    "action_name": "MUTATION_UNDERGROUND_CREDIT_POOL"
                },
                {
                    "type": "MUTATION_INFORMAL_GRAIN_NOTE",
                    "title": "地下折色代券旁路",
                    "description": "【灵光一闪】将官府抑配之青苗借贷粮私自折价贴现换现银，绕开官办常平仓的高额交割回扣",
                    "action_name": "MUTATION_INFORMAL_GRAIN_NOTE"
                },
                {
                    "type": "MUTATION_COLLECTIVE_PETITION",
                    "title": "宗族联名哭庙与越级抗辩",
                    "description": "【灵光一闪】利用儒家孝道与饥荒生计，抬出同宗族长向提举常平司巡抚御史长跪哭诉官吏抑配之害",
                    "action_name": "MUTATION_COLLECTIVE_PETITION"
                }
            ]
        elif "middle_peasant" in group:
            innovations = [
                {
                    "type": "MUTATION_JOINT_LIABILITY_HEDGE",
                    "title": "保结对冲同盟",
                    "description": "【灵光一闪】中等户联合拒绝为不知底细的五等户做保结，成立自保公约抵制连坐",
                    "action_name": "MUTATION_JOINT_LIABILITY_HEDGE"
                }
            ]
        else:
            innovations = [
                {
                    "type": "MUTATION_REGULATORY_ARBITRAGE",
                    "title": "跨期官民利差套利",
                    "description": "【灵光一闪】大户以低息冒领青苗官贷，转手以二倍市价转借给破产农户",
                    "action_name": "MUTATION_REGULATORY_ARBITRAGE"
                }
            ]

        chosen = self.rng.choice(innovations)
        return {
            "triggered": True,
            "innovation": chosen
        }

