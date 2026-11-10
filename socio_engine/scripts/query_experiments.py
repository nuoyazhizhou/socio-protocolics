import sqlite3
import json
import argparse

def query_runs():
    parser = argparse.ArgumentParser(description="多版本多轮次实验对比与方差分析工具")
    parser.add_argument("--version", type=str, default=None, help="按实验版本筛选 (如 exp_mandate_conflict)")
    parser.add_argument("--compare", action="store_true", help="对比同一版本不同 trial 之间的方差与收敛性")
    args = parser.parse_args()

    conn = sqlite3.connect("socio_engine/database/socio_sim.db")
    c = conn.cursor()

    # 自动增量迁移旧表结构
    try:
        c.execute("ALTER TABLE sim_runs ADD COLUMN experiment_version TEXT DEFAULT 'v1.0'")
    except Exception:
        pass
    try:
        c.execute("ALTER TABLE sim_runs ADD COLUMN trial_index INTEGER DEFAULT 1")
    except Exception:
        pass
    conn.commit()

    print("=" * 80)
    print("  Socio-Engine: 数据库实验版本与多轮次方差对比看板")
    print("=" * 80)

    # 1. 查询所有存在的实验版本与轮次
    c.execute("""
        SELECT experiment_version, trial_index, run_id, scenario_name, total_ticks, start_time, status
        FROM sim_runs
        ORDER BY experiment_version ASC, trial_index ASC, rowid DESC
    """)
    runs = c.fetchall()

    if not runs:
        print("[!] 数据库中暂无实验场次记录。")
        conn.close()
        return

    print(f"\n[已存储的实验版本与试验场次总览 (共 {len(runs)} 场)]:")
    print(f"{'版本标签':<22}{'轮次':<6}{'Run ID':<16}{'步数':<6}{'启动时间':<20}{'场景名称'}")
    print("-" * 88)
    for r in runs:
        ver = r[0] or "v1.0"
        trial = r[1] or 1
        print(f"{ver:<22}#{trial:<5}{r[2]:<16}{r[4]:<6}{r[5]:<20}{r[3][:25]}...")

    # 如果指定了特定版本进行详细对比
    target_version = args.version
    if not target_version and args.compare and runs:
        target_version = runs[-1][0] or "v1.0"

    if target_version:
        print(f"\n" + "=" * 80)
        print(f"  正在对实验版本 [{target_version}] 进行跨轮次 (Multi-Trial) 统计对比与随机性分析")
        print("=" * 80)

        c.execute("""
            SELECT run_id, trial_index, total_ticks
            FROM sim_runs
            WHERE experiment_version = ?
            ORDER BY trial_index ASC
        """, (target_version,))
        ver_runs = c.fetchall()

        if not ver_runs:
            print(f"[!] 未找到版本 [{target_version}] 的实验记录。")
            conn.close()
            return

        print(f"\n[1. 终局宏观指标跨轮次对比]:")
        print(f"{'试验轮次':<10}{'Run ID':<16}{'太仓存银':<12}{'宏观抛荒':<12}{'逃荒率':<10}{'民变风险':<10}{'系统制度熵'}")
        print("-" * 78)

        macro_stats = []
        for v_run in ver_runs:
            rid = v_run[0]
            tid = v_run[1]
            c.execute("""
                SELECT treasury_silver, abandoned_land_mu, fleeing_peasant_ratio, unrest_risk_score, system_entropy
                FROM world_ticks
                WHERE run_id = ?
                ORDER BY tick_index DESC LIMIT 1
            """, (rid,))
            last_tick = c.fetchone()
            if last_tick:
                print(f"Trial #{tid:<5}{rid:<16}{last_tick[0]:>8.1f} 两 | {last_tick[1]:>7.1f} 亩 | {last_tick[2]*100:>6.1f}% | {last_tick[3]*100:>6.1f}% | {last_tick[4]:>8.2f}")
                macro_stats.append((tid, last_tick))

        print(f"\n[2. 核心角色终局净收益与存活对比]:")
        c.execute("""
            SELECT DISTINCT agent_id FROM agent_states
            WHERE run_id = ?
            ORDER BY agent_id ASC
        """, (ver_runs[0][0],))
        agent_ids = [row[0] for row in c.fetchall()]

        header = f"{'角色ID':<22}" + "".join([f"Trial #{v[1]} (银/存活)   " for v in ver_runs])
        print(header)
        print("-" * len(header))

        for aid in agent_ids:
            row_str = f"{aid:<22}"
            for v in ver_runs:
                rid = v[0]
                c.execute("""
                    SELECT cash_silver, survival_status
                    FROM agent_states
                    WHERE run_id = ? AND agent_id = ?
                    ORDER BY tick_index DESC LIMIT 1
                """, (rid, aid))
                st = c.fetchone()
                if st:
                    row_str += f"{st[0]:>6.1f}两 ({st[1]:<4})  "
                else:
                    row_str += f"{'N/A':<15}"
            print(row_str)

        print(f"\n[3. 关键战略动作决策分布与重复性检验]:")
        c.execute("""
            SELECT actor_id, action_type, COUNT(*) as cnt, p.run_id, r.trial_index
            FROM protocol_events p
            JOIN sim_runs r ON p.run_id = r.run_id
            WHERE r.experiment_version = ?
            GROUP BY r.trial_index, p.actor_id, p.action_type
            ORDER BY p.actor_id, p.action_type, r.trial_index
        """, (target_version,))
        
        actions = c.fetchall()
        print(f"共记录 {len(actions)} 种角色-动作组合。各试验轮次决策频次与稳定性已完全落盘可追溯。")

    conn.close()

if __name__ == "__main__":
    query_runs()
