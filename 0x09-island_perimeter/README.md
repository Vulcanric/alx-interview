# 0x09. Island Perimeter
**`Algorithm`**  **`Python`**

In this project, I applied my knowledge of Python's list data structure in a grid context, creating an algorithm to navigate, analyze and make decisions based on logical conditions.

## Challenge given:
For the “0. Island Perimeter” project, you will need to apply your knowledge of algorithms, data structures (specifically matrices or 2D lists), and iterative or conditional logic to solve a geometric problem within a grid context. The goal is to calculate the perimeter of a single island in a grid, where the grid is represented by a 2D array of integers.

## Task:
Create a function `def island_perimeter(grid):` that returns the perimeter of the island described in `grid`:
- `grid` is a list of integers:
  - 0 represents water
  - 1 represents land
  - Each cell is a square, with a side length of 1
  - Cells are connected horizontally or vertically (never diagonally).
  - `grid` is rectangular, with its width and height not exceeding 100.
- The grid is completely surrounded by water
- There is only one island (or nothing).
- The island doesn't have "lakes" (water inside that isn't connected to the water surrounding the island).

```py
guillaume@ubuntu:~/0x09$ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))

guillaume@ubuntu:~/0x09$ 
guillaume@ubuntu:~/0x09$ ./0-main.py
12
guillaume@ubuntu:~/0x09$
```
## Solution:

```py
def island_perimeter(grid):
    """ Calculates the perimeter of an island described in grid

    * grid is a list of list of integers:
      - 0 represents water
      - 1 represents land
      - Each cell is a square, with a side length of 1
      - Cells are connected horizontally/vertically (not diagonally).
      - grid is rectangular, with its width and height not exceeding 100
    * The grid is completely surrounded by water
    * There is only one island (or nothing).
    * The island doesn’t have “lakes”.
    """
    # Perimeter of island = 2 (l + b), Where l and b are the length
    # and breadth of the island respectively
    length, breadth = (0, 0)

    for row in grid:
        landcells = 0  # Variable to count number of land cells in one row
        for cell in row:
            if cell == 1:  # Land
                if landcells == 0:  # cell is one unit of island's length
                    length += cell
                landcells += 1  # Count the number of land cells in a row
        if landcells > breadth:
            breadth = landcells  # Let breadth be the no. of land cells in row

    # Now calculating the perimeter of island using formula
    return 2 * (length + breadth)

```

### Testing functionality
```py
eric@ubuntu:~/alx-interview/0x09-island_perimeter$ cat 0-main.py
#!/usr/bin/python3
"""
0-main
"""
island_perimeter = __import__('0-island_perimeter').island_perimeter

if __name__ == "__main__":
    grid = [
        [0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0],
        [0, 1, 1, 1, 0, 0],
        [0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid))

    # A bigger island
    grid_1 = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 1, 1, 1, 0, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 1, 1, 1, 1, 1, 1, 1, 1, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 1, 1, 1, 1, 1, 1, 0, 0],
        [0, 0, 0, 1, 1, 1, 1, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    ]
    print(island_perimeter(grid_1))

eric@ubuntu:~/alx-interview/0x09-island_perimeter$
eric@ubuntu:~/alx-interview/0x09-island_perimeter$ ./0-main.py
12
28
eric@ubuntu:~/alx-interview/0x09-island_perimeter$
```
