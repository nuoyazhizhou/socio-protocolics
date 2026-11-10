import sqlite3
import json

conn = sqlite3.connect('socio_engine/database/socio_sim.db')
cur = conn.cursor()

print("=== 海瑞突破版 Trial #2 (run_e422c3a8) 每季度决策与心智日志 ===")
cur.execute("""
    SELECT tick_index, action_type, target_id, action_payload
    FROM protocol_events 
    WHERE run_id = 'run_e422c3a8' AND actor_id = 'magistrate_hai_rui' 
    ORDER BY tick_index
""")
for tick, act, tgt, payload in cur.fetchall():
    print(f"【第 {tick} 季度】动作: [{act}] | 目标: {tgt}")
    try:
        p = json.loads(payload)
        print(f"  载荷: {p}")
    except:
        print(f"  载荷: {payload}")

print("\n=== 全部重点实验终局宏观对比 ===")
cur.execute("""
    SELECT r.run_id, r.experiment_version, r.trial_index,
           w.treasury_silver, w.abandoned_land_mu, w.fleeing_peasant_ratio, w.unrest_risk_score, w.system_entropy
    FROM sim_runs r
    JOIN world_ticks w ON r.run_id = w.run_id
    WHERE r.run_id IN ('run_52ed940d', 'run_2df8b194', 'run_cf7532c3', 'run_e422c3a8')
      AND w.tick_index = 8
    ORDER BY r.start_time
""")
runs = cur.fetchall()
print(f"{'版本':<25} | {'轮次':<4} | {'Run ID':<13} | {'太仓存银':<10} | {'官田抛荒':<8} | {'逃亡率':<8} | {'民变风险':<8} | {'系统制度熵'}")
print("-" * 105)
for r in runs:
    print(f"{r[1]:<25} | #{r[2]:<3} | {r[0]:<13} | {r[3]:<10.1f} | {r[4]:<8.1f} | {r[5]*100:<7.1f}% | {r[6]*100:<7.1f}% | {r[7]:.2f}")

print("\n=== Trial #2 核心角色终局净资产与存活 ===")
cur.execute("""
    SELECT agent_id, cash_silver, stored_grain, land_owned_mu, survival_status
    FROM agent_states
    WHERE run_id = 'run_e422c3a8' AND tick_index = 8
    ORDER BY cash_silver DESC
""")
for ag, sil, grn, lnd, st in cur.fetchall():
    print(f"  - {ag:<22}: 银={sil:.2f}两, 粮={grn:.1f}石, 地={lnd:.1f}亩, 状态={st}")

conn.close()
