#!/usr/bin/env python

"""
Напишите функцию, которая принимает на вход строку `s` и некоторый разделитель `sep`.
Функция должна удалить из строки всё, что находится между первым и последним разделителем, а также их самих.
Если таких разделителей в строке меньше двух, вернуть исходную строку.
"""


def remove_fragment(s: str, sep: str) -> str:
    if s.count(sep) < 2:
        result = s
    else:
        start = s.find(sep)
        end = s.rfind(sep) + len(sep)
        result = s[:start] + s[end:]
    return result



