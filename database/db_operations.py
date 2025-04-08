import sqlite3
import time

def write_to_database(conn, device_id, timestamp, power_consumption):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO energy_usage (device_id, timestamp, power_consumption)
            VALUES (?, ?, ?)
        ''', (device_id, timestamp, power_consumption))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        conn.rollback()
        time.sleep(5)  # Retry after a delay
        write_to_database(conn, device_id, timestamp, power_consumption)

def write_energy_generation(conn, energy_source, timestamp, power_generated):
    try:
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO energy_generation (energy_source, timestamp, power_generated)
            VALUES (?, ?, ?)
        ''', (energy_source, timestamp, power_generated))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
        conn.rollback()
        time.sleep(5)  # Retry after a delay
        write_energy_generation(conn, energy_source, timestamp, power_generated)

def query_real_time(device_id=None, energy_source=None):
    conn = sqlite3.connect('energy_monitoring.db')
    cursor = conn.cursor()

    query = "SELECT * FROM energy_usage WHERE 1=1"
    params = []

    if device_id:
        query += " AND device_id = ? ORDER BY timestamp DESC LIMIT 1"
        params.append(device_id)
    
    cursor.execute(query, params)
    row = cursor.fetchone()

    conn.close()
    return row

def view_statistics(device_id=None, energy_source=None):
    conn = sqlite3.connect('energy_monitoring.db')
    cursor = conn.cursor()

    query_avg = "SELECT AVG(power_consumption) FROM energy_usage WHERE 1=1"
    query_peak = "SELECT MAX(power_consumption) FROM energy_usage WHERE 1=1"
    params = []

    if device_id:
        query_avg += " AND device_id = ?"
        query_peak += " AND device_id = ?"
        params.append(device_id)
    
    cursor.execute(query_avg, params)
    avg_consumption = cursor.fetchone()[0]

    cursor.execute(query_peak, params)
    peak_consumption = cursor.fetchone()[0]

    conn.close()
    return avg_consumption, peak_consumption

def view_total_energy_generation(energy_source=None):
    conn = sqlite3.connect('energy_monitoring.db')
    cursor = conn.cursor()

    query = "SELECT SUM(power_generated) FROM energy_generation WHERE 1=1"
    params = []

    if energy_source:
        query += " AND energy_source = ?"
        params.append(energy_source)

    cursor.execute(query, params)
    total_generated = cursor.fetchone()[0]

    conn.close()
    return total_generated

def compare_energy_source_efficiency():
    conn = sqlite3.connect('energy_monitoring.db')
    cursor = conn.cursor()

    query = "SELECT energy_source, AVG(power_generated) FROM energy_generation GROUP BY energy_source"
    cursor.execute(query)
    efficiency_data = cursor.fetchall()

    conn.close()
    return efficiency_data

def alert_low_generation(threshold):
    conn = sqlite3.connect('energy_monitoring.db')
    cursor = conn.cursor()

    query = "SELECT energy_source, AVG(power_generated) FROM energy_generation GROUP BY energy_source HAVING AVG(power_generated) < ?"
    cursor.execute(query, (threshold,))
    low_generation_sources = cursor.fetchall()

    conn.close()
    return low_generation_sources