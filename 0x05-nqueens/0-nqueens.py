#!/usr/bin/python3
""" The N queens puzzle is the challenge of placing N non-attacking queens
on an NxN chessboard.
 This module defines a program that solves the N queens problem.

    Usage:
    ------
    nqueens N

    Edge Cases:
    -----------
    - If N is not an integer, prints "N must be a number" and exits with stat 1
    - If N is less than 4, prints "N must be at least 4" and exits with stat 1

    Output:
    -------
    Prints to standard output lists containing coordinates referring to
    positions on the chessboard where N non-attacking queens can be placed.

    Prints out all possible solutions.

    Example:
    --------
    $ ./0-nqueens.py
    Usage: nqueens N
    $ ./0-nqueens.py 4
    [[0, 1], [1, 3], [2, 0], [3, 2]]
    [[0, 2], [1, 0], [2, 3], [3, 1]]
"""
import sys


def error(msg):
    """ Prints error message and exits """
    print(msg)
    exit(1)


def print_board(board, size):
    """ Pretty-prints a chessboard """
    print('\t+', '-----+' * size, sep='')
    for x in range(size):
        print('\t|', end='')
        for y in range(size):
            print(f'  {board[x][y]!r}  |', end='')
            if y == size - 1:
                print('\n\t+', '-----+' * size, sep='')


def fill_queen_path(queen, board, size, x, y):
    """ Fill queen's path (squares) on the board with her no.
    """
    # Fill queen's path (squares) on the board with her no.
    for i in range(size):
        board[x][i] = queen  # Fill vertical squares (|)
        board[i][y] = queen  # Fill horizontal squares (---)

        # Fill diagonal squares (/) x++ y-- | x-- y++
        if (x + i <= size - 1) and (y - i >= 0):  # Avoid IndexError
            board[x + i][y - i] = queen
        if (x - i >= 0) and (y + i <= size - 1):  # Avoid IndexError
            board[x - i][y + i] = queen

        # Fill diagonal (2) squares (\) x++ y++ | x-- y--
        if (x + i <= size - 1) and (y + i <= size - 1):
            board[x + i][y + i] = queen
        if (x - i >= 0) and (y - i >= 0):
            board[x - i][y - i] = queen


def main(board, size, x, y, no_of_successful_queens):
    """ Solves the N queens problem and prints all possible solutions to it

        Algorithm:
        ----------
        1. Creates a board of size @size and fill it with 0s/empty.
        2. Checks if a position I want to place a queen is empty or contained
        with 0.
            If yes:
            -------
                inserts the queen there as her number, storing the position and
                filling her vertical, hrizontal and diagonal paths with her no.
            Else (occupied with another queens no.):
            ----------------------------------------
                go to the next position.
        3. If all queens were inserted successfully:
        ---------------------------------------------
            then it prints out the all the queens position as a list of
            coordinates and recursively call itself for the next solution
            passing the board, the size of the board and an x-y coordinate as
            position to place the first queen for initialization.
        4. Else if there were not all inserted successfully:
        ----------------------------------------------------
            return! (End)
    """

    queens_position = []
    _x, _y = x, y
    # complete = False

    for queen in range(1, size + 1):  # There should be @size number of queens
        status = False  # decides if the current queen has found her position

        if all(idx in range(size) for idx in (x, y)) and queen == 1:  # Init
            board[x][y] = queen
            fill_queen_path(queen, board, size, x, y)
            queens_position.append([x, y])  # Store her position
            continue

        for x in range(size):
            for y in range(size):
                if board[x][y] == 0:  # Empty, insert queen
                    board[x][y] = queen
                    queens_position.append([x, y])  # Store her position
                    status = True

                    fill_queen_path(queen, board, size, x, y)
                    break
            if status:
                break

        # Current solution is complete
        if len(queens_position) == size:
            print(queens_position)
            board = [[0 for i in range(size)] for j in range(size)]
            main(board, size, _x, _y + 1, len(queens_position))

    if no_of_successful_queens != size:
        # Try every possible solution
        randint = __import__('random').randint
        a, b = randint(0, size), randint(0, size)
        board = [[0 for i in range(size)] for j in range(size)]
        main(board, size, a, b, no_of_successful_queens)
    else:
        exit(0)


if __name__ == "__main__":

    if len(sys.argv) != 2:
        error("Usage: nqueens N")
    elif not sys.argv[1].isdigit():
        error("N must be a number")
    elif int(sys.argv[1]) < 4:
        error("N must be at least 4")
    else:
        size = int(sys.argv[1])

    # Create board
    board = [[0 for i in range(size)] for j in range(size)]

    try:
        main(board, size, 0, 1, 0)
    except RecursionError:
        pass
