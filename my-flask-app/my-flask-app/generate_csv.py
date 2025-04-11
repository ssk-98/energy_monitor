
import csv
import time
import random
from datetime import datetime

# List of device IDs
device_ids = ['A100', 'B200', 'C300', 'D400', 'E500']

# File name
csv_file = 'device_power_data.csv'

# Write header if file doesn't exist
try:
    with open(csv_file, 'x', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(['device_id', 'timestamp', 'power_consumption'])
except FileExistsError:
    pass  # File already exists, do nothing

# Start appending data every 5 seconds
print("Generating data... Press Ctrl+C to stop.")
try:
    while True:
        device_id = random.choice(device_ids)
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        power = round(random.uniform(20.0, 100.0), 2)  # Random power between 20W and 100W

        with open(csv_file, 'a', newline='') as f:
            writer = csv.writer(f)
            writer.writerow([device_id, timestamp, power])

        print(f"Added: {device_id}, {timestamp}, {power}W")
        time.sleep(5)
except KeyboardInterrupt:
    print("\nStopped data generation.")

