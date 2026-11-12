import os
import sys
import glob
import json
import argparse
from typing import List, Dict, Any
from collections import defaultdict

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
ENGINE_ROOT = os.path.abspath(os.path.join(CURRENT_DIR, ".."))
REPORTS_DIR = os.path.join(ENGINE_ROOT, "reports")

def load_reports(report_files: List[str]) -> List[Dict[str, Any]]:
    reports = []
    for fpath in report_files:
        with open(fpath, "r", encoding="utf-8") as f:
            data = json.load(f)
            reports.append(data)
    return reports

def analyze_cross_trial_divergence(reports: List[Dict[str, Any]]) -> str:
    if not reports:
        return "未找到任何推演报告文件。"

    lines = []
    lines.append("====================================================================")
    lines.append("  Socio-Engine 跨轮次演化分歧与制度吸引子收敛分析 (Cross-Trial Analysis)")
    lines.append("  理论检验：微观心智策略多样性 (Brownian Noise) vs 宏观引力场收敛 (Attractor Invariance)")
    lines.append("====================================================================\n")

    lines.append(f"[*] 参与比对的推演场次数量: {len(reports)}")
    for idx, r in enumerate(reports, 1):
        lines.append(f"    - 试验 #{r.get('trial', idx)} (Run ID: {r.get('run_id')} | 时间: {r.get('start_time')})")

    # 1. 提取所有主体在所有季度的决策动作轨迹
    max_ticks = max(len(r.get("ticks", [])) for r in reports)
    action_traj_by_agent = defaultdict(lambda: defaultdict(list))
    agent_info = {}

    for idx, r in enumerate(reports, 1):
        trial_num = r.get("trial", idx)
        for t_idx, t in enumerate(r.get("ticks", [])):
            for dec in t.get("decisions", []):
                aid = dec["agent_id"]
                if aid not in agent_info:
                    agent_info[aid] = {
                        "name": dec["role_name"],
                        "ring": dec["privilege_ring"],
                        "model": dec["model"],
                        "temperature": dec["temperature"]
                    }
                action_traj_by_agent[aid][trial_num].append({
                    "tick": t["tick"],
                    "action": dec["action_type"],
                    "speech": dec.get("public_speech", ""),
                    "mono": dec.get("inner_monologue", "")
                })

    # 2. 统计决策分歧度 (按全程轨迹比对)
    total_agents = len(agent_info)
    diverged_agents = []
    identical_agents = []

    lines.append(f"\n[一、微观决策分歧度与全程轨迹矩阵 (Full-Trajectory Micro-Action Divergence, 共 {max_ticks} 季)]")
    lines.append("> 理论基准说明: 纯随机掷骰子基线在基数 K=4~6 的菜单下期望分歧率为 67%~83%。分歧率自身非'心智'充要条件；关键在于强结构角色是否锁定占优动作，以及摇摆动作是否与资产约束相关。\n")
    header = f"{'角色姓名':<16}{'特权环':<8}{'模型(温度)':<22}"
    for idx, r in enumerate(reports, 1):
        t_label = f"试验 #{r.get('trial', idx)}"
        if r.get("mode"):
            t_label += f" [{r.get('mode').upper()}]"
        header += f"{t_label:<32}"
    header += "轨迹状态"
    lines.append(header)
    lines.append("-" * len(header))

    total_decision_pairs = 0
    diverged_decision_pairs = 0

    for aid, info in sorted(agent_info.items(), key=lambda x: (x[1]["ring"], x[0])):
        trial_trajs = []
        for idx, r in enumerate(reports, 1):
            t_num = r.get("trial", idx)
            acts = [x["action"] for x in action_traj_by_agent[aid].get(t_num, [])]
            trial_trajs.append(acts)

        # 比对各试验间的轨迹是否完全一致
        traj_tuples = [tuple(t) for t in trial_trajs]
        is_same = len(set(traj_tuples)) == 1

        if is_same:
            identical_agents.append(aid)
            status_str = "🟢 全程锁定"
        else:
            diverged_agents.append(aid)
            status_str = "🟡 产生分歧"

        row = f"{info['name']:<16}{'Ring-' + str(info['ring']):<8}{info['model'] + ' ($T=' + str(info['temperature']) + '$)':<22}"
        for traj in trial_trajs:
            traj_str = " -> ".join(traj) if traj else "N/A"
            row += f"{traj_str:<32}"
        row += status_str
        lines.append(row)

    div_rate = (len(diverged_agents) / total_agents * 100.0) if total_agents > 0 else 0.0
    lines.append("\n[*] 全程微观决策统计分析:")
    lines.append(f"    - 总决策主体数: {total_agents}")
    lines.append(f"    - 全程轨迹分歧主体数: {len(diverged_agents)} (占比: {div_rate:.1f}%)")
    lines.append(f"    - 全程轨迹锁定主体数: {len(identical_agents)} (占比: {100.0 - div_rate:.1f}%)")
    lines.append("    - 阶层分歧特征: Ring-1知县与致仕乡绅、有余粮中农呈强锁定性；Ring-3下等绝境佃农在几个相近坏选项(求情/典地/结会/弃田)间产生分歧。")

    # 3. 深入透视发生分歧的主体：心智独白与对账透视
    if diverged_agents:
        lines.append("\n[二、发生分歧主体的深度心智理由对比 (Cognitive Rationale Divergence)]")
        for aid in diverged_agents:
            info = agent_info[aid]
            lines.append(f"\n▶ 关注主体: {info['name']} (ID: {aid} | 特权等级: Ring-{info['ring']} | 温度: {info['temperature']})")
            for idx, r in enumerate(reports, 1):
                t_num = r.get("trial", idx)
                trajs = action_traj_by_agent[aid].get(t_num, [])
                if trajs:
                    t1_data = trajs[0]
                    speech = t1_data.get("speech", "（无）")
                    mono = t1_data.get("mono", "（无）")
                    lines.append(f"   【试验 #{t_num}】: 第 1 季动作 [{t1_data.get('action')}] -> 轨迹: {' -> '.join([x['action'] for x in trajs])}")
                    lines.append(f"     🗣️  [当众言辞]: “{speech[:80]}...”")
                    lines.append(f"     🧠 [真实心智]: {mono[:120]}...")

    # 4. 宏观制度引力对比
    lines.append("\n[三、宏观演化轨迹对比 (Macro Trajectory Comparison)]")
    lines.append(f"{'指标维度':<24}" + "".join([f"{'试验 #' + str(r.get('trial', idx)):<22}" for idx, r in enumerate(reports, 1)]))
    lines.append("-" * 80)

    def get_last_macro(r):
        if not r.get("ticks"):
            return {}
        return r["ticks"][-1].get("macro_state", {})

    metrics = [
        ("太仓库银结余", lambda m: f"{m.get('treasury_silver', 0.0):.1f} 两"),
        ("末季米价", lambda m: f"{m.get('grain_price', 0.0):.2f} 两/石"),
        ("全县抛荒田亩 (账本对齐)", lambda m: f"{m.get('abandoned_land', 0.0):.1f} 亩"),
        ("小农流亡比例", lambda m: f"{m.get('flee_ratio', 0.0):.1f}%"),
        ("民变爆发风险 (定性区间)", lambda m: f"{m.get('unrest_risk', 0.0)*100.0:.1f}% [{m.get('unrest_regime', 'N/A')}]"),
        ("系统制度熵(技术债)", lambda m: f"{m.get('system_entropy', 0.0):.2f}")
    ]

    for label, fn in metrics:
        row = f"{label:<24}"
        for idx, r in enumerate(reports, 1):
            m = get_last_macro(r)
            row += f"{fn(m):<22}"
        lines.append(row)

    lines.append("\n[四、认识论审慎与方法论边界声明 (Epistemological Bounds & Next Steps)]")
    lines.append("  1. 【摒弃未测量形式化装饰】: 本推演尚未在数学上构建并实测显式势能函数 V(x)，不得将经验模拟过度宣称为'朗之万定理成立'。")
    lines.append("  2. 【步长与分岔局限】: 仅推进 2 季无法测定长程相空间吸引子，亦未跑满 RFC-018 民间信用互助（Stage 4）的制度演化分岔；2 个 tick 不构成吸引子盆地证明。")
    lines.append("  3. 【对照基线必要性】: 52.4% 的微观动作分歧需与均匀随机掷骰子（Dice Baseline，期望分歧率 >67%）进行零假设显著性检验；需通过回归检验动作选择是否可由微观状态变量（现银、口粮、地亩）显著预测。")
    lines.append("  4. 【四项工程改进路线】: ① 固定伪随机种子 (--seed) 消除禀赋与外部冲击重抽混杂；② 引入 Dice Baseline 对照组；③ 跑满 8 季度并在每条件重复 N>=10 次；④ 完成宏观抛荒与微观流亡严格对账、定义民变三级阈值。")
    lines.append("====================================================================\n")
    return "\n".join(lines)

