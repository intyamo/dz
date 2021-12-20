#!/usr/bin/env python

# Бабушка Зина любит печь блины своему любимому внуку Васе.
# А внук Вася любит математику и знает, что периметр и площадь блина можно найти по диаметру сковородки.
# Напишите программу, которая поможет Васе проверить его вычисления.

pi = 3.141592653589793


def perimeter(d):
    perimeter = pi * d
    return perimeter


def area(d):
    area = pi * d ** 2 / 4
    return area


if __name__ == "__main__":
    d = int(input("Диаметр сковородки = "))

    print(perimeter(d))
    print(area(d))
