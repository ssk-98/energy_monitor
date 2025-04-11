import os
import csv

def setup_csv(file_path):
    # Create CSV file with header if it doesn't exist
    if not os.path.exists(file_path):
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['device_id', 'energy_source', 'timestamp', 'power_consumption', 'power_generated'])