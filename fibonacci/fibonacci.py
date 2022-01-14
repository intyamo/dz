#!/usr/bin/env python

"""
Напишите функцию, которая выводят n-ое число Фибоначчи.
Разрешается использовать временные переменные, циклы и условные операторы.

https://en.wikipedia.org/wiki/Fibonacci_number
"""


def fibonacci(n: int) -> int:
    fib = [0, 1]+[0]*(n-1)
    for i in range(2, n+1):
        fib[i] = fib[i-1] + fib[i - 2]
    return fib[n]


