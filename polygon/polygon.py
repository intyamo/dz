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
    ugol = 2 * pi / n
    ugol_0 = 0
    koord = []
    for i in range(n):
        y = cos(ugol_0) * R
        x = sin(ugol_0) * R
        koord.append((x, y))
        ugol_0 += ugol
    return koord

# n = int(input())
# itog = polygon_vertices(n, R)
# print(itog)
