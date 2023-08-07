#!/usr/bin/env python3

import sys

# Process each line from standard input
for line in sys.stdin:
    line = line.strip()
    fields = line.split(',')  # Split the CSV line into fields

    # Assuming "body_type" is the 4th column in your CSV data
    if len(fields) >= 4:
        body_type = fields[3].strip().lower()  # Extract and convert the body_type to lowercase
        print(f"{body_type}\t1")  # Output the body_type as key and 1 as value
