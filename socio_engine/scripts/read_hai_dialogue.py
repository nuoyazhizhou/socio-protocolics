import sqlite3

conn = sqlite3.connect('socio_engine/database/socio_sim.db')
cur = conn.cursor()
cur.execute("""
    SELECT tick_index, parsed_intent 
    FROM dialogue_logs 
    WHERE run_id = 'run_e422c3a8' AND speaker_id = 'magistrate_hai_rui'
    ORDER BY tick_index
""")
for tick, intent in cur.fetchall():
    print(f"=== Tick {tick} 海瑞心智决策 ===")
    print(intent)
    print()

conn.close()
