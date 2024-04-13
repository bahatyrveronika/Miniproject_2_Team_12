# Варіант 1
def last_digit_of_power(numbers):
    result = 1
    for num in numbers:
        result = (result ** num) % 10
    return result

def last_digit(numbers):
    if numbers == [0,0] or numbers ==[]:
        return 1

    result = numbers[0]%10
    for num in numbers[1:]:
        if result == 0 or num == 0:
            return result

        if result == 1 or num == 1:
            continue

        if result == 5 or result == 6:
            result = (result * num) % 10
            continue

        if num == 2 or num == 3 or num == 7 or num == 8:
            result = (result * num) % 10

        if num == 4 or num == 9:
            if result == 6:
                result = 4
            else:
                result = 6

    if result == 2 or result == 4 or result == 6 or result == 8:
        return 6
    elif result == 3 or result == 9:
        return 9
    else:
        return last_digit_of_power([result] + numbers[1:])
#Варіант2
def last_digit(numbers):
    if not numbers:
        return 1

    last_digit = 1
    for number in numbers:
        if number % 2 == 0:
            last_digit = (last_digit * last_digit) % 10
        else:
            last_digit = (last_digit * (number % 10)) % 10

    return last_digit