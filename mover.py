import os
import shutil
import csv
import time
from datetime import datetime, timedelta
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

def move_and_rename_file(source_file, destination_dir, new_name):
    """Copies a file to the destination directory and renames it."""

    if not os.path.exists(destination_dir):
        os.makedirs(destination_dir)
        print(f"{Fore.YELLOW}Warning: Destination directory '{destination_dir}' does not exist. Creating it.")

    destination_file = os.path.join(destination_dir, new_name)
    shutil.copy2(source_file, destination_file)
    print(f"{Fore.GREEN}Success: File '{source_file}' copied and renamed to '{destination_file}'.")


def process_csv(csv_file):
    """Processes the CSV file and schedules file operations based on the defined time."""

    print(f"{Fore.BLUE}Info: Processing the CSV file: '{csv_file}'")
    with open(csv_file, newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            source_dir = row['source_dir']
            destination_dir = row['destination_dir']
            new_name = row['new_name']
            date = row['date']
            time_str = row['time']

            # Combine date and time into a single datetime object
            schedule_time = datetime.strptime(f"{date} {time_str}", "%Y-%m-%d %H:%M")
            current_time = datetime.now()

            # Log the details of the scheduled operation
            print(f"{Fore.BLUE}Info: Scheduled operation: Copy from '{source_dir}' to '{destination_dir}' as '{new_name}' "
                  f"on {schedule_time.strftime('%Y-%m-%d %H:%M')}")

            # If the current time matches the scheduled time, perform the operation
            if current_time >= schedule_time and current_time < schedule_time + timedelta(minutes=1):
                if os.path.exists(source_dir):
                    for filename in os.listdir(source_dir):
                        source_file = os.path.join(source_dir, filename)
                        if os.path.isfile(source_file):
                            move_and_rename_file(source_file, destination_dir, new_name)
                        else:
                            print(f"{Fore.YELLOW}Warning: Skipping '{filename}' - Not a file.")
                else:
                    print(f"{Fore.YELLOW}Warning: Source directory '{source_dir}' does not exist. Will retry later.")
            else:
                print(f"{Fore.BLUE}Info: The scheduled operation for '{new_name}' is not yet due. Current time is {current_time.strftime('%Y-%m-%d %H:%M')}.")


if __name__ == "__main__":
    csv_file = input(f"{Fore.BLUE}Enter the path to the CSV file: ")

    try:
        print(f"{Fore.BLUE}Info: Starting the file mover script. Press Ctrl+C to stop.")
        while True:
            print(f"\n{Fore.BLUE}Info: Checking scheduled operations...")
            process_csv(csv_file)
            print(f"{Fore.BLUE}Info: Waiting for the next check...")
            time.sleep(60)  # Wait for 60 seconds before checking again
    except KeyboardInterrupt:
        print(f"\n{Fore.RED}Error: Operation interrupted by the user. Exiting...")
    except Exception as e:
        print(f"{Fore.RED}Fatal Error: An error occurred: {e}")
