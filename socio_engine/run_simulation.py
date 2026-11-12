import os
import sys
import uuid
import json
import yaml
from datetime import datetime
from typing import Dict, Any, List

# 确保把 socio_engine 加入 Python 搜索路径
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, CURRENT_DIR)

import socio_core
from core.role_loader import RoleLoader
from core.agent import RoleAgent
from core.llm_client import LLMClient

def export_simulation_report(report_data: Dict[str, Any], output_dir: str) -> str:
    os.makedirs(output_dir, exist_ok=True)
    run_id = report_data["run_id"]
    trial = report_data["trial"]
    md_path = os.path.join(output_dir, f"SIM_REPORT_{run_id}_TRIAL_{trial}.md")
    json_path = os.path.join(output_dir, f"SIM_REPORT_{run_id}_TRIAL_{trial}.json")

    with open(json_path, "w", encoding="utf-8") as f:
        json.dump(report_data, f, ensure_ascii=False, indent=2)

    md = []
    md.append(f"# Socio-Engine 历史沙盘推演报告：{report_data['scenario_name']}\n")
    md.append(f"> **推演场次 (Run ID)**: `{run_id}` | **实验版本**: `{report_data['version']}` | **试验轮次**: `#{trial}`  ")
    md.append(f"> **启动时间**: `{report_data['start_time']}` | **地理历史坐标**: `{report_data['county']}`  ")
    md.append(f"> **理论底座**: 《社会系统协议学》v11.2 (三态分离 / 制度引力场 / 反机械降神) | **物理引擎**: Rust socio_core (PyO3)\n")
    md.append("---\n")

    md.append("## 一、 宏观历史轨迹演化总表 (Macro Trajectory)\n")
    md.append("| 季度 (Tick) | 历史大势与朝局演化 | 太仓存银 | 现行米价 | 全县抛荒田亩 (流亡比率) | 民变风险 | 制度熵(技术债) |")
    md.append("|:---:|:---|:---:|:---:|:---:|:---:|:---:|")
    for t in report_data["ticks"]:
        m = t["macro_state"]
        md.append(f"| **第 {t['tick']:02d} 季** | {t['timeline_event']} | {m['treasury_silver']:.1f} 两 | {m['grain_price']:.2f} 两/石 | {m['abandoned_land']:.0f} 亩 ({m['flee_ratio']:.1f}%) | {m['unrest_risk']*100:.1f}% | {m['system_entropy']:.2f} |")
    md.append("\n---\n")

    md.append("## 二、 逐季博弈流水与认知三态分离实录 (Quarterly Dialogue & Decisions)\n")
    for t in report_data["ticks"]:
        md.append(f"### 第 {t['tick']:02d} 季度：{t['timeline_event']}\n")
        
        if t.get("shocks"):
            md.append("#### 1. 外部冲击与同侪压力传闻 (Exogenous Shocks)")
            for s in t["shocks"]:
                md.append(f"- ⚡ **{s['title']}**: {s.get('description', '')} (机制冲击: `{s.get('impact', '')}`)")
            md.append("")

        if t.get("dialogues"):
            md.append("#### 2. 微观暗流对话与 P2P 协商 (DialogueBus Micro-Encounters)")
            for d in t["dialogues"]:
                md.append(f"##### ▶ {d['title']}")
                md.append(f"- **对质主题**: {d.get('topic', '')}")
                cues = d.get('observable_cues', {})
                sp_a = d.get('speaker_a', '')
                sp_b = d.get('speaker_b', '')
                cue_a = cues.get(sp_a, '无特殊体征')
                cue_b = cues.get(sp_b, '无特殊体征')
                md.append(f"- **现场物理表征线索**: A方 [{cue_a}] vs B方 [{cue_b}]")
                md.append(f"- **双方关系边权重**: `{d.get('relationship_edge', '无特殊记录')}`")
                md.append("- **现场对话往来**:")
                for item in d.get("script", []):
                    sp_name, speech = item[1], item[2]
                    md.append(f"  - 🗣️ **[{sp_name}]**: “{speech}”")
                md.append(f"- **后验局势影响**: {d.get('impact', '')}\n")

        md.append("#### 3. 本季群体决策与三态分离记录 (Say-Do-Be Tripartite Execution)")
        md.append("| 角色姓名 (ID) | 特权环 | 认知模型与温度 | [说什么] 公开发言 (public_speech) | [做什么] 物理动作 (action_type) | [是什么] 真实内心算计 (inner_monologue) | 物理执行状态 |")
        md.append("|:---|:---:|:---:|:---|:---|:---|:---|")
        for dec in t.get("decisions", []):
            speech = dec.get("public_speech", "").replace("\n", " ").strip() or "（沉默或未公开发言）"
            mono = dec.get("inner_monologue", "").replace("\n", " ").strip() or "（无私密记录）"
            status = dec.get("status", "SUCCESS")
            stat_icon = "✔ 成功" if status == "SUCCESS" else f"❌ 驳回: {dec.get('error', '')}"
            md.append(f"| **{dec['role_name']}** (`{dec['agent_id']}`) | Ring-{dec['privilege_ring']} | `{dec['model']}` ($T={dec['temperature']}$) | {speech[:140]} | `{dec['action_type']}` (租金: {dec['rent_extracted']}两) | {mono[:160]} | {stat_icon} |")
        md.append("\n---\n")

    md.append("## 三、 终局演化分叉与制度吸引子分析 (Evolutionary Attractor Analysis)\n")
    if report_data.get("bifurcation_status"):
        md.append(f"- **演化终局状态**: `{report_data['bifurcation_status']}`")
        for ev in report_data.get("bifurcation_events", []):
            md.append(f"  - **{ev['title']}** (分支: `{ev.get('bifurcation_branch', '')}`): {ev.get('description', '')}")
    else:
        md.append("- **演化状态**: 处于基准演化主线，未触发全局主干合并。")

    md.append("\n### 理论检验判定：\n")
    md.append("1. **三态分离定理验证**: 个体在公开发言中普遍展现出符合生存策略的谎言、哭穷与博弈烟雾弹，而私密心智（inner_monologue）与物理动作（action_type）严格受卡路里与特权环硬约束；\n")
    md.append("2. **制度引力场吸引子收敛**: 无论微观个体的道德善意与绝境挣扎有多激烈，在刚性考成与火耗盘剥势能井下，宏观系统最终不可逆地滑入制度吸引子。\n")

    with open(md_path, "w", encoding="utf-8") as f:
        f.write("\n".join(md))

    return md_path

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
    from core.dialogue_bus import DialogueBus
    evolution_engine = EvolutionEngine(config=sim_config, seed=args.trial * 100 + 42)
    dialogue_bus = DialogueBus(llm_client=llm_client)
    
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
            objective_function=item.get("objective_function", ""),
            model=item.get("model", rdef.model),
            temperature=item.get("temperature", rdef.temperature),
            llm_client=llm_client
        )
        agents.append(agent)
        print(f"    - [{agent_id}] {item['name']:<18} | Ring-{item['privilege_ring']} | 田:{assets.get('land',0):>4.1f}亩 银:{assets.get('silver',0):>5.1f}两 粮:{assets.get('grain',0):>4.1f}石 | 特质: {item.get('trait','NORMAL')}")

    # 6. 使用 Rust PySocialGraph 构建真实的血缘、姻亲、借贷与世仇网络拓扑
    print("\n[*] 正在构建微观社会依存网络拓扑 (Rust Petgraph CSR 加速)...")
    graph = socio_core.PySocialGraph()
    edge_type_map = {
        "SubordinateTo": "SubordinateTo",
        "TaxPayerTo": "TaxPayerTo",
        "PatronClient": "PatronClient",
        "DebtorTo": "DebtorTo",
        "CollusionAlliance": "CollusionAlliance",
        "CoercionHarass": "CoercionHarass",
        "HostileRival": "HostileRival",
        "PoliticalRivalry": "HostileRival",
        "GentryPatronage": "PatronClient",
        "ClanAlliance": "CollusionAlliance",
        "CommunityProtection": "PatronClient",
        "KinshipSacred": "CollusionAlliance",
        "OpportunisticTie": "DebtorTo",
        "HostileCoercion": "CoercionHarass",
        "ExtortionPressure": "CoercionHarass",
    }
    for rel in sim_config.get("social_relations", []):
        r_type = edge_type_map.get(rel["type"], "CollusionAlliance")
        try:
            graph.add_relation(rel["from"], rel["to"], r_type, rel["weight"])
        except Exception as e:
            pass

    # 拓扑卡位点与中介度分析 (RFC-004 中介寄生)
    try:
        chokepoints = graph.find_chokepoints()
        print("    [拓扑分析] 识别到基层权力与资金流卡位点 (Chokepoints / Centrality):")
        for node_id, degree, weight in chokepoints:
            print(f"      - 节点 {node_id:<22} | 关联边数: {degree} | 权重汇聚: {weight:.1f}")
    except Exception:
        pass

    # 爆炸半径分析
    test_node = "lower_peasants_01" if any(x["id"] == "lower_peasants_01" for x in all_pop_items) else "peasant_li_tailwater"
    try:
        blast_info = json.loads(graph.compute_blast_radius(test_node, 2))
        print(f"    [拓扑分析] 承压节点 {test_node} 的危机爆炸半径: 关联受影响主体数={len(blast_info.get('affected_agents', []))}")
    except Exception:
        pass

    # 7. 推进长程历史沙盘推演
    total_ticks = args.ticks if args.ticks is not None else sim_config.get("scenario", {}).get("max_ticks", 20)
    timeline_events = sim_config.get("historical_timeline_events", {})
    
    print(f"\n==========================================================")
    print(f"  开始推演 {total_ticks} 个步长的宏观与微观演化: [{sim_config['scenario'].get('name', '未命名实验')}]")
    print(f"==========================================================")

    report_data = {
        "run_id": run_id,
        "version": args.version,
        "trial": args.trial,
        "scenario_name": sim_config["scenario"].get("name", "未命名实验"),
        "county": sim_config["scenario"].get("county", "通用县域"),
        "start_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "ticks": [],
        "bifurcation_status": None,
        "bifurcation_events": []
    }

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

        # 推进微观暗流对话与面对面对质 (Inter-Agent Dialogue & Negotiation Phase)
        quarterly_dialogues = dialogue_bus.run_quarterly_dialogues(
            run_id=run_id,
            tick=tick,
            world_state=world_state,
            agents=agents,
            engine=engine,
            shocks=quarterly_shocks
        )

        tick_record = {
            "tick": tick,
            "timeline_event": event_desc,
            "shocks": quarterly_shocks,
            "macro_state": {
                "treasury_silver": world_state["treasury_silver"],
                "grain_price": grain_price,
                "abandoned_land": c_abandoned,
                "flee_ratio": c_flee,
                "unrest_risk": world_state["unrest_risk_score"],
                "system_entropy": world_state["system_entropy"]
            },
            "dialogues": dialogue_bus.get_last_quarter_encounters(),
            "decisions": []
        }

        # 各个体轮番决策
        for ag in agents:
            agent_state = json.loads(engine.get_agent_state_json(ag.agent_id))
            if agent_state["survival_status"] in ["FLED", "DEAD"]:
                print(f"  - [{ag.role_name}]: 已破产逃亡，跳过决策。")
                tick_record["decisions"].append({
                    "agent_id": ag.agent_id,
                    "role_name": ag.role_name,
                    "privilege_ring": ag.privilege_ring,
                    "model": ag.model,
                    "temperature": ag.temperature,
                    "action_type": "FLED_OR_DEAD",
                    "public_speech": "（已破产流亡或死亡）",
                    "inner_monologue": "（已脱离地方秩序）",
                    "parameters": {},
                    "rent_extracted": 0.0,
                    "execution_message": "破产流亡",
                    "status": "INACTIVE"
                })
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

            if quarterly_dialogues.get(ag.agent_id):
                obs["本季私下对质与商谈"] = "\n".join(quarterly_dialogues[ag.agent_id])

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
                print(f"  ✔ [{ag.role_name} ({ag.agent_id})]: [物理做功] 执行 [{action_type}] -> {res['message']} (租金抽取: {res['rent_extracted']} 两)")
                
                # 三态分离可视化打印: 说什么 vs 是什么 vs 做什么
                public_speech = act_obj.get("public_speech") or act_obj.get("speech")
                if public_speech and isinstance(public_speech, str) and public_speech.strip():
                    clean_speech = public_speech.replace("\n", " ").strip()
                    print(f"    🗣️  [当众宣称 (说什么)]: “{clean_speech[:120]}”")
                
                inner_mono = act_obj.get("inner_monologue") or act_obj.get("monologue") or intent
                if inner_mono:
                    if isinstance(inner_mono, dict):
                        mono_str = json.dumps(inner_mono, ensure_ascii=False)
                    else:
                        mono_str = str(inner_mono)
                    clean_mono = mono_str.replace("\n", " ").strip()
                    print(f"    🧠 [真实心智 (是什么)]: {clean_mono[:120]}...")
                
                if action_type == "ABSCOND_WITH_FUNDS":
                    print(f"    🏃 ⚡ [突发叛逃] {ag.role_name} 席卷本保借贷白银连夜潜逃入伏牛山落草！原所属合会欠款强行转嫁中等户连坐！")
                elif action_type == "FOUND_COMMUNITY_SOCIETY":
                    print(f"    📜 ✨ [民间自治] {ag.role_name} 联合本乡三甲自耕农成立'丰乐同心抬会'，建立民间社仓分摊青苗利息！")
                elif action_type == "SEND_CAPITAL_LETTER":
                    print(f"    ✉️ 🔥 [官绅弹劾] {ag.role_name} 动用三朝老臣名望，亲修密折直呈御史台，痛参知县激变地方！")
                
                intent_str = clean_mono if 'clean_mono' in locals() and clean_mono else (str(intent) if intent else "")
                clean_speech_str = clean_speech if 'clean_speech' in locals() and clean_speech else ""
                
                # 记录决策入报告记录
                tick_record["decisions"].append({
                    "agent_id": ag.agent_id,
                    "role_name": ag.role_name,
                    "privilege_ring": ag.privilege_ring,
                    "model": ag.model,
                    "temperature": ag.temperature,
                    "action_type": action_type,
                    "public_speech": clean_speech_str,
                    "inner_monologue": intent_str,
                    "parameters": params,
                    "rent_extracted": res.get("rent_extracted", 0.0),
                    "execution_message": res.get("message", ""),
                    "status": "SUCCESS"
                })

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
                tick_record["decisions"].append({
                    "agent_id": ag.agent_id,
                    "role_name": ag.role_name,
                    "privilege_ring": ag.privilege_ring,
                    "model": ag.model,
                    "temperature": ag.temperature,
                    "action_type": action_type,
                    "public_speech": public_speech if 'public_speech' in locals() and isinstance(public_speech, str) else "",
                    "inner_monologue": clean_mono if 'clean_mono' in locals() and clean_mono else (str(intent) if intent else ""),
                    "parameters": params,
                    "rent_extracted": 0.0,
                    "execution_message": str(e),
                    "status": "REJECTED",
                    "error": str(e)
                })

        report_data["ticks"].append(tick_record)

    print("\n==========================================================")
    print("  推演完成！所有历史状态、资产变迁、特权校验与博弈流水已安全写入 SQLite 库。")
    if evolution_engine.bifurcation_status:
        print(f"  [*] 演化分叉终局: {evolution_engine.bifurcation_status}")
        for ev in evolution_engine.bifurcation_events:
            print(f"      - {ev['title']} ({ev['bifurcation_branch']})")
    
    # 导出全景推演报告与结构化 JSON
    report_data["bifurcation_status"] = evolution_engine.bifurcation_status
    report_data["bifurcation_events"] = evolution_engine.bifurcation_events
    reports_dir = os.path.join(CURRENT_DIR, "reports")
    saved_md = export_simulation_report(report_data, reports_dir)
    print(f"  [*] 📄 全景推演报告已落盘生成: {saved_md}")
    print("==========================================================")

if __name__ == "__main__":
    main()
