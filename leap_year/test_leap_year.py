from leap_year import is_leap_year


def test_year_not_divisible_by_4():
    assert not is_leap_year(2021)


def test_year_divisible_by_2_but_not_by_4():
    assert not is_leap_year(1970)


def test_year_divisible_by_4_not_by_100():
    assert is_leap_year(1996)


def test_year_divisible_by_100_not_divisible_by_400():
    assert not is_leap_year(1900)


def test_year_divisible_by_400():
    assert is_leap_year(2000)
