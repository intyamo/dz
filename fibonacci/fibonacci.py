#!/usr/bin/env python

"""
Напишите функцию, которая выводят n-ое число Фибоначчи.
Разрешается использовать временные переменные, циклы и условные операторы.

https://en.wikipedia.org/wiki/Fibonacci_number
"""


def fibonacci(n: int) -> int:
    if n < 2:
        return n
    else:
        i = 2
        fibo = [0, 1, 1]
        while i <= n:
            fibo[2] = fibo[0] + fibo[1]
            fibo[0] = fibo[1]
            fibo[1] = fibo[2]
            i += 1
        return fibo[1]

