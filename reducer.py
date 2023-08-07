#!/usr/bin/env python3

import sys

# Initialize variables to track the current body_type and count
current_body_type = None
current_count = 0

# Process each line from standard input
for line in sys.stdin:
    line = line.strip()
    body_type, count = line.split('\t', 1)  # Split the input into body_type and count

    try:
        count = int(count)  # Convert count to integer
    except ValueError:
        continue  # Skip lines with invalid counts

    # If the body_type is the same as the current one, increment the count
    if current_body_type == body_type:
        current_count += count
    else:
        # If a new body_type is encountered, print the count for the previous body_type
        if current_body_type:
            print(f"{current_body_type}\t{current_count}")
        current_body_type = body_type  # Update current body_type
        current_count = count  # Reset count for the new body_type

# Print the count for the last body_type encountered
if current_body_type:
    print(f"{current_body_type}\t{current_count}")
