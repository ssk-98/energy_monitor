import sqlite3

def setup_database():
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect('energy_monitoring.db')
    cursor = conn.cursor()

    # Create table for appliance energy usage
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS energy_usage (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            device_id TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            power_consumption REAL NOT NULL
        )
    ''')

    # Create table for energy generation from sources
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS energy_generation (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            energy_source TEXT NOT NULL,
            timestamp TEXT NOT NULL,
            power_generated REAL NOT NULL
        )
    ''')

    # Commit changes and close connection
    conn.commit()
    conn.close()