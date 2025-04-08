import threading
from database.db_setup import setup_database
from csv_handler.csv_setup import setup_csv
from sensors.simulator import simulate_sensor_data
from gui.app import setup_gui

def main():
    setup_database()
    csv_file = 'energy_usage.csv'
    setup_csv(csv_file)

    # Start simulation in separate threads
    devices = ["device_1", "device_2", "device_3"]
    threads = []

    for device_id in devices:
        thread = threading.Thread(target=simulate_sensor_data, args=(device_id, csv_file))
        threads.append(thread)
        thread.start()

    # Start GUI
    setup_gui()

if __name__ == '__main__':
    main()