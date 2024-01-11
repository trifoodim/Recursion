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

    if i == len(numbers):
        return None

    if numbers[i] > max_num:
        second_max_num = max_num
        max_num = numbers[i]

    if numbers[i] < max_num:
        second_max_num = numbers[i]

    idx = i + 1

    return find_second_max_num_recursive(idx, numbers, max_num, second_max_num)


def find_second_max_num_recursive(idx, numbers, max_num, second_max_num):
    if idx >= len(numbers):
        return second_max_num

    current_num = numbers[idx]
    if current_num > max_num:
        second_max_num = max_num
        max_num = current_num

    elif current_num < max_num and second_max_num is None:
        second_max_num = current_num

    elif current_num > second_max_num:
        second_max_num = current_num

    return find_second_max_num_recursive(idx + 1, numbers, max_num, second_max_num)


print(find_second_max_num([2, 4, 5, 9, 2, 8]))
