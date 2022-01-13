from fibonacci import fibonacci


def test_first_3():
    assert fibonacci(0) == 0
    assert fibonacci(1) == 1
    assert fibonacci(2) == 1


def test_13th():
    assert fibonacci(13) == 233


def test_17th():
    assert fibonacci(17) == 1597


def test_20th():
    assert fibonacci(20) == 6765
