#!/usr/bin/env python

# Бабушка Зина любит печь блины своему любимому внуку Васе.
# А внук Вася любит математику и знает, что периметр и площадь блина можно найти по диаметру сковородки.
# Напишите программу, которая поможет Васе проверить его вычисления.
from math import pi


def perimeter(diameter):
    parim = pi * diameter
    return parim


def area(diameter):
    areas = pi * (diameter / 2) ** 2
    return areas


if __name__ == "__main__":
    d = int(input("Диаметр сковородки = "))

    print(perimeter(d))
    print(area(d))
