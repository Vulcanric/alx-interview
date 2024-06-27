#!/usr/bin/python3
""" This module defines a function that returns a list of lists of integers
    representing the Pascal's Triangle of `n`
"""


def pascal_triangle(n):
    """
    Returns a 2D list representing the n's Pascal Triangle
    `param n`(Integer): The number to represent Pascal's Triangle in
    Returns:
        2D list with each list representing a row of the triangle
    """
    if (n < 1):
        return []

    triangle = []

    first_row_line = [1]  # Defaulting to the first row
    triangle.append(first_row_line)
    row = 1

    while row < n:  # 2
        row_line = []

        for col in range(row + 1):  # The nth row has n number of elements
            if (col - 1) < 0:
                elem_1 = 0
            else:
                elem_1 = triangle[row - 1][col - 1]

            if col >= len(triangle[row - 1]):
                elem_2 = 0
            else:
                elem_2 = triangle[row - 1][col]

            row_line.append(elem_1 + elem_2)  # Sum of the two element above it
        triangle.append(row_line)
        row += 1  # Go to the next row

    return triangle
