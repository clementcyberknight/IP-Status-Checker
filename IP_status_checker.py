import csv
import os


def ping_ip(ip_address):
    """
    Check if an IP address is reachable by executing the ping command.
    """
    try:
        # Execute the ping command and capture the output
        response = os.popen(f"ping -c 4 {ip_address}").read()

        # Check if the response contains any indication of success or failure
        if "Request timed out." in response or "unreachable" in response:
            return False
        else:
            return True
    except Exception as e:
        print(f"Error occurred while pinging {ip_address}: {e}")
        return False


def main():
    # Path to the input CSV file containing IP addresses
    input_csv_file = "ip_addresses.csv"

    # Open the input CSV file and read IP addresses
    with open(input_csv_file, "r") as file:
        reader = csv.reader(file)
        ip_addresses = [row[0] for row in reader]

    # Ping each IP address and print the result
    print("IP Address\t\tStatus")
    with open("ip_status.csv", "w") as output_file:
        writer = csv.writer(output_file)
        writer.writerow(["IP Address", "Status"])

        for ip_address in ip_addresses:
            status = "up" if ping_ip(ip_address) else "down"
            print(f"{ip_address}\t\t{status}")
            writer.writerow([ip_address, status])


if __name__ == "__main__":
    main()
