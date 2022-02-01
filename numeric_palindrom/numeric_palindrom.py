#!/usr/bin/env python

"""
Напишите функцию, которая проверяет, является ли целое положительное число палиндромом.

Можно работать только с числами, конвертировать в строку нельзя :)
"""


def is_palindrom(n: int) -> bool:
    if n <= 0:
        raise ValueError("Number must be a positive integer")

    n1 = 0
    n2 = n
    while n2 > 0:
        digit = n2 % 10
        n2 = n2 // 10
        n1 = n1 * 10
        n1 = n1 + digit

    if n == n1:
        return True
    else:
        return False


n = int(input('введите число - '))
print(is_palindrom(n))
