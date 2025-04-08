import csv

def write_to_csv(file_path, device_id, timestamp, power_consumption):
    try:
        with open(file_path, mode='a', newline='') as file:
            writer = csv.writer(file)
            writer.writerow([device_id, timestamp, power_consumption])
    except IOError as e:
        print(f"CSV write error: {e}")