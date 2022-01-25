#!/usr/bin/env python

"""
Напишите функцию, которая принимает на вход строку `s` и некоторый разделитель `sep`.
Функция должна удалить из строки всё, что находится между первым и последним разделителем, а также их самих.
Если таких разделителей в строке меньше двух, вернуть исходную строку.
"""



def remove_fragment(s: str, sep: str) -> str:
    if s.count(sep) < 2:
        c = s
    else:
        a = s.find(sep)
        b = s.rfind(sep) + len(sep)
        c = s[:a] + s[b:]
    return c

# s, sep = input(), input()
# c = remove_fragment(s, sep)
# print(c)

