def fib(n):
    memo = {0: 0, 1: 1}

    def fib_iter(m):
        if m not in memo:
            a, b = 0, 1
            for _ in range(m - 1):
                a, b = b, a + b
            memo[m] = b
        return memo[m]

    if n < 0:
        if n == -1:
            return 1
        else:
            if -n%2 ==0:
                return -fib_iter(-n)
            else:
                return fib_iter(-n)
    else:
        return fib_iter(n)