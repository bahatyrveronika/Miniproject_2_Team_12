"""
This module contains the calculate_expression function,
which allows you to calculate the result of a simple
string statement that adheres to this template:
"Скільки буде <number> <operator> <number> ... ?"
"""
import operator

ALLOWED_CHARS = {
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "+", "-", "*", "/",
    "а", "б", "в", "г", "д", "е", "є", "ж", "з", "и", "й", "к", "л", "м",
    "н", "о", "п", "р", "с", "т", "у", "ф", "х", "ц", "ч", "ш", "щ", "ь",
    "ю","я", "просто", "і", "С", " "
}

OPERATORS = {
    "додати": "+",
    "плюс": "+",
    "відняти": "-",
    "мінус": "-",
    "помножитина": "*",
    "поділитина": "/"
}

OPERATOR_FUNCTIONS = {
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv
}


def calculate_expression(expression: str) -> int:
    """
    Calculates the result of a simple mathematical expression.

    The function accepts a string that represents a simple mathematical expression
    and returns its result. The expression can only contain addition, subtraction,
    multiplication, and division. The function doesn't take into account the priority
    of operations. If the argument isn't a string, or if the expression isn't a
    correct statement, the function returns 'Неправильний вираз!'.

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
    """
    if not (isinstance(expression, str) and expression[-1] == "?"\
             and expression[:12] == "Скільки буде"):
        return "Неправильний вираз!"

    expression = expression.replace(" на", "на").replace("?", " ?").replace('Скільки буде ', '')
    for char in expression:
        if char not in ALLOWED_CHARS:
            expression = expression.replace(char, " ")

    words = expression.split()
    if any(not word.lstrip("-").isnumeric() for word in words[::2]):
        return "Неправильний вираз!"

    if any(word not in OPERATORS for word in words[1::2]):
        return "Неправильний вираз!"

    stack = []
    for word in words:

        if not stack:
            stack.append(int(word))

        elif word in OPERATORS:
            stack.append(OPERATORS[word])

        else:
            operation = stack.pop()
            number = stack.pop()

            if operation == "/" and word == "0":
                return "Неправильний вираз!"

            stack.append(int(OPERATOR_FUNCTIONS[operation](number, int(word))))

    if len(stack) != 1:
        return "Неправильний вираз!"

    return stack[0]


if __name__ == "__main__":
    import doctest
    print(doctest.testmod())
