# 0x0A. Prime Game
**`Algorithm`**   **`Python`**
<br>

## Description
In this project, I leveraged my understanding of *prime numbers*, *game theory*, and *algorithm optimization* to solve a competitive game scenario.
The challenge involves determining the winner of a game based on strategic removal of prime numbers and their multiples from a set of consecutive integers.

## Task
**`0. Prime Game`**

Maria and Ben are playing a game. Given a set of consecutive integers starting from `1` up to and including `n`, they take turns choosing a prime number from the set and removing that number and its multiples from the set. The player that cannot make a move loses the game.

They play `x` rounds of the game, where `n` may be different for each round. Assuming *Maria* always goes first and both players play optimally, determine who the winner of each game is.
- Prototype: `def isWinner(x, nums)`
- where `x` is the number of rounds and `nums` is an array of `n`
- Return: name of the player that won the most rounds
- If the winner cannot be determined, return None
- You can assume `n` and x` will not be larger than 10000
- You must not import any packages in this task

Example:
	- `x` = `3`, `nums` = `[4, 5, 1]`

First round: `4`
	- Maria picks 2 and removes 2, 4, leaving 1, 3
	- Ben picks 3 and removes 3, leaving 1
	- Ben wins because there are no prime numbers left for Maria to choose

Second round: `5`
	- Maria picks 2 and removes 2, 4, leaving 1, 3, 5
	- Ben picks 3 and removes 3, leaving 1, 5
	- Maria picks 5 and removes 5, leaving 1
	- Maria wins because there are no prime numbers left for Ben to choose

Third round: `1`
	- Ben wins because there are no prime numbers for Maria to choose

**Therefore Ben has the most wins (Winner)**


## My Solution: [`0-prime_game.py`](https://github.com/Vulcanric/alx-interview/blob/main/0x0A-primegame/0-prime_game.py)
Having read the examples above you can just skip doc string and comments explaining what the algorithm is doing.

```py
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


def updateTurn(player):
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
        # Prime picking takes place
        while primes_up_to_n[primes_len - 1] != 1:
            out = primes_up_to_n.pop()  # <whose_turn> takes turn in picking
            primes_len = len(primes_up_to_n)
            round_winner = whose_turn
            updateTurn("Ben") if whose_turn == "Maria" else updateTurn("Maria")

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

```

## Test: [`0-main.py`](https://github.com/Vulcanric/alx-interview/blob/main/0x0A-primegame/0-main.py)

```bash
eric@ubuntu:~/0x0A-primegame$ cat 0-main.py
#!/usr/bin/python3
""" Main file to test code
"""

isWinner = __import__('0-prime_game').isWinner

print("Winner: {}".format(isWinner(5, [2, 5, 1, 100, 200])))
print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
print("Winner: {}".format(isWinner(2, [2, 4])))

eric@ubuntu:~/0x0A-primegame$
```
```bash
eric@ubuntu:~/0x0A-primegame$ ./0-main.py
Winner: Maria
Winner: Ben
Winner: None
eric@ubuntu:~/0x0A-primegame$
```

## Concepts Utilized:
1. **Prime Numbers:**
The ability of understanding what prime numbers are, and drafting efficient algorithms for identifying prime numbers within a range.
2. **Sieve of Eratosthenes:**
An efficient algorithm for finding all prime numbers up to any given limit, which can be particularly useful for this task.
3. **Game Theory:**
- Understanding basic principles of competitive games where players take turns and the concept of optimal play.
- Understanding win conditions and strategies that lead to a win or loss.
4. **Dynamic Programming/Memoization:**
- Using previous results to make future calculations faster, potentially necessary for optimizing the solution for multiple rounds of the game.
5. **Python Programming:**
- Loops and conditional statements for implementing game logic and algorithms.
- Arrays and lists for storing the integers and tracking removed numbers.

By making use of these concepts, I was well equipped to approach the problem with solid understanding of both the mathematical and programming challenges involved.
The key to this project success was the ability to apply efficient algorithms to manage the game's state and making optimal decisions based on the game's rules.
