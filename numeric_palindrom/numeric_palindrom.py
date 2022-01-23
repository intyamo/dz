#!/usr/bin/env python

"""
Напишите функцию, которая проверяет, является ли целое положительное число палиндромом.

Можно работать только с числами, конвертировать в строку нельзя :)
"""


def is_palindrom(n: int) -> bool:
    if n <= 0:
        raise ValueError("Number must be a positive integer")
    CopyNum = n
    Contra = 0
    while n > 0:
        rem = n % 10
        Contra = Contra * 10 + rem
        n = n // 10
    if Contra == CopyNum:
        return True
    else:
        return False
