#!/usr/bin/env python

"""
Напишите *генератор* пар соседних чисел Фибоначчи (в функции вместо `result` будет `yield`):

(1, 1), (1, 2), (2, 3), (3, 5), (5, 8) ...

https://en.wikipedia.org/wiki/Fibonacci_number

С помощью генератора найдите 2 таких числа Фибоначчи,
через которые можно будет вычислить золотое сечение с заданной точностью.

https://en.wikipedia.org/wiki/Golden_ratio#Relationship_to_Fibonacci_sequence
"""

# Golden Ratio
GOLDEN = (1 + 5 ** 0.5) / 2


def fib_pair_gen():
    """
    Generator to produce Fibonacci numbers indefinitely.
    """
    a = 0
    b = 1
    while True:
        a, b = b, a + b
        yield a, b



def fib_phi_calc(precision):
    """
    Returns 2 consecutive Fibonacci numbers to calculate Golden Ratio with a given precision.
    """

    for i in fib_pair_gen():
        z = abs((i[1] / i[0]) - GOLDEN)
        if not z > precision:
            func = i
            break
    return func


