from math import pi

import pytest
from circle import perimeter, area


def float_eq(real, expected):
    """
    Helper function to compare floats
    """
    return abs(real - expected) < 0.001


def test_perimeter():
    d = 3
    assert float_eq(perimeter(d), pi * d)


def test_square():
    d = 4.2
    assert float_eq(area(d), pi * (d / 2) ** 2)


def test_invalid_types():
    with pytest.raises(TypeError):
        perimeter("2")