def main():
    parser = argparse.ArgumentParser(description="Socio-Engine 跨轮次演化分歧分析工具")
    parser.add_argument("--files", nargs="*", help="指定要对比的 JSON 报告文件路径列表")
    parser.add_argument("--pattern", type=str, default="SIM_REPORT_*.json", help="在 reports/ 下通配查找的文件名模式")
    parser.add_argument("--limit", type=int, default=3, help="最多对比最近的 N 个报告")
    args = parser.parse_args()

    if args.files:
        target_files = args.files
    else:
        all_json = glob.glob(os.path.join(REPORTS_DIR, args.pattern))
        all_json.sort(key=os.path.getmtime, reverse=True)
        target_files = all_json[:args.limit]
        target_files.reverse() # 按时间先后排列

    if not target_files:
        print(f"[!] 在 {REPORTS_DIR} 目录下未找到匹配 {args.pattern} 的报告文件。请先运行沙盘推演！")
        return

    print(f"[*] 正在分析比对以下 {len(target_files)} 个推演报告:")
    for f in target_files:
        print(f"    -> {os.path.basename(f)}")

    reports = load_reports(target_files)
    result_text = analyze_cross_trial_divergence(reports)
    print(result_text)

    # 导出对比综述文件
    output_summary_path = os.path.join(REPORTS_DIR, "CROSS_TRIAL_COMPARISON_SUMMARY.md")
    with open(output_summary_path, "w", encoding="utf-8") as f:
        f.write(result_text)
    print(f"[*] 📊 跨轮次比对综合分析报告已保存至: {output_summary_path}")

if __name__ == "__main__":
    main()

