# Continuous Okla Speedtest
This script continuously runs speed tests using the Okla Speedtest CLI tool, saving the results in a CSV file. The script allows for flexible test configuration, including specifying the test duration, interval between tests, and selecting a specific server for the speed test.

## Prerequisites:
-	Python 3.11.9 or higher
-	Speedtest CLI (version 1.2.0)
-	Windows 10/11 with CMD

## First Time Usage
Run the provided batch script (install-python-repo.bat) to automatically install Python and download the Speedtest CLI.
```
Install-python-repo.bat
```
The script checks if Python and the necessary directories are already installed. If they are, the installation steps are skipped.

## Usage
Run the Continuous Speed Test
1.	Open your terminal or command prompt.
2.	Navigate to the directory containing the script.
3.	Run the script:
```
Start Continuous Okla Speedtest rev02.bat
```
## Configuration
•	Test Duration: Specify the duration for running the test in hours.
•	Interval: Set the interval between tests in minutes.
•	Server ID: (Optional) Specify a Speedtest server ID to test against a specific server. If not provided, the script will automatically select a server.

## Example Usage
```
Start Continuous Okla Speedtest rev02.bat
```
-- or --

```
python3 Continuous-okla-Speedtest-rev02.py
```
The script will prompt you to enter the test name, duration, and interval. It will also give you the option to specify a server ID.
Output
The results are saved in a CSV file with a timestamp and the test name in the filename (e.g., testname-20240827-171413.csv).
The CSV file includes detailed information from each test, such as:
-	Timestamp
-	Ping (jitter and latency)
-	Download speed (bandwidth, bytes, and elapsed time)
-	Upload speed (bandwidth, bytes, and elapsed time)
-	Packet loss
-	ISP details
-	Interface details (internal and external IPs)
-	Server information (ID, host, location, IP)
-	Result URL
## Countdown Timer
During the waiting period between tests, the script displays a countdown timer showing the time remaining until the next test.

## Error Handling
If the script encounters any errors during testing, it will log the error and continue with the next test.

## Noted
This was create for fun and work propose and do not expect me to update this anytime soon. Feel free to fork this repo and improve it as you like
This Script was inspire from nikiluk automate-ookla-speedtest

