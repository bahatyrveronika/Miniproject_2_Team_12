def last_digit(lst):
    if lst == []:
        return 1
    result = 1
    for num in lst[::-1]:
        result = num ** (result if result < 4 else result % 4 + 4)
    return result % 10