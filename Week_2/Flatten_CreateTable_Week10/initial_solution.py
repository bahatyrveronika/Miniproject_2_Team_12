import random
def create_table(n: int, m: int)-> list[list[int]]:
    '''
    This function uses recursion to create a 2D list,
    which consists of numbers, with a given number
    of rows and columns. Each number in the first row
    and the first column is equal to 1, any other number is
    calculated like this:
    list[i][j] = list[i - 1][j] + list[i][j - 1].

    >>> create_table(4,6)
    [[1, 1, 1, 1, 1, 1], [1, 2, 3, 4, 5, 6], [1, 3, 6, 10, 15, 21], [1, 4, 10, 20, 35, 56]]
    '''

    if n == 1:
        return [[1 for _ in range(m)]]

    outcome = [1]
    for num in range(1, m):
        outcome.append(outcome[num - 1] + create_table(n - 1, m)[-1][num])

    return create_table(n-1, m) + [outcome]
def flatten(lst: list)-> list:
    '''
    This function uses recursion to transform
    a given multidimensional list into a flat
    list. If input isn't a list, the function
    returns the input back.

    >>> flatten1([1,[2]])
    [1, 2]
    >>> flatten1([1,2,[3,[4,5],6],7])
    [1, 2, 3, 4, 5, 6, 7]
    >>> flatten1(['wow', [2,[[]]], [True]])
    ['wow', 2, True]
    >>> flatten1([])
    []
    >>> flatten1([[]])
    []
    >>> flatten1(3)
    3
    '''
    if not isinstance(lst, list):
        return lst

    result = []

    for line in lst:
        if not isinstance(line, list):
            result.append(line)
        else:
            result += flatten(line)
    return result