def find_max_1(f: callable, points: list) -> int:
    """
    (function, list(number)) -> (number)
    
    Find and return maximal value of function f in points.
    
    >>> find_max_1(lambda x: x ** 2 + x, [1, 2, 3, -1])
    12
    >>> find_max_1(lambda x: x ** 2 - x, [1, 2, 3, -1])
    6
    """
    max_value = -float('inf')
    for point in points:
        value = f(point)
        if value > max_value:
            max_value = value
    return max_value
def find_max_2(f: callable, points: list) -> list:
    """
    (function, list(number)) -> (number)
    
    Find and return list of points where function f has the maximal value.
    
    >>> find_max_2(lambda x: x ** 2 + x, [1, 2, 3, -1])
    [3]
    >>> find_max_2(lambda x: x ** 2 - x, [1, 2, 3, -1])
    [3]
    """
    max_val = max(f(point) for point in points)
    return [point for point in points if f(point) == max_val]
def compute_limit(seq: callable, epsilon: float = 0.001) -> float:
    """
    (function) -> (number)
    
    Compute and return limit of a convergent sequence.
    
    >>> compute_limit(lambda n: (n ** 2 + n) / n ** 2)
    1.0
    >>> compute_limit(lambda n: 2 * (n ** 2 + n) / n ** 2)
    2.0
    """
    prev_val = seq(1)
    i = 1
    while True:
        curr_val = seq(10 ** i)
        if abs(curr_val - prev_val) < epsilon:
            return round(curr_val, 2)
        prev_val = curr_val
        i += 1
def compute_derivative(f: callable, x_0: float, tol=0.001) -> float:
    """
    (callable, number) -> number
    
    Compute and return derivative of function f in the point x_0.
    
    The function uses the definition of a derivative:
    f'(x) = (f(x + h) - f(x)) / h
    
    where h is a small number. The function keeps decreasing h until
    the difference between the current and the previous estimate of
    the derivative is smaller than a specified tolerance `tol`.
    
    >>> compute_derivative(lambda x: x ** 2 + x, 2)
    5.0
    >>> compute_derivative(lambda x: x ** 2 - x, 2)
    3.0
    """
    h = 1e-1
    prev_derivative = None
    while True:
        derivative = (f(x_0 + h) - f(x_0)) / h
        if prev_derivative and abs(derivative - prev_derivative) < tol:
            return round(derivative, 2)
        prev_derivative = derivative
        h /= 10
def get_tangent(f: callable, x_0: float) -> str: 
    """
    (callable, number) -> str
    
    Compute and return tangent line to function f in the point x_0.
    
    The function computes the derivative of the function f in the point x_0
    using the `compute_derivative` function and uses it to calculate the
    slope `k` of the tangent line. The function then calculates the y-intercept
    `b` of the tangent line using the point-slope form of a linear equation:
    y - y_0 = k * (x - x_0)
    
    The function returns the equation of the tangent line as a string in the
    form of `ax + b`, where `a` is the slope `k` and `b` is the y-intercept.
    
    >>> get_tangent(lambda x: x ** 2 + x, 2)
    '5.0 * x - 4.0'
    >>> get_tangent(lambda x: - x ** 2 + x, 2)
    '-3.0 * x + 4.0'
    """
    k = compute_derivative(f, x_0)
    b = f(x_0) - k * x_0
    return f"{k:.1f} * x {{'+' if k >= 0 else '-'}} {abs(b):.1f}"
def get_root(f: callable, a: float, b: float) -> float:
    """
    Compute and return root of the function f in the interval (a, b).

    :param f: function for which to find the root
    :param a: left endpoint of the interval
    :param b: right endpoint of the interval
    :return: root of the function f in the interval (a, b)

    >>> get_root(lambda x: x + 1, -2, 1)
    -1.0
    >>> get_root(lambda x: x, -1, 1)
    0.0
    """
    epsilon = 1e-5  # set a smaller epsilon value for better precision

    while abs(b - a) > epsilon:
        c = (a + b) / 2
        if abs(f(c)) < epsilon:
            return round(c, 2)  # return the result with 2 decimal places

        if f(c) * f(a) < 0:
            b = c
        else:
            a = c

    return round((a + b) / 2, 2)  # return the final result with 2 decimal places
