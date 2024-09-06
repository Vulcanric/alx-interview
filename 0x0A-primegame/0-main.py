#!/usr/bin/python3
""" Main file to test code
"""

isWinner = __import__('0-prime_game').isWinner

print("Winner: {}".format(isWinner(5, [2, 5, 1, 100, 200])))
print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
