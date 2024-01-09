# 6. печать элементов списка с чётными индексами;


def print_even_idx(i, arr):
    if i >= len(arr):
        return

    print(arr[i])

    print_even_idx(i + 2, arr)
