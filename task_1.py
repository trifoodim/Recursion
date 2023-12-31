# 1. возведение числа N в степень M;

def power_fnc(N, M):
    """Recursive function of power N(number) into M(power).

    Keyword arguments:
    N -- number
    M -- power

    """
    if M == 0:
        return 1
    t = power_fnc(N * N, M // 2)
    if M % 2:
        t *= N
    return t
