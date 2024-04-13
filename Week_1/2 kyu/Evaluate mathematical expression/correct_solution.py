import re

def calc(expression):

    operations = {'+': (1, lambda x, y: x + y),
                  '-': (1, lambda x, y: x - y),
                  '*': (2, lambda x, y: x * y),
                  '/': (2, lambda x, y: x / y)}
    stack = []
    output = []
    tokens = re.findall(r"[-+/*()]|\d+", expression)

    for i, token in enumerate(tokens):

        if token in operations:

            if token == '-' and (i == 0 or tokens[i-1] in operations or tokens[i-1] == '('):
                output.append(-1.0)
                stack.append('*')

            else:

                while stack and stack[-1] != "(" and operations[token][0] <= operations[stack[-1]][0]:

                    op = stack.pop()
                    arg2 = output.pop()
                    arg1 = output.pop()
                    output.append(operations[op][1](arg1, arg2))

                stack.append(token)

        elif token == "(":
            stack.append(token)

        elif token == ")":

            while stack and stack[-1] != "(":

                op = stack.pop()
                arg2 = output.pop()
                arg1 = output.pop()
                output.append(operations[op][1](arg1, arg2))

            stack.pop()

        else:

            output.append(float(token))

    while stack:

        op = stack.pop()
        arg2 = output.pop()
        arg1 = output.pop()
        output.append(operations[op][1](arg1, arg2))

    return output[0]
