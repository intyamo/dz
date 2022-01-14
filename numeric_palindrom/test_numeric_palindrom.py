from numeric_palindrom import is_palindrom


def test_12321():
    assert is_palindrom(12321)


def test_123321():
    assert is_palindrom(123321)


def test_1():
    assert is_palindrom(1)


def test_not_palindrom():
    assert not is_palindrom(123)
