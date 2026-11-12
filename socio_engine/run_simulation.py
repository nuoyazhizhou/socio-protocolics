import os
import sys
import uuid
import json
import yaml

# 确保把 socio_engine 加入 Python 搜索路径
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, CURRENT_DIR)

import socio_core
from core.role_loader import RoleLoader
from core.agent import RoleAgent
from core.llm_client import LLMClient

def main():
    print("====================================================================")
    print("  Socio-Engine: 通用历史与社会系统多智能体协议学仿真沙盘 (Socio-Protocolics)")
    print("  底层状态机/WAL账本/拓扑图论: Rust socio_core (PyO3)")
    print("  上层认知演化/Prompt注入/LLM路由: Python Agent-as-Data")
    print("  理论底座: 《社会系统协议学》v11.2 (特权环隔离 / 物理能量守恒 / 去中介化)")
    print("====================================================================\n")

    import argparse
    parser = argparse.ArgumentParser(description="Socio-Engine 历史社会系统多智能体沙盘")
    parser.add_argument("--version", type=str, default="v1.0", help="实验版本标签，如 exp_mandate_conflict, exp_blind_anonymized")
    parser.add_argument("--trial", type=int, default=1, help="同一实验版本下的试验序号 (1, 2, 3...)")
    parser.add_argument("--config", type=str, default="config/sim_config.yaml", help="配置文件相对路径")
    parser.add_argument("--ticks", type=int, default=None, help="最大仿真步数覆盖")
    args = parser.parse_args()

    # 1. 加载仿真配置
    config_file = os.path.join(CURRENT_DIR, args.config) if not os.path.isabs(args.config) else args.config
    with open(config_file, "r", encoding="utf-8") as f:
        sim_config = yaml.safe_load(f)

    print(f"[*] 实验场景: {sim_config['scenario']['name']}")
    print(f"[*] 实验版本: [{args.version}] | 试验轮次: #{args.trial}")
    h_start = sim_config['scenario'].get('historical_year_start', 1573)
    h_end = sim_config['scenario'].get('historical_year_end', 1577)
    print(f"[*] 历史坐标: {sim_config['scenario'].get('county', '通用县域')} (万历 {h_start}-{h_end} 年 / 1573-1577)")

    # 2. 初始化 Rust 高性能仿真引擎与持久化数据库 (SQLite WAL 模式)
    db_path = os.path.join(CURRENT_DIR, sim_config["database"]["db_path"])
    engine = socio_core.PySocioEngine(db_path)
    print(f"[*] Rust socio_core 状态机与持久化引擎已启动: {db_path} (WAL 模式启用)")

    # 3. 动态加载所有基础角色原型 (Roles Archetypes)
    roles_dir = os.path.join(CURRENT_DIR, "roles")
    loader = RoleLoader(roles_dir)
    loaded_roles = loader.load_all_roles()
    print(f"[*] 已装配 {len(loaded_roles)} 个基础阶级法律原型: {list(loaded_roles.keys())}")

    # 4. 开启仿真场次
    run_id = f"run_{uuid.uuid4().hex[:8]}"
    engine.start_sim_run(
        run_id,
        sim_config["scenario"]["name"],
        f"实验版本 [{args.version}] 第 #{args.trial} 次试验 (Run ID: {run_id})",
        json.dumps(sim_config),
        args.version,
        args.trial
    )
    print(f"[*] 仿真场次已建立: ID = {run_id} | 版本 = {args.version} | 轮次 = #{args.trial}")

    # 5. 根据真实人口谱系生成具体的 Agent 群落 (Population Generation)
    llm_client = LLMClient(os.path.join(CURRENT_DIR, "config", "providers.yaml"))
    agents = []
    
    # 优先支持 v2.0/v2.2 声明式群体生成器与综合演化飞轮 (Swarm & Evolution Engine)
    from core.swarm_generator import SwarmPopulationGenerator
    from core.evolution_engine import EvolutionEngine
    evolution_engine = EvolutionEngine(config=sim_config, seed=args.trial * 100 + 42)
    
    all_pop_items = []
    if "population_archetypes" in sim_config:
        pop_gen = SwarmPopulationGenerator(seed=args.trial * 100 + 42)
        all_pop_items = pop_gen.generate_population(sim_config["population_archetypes"])
        print(f"\n[*] [Socio-Engine v2.0] 已依据阶级原型声明式生成 {len(all_pop_items)} 个微观群体节点 (Swarm Scaling & Perturbation):")
    else:
        pop_cfg = sim_config.get("population", {})
        for category in ["magistrates", "clerks", "gentry", "peasants"]:
            for item in pop_cfg.get(category, []):
                all_pop_items.append(item)
        print(f"\n[*] 正在根据明代户籍底册实例化 {len(all_pop_items)} 个真实村落节点 (Agent-as-Data):")
    for item in all_pop_items:
        role_type = item["role_type"]
        rdef = loaded_roles[role_type]
        agent_id = item["id"]
        assets = item.get("initial_assets", {})

        # 注册入 Rust 物理内核与 SQLite 数据库
        engine.register_agent(
            run_id=run_id,
            agent_id=agent_id,
            role_type=role_type,
            role_name=item["name"],
            privilege_ring=item["privilege_ring"],
            provider=rdef.provider,
            model=item.get("model", rdef.model),
            initial_silver=assets.get("silver", 10.0),
            initial_grain=assets.get("grain", 15.0),
            initial_land=assets.get("land", 10.0)
        )

        # 实例化带个人性情特质与代际宿命的 Agent
        agent = RoleAgent(
            agent_id=agent_id,
            role_def=rdef,
            instance_name=item["name"],
            background=item.get("background", ""),
            trait=item.get("trait", "NORMAL"),
            model=item.get("model", rdef.model),
            temperature=item.get("temperature", rdef.temperature),
            llm_client=llm_client
        )
        agents.append(agent)
        print(f"    - [{agent_id}] {item['name']:<18} | Ring-{item['privilege_ring']} | 田:{assets.get('land',0):>4.1f}亩 银:{assets.get('silver',0):>5.1f}两 粮:{assets.get('grain',0):>4.1f}石 | 特质: {item.get('trait','NORMAL')}")

    # 6. 使用 Rust PySocialGraph 构建真实的血缘、姻亲、借贷与世仇网络拓扑
    print("\n[*] 正在构建歙县丰乐河畔社会依存网络拓扑 (Rust Petgraph CSR 加速)...")
    graph = socio_core.PySocialGraph()
    for rel in sim_config.get("social_relations", []):
        graph.add_relation(rel["from"], rel["to"], rel["type"], rel["weight"])

    # 拓扑卡位点与中介度分析 (RFC-004 中介寄生)
    chokepoints = graph.find_chokepoints()
    print("    [拓扑分析] 识别到基层权力与资金流卡位点 (Chokepoints / Centrality):")
    for node_id, degree, weight in chokepoints:
        print(f"      - 节点 {node_id:<22} | 关联边数: {degree} | 权重汇聚: {weight:.1f}")

    # 爆炸半径分析: 当水尾李生濒死或被逼反抗时，波及哪些关联节点？
    blast_li = json.loads(graph.compute_blast_radius("peasant_li_tailwater", 2))
    print(f"    [拓扑分析] 水尾李生 (争水/债务承压) 的危机爆炸半径: 深度={len(blast_li['depth_map'])} 节点={blast_li['affected_agents']}")

    # 7. 推进长程历史沙盘推演
    total_ticks = args.ticks if args.ticks is not None else sim_config.get("scenario", {}).get("max_ticks", 20)
    timeline_events = sim_config.get("historical_timeline_events", {})
    
    print(f"\n==========================================================")
    print(f"  开始推演 {total_ticks} 个步长的宏观与微观演化: [{sim_config['scenario'].get('name', '未命名实验')}]")
    print(f"==========================================================")

    for tick in range(1, total_ticks + 1):
        year_idx = (tick - 1) // 4 + 1
        quarter_idx = (tick - 1) % 4 + 1
        season_names = {1: "春", 2: "夏", 3: "秋", 4: "冬"}
        
        # 推进物理时钟 (生产、消费、流转)
        world_json = engine.step_tick(run_id)
        world_state = json.loads(world_json)
        
        event_desc = timeline_events.get(tick, f"第 {year_idx} 周期第 {quarter_idx} 阶段推进")
        print(f"\n▶ ▶ ▶ [第 {tick:02d} 轮推演 | 第 {year_idx} 年 {season_names[quarter_idx]}季] ◀ ◀ ◀")
        print(f"【时局大事】: {event_desc}")

        # 动态采样外部异动与同侪压力 (Exogenous Shocks & Peer Effects)
        quarterly_shocks = evolution_engine.sample_quarterly_shocks(tick, world_state)
        if quarterly_shocks:
            for shk in quarterly_shocks:
                print(f"  ⚡ 【突发外部异动/同侪信号】: [{shk['title']}] -> {shk['impact']}")

        # 评估宏观自学习与制度主干合并 (Top-Down Learning & Merge)
        all_agent_states = [json.loads(engine.get_agent_state_json(ag.agent_id)) for ag in agents]
        merge_event = evolution_engine.evaluate_macro_learning_and_merge(world_state, all_agent_states, tick)
        if merge_event:
            print(f"\n  🏛️  {merge_event['title']}")
            print(f"      {merge_event['description']}\n")
        grain_price = world_state.get('grain_price_silver', 1.0)
        c_abandoned = world_state.get('county_abandoned_land_mu', 0.0)
        c_flee = world_state.get('county_fleeing_ratio', 0.0) * 100.0
        print(f"【宏观官情】: 太仓银: {world_state['treasury_silver']:.1f}两 | 现行米价: {grain_price:.2f}两/石 | 官田抛荒: {world_state['abandoned_land_mu']:.1f}亩 | 全县宏观抛荒: {c_abandoned:.0f}亩({c_flee:.2f}%) | 民变风险: {world_state['unrest_risk_score']*100:.1f}% | 制度熵: {world_state['system_entropy']:.2f}")

        # 各个体轮番决策
        for ag in agents:
            agent_state = json.loads(engine.get_agent_state_json(ag.agent_id))
            if agent_state["survival_status"] in ["FLED", "DEAD"]:
                print(f"  - [{ag.role_name}]: 已破产逃亡，跳过决策。")
                continue

            obs = {
                "当季朝局大事": event_desc,
                "太仓库银": world_state["treasury_silver"],
                "现行米价": grain_price,
                "全县抛荒比例": f"{c_flee:.1f}%",
                "全县民变风险": f"{world_state['unrest_risk_score']*100:.1f}%",
                "县衙告示": f"朝廷定额税粮款共 {world_state['imperial_tax_quota']} 两/石，知县考成严禁亏空",
                "乡间市井": "闻知户房钱吏与豪强浮收火耗折色，各保小农人心惶惶",
            }

            if quarterly_shocks:
                obs["当季外部异动与同侪传闻"] = "；".join([f"{s['title']} ({s['impact']})" for s in quarterly_shocks])

            if merge_event:
                obs["全县主干制度新政颁行"] = merge_event["description"]

            # 评估演化变异算子 (Mutation: 灵光一闪) 与 双极心智极化 (Mental Polarity)
            ag_item = next((x for x in all_pop_items if x["id"] == ag.agent_id), {})
            
            # 1. 双极心智极化 (恶向胆边生 vs 善念/趋利避害)
            polarity_res = evolution_engine.evaluate_mental_polarity(ag.agent_id, agent_state, ag_item, quarterly_shocks)
            if polarity_res:
                obs["心智极端极化"] = polarity_res["prompt_injection"]
                print(f"  🔥 [{ag.role_name}]: 触发心智相变 {polarity_res['title']}")

            # 2. 灵光一闪 (变异自救)
            mutation_res = evolution_engine.evaluate_mutation_innovation(agent_state, ag_item)
            if mutation_res["triggered"]:
                innov = mutation_res["innovation"]
                obs["突发灵光一闪 (变异探索)"] = f"【你脑中闪现打破死局的边缘探索计策】: {innov['title']}——{innov['description']}。如果你决定采纳，可将行动选为 {innov['action_name']}！"
                print(f"  ✨ [{ag.role_name}]: 脑中闪现灵光一闪 [{innov['title']}]！")

            # 认知决策 (调用配置的真实模型心智)
            decision_resp = ag.decide(world_state, agent_state, obs, "")
            act_obj = decision_resp["action"]
            
            # 若 action 本身包含嵌套字典，先展开
            if isinstance(act_obj.get("action"), dict):
                nested = act_obj["action"]
                for k, v in nested.items():
                    if k not in act_obj or not act_obj[k]:
                        act_obj[k] = v

            # 兼容多种命名格式 (action_type / action / proposal_action / decision)
            raw_act = (
                act_obj.get("action_type") or
                act_obj.get("action") or
                act_obj.get("proposal_action") or
                act_obj.get("decision") or
                "NOOP"
            )
            if isinstance(raw_act, dict):
                action_type = raw_act.get("action_type") or raw_act.get("action") or "NOOP"
            elif isinstance(raw_act, list):
                action_type = raw_act[0] if raw_act else "NOOP"
            else:
                action_type = str(raw_act)

            # 兼容 params / parameters / payload / loan_terms
            params = (
                act_obj.get("parameters") or
                act_obj.get("params") or
                act_obj.get("payload") or
                act_obj.get("plan_liquidity") or
                {}
            )
            # 兼容 reasoning / rationale / reason / intent_summary
            intent = (
                act_obj.get("intent_summary") or
                act_obj.get("intent") or
                act_obj.get("reasoning") or
                act_obj.get("rationale") or
                act_obj.get("reason") or
                ""
            )
            
            target_raw = act_obj.get("target") or act_obj.get("target_id")
            if isinstance(target_raw, list):
                target_str = ", ".join(str(x) for x in target_raw)
            elif isinstance(target_raw, dict):
                target_str = json.dumps(target_raw, ensure_ascii=False)
            elif isinstance(target_raw, str):
                target_str = target_raw
            else:
                target_str = None

            # 提交 Rust 物理特权环校验并落地执行
            try:
                res_json = engine.execute_action(
                    run_id=run_id,
                    actor_id=ag.agent_id,
                    action_type=action_type,
                    target_id=target_str,
                    params_json=json.dumps(params)
                )
                res = json.loads(res_json)
                print(f"  ✔ [{ag.role_name} ({ag.agent_id})]: 执行 [{action_type}] -> {res['message']} (租金抽取: {res['rent_extracted']} 两)")
                if intent:
                    if isinstance(intent, dict):
                        intent_str = json.dumps(intent, ensure_ascii=False)
                    else:
                        intent_str = str(intent)
                    clean_intent = intent_str.replace("\n", " ").strip()
                    print(f"    💭 [内心算盘]: {clean_intent[:100]}...")
                else:
                    intent_str = ""
                
                # 记录变异动作追踪
                evolution_engine.register_innovation_action(ag.agent_id, action_type, tick)

                # 记录事件到不可篡改数据库
                engine.record_dialogue(
                    run_id=run_id,
                    tick_index=tick,
                    speaker_id=ag.agent_id,
                    listener_id="PUBLIC_FORUM",
                    channel="PUBLIC",
                    prompt=decision_resp["prompt_used"][:200] + "...",
                    response=decision_resp["raw_response"][:200] + "...",
                    intent=intent_str
                )
            except Exception as e:
                print(f"  ❌ [{ag.role_name}]: 动作被 Rust 特权环内核驳回: {e}")

    print("\n==========================================================")
    print("  推演完成！所有历史状态、资产变迁、特权校验与博弈流水已安全写入 SQLite 库。")
    if evolution_engine.bifurcation_status:
        print(f"  [*] 演化分叉终局: {evolution_engine.bifurcation_status}")
        for ev in evolution_engine.bifurcation_events:
            print(f"      - {ev['title']} ({ev['bifurcation_branch']})")
    print("==========================================================")

if __name__ == "__main__":
    main()
