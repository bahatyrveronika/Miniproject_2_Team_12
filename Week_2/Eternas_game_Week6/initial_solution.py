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
    boolean = False
    lst_tupl = []
    for i, j in enumerate(board):
        if j[0] == j[1] == j[2] == j[3] != 0:
            boolean = True
            lst_tupl.append([(1, i), (2, i), (3, i), (4, i)])
        for k in range(4):
            if j[k] == board[(i+1)%16][k] != 0:
                if j[k] == board[(i + 2)%16][k] == board[(i + 3)%16][k]:
                    boolean = True
                    lst_tupl.append([(k, i), (k, (i+1)%16), (k, (i+2)%16), (k, (i+3)%16)])
        if j[0] == board[(i+1)%16][1] != 0:
            if j[0] == board[(i+2)%16][2] == board[(i+3)%16][3]:
                boolean = True
                lst_tupl.append([(0, i), (1, (i+1)%16), (2, (i+2)%16), (3, (i+3)%16)])
        if j[3] == board[(i+1)%16][2] != 0:
            if j[3] == board[(i+2)%16][1] == board[(i+3)%16][0]:
                boolean = True
                lst_tupl.append([(3, i), (2, (i+1)%16), (1, (i+2)%16), (0, (i+3)%16)])
    if not boolean:
        return boolean
    return (boolean, lst_tupl)

def board_generation() -> list[list]:
    """
    Generates a game board of 16 x 4 size,
    i.e. two dimensional list (array) of 'g's, 'w's and '0's  that is used for the game.

    ### 16 x 4 | g - green, w - white, 0 - whitespace

    e.g. [[0, 0, 0, 0], [0, 0, 0, 'w'], [0, 0, 'g', 'g'], [0, 0, 'g', 'g'],
          [0, 'w', 'w', 'w'], [0, 0, 'w', 'g'], [0, 0, 0, 'g'], [0, 0, 'g', 'w'],
          [0, 'g', 'g', 'w'], [0, 0, 0, 0], ['w', 'g', 'w', 'w'], [0, 0, 0, 'g'],
          [0, 0, 0, 'g'], ['w', 'g', 'g', 'w'], [0, 'w', 'w', 'w'], [0, 0, 'g', 'w']]

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
