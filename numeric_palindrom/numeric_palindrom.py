#!/usr/bin/env python

"""
Напишите функцию, которая проверяет, является ли целое положительное число палиндромом.

Можно работать только с числами, конвертировать в строку нельзя :)
"""


def is_palindrom(n: int) -> bool:
    n_0 = n
    if n <= 0:
        raise ValueError("Number must be a positive integer")
    list_1 = []
    while n != 0:
        last_digit = n % 10
        list_1.append(last_digit)
        n //= 10
    summa = 0
    for i in range(len(list_1), 0, -1):
        summa += list_1[-i] * (10 ** (i - 1))
    if n_0 == summa:
        vivod = True
    else:
        vivod = False
    return vivod


# n = int(input())
# itog = is_palindrom(n)
# print(itog)
