import os
import shutil
import csv
import time
from datetime import datetime, timedelta


def move_and_rename_file(source_file, destination_dir, new_name):
    """Copies a file to the destination directory and renames it."""

    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)

    destination_file = os.path.join(destination_dir, new_name)
    shutil.copy2(source_file, destination_file)
    print(f"File '{source_file}' copied and renamed to '{destination_file}'.")


def process_csv(csv_file):
    """Processes the CSV file and schedules file operations based on the defined time."""

    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            source_dir = row[0]
            destination_dir = row[1]
            new_name = row[2]
            date = row[3]
            time_str = row[4]

            # Combine date and time into a single datetime object
            schedule_time = datetime.strptime(f"{date} {time_str}", "%Y-%m-%d %H:%M")
            current_time = datetime.now()

            # If the current time matches the scheduled time, perform the operation
            if schedule_time <= current_time < schedule_time + timedelta(minutes=1):
                if os.path.exists(source_dir):
                    for filename in os.listdir(source_dir):
                        source_file = os.path.join(source_dir, filename)
                        if os.path.isfile(source_file):
                            move_and_rename_file(source_file, destination_dir, new_name)
                else:
                    print(f"Source directory '{source_dir}' does not exist. Will retry later.")
            else:
                print(f"The scheduled operation for '{new_name}' is not yet due.")


if __name__ == "__main__":
    csv_file = input("Enter the path to the CSV file: ")

    try:
        print("Starting the file mover script. Press Ctrl+C to stop.")
        while True:
            process_csv(csv_file)
            time.sleep(60)  # Wait for 60 seconds before checking again
    except KeyboardInterrupt:
        print("\nOperation interrupted by the user. Exiting...")
    except Exception as e:
        print(f"Error: {e}")
