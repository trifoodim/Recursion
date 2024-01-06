# 4. проверка, является ли строка палиндромом;


def is_palindrome(string):

    if string[0] == string[-1]:
        return is_palindrome(string[1:-1])
    else:
        return False
