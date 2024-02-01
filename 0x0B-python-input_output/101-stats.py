#!/usr/bin/python3
"""reads stdin line by line and compute metrics"""
import sys
from collections import defaultdict

total_size = 0
status_counts = defaultdict(int)
line_count = 0

try:

    for line in sys.stdin:
        """insert comment here later"""
        parts = line.strip().split()
        size = int(parts[-1])
        status_code = parts[-2]

        total_size += size

        status_counts[status_code] += 1

        line_count += 1

        if line_count % 10 == 0:
            print("Total file size:", total_size)
            for status_code in sorted(status_counts.keys()):
                count = status_counts[status_code]
                print(status_code + ":", count)

    print("Total file size:", total_size)
    for status_code in sorted(status_counts.keys()):
        count = status_counts[status_code]
        print(status_code + ":", count)

except KeyboardInterrupt:

    print("\nTotal file size:", total_size)
    for status_code in sorted(status_counts.keys()):
        count = status_counts[status_code]
        print(status_code + ":", count)

