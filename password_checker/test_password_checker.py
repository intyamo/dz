from password_checker import is_strong_password

STRONG_PWD = "даLadno?$123.4"


def test_strong():
    assert is_strong_password(STRONG_PWD)


def test_too_short():
    assert not is_strong_password("Rly?1")


def test_no_digits():
    assert not is_strong_password("даLaaadno?!")


def test_no_mixed_case():
    assert not is_strong_password(STRONG_PWD.lower())
    assert not is_strong_password(STRONG_PWD.upper())


def test_no_punctuation():
    assert not is_strong_password("даLadno98765")
