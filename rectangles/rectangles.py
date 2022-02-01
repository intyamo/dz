#!/usr/bin/env python

"""
Даны два прямоугольника, стороны которых параллельны осям координат. Известны координаты левого нижнего угла x, y, а также ширина и высота прямоугольника w, h.

                w
    ┌───────────────────────┐
    │                       │
    │                       │ h
    │                       │
    └───────────────────────┘
 (x, y)

- определить, принадлежат ли все точки второго прямоугольника первому (`all`).
- определить, пересекаются ли эти прямоугольники (`any`, `all`).
"""

from collections import namedtuple

Rect = namedtuple("Rect", "x y w h".split())


def rect_inside(a: Rect, b: Rect) -> bool:
    """
    Checks if whole rectangle `b` is within rectangle `a`.
    """
    if b[0] >= a[0] and b[1] >= a[1] and b[2] + b[0] <= a[2] + a[0] and b[3] + b[1] <= a[3] + a[1]:
        return True
    else:
        return False


def rects_intersect(a: Rect, b: Rect) -> bool:
    """
    Checks if 2 rectangles `a` and `b` have at least a single intersection point.
    """
    if (a[0] <= b[0] <= a[0] + a[2] and a[1] <= b[1] <= a[1] + a[3]
            or a[0] <= b[0] <= a[0] + a[2] and a[1] <= b[1] + b[3] <= a[1] + a[3]
            or a[0] <= b[0] + b[2] <= a[0] + a[2] and a[1] <= b[1] + b[3] <= a[1] + a[3]
            or a[0] <= b[0] + b[2] <= a[0] + a[2] and a[1] <= b[1] <= a[1] + a[3]):
        return True
    else:
        return False


a = Rect(0, 1, 15, 20)
b = Rect(-5, 0, 8, 8)
print('Прямоугольник а', a)
print('Прямоугольник b', b)
print('____')
print('принадлежат ли все точки второго прямоугольника первому', rect_inside(a, b))
print('____')
print('пересекаются ли эти прямоугольники', rects_intersect(a, b))
