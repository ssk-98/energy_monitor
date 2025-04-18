import threading
from database.db_setup import setup_database
from csv_handler.csv_setup import setup_csv
from sensors.simulator import simulate_sensor_data, simulate_energy_generation
from gui.app import setup_gui

def main():
    # Setup database and CSV file
    setup_database()
    csv_file = 'energy_usage.csv'
    setup_csv(csv_file)

    # Start simulation for appliances
    devices = ["TV", "Fan", "Air Conditioner"]
    threads = []

    for device_id in devices:
        thread = threading.Thread(target=simulate_sensor_data, args=(device_id, csv_file))
        threads.append(thread)
        thread.start()

    # Start simulation for energy sources
    energy_sources = ["solar", "wind turbine", "storage battery", "grid"]
    for energy_source in energy_sources:
        thread = threading.Thread(target=simulate_energy_generation, args=(energy_source, csv_file))
        threads.append(thread)
        thread.start()

    # Start GUI
    setup_gui()

if __name__ == '__main__':
    main()