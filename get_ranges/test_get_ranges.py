from get_ranges import get_ranges


def test_empty():
    assert get_ranges([]) == ""


def test_3_ranges():
    assert get_ranges([0, 1, 2, 3, 4, 7, 8, 10]) == "0-4, 7-8, 10"


def test_no_ranges():
    assert get_ranges([4, 7, 10]) == "4, 7, 10"


def test_mixed():
    assert get_ranges([2, 3, 5, 8, 9, 11, 12, 13, 20]) == "2-3, 5, 8-9, 11-13, 20"
