#!/usr/bin/env python

# Бабушка Зина любит печь блины своему любимому внуку Васе.
# А внук Вася любит математику и знает, что периметр и площадь блина можно найти по диаметру сковородки.
# Напишите программу, которая поможет Васе проверить его вычисления.


from math import pi

def perimeter(diameter):
    return pi * diameter


def area(diameter):
    return pi * (diameter ** 2) / 4


if __name__ == "__main__":
    d = int(input("Диаметр сковородки = "))

    print('периметр блина - ', perimeter(d))
    print('площадь блина - ', area(d))
