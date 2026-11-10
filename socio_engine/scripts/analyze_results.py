import sqlite3
import json

def analyze():
    conn = sqlite3.connect('socio_engine/database/socio_sim.db')
    c = conn.cursor()

    # 1. Latest run
    c.execute("SELECT run_id, scenario_name, start_time FROM sim_runs ORDER BY rowid DESC LIMIT 1")
    run_row = c.fetchone()
    print("="*65)
    print(f"  最新推演实验: {run_row[0]} | {run_row[1]}")
    print(f"  启动时间: {run_row[2]}")
    print("="*65)
    run_id = run_row[0]

    # 2. Macro evolution over 20 ticks
    print("\n[一、宏观五年 (20 季度) 动态演化总表 (Macro Evolution)]")
    print(f"{'季度':<6}{'朝代纪年':<12}{'太仓存银':<10}{'当季米价':<10}{'抛荒田亩':<10}{'流亡比率':<10}{'民变风险':<10}{'制度熵(技术债)':<12}")
    print("-" * 82)
    c.execute("""
        SELECT tick_index, treasury_silver, grain_price_silver, abandoned_land_mu, fleeing_peasant_ratio, unrest_risk_score, system_entropy
        FROM world_ticks WHERE run_id = ?
        ORDER BY tick_index ASC
    """, (run_id,))
    
    ticks = c.fetchall()
    season_names = {1: "春", 2: "夏", 3: "秋", 4: "冬"}
    for r in ticks:
        t = r[0]
        y = (t - 1) // 4 + 1
        q = (t - 1) % 4 + 1
        chron = f"万历{y}年{season_names[q]}"
        print(f"Tick {t:02d} | {chron:<10} | {r[1]:>7.1f} 两 | {r[2]:>6.2f} 两/石 | {r[3]:>6.1f} 亩 | {r[4]*100:>6.1f}% | {r[5]*100:>6.1f}% | {r[6]:>8.2f}")

    # 3. Agent states at tick 0 vs tick 20
    print("\n[二、微观家庭资产与生存状态大分化 (Micro Agents Comparison: Tick 0 vs Tick 20)]")
    print(f"{'角色':<22}{'初始银/粮/田':<20}{'最终银/粮/田(隐亩)':<24}{'赋税积欠':<10}{'终局效用':<10}{'状态':<8}")
    print("-" * 96)
    
    c.execute("""
        SELECT a.agent_id, a.role_name, 
               s0.cash_silver, s0.stored_grain, s0.land_owned_mu,
               s20.cash_silver, s20.stored_grain, s20.land_owned_mu, s20.land_hidden_mu, s20.tax_arrears, s20.utility_score, s20.survival_status
        FROM agent_registry a
        LEFT JOIN agent_states s0 ON a.agent_id = s0.agent_id AND s0.run_id = ? AND s0.tick_index = 0
        LEFT JOIN agent_states s20 ON a.agent_id = s20.agent_id AND s20.run_id = ? AND s20.tick_index = 20
        WHERE a.run_id = ?
        ORDER BY s20.utility_score DESC
    """, (run_id, run_id, run_id))

    for row in c.fetchall():
        aid, name, s0_sil, s0_gr, s0_ld, s20_sil, s20_gr, s20_ld, s20_hld, s20_arr, s20_ut, s20_st = row
        init_str = f"{s0_sil:.0f}两/{s0_gr:.0f}石/{s0_ld:.0f}亩"
        fin_str = f"{s20_sil:.1f}两/{s20_gr:.1f}石/{s20_ld:.1f}亩(+{s20_hld:.0f})"
        print(f"{name:<22} | {init_str:<18} | {fin_str:<22} | {s20_arr:>6.1f}两 | {s20_ut:>8.1f} | {s20_st}")

    # 4. Action breakdown and Rent extraction
    print("\n[三、中介寻租与兼并剥夺汇总 (RFC-004 & O4 Middleware Exploitation)]")
    c.execute("""
        SELECT a.role_name, p.action_type, COUNT(*), SUM(p.rent_extracted)
        FROM protocol_events p
        JOIN agent_registry a ON p.actor_id = a.agent_id AND p.run_id = a.run_id
        WHERE p.run_id = ?
        GROUP BY p.actor_id, p.action_type
        ORDER BY SUM(p.rent_extracted) DESC
    """, (run_id,))
    for row in c.fetchall():
        print(f"  - {row[0]:<20} | 动作: {row[1]:<20} | 频次: {row[2]:>2} 次 | 提取租金/兼并额: {row[3]:>6.1f} 两/折银")

    # 5. Key critical dialogues/intents
    print("\n[四、关键转折点心智博弈 (Key Cognitive Decisions & Turning Points)]")
    c.execute("""
        SELECT tick_index, speaker_id, parsed_intent
        FROM dialogue_logs
        WHERE run_id = ? AND tick_index IN (2, 3, 5, 8, 12, 16, 20)
        ORDER BY tick_index ASC, dialogue_id ASC
    """, (run_id,))
    
    current_tick = -1
    for r in c.fetchall():
        if r[0] != current_tick:
            current_tick = r[0]
            y = (current_tick - 1) // 4 + 1
            q = (current_tick - 1) % 4 + 1
            print(f"\n  === 第 {current_tick:02d} 轮 (万历 {y} 年 {season_names[q]}季) ===")
        intent_clean = r[2].replace('\n', ' ').strip()
        print(f"    * [{r[1]}]: {intent_clean[:120]}...")

    conn.close()

if __name__ == '__main__':
    analyze()
