#!/usr/bin/env python

"""
Реализовать функцию `get_ranges` которая “сворачивает” список неповторяющихся целых чисел, отсортированных по возрастанию:

- [0, 1, 2, 3, 4, 7, 8, 10] -> "0-4, 7-8, 10"
- [4, 7, 10] -> "4, 7, 10"
- [2, 3, 8, 9]) -> "2-3, 8-9"
"""

from itertools import groupby
from operator import itemgetter


def get_ranges(l: list) -> str:
    X = l[0]
    itog1 = []
    itog2 = []
    for i in range(len(l)):
        if i == 0:
            itog1.append(l[i])
            X = l[i]
        elif l[i] == X + 1:
            itog1.append(l[i])
            X = l[i]
        else:
            if len(itog1) == 1:
                itog2.append(str(itog1[0]))
            else:
                itog2.append(str(itog1[0]) + '-' + str(itog1[-1]))
            itog1 = []
            itog1.append(l[i])
            X = l[i]
    if len(itog1) == 1:
        itog2.append(str(itog1[0]))
    else:
        itog2.append(str(itog1[0]) + '-' + str(itog1[-1]))
    return itog2


a = [1, 3, 2, 8, 9, 34, 44, 45, 12, 9, 12]
l = sorted(set(a))
print(l)
print('_____')
print(get_ranges(l))
