total = 0  # Variable to keep track of total file size
counter = 0  # Counter to keep track of the number of lines processed
sc_dict = {'200': 0, '301': 0, '400': 0, '401': 0,
           '403': 0, '404': 0, '405': 0, '500': 0}  # Dictionary to count status codes

def print_data(total):
    ''' Function to print statistics for the input '''
    print('File size: {}'.format(total))
    for key, value in sorted(sc_dict.items()):
        if value != 0:
            print('{}: {}'.format(key, value))

try:
    for line in sys.stdin:  # Read each line from input
        rline = line.split(" ")  # Split line into parts
        if len(rline) > 4:  # Check if line has enough parts
            code = rline[-2]  # Get the status code
            if code in sc_dict.keys():
                sc_dict[code] += 1  # Count the status code
            filesize = int(rline[-1])  # Get the file size
            total += filesize  # Add to total file size
            counter += 1  # Increment the counter
        if counter == 10:  # If 10 lines have been processed
            counter = 0  # Reset the counter
            print_data(total)  # Print statistics
except Exception as ex:
    pass
finally:
    print_data(total)  # Print final statistics
