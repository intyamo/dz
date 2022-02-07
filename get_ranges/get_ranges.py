#!/usr/bin/env python

"""
Реализовать функцию `get_ranges` которая “сворачивает” список неповторяющихся целых чисел, отсортированных по возрастанию:

- [0, 1, 2, 3, 4, 7, 8, 10] -> "0-4, 7-8, 10"
- [4, 7, 10] -> "4, 7, 10"
- [2, 3, 8, 9]) -> "2-3, 8-9"
"""


def get_ranges(l: list) -> str:
    if l == []:
        result_1 = ''
    else:
        result = []
        result_1 = []
        for i in range(len(l)):
            if i == 0:
                result.append(l[i])
                v = l[i]
            elif l[i] == (v + 1):
                result.append(l[i])
                v = l[i]
            else:
                if len(result) == 1:
                    result_1.append(str(result[0]))
                else:
                    result_1.append(str(result[0]) + '-' + str(result[-1]))
                result = []
                result.append(l[i])
                v = l[i]
        if len(result) == 1:
            result_1.append(str(result[0]))
        else:
            result_1.append(str(result[0]) + '-' + str(result[-1]))
        result_1 = ', '.join(result_1)
    return result_1
