# 5. печать только чётных значений из списка;


def print_even(i, arr):
    if i >= len(arr):
        return

    if arr[i] % 2 == 0:
        print(arr[i])

    print_even(i + 1, arr)
