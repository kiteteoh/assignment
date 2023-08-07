                                                                                                                    wordcount.py                                                                                                                                  
#!/usr/bin/env python3

import sys

#Dictionary to store the word count for the "body_type" column
body_type_count = {}

#Iterate through each line in the input data received from Hadoop Streaming
for line in sys.stdin:
    line = line.strip()  # Remove leading/trailing whitespaces
    fields = line.split(',')  # Split the CSV line into fields

    # Assuming "body_type" is the 4th column in your CSV data
    if len(fields) >= 4:
        body_type = fields[3].strip().lower()  # Extract and convert the body_type to lowercase

        # Increment the count of the manufacturer in the dictionary
        body_type_count[body_type] = body_type_count.get(body_type, 0) + 1

#Output the result
for body_type, count in body_type_count.items():
    print(f"{body_type}: {count}")
