#!/usr/bin/env python

"""
Напишите функцию, которая проверяет, является ли целое положительное число палиндромом.

Можно работать только с числами, конвертировать в строку нельзя :)
"""


def is_palindrom(n: int) -> bool:
    v = 0
    m = n
    if n <= 0:
        raise ValueError("Number must be a positive integer")
    while m > 0:
        a = m % 10
        v = (v * 10) + a
        m = m // 10
    if v == n:
        return True
    else:
        return False
