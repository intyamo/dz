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

    conditions_1 = x1 <= x2 <= x1 + w1
    conditions_2 = y1 <= y2 <= y1 + h1
    conditions_3 = (x2 + w2) <= (x1 + w1)
    conditions_4 = (y2 + h2) <= (y1 + h1)
    if all([conditions_1, conditions_2, conditions_3, conditions_4]):
        return True
    else:
        return False


def rects_intersect(a: Rect, b: Rect) -> bool:
    """
    Checks if 2 rectangles `a` and `b` have at least a single intersection point.
    """
    x1, y1, w1, h1 = a
    x2, y2, w2, h2 = b
    conditions_1 = x1 <= x2 <= (x1 + w1) and y1 <= y2 <= (y1 + h1)
    conditions_2 = x1 <= x2 <= (x1 + w1) and y1 <= y2 + h2 <= (y1 + h1)
    conditions_3 = x1 <= x2 + w2 <= (x1 + w1) and y1 <= y2 <= (y1 + h1)
    conditions_4 = x1 <= x2 + w2 <= (x1 + w1) and y1 <= y2 + h2 <= (y1 + h1)
    conditions_5 = x2 <= x1 <= (x2 + w2) and y2 <= y1 <= (y2 + h2)
    conditions_6 = x2 <= x1 <= (x2 + w2) and y2 <= y1 + h1 <= (y2 + h2)
    conditions_7 = x2 <= x1 + w1 <= (x2 + w2) and y2 <= y1 <= (y2 + h2)
    conditions_8 = x2 <= x1 + w1 <= (x2 + w2) and y2 <= y1 + h1 <= (y2 + h2)
    if any([conditions_1, conditions_2, conditions_3, conditions_4, conditions_5, conditions_6, conditions_7,
            conditions_8]) == True:
        result = True
    else:
        result = False
    return result
