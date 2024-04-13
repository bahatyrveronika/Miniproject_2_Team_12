def calc(expression):

    # First, we need to handle negation of numbers and parentheses
    expression = expression.replace("--", "+").replace("+-", "-")
    expression = expression.replace("- ", " -").replace("((", "(").replace("))", ")")
    expression = expression.replace("(((", "(").replace(")))", ")").replace('-(', '- (')


    while "(" in expression:
        # Find the innermost pair of parentheses
        start = expression.index("(")
        end = start + 1
        count = 1
        while count > 0:
            end += 1
            if expression[end] == "(":
                count += 1
            elif expression[end] == ")":
                count -= 1
        # Evaluate the expression inside the parentheses
        subexpression = expression[start+1:end]
        expression = expression[:start] + str(calc(subexpression)) + expression[end+1:]

    # Now we can evaluate the expression from left to right
    expression=expression.replace(' - -', ' + ')
    tokens = expression.split()
    operators = []
    values = []
    i = 0
    while i < len(tokens):
        if tokens[i] == "+" or tokens[i] == "-":
            # If we encounter a unary operator, we need to handle it specially
            if i == 0 or tokens[i-1] in ("+", "-", "*", "/"):
                if tokens[i] == "-":
                    values.append(-float(calc(tokens[i+1])))
                    i += 2
                else:
                    values.append(float(calc(tokens[i+1])))
                    i += 2
            else:
                operators.append(tokens[i])
                i += 1
        elif tokens[i] == "*" or tokens[i] == "/":
            operators.append(tokens[i])
            i += 1
        else:
            if '/' in tokens[i]:
                values.append(float(int(tokens[i].split('/')[0])/int(tokens[i].split('/')[1])))
                i += 1
            else:
                tokens[i]=tokens[i].replace('--', '-')
                if tokens[i][-1]=='-':
                    tokens[i]=tokens[i][:-1]
                values.append(float(tokens[i]))
                i += 1

    # Now we can evaluate the operators from left to right
    while operators:
        op = operators.pop(0)
        if op == "+":
            values[1] += values[0]
        elif op == "-":
            values[1] -= values[0]
        elif op == "*":
            values[1] *= values[0]
        elif op == "/":
            values[1] /= values[0]
        values.pop(0)
    if int(values[0])==float(values[0]):
        return int(values[0])
    return values[0]
