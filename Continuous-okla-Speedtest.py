import subprocess
import time
import csv
import json
from datetime import datetime, timedelta


# Function to flatten JSON data, including updated latency details
def flatten_json(json_data):
    flat_data = {}
    for key, value in json_data.items():
        if isinstance(value, dict):
            for sub_key, sub_value in value.items():
                if isinstance(sub_value, dict):
                    for sub_sub_key, sub_sub_value in sub_value.items():
                        flat_data[f"{key}_{sub_key}_{sub_sub_key}"] = sub_sub_value
                else:
                    # Insert calculated_download_speed right after download_bandwidth
                    if key == 'download' and sub_key == 'bandwidth':
                        flat_data[f"{key}_{sub_key}"] = sub_value
                        flat_data['download_bandwidth_mbps'] = sub_value / 125000  # Example calculation
                    elif key == 'upload' and sub_key == 'bandwidth':
                        flat_data[f"{key}_{sub_key}"] = sub_value
                        flat_data['upload_bandwidth_mbps'] = sub_value / 125000  # Example calculation
                    else:
                        flat_data[f"{key}_{sub_key}"] = sub_value
        else:
            flat_data[key] = value
    return flat_data

# Function to convert JSON to CSV and write to a file in real-time
def write_json_to_csv(flat_data, csv_file):
    with open(csv_file, 'a', newline='') as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=flat_data.keys())
        
        # Write header only if file is empty
        if csvfile.tell() == 0:
            writer.writeheader()
        
        # Write data
        writer.writerow(flat_data)

# Function to run the speed test
def run_speedtest(server_id=None):
    command = ["speedtest", "--format=json", "--unit=Mbps"]
    
    if server_id:
        command.extend(["--server-id", server_id])
    
    result = subprocess.run(command, capture_output=True, text=True)
    if result.returncode != 0:
        print(f"Error running speedtest: {result.stderr}")
        return None
    
    return json.loads(result.stdout)

# Function to show countdown timer
def countdown(minutes):
    for i in range(minutes * 60, 0, -1):
        mins, secs = divmod(i, 60)
        timeformat = f"{mins:02}:{secs:02}"
        print(f"Time until next test: {timeformat}", end='\r')
        time.sleep(1)
    print()  # Clear the line after countdown

# User input for test details
test_name = input("Enter test name: ")
# Default values
default_test_duration_hours = 1.0  # Default to 1 hour
default_interval_minutes = 5       # Default to 5 minutes
# User input for test duration and interval
test_duration_hours = input(f"Enter test duration in hours (default: {default_test_duration_hours}): ")
interval_minutes = input(f"Enter interval between tests in minutes (default: {default_interval_minutes}): ")

server_id = input("Enter server ID (or press Enter for auto-select): ")

# Convert input to float/int, or use default values if input is empty
test_duration_hours = float(test_duration_hours) if test_duration_hours else default_test_duration_hours
interval_minutes = int(interval_minutes) if interval_minutes else default_interval_minutes
# Calculate number of tests based on duration and interval
end_time = datetime.now() + timedelta(hours=test_duration_hours)
csv_file = fr"results\{test_name}-{datetime.now().strftime('%Y%m%d-%H%M%S')}.csv"

print(f"---\n Continuous Speedtest \n Start at: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')} \n End at: {end_time.strftime('%Y-%m-%d %H:%M:%S')} \n---")
i=0
# Run the tests
while datetime.now() < end_time:
    # Run the speedtest
    i += 1
    print(f"===\nTest No: {i} \nStart at {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    test_data = run_speedtest(server_id)
    
    if test_data:
        
        # Calculate download and upload speeds
        download_speed = test_data['download']['bandwidth'] / 125000  # Convert to Mbps
        upload_speed = test_data['upload']['bandwidth'] / 125000  # Convert to Mbps
        
        flat_data = flatten_json(test_data)
        # Save the data to CSV in real-time
        write_json_to_csv(flat_data, csv_file)
        
        # Display the download and upload speeds
        print(f"\nServer: {test_data['server']['name']}, ID: {test_data['server']['id']}")
        print(f"Download Speed: {download_speed:.2f} Mbps")
        print(f"Upload Speed: {upload_speed:.2f} Mbps")
        print(f"Latency: {test_data['ping']['latency']:.2f} ms, Packet Loss: {test_data['packetLoss']:.2f} % ")
    else:
        print("Failed to run the speedtest.")
    
    print(f"\nNext Test will start at {(datetime.now() + timedelta(minutes=interval_minutes)).strftime('%H:%M:%S')}")
    # Countdown until the next test
    if datetime.now() < end_time:
        countdown(interval_minutes)

print("All tests completed.")

#tasuke93 - project for fun and use for telco VQ
