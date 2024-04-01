# Network Professional Must-Have: IP Ping Checker

## Overview
This Python script serves as a fundamental tool for network professionals by providing a simple yet effective means to check the reachability of multiple IP addresses. It utilizes the `ping` command to ascertain whether an IP address is responsive or not.

## Features
- **Bulk IP Address Checking**: The script reads IP addresses from an input CSV file, allowing network professionals to check the status of multiple IPs in one go.
- **Concise Status Reporting**: It outputs the status of each IP address, indicating whether it is up or down, in both the console and an output CSV file.
- **Error Handling**: The script handles potential errors gracefully, ensuring smooth execution even in the presence of network issues or incorrect input.

## Usage
1. **Input CSV File**: Prepare an input CSV file named `ip_addresses.csv` containing the list of IP addresses to be checked. Ensure that each IP address is listed in a separate row under the first column.
2. **Execute the Script**: Run the script by executing the `main()` function. Ensure that the script file and the input CSV file are in the same directory.
3. **Check IP Status**: Once executed, the script will ping each IP address listed in the input CSV file and display its status (up/down) in the console. Additionally, it will generate an output CSV file named `ip_status.csv` containing the IP addresses and their corresponding statuses.

## Requirements
- Python 3.x
- `csv` module (standard library)
- Operating System supporting the `ping` command (e.g., Linux, macOS, Windows)

## Example
Suppose you have an input CSV file `ip_addresses.csv` with the following IP addresses:
192.168.1.1
8.8.8.8
10.0.0.1
Executing the script will produce output similar to the following in the console:
- 192.168.1.1
- 8.8.8.8
- 10.0.0.1

Simultaneously, it will generate an output CSV file `ip_status.csv` containing:
- IP Address,Status
- 192.168.1.1,up
- 8.8.8.8,up
- 10.0.0.1,down
