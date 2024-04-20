'''Eternas game'''

import random

def winning_combination(board: list[list]) -> bool:
    """
    (list) -> bool

    Checks for winning combinations on the board.
    Returns a bool value of True and all winning positions
    if there is winning combination or False if not.

    >>> winning_combination([['w', 'g', 'g', 'w'], [0, 0, 0, 0], [0, 'g', 'w', 'g'], \
['g', 'w', 'w', 'w'], [0, 0, 0, 'g'], [0, 0, 0, 0], [0, 0, 0, 'w'], [0, 0, 0, 0], \
[0, 0, 'w', 'w'], ['w', 'g', 'w', 'g'], [0, 0, 0, 'w'], [0, 0, 0, 'g'], [0, 0, 'g', 'w'], \
[0, 0, 0, 'w'], [0, 0, 'g', 'g'], [0, 0, 0, 'g']])
    False
    >>> winning_combination([[0, 0, 0, 'w'], [0, 'g', 'g', 'w'], [0, 0, 'w', 'w'], \
[0, 'g', 'w', 'w'], [0, 0, 0, 'g'], [0, 0, 0, 0], [0, 0, 'w', 'g'], [0, 0, 0, 'g'], [0, 0, 0, 0], \
[0, 'w', 'w', 'w'], ['g', 'w', 'w', 'g'], [0, 0, 0, 0], [0, 0, 0, 'g'], [0, 0, 'g', 'g'], \
['g', 'g', 'w', 'w'], [0, 0, 'g', 'w']])
    (True, [[(3, 0), (3, 1), (3, 2), (3, 3)], [(3, 14), (3, 15), (3, 0), (3, 1)], \
[(3, 15), (3, 0), (3, 1), (3, 2)]])
    >>> winning_combination([['w', 'w', 'w', 'w'], [0, 'g', 'g', 'w'], [0, 0, 'w', 'w'], \
[0, 'g', 'w', 'w'], [0, 0, 0, 'g'], [0, 0, 0, 0], [0, 0, 'w', 'g'], [0, 0, 0, 'g'], [0, 0, 0, 0], \
[0, 'w', 'w', 'w'], ['g', 'w', 'w', 'g'], [0, 0, 0, 0], [0, 0, 0, 'g'], [0, 0, 'g', 'g'], \
['g', 'g', 'w', 'w'], [0, 0, 'g', 'w']])
    (True, [[(1, 0), (2, 0), (3, 0), (4, 0)], [(3, 0), (3, 1), (3, 2), (3, 3)], [(3, 14), (\
3, 15), (3, 0), (3, 1)], [(3, 15), (3, 0), (3, 1), (3, 2)]])
    
    """
    winning_positions = []
    for i, j in enumerate(board):
        if j[0] == j[1] == j[2] == j[3] != 0:
            winning_positions.append([(1, i), (2, i), (3, i), (4, i)])
        for k in range(4):
            if j[k] == board[(i + 1) % 16][k] != 0:
                if j[k] == board[(i + 2) % 16][k] == board[(i + 3) % 16][k]:
                    winning_positions.append([(k, i), (k, (i + 1) % 16), (k, (i + 2) % 16), (k, (i + 3) % 16)])
        if j[0] == board[(i + 1) % 16][1] != 0:
            if j[0] == board[(i + 2) % 16][2] == board[(i + 3) % 16][3]:
                winning_positions.append([(0, i), (1, (i + 1) % 16), (2, (i + 2) % 16), (3, (i + 3) % 16)])
        if j[3] == board[(i + 1) % 16][2] != 0:
            if j[3] == board[(i + 2) % 16][1] == board[(i + 3) % 16][0]:
                winning_positions.append([(3, i), (2, (i + 1) % 16), (1, (i + 2) % 16), (0, (i + 3) % 16)])
    if winning_positions:
        return True, winning_positions
    return False


def board_generation() -> list[list]:
    """
    Generates a game board of 16 x 4 size,
    i.e. two dimensional list (array) of 'g's, 'w's and '0's  that is used for the game.
    """
    lst = [([0, 0, 0, 0]) for _ in range(16)]
    const = 3
    amount = random.randrange(3, 35)
    while const < amount:
        row = random.randrange(0, 16)
        if 0 in lst[row]:
            word = 'w' if const%2 else 'g'
            for i in range(1, 5):
                if lst[row][-i] == 0:
                    lst[row][-i] = word
                    const += 1
                    break
            if winning_combination(lst):
                return lst
    return lst






if __name__ == "__main__":
    import doctest
    doctest.testmod()

"""
The winning_combination() function has been optimized by returning all possible winning combinations as a list of tuples.

Note: The optimization of the code has been done by returning all possible winning combinations and generating the board with a more even distribution of 'g's and 'w's. The speed and memory usage of the code have not been measured, but the code should be faster and use less memory than the original code.

In this modified version of the board_generation function, the loop that generates the board will stop as soon as a winning combination is found. This is because the winning_combination function is called after each move, and if it returns True, the function will immediately return the current state of the board. This ensures that the board will not be generated further if there is a winning combination.
"""