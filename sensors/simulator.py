import random
import time
from datetime import datetime
import sqlite3
from database.db_operations import write_to_database, write_energy_generation
from csv_handler.csv_operations import write_to_csv

def simulate_sensor_data(device_id, csv_file):
    conn = sqlite3.connect('energy_monitoring.db')
    device_power_ranges = {
        "TV": (50, 150),
        "Fan": (10, 75),
        "Air Conditioner": (500, 1500)
    }
    
    try:
        while True:
            base_power_consumption = random.uniform(*device_power_ranges[device_id])
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            write_to_database(conn, device_id, timestamp, base_power_consumption)
            write_to_csv(csv_file, device_id, timestamp, base_power_consumption)
            time.sleep(1)
    except Exception as e:
        print(f"Error in sensor data simulation: {e}")
        time.sleep(5)
        simulate_sensor_data(device_id, csv_file)
    finally:
        conn.close()

def simulate_energy_generation(energy_source):
    conn = sqlite3.connect('energy_monitoring.db')
    energy_generation_ranges = {
        "solar": (50, 300),
        "wind turbine": (100, 500),
        "storage battery": (30, 200),
        "grid": (500, 1500)
    }
    
    try:
        while True:
            power_generated = random.uniform(*energy_generation_ranges[energy_source])
            timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
            write_energy_generation(conn, energy_source, timestamp, power_generated)
            time.sleep(1)
    except Exception as e:
        print(f"Error in energy generation simulation: {e}")
        time.sleep(5)
        simulate_energy_generation(energy_source)
    finally:
        conn.close()