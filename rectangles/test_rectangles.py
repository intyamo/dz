from rectangles import Rect, rect_inside, rects_intersect


def test_intersect():
    a = Rect(0, 0, 2, 3)
    b = Rect(x=-1, y=-1, w=2, h=3)

    assert not rect_inside(a, b)


def test_intersect_single_point():
    a = Rect(0, 0, 2, 3)
    b = Rect(x=2, y=3, w=4, h=5)

    assert rects_intersect(a, b)


def test_dont_intersect():
    a = Rect(0, 0, 2, 3)
    b = Rect(x=4, y=5, w=6, h=7)

    assert not rects_intersect(a, b)


def test_b_inside_a():
    a = Rect(0, 0, 2, 3)
    b = Rect(0, 0, 1, 2)

    assert rect_inside(a, b)


def test_b_outside_a():
    a = Rect(0, 0, 2, 3)
    b = Rect(x=-1, y=-1, w=2, h=3)

    assert not rect_inside(a, b)
