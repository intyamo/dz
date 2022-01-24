#!/usr/bin/env python

"""
Напишите функцию, которая проверяет, является ли целое положительное число палиндромом.

Можно работать только с числами, конвертировать в строку нельзя :)
"""


def is_palindrom(n: int) -> bool:
    reversed_number = 0
    tmp_original = n
    if n <= 0:
        raise ValueError("Number must be a positive integer")
    while tmp_original > 0:
        reversed_number = (reversed_number * 10) + tmp_original % 10
        tmp_original = tmp_original // 10

    if n == reversed_number:
        return True
    else:
        return False
