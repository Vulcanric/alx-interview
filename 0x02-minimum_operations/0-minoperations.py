#!/usr/bin/python3
""" Minimum Operations """


first_prime_numbers = [
    2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43,
    47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103,
    107, 109, 113, 127, 131, 137, 139, 149, 151, 157, 163,
    167, 173, 179, 181, 191, 193, 197, 199, 211, 223, 227,
    229, 233, 239, 241, 251, 257, 263, 269, 271, 277, 281,
    283, 293, 307, 311, 313, 317, 331, 337, 347, 349, 353
]


def minOperations(n):
    """
    Computes the minimum number of operations required to result in @n
    number of characters in a file with just one character, given operations
    as 'Copy All' and 'Paste'.

    Args:
        n (integer): The number of characters

    Returns:
        The minimum number operations as int
    """
    # Number of chars to result in must be greater than or equal to 2,
    # this is because there is already one character in the file
    if (n < 2):
        return 0

    # Look for a prime number which is a factor of n
    for prime in first_prime_numbers:
        if n % prime == 0 and n != prime:
            factor_1, factor_2 = prime, n / prime
            break

        # In case n is a prime no., it's factors are itself and 1
        else:
            factor_1, factor_2 = n, 1

    # Add all prime factors of the number, n to get the minimum operation
    return round(factor_1 + minOperations(factor_2))


if __name__ == "__main__":
    n = 4
    print(f'Minimum number of operations to result in {n} characters: {minOperations(n)}')
    n = 12
    print(f'Minimum number of operations to result in {n} characters: {minOperations(n)}')
    n = 17078
    print(f'Minimum number of operations to result in {n} characters: {minOperations(n)}')
