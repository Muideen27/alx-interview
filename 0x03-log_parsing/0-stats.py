#!/usr/bin/python3
''' module for log parsing '''

import sys

# Initialize metrics
total_file_size = 0
status_code_counts = {}

try:
    line_count = 0
    for line in sys.stdin:
        line_count += 1
        
        # Split the line into components
        parts = line.strip().split()
        if len(parts) != 7:
            continue  # Skip lines with incorrect format
        
        ip_address, _, _, _, status_code, file_size = parts
        
        # Check if status code is a valid integer
        if not status_code.isdigit():
            continue
        
        # Update metrics
        total_file_size += int(file_size)
        status_code_counts[int(status_code)] = status_code_counts.get(int(status_code), 0) + 1
        
        # Print statistics every 10 lines
        if line_count % 10 == 0:
            print("Total file size:", total_file_size)
            for code in sorted(status_code_counts.keys()):
                print(f"{code}: {status_code_counts[code]}")
            print()
            
except KeyboardInterrupt:
    print("\nKeyboard interruption detected. Printing statistics:")
    print("Total file size:", total_file_size)
    for code in sorted(status_code_counts.keys()):
        print(f"{code}: {status_code_counts[code]}")

