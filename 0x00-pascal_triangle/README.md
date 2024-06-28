# 0x00. Pascal's Triangle
**`Algorithm`**  **`Python`**<br>
---
This project contains a Python function that generates Pascal's Triangle up to a given number of rows, `n`. Pascal's Triangle is a triangular array of the binomial coefficients, which has many applications in mathematics and computer science, such as combinatorics, algebra, and probability.

## Function definition
```py
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
```

## Example
```py
def print_triangle(triangle):
    """
    Print the triangle
    """
    for row in triangle:
        print("[{}]".format(",".join([str(x) for x in row])))


if __name__ == "__main__":
    print_triangle(pascal_triangle(5))
```

## Output
```
[1]
[1, 1]
[1, 2, 1]
[1, 3, 3, 1]
[1, 4, 6, 4, 1]
```
