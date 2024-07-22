# Log Parsing
## Description
For this project, I applied my knowledge of Python programming, focusing on parsing and processing data streams in real time. This project involves reading from standard input (stdin), handling data in specific format, and performing calculations based on the input data.
Here's a list of concepts I used in implementing this algorithm.
## Concepts
1. File I/O in Python:
Read from `sys.stdin` line by line.
2. Signal Handling in Python:
Handling keyboard interruption `ctrl + c` using signal handling in Python.
3. Data Processing:
- Parsing strings to extract specific data points.
- Aggregating data to compute summaries.
4. Regular Expressions:
Using regular expressions to validate the format of each line.
5. Dictionaries in Python:
Using dictionaries to the count occurences of status codes and accumulate file sizes.
6. Exception Handling:
Handling possible exceptions that may arise during file reading and data processing.

**By utilizing the above concepts, I was able to tackle this project, effectively handling data streams, parsing log entries, and computing metrics based on the processed data.**

## Task
Write a script that reads `stdin` line by line and computes metrics:<br>
- Input format: `<IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>` (If the format is not this one, the line is skipped)
- After every 10 lines and/or a keyboard interruption `ctrl + c`, it prints these statistics from the beginning:
- Total file size: `File size: <total size>` (where `<total size>` is the sum of all previous `<file size>` (see input format above))<br>
    - Number of lines by staus code 