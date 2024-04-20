def find_max_1(f:callable, points:list) -> int:
    """ 
    (function, list(number)) -> (number)
    
    Find and return maximal value of function f in points.
    
    >>> find_max_1(lambda x: x ** 2 + x, [1, 2, 3, -1])
    12
    >>> find_max_1(lambda x: x ** 2 - x, [1, 2, 3, -1])
    6
    """
    lst = points[:]
    for index, value in enumerate(lst):
        lst[index] = f(value)
    return max(lst)
def find_max_2(f:callable, points:list) -> list:
    """ 
    (function, list(number)) -> (number)
    
    Find and return list of points where function f has the maximal value.
    
    >>> find_max_2(lambda x: x ** 2 + x, [1, 2, 3, -1])
    [3]
    >>> find_max_2(lambda x: x ** 2 - x, [1, 2, 3, -1])
    [3]
    """
    lts = []
    max_ = find_max_1(f, points)
    for index, value in enumerate(points):
        if f(value) == max_:
            lts.append(points[index])
    return lts
def compute_limit(seq:callable) -> float:
    """
    (function) -> (number)
    
    Compute and return limit of a convergent sequence.
    
    >>> compute_limit(lambda n: (n ** 2 + n) / n ** 2)
    1.0
    >>> compute_limit(lambda n: 2 * (n ** 2 + n) / n ** 2)
    2.0
    """
    lst = []
    i = 0
    while True:
        n = 10 ** i
        lst.append(seq(n))
        if i != 0 and abs(lst[i] - lst[i - 1]) < 0.001:
            return round(lst[i], 2)
        i += 1
def compute_derivative(f:callable, x_0:float) -> float:
    """
    (function, number) -> (number)
    
    Compute and return derivative of function f in the point x_0.
    
    >>> compute_derivative(lambda x: x ** 2 + x, 2)
    5.0
    >>> compute_derivative(lambda x: x ** 2 - x, 2)
    3.0
    """
    aprox = []
    i = 0
    while True:
        dx =  10 ** -i
        x = x_0 + dx
        df = f(x)
        x = x_0
        df -= f(x)
        der = df / dx
        aprox.append(der)
        if i != 0 and abs(aprox[i] - aprox[i - 1]) < 0.001:
            return((round(aprox[i],2)))
        i += 1
def get_tangent(f:callable, x_0:float) -> str:
    """
    (function, number) -> (str)
    
    Compute and return tangent line to function f in the point x_0.
    
    >>> get_tangent(lambda x: x ** 2 + x, 2)
    '5.0 * x - 4.0'
    >>> get_tangent(lambda x: - x ** 2 + x, 2)
    '- 3.0 * x + 4.0'
    """
    k = compute_derivative(f, x_0)
    b = -k * x_0 + f(x_0)
    strin = f"{abs(k):.1f} * x + {abs(b):.1f}"
    if b < 0:
        strin = strin.replace("+", "-")
    if k < 0:
        strin = "- " + strin
    return strin
def get_root(f:callable, a:float, b:float) -> float:
    """
    (function, number, number) -> (number)
    
    Compute and return root of the function f in the interval (a, b).
    
    >>> get_root(lambda x: x + 1, -2, 1)
    -1.0
    >>> get_root(lambda x: x, -1, 1)
    0.0
    """
    epsilon = 0.0001
    while abs(abs(b) - abs(a)) > epsilon:
        c = (a + b)/2
        if abs(f(c)) < epsilon:
            return round(c, 2)
        if f(c) * f(a) < 0:
            b = c
        else:
            a = c
    return round((a+b)/2, 2)
