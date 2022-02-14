#!/usr/bin/env python

"""
Напишите функцию, которая проверяет, является ли целое положительное число палиндромом.

Можно работать только с числами, конвертировать в строку нельзя :)
"""


def is_palindrom(n: int) -> bool:
    if n <= 0:
        raise ValueError("Number must be a positive integer")
    num = n
    contra = 0
    while n > 0:
        rem = n % 10
        contra = contra * 10 + rem
        n = n // 10
    if contra == num:
        return True
    else:
        return False
