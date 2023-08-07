#!/usr/bin/env python3

import sys

# Read lines from standard input
for line in sys.stdin:
    # Split the line into fields
    fields = line.strip().split(',')
    
    # Check if the line has the right number of fields
    if len(fields) >= 4:
        # Get the body type (column number 4)
        body_type = fields[3]

        # Emit the body type as the key with a count of 1
        print(f"{body_type}\t1")
