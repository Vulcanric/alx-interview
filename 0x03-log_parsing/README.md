# Log Parsing
## Description
For this project, I applied my knowledge of Python programming, focusing on parsing and processing data streams in real time. This project involves reading from standard input (stdin), handling data in specific format, and performing calculations based on the input data.
Here's a list of concepts I used in implementing this algorithm.
## Concepts
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

## Task
Write a script that reads `stdin` line by line and computes metrics:<br>
- Input format: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>` (If the format is not this one, the line is skipped)
- After every 10 lines and/or a keyboard interruption `ctrl + c`, it prints these statistics from the beginning:
    - Total file size: `File size: <total size>` (where `<total size>` is the sum of all previous `<file size>` (see input format above))<br>
    - Number of lines by staus code:
        - possible status code: `200`, `301`, `400`, `401`, `403`, `404`, `405` and `500`
        - Doesn't print anything for the status code, if a status code doesn't appear in the list of possible status code or is not an integer.
        - format: `<status code>: <count>`
        - status codes is printed in ascending order
## Solution
<center><p style="background-color: magenta;color: black"><b>0-stat.py</b></p></center>

```py
if __name__ == "__main__":
    main()
```

## Test file - `0-generator.py`
This file generates random log values and flush them to standard output for testing purposes. The `0-stats.py` script is run against it using Unix piping symbol to test its functionality.

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
