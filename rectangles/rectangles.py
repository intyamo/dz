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
    x1, y1, w1, h1 = a
    x2, y2, w2, h2 = b
    z1 = x1 <= x2 <= (x1 + w1)
    z2 = y1 <= y2 <= (y1 + h1)
    z3 = (x2 + w2) <= (x1 + w1)
    z4 = (y2 + h2) <= (y1 + h1)
    if all([z1, z2, z3, z4]) == True:
        result = True
    else:
        result = False
    return result


def rects_intersect(a: Rect, b: Rect) -> bool:
    """
    Checks if 2 rectangles `a` and `b` have at least a single intersection point.
    """
    x1, y1, w1, h1 = a
    x2, y2, w2, h2 = b
    z1 = x1 <= x2 <= (x1 + w1) and y1 <= y2 <= (y1 + h1)
    z2 = x1 <= x2 <= (x1 + w1) and y1 <= y2 + h2 <= (y1 + h1)
    z3 = x1 <= x2 + w2 <= (x1 + w1) and y1 <= y2 <= (y1 + h1)
    z4 = x1 <= x2 + w2 <= (x1 + w1) and y1 <= y2 + h2 <= (y1 + h1)
    z5 = x2 <= x1 <= (x2 + w2) and y2 <= y1 <= (y2 + h2)
    z6 = x2 <= x1 <= (x2 + w2) and y2 <= y1 + h1 <= (y2 + h2)
    z7 = x2 <= x1 + w1 <= (x2 + w2) and y2 <= y1 <= (y2 + h2)
    z8 = x2 <= x1 + w1 <= (x2 + w2) and y2 <= y1 + h1 <= (y2 + h2)
    if any([z1, z2, z3, z4, z5, z6, z7, z8]) == True:
        result = True
    else:
        result = False
    return result
