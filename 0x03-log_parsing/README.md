# Log Parsing
## Description:
In this project, I applied my knowledge of Python programming, focusing on parsing and processing data streams in real time. This project involves reading from standard input (stdin), handling data in specific format, and performing calculations based on the input data.
Here's a list of concepts I used in implementing this algorithm.
## Concepts Used:
1. File I/O in Python:<br>
    - Read from `sys.stdin` line by line.
2. Signal Handling in Python:<br>
    - Handling keyboard interruption `ctrl + c` using signal handling in Python.
3. Data Processing:<br>
    - Parsing strings to extract specific data points.
    - Aggregating data to compute summaries.
4. Regular Expressions:<br>
    - Using regular expressions to validate the format of each line.
5. Dictionaries in Python:
    - Using dictionaries to the count occurences of status codes and accumulate file sizes.
6. Exception Handling:
    - Handling possible exceptions that may arise during file reading and data processing.

**By utilizing the above concepts, I was able to tackle this project, effectively handling data streams, parsing log entries, and computing metrics based on the processed data.**

## Task:
Write a script that reads `stdin` line by line and computes metrics:<br>
- Input format: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>` (If the format is not this one, the line is skipped)
- After every 10 lines and/or a keyboard interruption `ctrl + c`, it prints these statistics from the beginning:
    - Total file size: `File size: <total size>` (where `<total size>` is the sum of all previous `<file size>` (see input format above))<br>
    - Number of lines by staus code:
        - possible status code: `200`, `301`, `400`, `401`, `403`, `404`, `405` and `500`
        - Doesn't print anything for the status code, if a status code doesn't appear in the list of possible status code or is not an integer.
        - format: `<status code>: <count>`
        - status codes is printed in ascending order
## My Solution:
<center><b><p style="background-color: magenta;color: black">0-stat.py</p></b></center>

```py
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

            if i % 10 == 0:
                print(f"File size: {total_size}")
                for status in sorted(status_count.keys()):
                    print(f"{status}: {status_count[status]}")

    except KeyboardInterrupt:  # ctrl + c event
        print(f"File size: {total_size}")
        for status in sorted(status_count.keys()):
            print(f"{status}: {status_count[status]}")

```

## Test file:
### `0-generator.py`
This file generates random log values and flush them to standard output for testing purposes. The output of `0-generator.py` is casted to `0-stat.py` as input using the Linux pipe operator `|` in order to view its functionality.
### Command:
`./0-generator | ./0-stat.py`. Below is a view of the output.

```bash
eric@John-Eric:~alx-interview/0x03-log_parsing$ cat 0-generator.py
#!/usr/bin/python3
import random
import sys
from time import sleep
import datetime

for i in range(10000):
    sleep(random.random())
    sys.stdout.write("{:d}.{:d}.{:d}.{:d} - [{}] \"GET /projects/260 HTTP/1.1\" {} {}\n".format(
        random.randint(1, 255), random.randint(1, 255), random.randint(1, 255), random.randint(1, 255),
        datetime.datetime.now(),
        random.choice([200, 301, 400, 401, 403, 404, 405, 500]),
        random.randint(1, 1024)
    ))
    sys.stdout.flush()

eric@John-Eric:~alx-interview/0x03-log_parsing$ ./0-generator.py | ./0-stats.py
File size: 11320
200: 3
301: 2
400: 1
401: 2
403: 3
404: 4
405: 2
500: 3
File size: 16305
200: 3
301: 3
400: 4
401: 2
403: 5
404: 5
405: 4
500: 4
^CFile size: 17146
200: 4
301: 3
400: 4
401: 2
403: 6
404: 6
405: 4
500: 4
Traceback (most recent call last):
  File "./0-stats.py", line 15, in <module>
Traceback (most recent call last):
  File "./0-generator.py", line 8, in <module>
    for line in sys.stdin:
KeyboardInterrupt
    sleep(random.random())
KeyboardInterrupt
```
