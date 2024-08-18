#!/usr/bin/env python3
""" Check if a given string is an additive sequence.

    Example
    --------
    >>> is_additive("34711182947")
    True
    >>> is_additive("15051101152")
    True
    >>> is_additive("45023452345")
    False

    Explanation
    ------------
    1. The first number can be added as: "3 4 7 11 18 29 47"
       3 + 4 = 7, 4 + 7 = 11, 7 + 11 = 18, 11 + 18 = 29, and 18 + 29 = 47
    2. The second number can be added as: "1 50 51 101 152"
       1 + 50 = 51, 50 + 51 = 101, and 51 + 101 = 152
    3. The third number can not be partitioned or added in any way
"""


def is_additive(s: str) -> bool:
    """ Check if a string is an additive sequence
    """
    for i in range(1, len(s)):
        fn = s[0:i]  # first no.

        for j in range(i + 1, len(s)):
            sn = s[i:j]  # second no.
            res = str(int(fn) + int(sn))
            # slice out result candidate number from string remainder
            candidate = s[j:j+len(res)]

            if res == candidate:  # current substring is an additive sequence
                whatsnext = s[i:]  # From sn to the end of the string
                if (len(fn) + len(sn) + len(res)) == len(s):  # end of string
                    return True
                if is_additive(whatsnext):  # perform validation on the remaining string
                    return True

    return False  # No additive sequence was found

print(is_additive("34711182947"))
print(is_additive("15051101152"))
print(is_additive("45023452345"))
print(is_additive("4555055105150"))

# From ChatGpt: All Wrong! False
# print(is_additive("01112233555813132134342155"))
# print(is_additive("0112358132134"))
# print(is_additive("0123581313213455"))

# Fibonacci sequence concatenated
print(is_additive("0112358132134558914423337761098715972584418167651094617711286574636875025121393196418317811514229"))
