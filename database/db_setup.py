import sqlite3

def setup_database():
    conn = sqlite3.connect('energy_monitoring.db')
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS energy_usage (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            device_id TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            power_consumption REAL NOT NULL
        )
    ''')
    conn.commit()
    conn.close()