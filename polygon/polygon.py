#!/usr/bin/env python

r"""
Напишите функцию, которая генерирует вершины n-угольника.

Функция возвращает список вершин. Каждая вершина задаётся таплом из координат x и y.
Первая вершина лежит на оси Y: `(0.0, R)` (т.е. на 12 часов), следующие идут по часовой стрелке.

Например, квадрат будет иметь следующие 4 вершины:

`[(0.0, R), (R, 0.0), (0.0, -R), (-R, 0.0)]`


   1
  / \
 /   \
4     2
 \   /
  \ /
   3
"""

from math import pi, sin, cos


def polygon_vertices(n: int, r: float) -> list:
    alfa = (2 * pi) / n
    point = [(0.0, r)]
    for i in range(1, n):
        point += [(round(sin(alfa * i) * r, 1), round(cos(alfa * i) * r, 1))]
    return point


n = int(input('Введите число вершин - '))
r = float(input('введите R - '))
print(polygon_vertices(n, r))
