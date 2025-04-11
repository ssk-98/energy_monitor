import csv
import time

def write_device_data_to_csv(file_path, device_id, timestamp, power_consumption):
    # Append device power consumption data to CSV file
    try:
        with open(file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([device_id, '', timestamp, power_consumption, ''])
    except IOError as e:
        print(f"CSV write error: {e}")
        time.sleep(5)  # Retry after a delay
        write_device_data_to_csv(file_path, device_id, timestamp, power_consumption)

def write_energy_source_data_to_csv(file_path, energy_source, timestamp, power_generated):
    # Append energy generation data to CSV file
    try:
        with open(file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['', energy_source, timestamp, '', power_generated])
    except IOError as e:
        print(f"CSV write error: {e}")
        time.sleep(5)  # Retry after a delay
        write_energy_source_data_to_csv(file_path, energy_source, timestamp, power_generated)