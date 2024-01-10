# 7. нахождение второго максимального числа в списке (с учётом, что максимальных может быть несколько, если они равны).
# Второе макс. -- это когда отсортировали список и берём второй элемент (отсчитывая с 1), если 5,4,3,2,5 например, то второе макс. должно получиться 5.
# Равенство или неравенство элементов значения не имеет, т.к. оно никак в условии не оговаривается.
# После того как вы отсортировали массив [2,5,4,3,5] по убыванию [5,5,4,3,2] берёте второй элемент 5, это и будет второе макс. Если массив [2,3,5,4], то второе макс будет 4, и т. д.


def find_second_max_num(numbers):
    if not numbers:
        return None

    max_num = numbers[0]
    second_max_num = None
    i = 1
    while i < len(numbers) and numbers[i] == max_num:
        i += 1

    if i == len(numbers):
        return None

    if numbers[i] > max_num:
        second_max_num = max_num
        max_num = numbers[i]

    if numbers[i] < max_num:
        second_max_num = numbers[i]

    return find_second_max_num_recursive(numbers[i + 1:], max_num, second_max_num)


def find_second_max_num_recursive(numbers, max_num, second_max_num):
    if not numbers:
        return second_max_num

    current_num = numbers[0]
    if current_num > max_num:
        second_max_num = max_num
        max_num = current_num

    elif current_num < max_num and second_max_num is None:
        second_max_num = current_num

    elif current_num > second_max_num:
        second_max_num = current_num

    return find_second_max_num_recursive(numbers[1:], max_num, second_max_num)
