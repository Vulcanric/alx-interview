#!/usr/bin/python3
""" Implementing The Sieve of Eratosthenes

    - The main code algorithm/main() function: `isWinner(x, nums)`
"""


def sieve_of_eratosthenes(n):
    """ Finds all the prime numbers from 1 up to a given number, n

    Arguments
    _________
        n (integer): The number
        ------------
    Returns
    _______
        A list of all the prime numbers up to n
    """
    # Store all numbr from 2 to n in a list, concluding that they're all primes
    candidates = [True for i in range(n + 1)]
    primes = []

    # Checking all numbers whose square isn't greater than n
    p = 2  # Starting from 2, because 2 is the first prime number
    while p * p <= n:
        # If the number at index p is marked as prime
        if candidates[p] is True:
            # Mark all multiples of p starting from its square as NOT Primes
            for i in range(p * p, n + 1, p):
                candidates[i] = False

        # Else: continue to the next number
        p += 1

    # Store all the prime numbers in a list and return
    for i in range(1, len(candidates)):
        if candidates[i] is True:
            primes.append(i)

    return primes


whose_turn = None


def nextTurn(player):
    """ Updates who is playing next
    """
    global whose_turn
    whose_turn = player


def isWinner(x, nums):
    """ Prime Game

    Description:
    ------------
    Maria and Ben are playing a game. Given a set of consecutive integers
    starting from 1 up to and including n, they take turns choosing a prime
    number from the set and removing that number and its multiples from the
    set. The player that cannot make a move loses the game.

    They play x rounds of the game, where n may be different for each round.
             ---                         ---
    Assuming Maria always goes first and both players play optimally, it
    determines who the winner of each game is.

    Example:
    --------
    x = 3, nums = [4, 5, 1]
    First round: 4

    Maria picks 2 and removes 2, 4, leaving 1, 3
    Ben picks 3 and removes 3, leaving 1
    Ben wins because there are no prime numbers left for Maria to choose

    Second round: 5

    Maria picks 2 and removes 2, 4, leaving 1, 3, 5
    Ben picks 3 and removes 3, leaving 1, 5
    Maria picks 5 and removes 5, leaving 1
    Maria wins because there are no prime numbers left for Ben to choose

    Third round: 1

    Ben wins because there are no prime numbers for Maria to choose

    Result: Ben has the most wins
    """
    rounds_won = {"Maria": 0, "Ben": 0}

    # For each round
    for i in range(x):

        global whose_turn
        whose_turn = "Maria"  # Maria always goes first

        # Remove all composite numbers from 1 up to n (n = nums[i]) and
        # return a list of only the prime numbers within that range
        # Each player can pick a prime number from that list and forget
        # about removing multiples of that number (composites) from the list
        primes_up_to_n = sieve_of_eratosthenes(nums[i])  # [1, 2, 3, 5, ...]

        primes_len, round_winner = len(primes_up_to_n), "Ben"

        if len(primes_up_to_n) >= 1:
            # Prime picking takes place
            while primes_up_to_n[primes_len - 1] != 1:
                out = primes_up_to_n.pop()  # <whose_turn> takes turn in pickng
                primes_len = len(primes_up_to_n)
                round_winner = whose_turn
                nextTurn("Ben") if whose_turn == "Maria" else nextTurn("Maria")

        rounds_won[round_winner] += 1

    # Get the player with the most wins
    scores = list(rounds_won.values())
    max_score, min_score = max(scores), min(scores)
    winner_index = scores.index(max_score)

    if max_score == min_score:  # No one won
        winner = None
    else:
        winner = list(rounds_won.keys())[winner_index]
    return winner
