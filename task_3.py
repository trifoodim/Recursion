# 3. расчёт длины списка, для которого разрешена только операция удаления первого элемента pop(0) (и получение длины конечно);

def recursion_len_counter(ls):
    length = 0
    if not ls:
        return length

    return length + 1 + recursion_len_counter(ls[1:])
