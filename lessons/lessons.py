#!/usr/bin/env python

"""
В школе, в которой учится В. Пупкин, занятия начинаются в 8 утра.
Урок длится 45 минут.
После каждого нечётного урока (1-го, 3-го, 5-го ...) перемена 5 минут,
а после каждого чётного (2-го, 4-го, 6-го ...) - 15.

Помогите непоседе Васе посчитать, когда заканчивается n-ый урок.
"""


def end_of_lesson(n: int) -> (int, int):
    minutes = 45 * n
    for i in range(1, n + 1):
        if i % 2 != 0:
            minutes += 5
        else:
            minutes += 15
    if n % 2 == 0:
        minutes -= 15
    else:
        minutes -= 5
    hours1 = minutes // 60
    hours = hours1 + 8
    minutes -= hours1 * 60
    return hours, minutes


if __name__ == "__main__":
    n = int(input("Номер урока: "))

    hours, minutes = end_of_lesson(n)

    print(f"{n}-ый урок заканчивается в {hours}:{minutes:02}")
