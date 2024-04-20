import concurrent.futures
from typing import List
import random
def create_table(n: int, m: int) -> List[List[int]]:
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

    # Base case: if n is 1, return a list with m 1s
    if n == 1:
        return [[1] * m]

    # Initialize the table with the first row and column
    table: List[List[int]] = [[1] * m] + [[1] + [0] * (m - 1) for _ in range(n - 1)]

    # Fill in the rest of the table using multithreading
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = []
        for i in range(1, n):
            futures.append(executor.submit(fill_row, table, i, m))

        for future in concurrent.futures.as_completed(futures):
            future.result()

    return table

def fill_row(table: List[List[int]], row_index: int, cols: int) -> None:
    # Fill in the values for the given row in the table
    for col_index in range(1, cols):
        table[row_index][col_index] = table[row_index - 1][col_index] + table[row_index][col_index - 1]

def flatten_recursive(lst: list) -> list:
    """
    Flattens a nested list into a single list.

    Args:
        lst (List): A nested list to be flattened.

    Returns:
        List: The flattened list.
    """
    if not isinstance(lst, list):
        return lst

    result = []
    for line in lst:
        if isinstance(line, list):
            result.extend(flatten_recursive(line))
        else:
            result.append(line)

    return result

def flatten_cycle(lst: list) -> list:
    """
    Flattens a nested list into a single list using a stack.

    Args:
        lst (List): A nested list to be flattened.

    Returns:
        List: The flattened list.
    """
    stack = [lst]
    result = []

    if not isinstance(lst, list):
        return lst

    while stack:
        current = stack.pop()

        if isinstance(current, list):
            for item in current[::-1]:
                stack.append(item)
        else:
            result.append(current)

    return result