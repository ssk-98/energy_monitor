import os
import csv

def setup_csv(file_path):
    if not os.path.exists(file_path):
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['device_id', 'timestamp', 'power_consumption'])