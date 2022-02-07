#!/usr/bin/env python

"""
Реализовать функцию `get_ranges` которая “сворачивает” список неповторяющихся целых чисел, отсортированных по возрастанию:

- [0, 1, 2, 3, 4, 7, 8, 10] -> "0-4, 7-8, 10"
- [4, 7, 10] -> "4, 7, 10"
- [2, 3, 8, 9]) -> "2-3, 8-9"
"""


def get_ranges(l: list) -> str:
    num1 = num2 = " "
    for i in sorted(l):
        if num1 is None:
            num1 = num2 = i
        elif i == num2 or i == num2 + 1:
            num2 = i
        else:
            yield num1, num2
            num1 = num2 = i
    if num1 is not None:
        yield num1, num2
    print(repr(", ".join(["%d" % num1 if num1 == num2 else "%d-%d" % (num1, num2) for (num1, num2) in get_ranges(l)])))
