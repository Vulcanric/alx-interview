#!/usr/bin/python3
""" Log Parsing """
import sys
import shlex
from collections import defaultdict

total_size = 0
status_counts = defaultdict(int)

for i, line in enumerate(sys.stdin):
    try:
        parts = shlex.split(line)
        if len(parts) != 7:
            continue
        ip, date, request = parts[0], parts[2], parts[3]
        status, size = parts[4], parts[5]
        if not (status.isdigit() and size.isdigit()):
            continue
        total_size += int(size)
        status_counts[int(status)] += 1
        if (i + 1) % 10 == 0:
            print(f"File size: {total_size}")
            for status in sorted(status_counts.keys()):
                print(f"{status}: {status_counts[status]}")
    except KeyboardInterrupt:
        print(f"File size: {total_size}")
        for status in sorted(status_counts.keys()):
            print(f"{status}: {status_counts[status]}")
        break
