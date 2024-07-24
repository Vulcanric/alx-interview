#!/usr/bin/python3
""" Log Parsing """
import sys
import signal
import re
from collections import defaultdict
from typing import Dict


if __name__ == "__main__":
    """
    Log format: <IPv4> - [<date>] "<http-request>" <status-code> <file-size>
    """
    status_count = defaultdict(int)
    total_size = 0

    # Retrieving individual data points using regex patterns
    ip_r = r'(?P<ip>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})'
    date_r, req_r = r'\[(?P<dt>.+)\]', r'(?P<req>.+)'
    stat_r, size_r = r'(?P<stat>\d{3})', r'(?P<sz>\d+)'

    # General line pattern involves all the above patterns
    rformat = f'{ip_r} - {date_r} {req_r} {stat_r} {size_r}'

    try:
        for i, line in enumerate(sys.stdin, start=1):
            res = re.match(rformat, line)

            if not res:  # Line doesn't match format
                continue  # Skip the line

            ip, date, request, status, size = \
                res.group('ip'),\
                res.group('dt'),\
                res.group('req'),\
                res.group('stat'),\
                res.group('sz')

            if not (status.isdigit() and size.isdigit()):
                continue

            status_count[int(status)] += 1
            total_size += int(size)

            # Case 1: After 10 lines
            if i % 10 == 0:
                print(f"File size: {total_size}")
                for status in sorted(status_count.keys()):
                    print(f"{status}: {status_count[status]}")

        # Case 2: After done reading
        print(f"File size: {total_size}")
        for status in sorted(status_count.keys()):
            print(f"{status}: {status_count[status]}")

    except KeyboardInterrupt:  # Case 3: ctrl + c event
        print(f"File size: {total_size}")
        for status in sorted(status_count.keys()):
            print(f"{status}: {status_count[status]}")
