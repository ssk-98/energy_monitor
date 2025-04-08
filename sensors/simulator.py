import random
import time
from datetime import datetime
import sqlite3
from database.db_operations import write_to_database
from csv_handler.csv_operations import write_to_csv

def simulate_sensor_data(device_id, csv_file):
    conn = sqlite3.connect('energy_monitoring.db')
    while True:
        power_consumption = random.uniform(100, 500)  # Simulate power consumption in watts
        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')  # Current timestamp
        write_to_database(conn, device_id, timestamp, power_consumption)
        write_to_csv(csv_file, device_id, timestamp, power_consumption)
        time.sleep(1)  # Simulate real-time data acquisition every second
    conn.close()