# 5. печать только чётных значений из списка;


def print_even(ls):
    if not ls:
        return

    if ls[0] % 2 == 0:
        print(ls[0])

    print_even(ls[1:])
