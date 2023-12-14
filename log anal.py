# Sample log file path (replace with your log file path)
log_file_path = 'sample.log_path'
def parse_log_file(log_path):
    with open(log_path, 'r') as file:
        # Read each line in the log file
        for line in file:
            # Process each line (you can modify this according to your log format)
            # For example, let's assume a simple format of 'timestamp - message'
            parts = line.split(' - ')
            if len(parts) == 2:
                timestamp = parts[0]
                message = parts[1].strip()  # Remove leading/trailing whitespaces
                # Here you can perform further analysis or print the extracted information
                print(f"Timestamp: {timestamp}, Message: {message}")

# Call the function with the log file path
parse_log_file(log_file_path)
