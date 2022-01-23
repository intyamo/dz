#!/usr/bin/env python

"""
Напишите функцию, которая выводят n-ое число Фибоначчи.
Разрешается использовать временные переменные, циклы и условные операторы.

https://en.wikipedia.org/wiki/Fibonacci_number
"""


def fibonacci(n: int) -> int:
    if n < 0:
        raise ValueError("Index must be >= 0")
    a = 0
    b = 1
    if n == 0:
        b = 0
    else:
        for i in range(n - 1):
            a, b = b, a + b
    return b

# n = int(input())
# itog = fibonacci(n)
# print(itog)
