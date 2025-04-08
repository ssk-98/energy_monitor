import sqlite3

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

def query_real_time(device_id=None):
    conn = sqlite3.connect('energy_monitoring.db')
    cursor = conn.cursor()

    query = "SELECT * FROM energy_usage WHERE 1=1"
    params = []

    if device_id:
        query += " AND device_id = ? ORDER BY timestamp DESC LIMIT 1"
        params.append(device_id)
    else:
        query += " ORDER BY timestamp DESC LIMIT 1"

    cursor.execute(query, params)
    row = cursor.fetchone()

    conn.close()
    return row

def view_statistics(device_id=None):
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