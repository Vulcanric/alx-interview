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

    triangle = [[1]]  # First row

    for i in range(1, n):  # Start from second row
        row = []
        for j in range(i + 1):  # nth row has n amount of elements
            elem_1 = 0 if (j - 1) < 0 else triangle[i - 1][j - 1]
            elem_2 = 0 if j >= len(triangle[i - 1]) else triangle[i - 1][j]
            row.append(elem_1 + elem_2)  # Sum of the 2 elements above it
        triangle.append(row)
    return triangle
