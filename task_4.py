# 4. проверка, является ли строка палиндромом;


def is_palindrome(i, string):
    if i >= len(string) / 2:
        return True

    if string[i] != string[len(string) - i - 1]:
        return False

    return is_palindrome(i + 1, string)
