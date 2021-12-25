#!/usr/bin/env python

"""
В школе, в которой учится В. Пупкин, занятия начинаются в 8 утра.
Урок длится 45 минут.
После каждого нечётного урока (1-го, 3-го, 5-го ...) перемена 5 минут,
а после каждого чётного (2-го, 4-го, 6-го ...) - 15.

Помогите непоседе Васе посчитать, когда заканчивается n-ый урок.
"""


def end_of_lesson(n: int) -> (int, int):
    hours = 8
    minutes = 0
    h = 0
    for i in range(1, n+1):
        if i % 2 == 0:
            minutes +=60
        else:
            minutes +=50
    if n % 2 == 0:
        minutes -= 15
    else:
        minutes -= 5
    h += minutes//60
    minutes -= h*60
    hours += h
    return hours, minutes


if __name__ == "__main__":
    n = int(input("Номер урока: "))

    hours, minutes = end_of_lesson(n)

    print(f"{n}-ый урок заканчивается в {hours}:{minutes:02}")
