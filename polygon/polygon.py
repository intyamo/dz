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

R = 3.0


def polygon_vertices(n: int, r: float = R) -> list:
    angle1 = 2 * pi / n
    angle2 = 0
    cords = []
    for i in range(n):
        y = cos(angle2) * r
        x = sin(angle2) * r
        cords.append((x, y))
        angle2 += angle1
    return cords
