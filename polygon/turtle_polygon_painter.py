#!/usr/bin/env python

"""
Рисует
"""

import sys
import turtle

from polygon import polygon_vertices


R = 200.0
PENSIZE = 10


if __name__ == "__main__":
    if len(sys.argv) > 1:
        n = int(sys.argv[1])
    else:
        n = 6  # draw hexagon by default
        # or read from stdin
        # n = int(input("n = "))

    vertices = polygon_vertices(n, R)

    # setup
    t = turtle.Turtle()
    t.color("red", "yellow")
    t.pensize(PENSIZE)

    # go to first vertex
    t.penup()
    t.goto(vertices[0])
    t.pendown()

    # draw polygon
    t.begin_fill()
    for x, y in vertices:
        t.goto(x, y)

    # go to initial vertex to finish the shape
    x, y = vertices[0]
    t.goto(x, y)
    t.end_fill()

    # done
    turtle.exitonclick()
