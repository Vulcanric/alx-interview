#!/usr/bin/python3
""" Defines a function that calculates an island perimeter
"""


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
