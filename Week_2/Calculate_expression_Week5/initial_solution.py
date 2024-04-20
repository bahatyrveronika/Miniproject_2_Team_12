'''
This module contains the calculate_expression function,
which allows you to calculate the result of a symple
string statement that adheres to this template:
"Скільки буде <number> <operator> <number> ... ?"
'''
def calculate_expression(expression: str)-> int:
    '''
    str -> int
    The function accepts a simple mathematical expression and
    returns its result. It only supports addition, subtraction,
    multiplication and division. Th function also doesn't take
    into account the priority of operations. If the argument
    isn't a string, or if the expression isn't a correct statement,
    the function returns 'Неправильний вираз!'
    >>> calculate_expression(123)
    'Неправильний вираз!'
    >>> calculate_expression('Скільки дерев у Стрийському парку?')
    'Неправильний вираз!'
    >>> calculate_expression('Скільки буде 12 помножити на 3 плюс -6?')
    30
    >>> calculate_expression('Скільки буде 5 помножити на 8 поділити на 2 мінус 5?')
    15
    >>> calculate_expression('Скільки буде 5 поділити на 0?')
    'Неправильний вираз!'
    >>> calculate_expression('Скільки буде 8?')
    8
    >>> calculate_expression('3 плюс 7?')
    'Неправильний вираз!'
    '''
    if not (isinstance(expression, str) and expression[-1] == '?'\
        and expression[:12] == 'Скільки буде'):
        return 'Неправильний вираз!'
    expression = expression.replace(' на','на')
    expression = expression.replace('?',' ?')
    for i in expression:
        if not (i.isalpha() or i.isnumeric() or i in (' ', '-', '?')):
            expression = expression.replace(i,'')
    lst = expression.split()
    words = ['Скільки', 'буде']
    oper = ["додати", "плюс", "відняти", "мінус", "помножитина", "поділитина"]
    for i in enumerate(lst[:-2]):
        ind, exp = i
        if ((exp.strip('-')).isnumeric() and (lst[ind+1].strip('-')).isnumeric()) or \
        (exp in oper and lst[ind+1] in oper):
            return  'Неправильний вираз!'
    result = int(lst[2])
    for i in enumerate(lst[:-2]):
        ind, exp = i
        if (exp.strip('-')).isnumeric() and not lst[ind-1] in oper and ind != 2:
            result += int(exp)
        elif exp in ('додати', 'плюс'):
            result += int(lst[ind+1])
        elif exp in ('відняти', 'мінус'):
            result -= int(lst[ind+1])
        elif exp == 'помножитина':
            result *= int(lst[ind+1])
        elif exp in ('поділитина') and int(lst[ind+1]):
            result //= int(lst[ind+1])
        elif not ((exp.strip('-')).isnumeric() or exp in words):
            return 'Неправильний вираз!'
    return result

if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
