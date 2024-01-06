# 5. печать только чётных значений из списка;


def print_even(ls):

    if ls[0] % 2 == 0:
        print(ls[0])

    ls.pop(0)
    print_even(ls)
