# 2. вычисление суммы цифр числа;

def sum_digits_in_number(number):
    if number < 10:
        return number
    return sum_digits_in_number(number // 10) + number % 10
