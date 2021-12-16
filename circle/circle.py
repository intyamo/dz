#!/usr/bin/env python

# Бабушка Зина любит печь блины своему любимому внуку Васе.
# А внук Вася любит математику и знает, что периметр и площадь блина можно найти по диаметру сковородки.
# Напишите программу, которая поможет Васе проверить его вычисления.
<< << << < HEAD
from math import pi


def perimeter(diameter):
    return pi * diameter


def area(diameter):
    r = diameter / 2
    return pi * r ** 2

== == == =

def perimeter(diameter):
    pass


def area(diameter):
    pass

>> >> >> > 111
fee6(Initial
commit)


if __name__ == "__main__":
    d = int(input("Диаметр сковородки = "))

    print(perimeter(d))
    print(area(d))
