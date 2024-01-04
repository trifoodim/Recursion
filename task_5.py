# 5. печать только чётных значений из списка;


# def print_even(num, lim):
#     # Ensure we start at the first even number desired.
#
#     if num % 2 == 1:
#         print_even(num + 1, lim)
#         return
#
#     # If current number is within limits, print and recurse to next.
#
#     if num <= lim:
#         print(num)
#         print_even(num + 2, lim)


def print_even(ls):
    if not ls:
        return

    else:
        if ls[0] % 2 == 0:
            print(ls[0])

        print_even(ls[1:])


print(print_even([1, 3]))