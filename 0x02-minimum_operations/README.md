# 0x02. Minimum Operations
**`Algorithm`**  **`Python`**
---

## Challenge/Problem:
In a text file, there is a single character `H`. Your text editor can execute only two operations in this file:
1. `Copy All`
2. `Paste`.
Given a number `n`, write an algorithm that calculates the fewest number of operations needed to result in exactly `n` `H` characters in this file.
    - Prototype: `def miniOperations(n)`
    - Returns an integer
    - If `n` is impossible to achieve, return 0

**Example:**
`n = 9`
`H` => `Copy All` => `Paste` => `HH` => `Paste` => `HHH` => `Copy All` => `Paste` => `HHHHHH` => `Paste` => `HHHHHHHHH`
Number of operations: `6`

## My Solution:

