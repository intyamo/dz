from str_remove_fragment import remove_fragment


def test_ahahaha():
    assert remove_fragment("ahahaha", "h") == "aa"


def test_aaaaa():
    assert remove_fragment("aaaaAAAaaaa", sep="a") == ""


def test_pipes():
    assert remove_fragment("Казнить|,| нельзя помиловать", "|") == "Казнить нельзя помиловать"
    assert remove_fragment("Казнить нельзя|,| помиловать", "|") == "Казнить нельзя помиловать"


def test_1_sep_first():
    s = "¿Por qué?"
    assert remove_fragment(s, "¿") == s


def test_1_sep_last():
    s = "¿Por qué?"
    assert remove_fragment(s, "?") == s


def test_no_separator():
    s = "*this* is a *test*"
    assert remove_fragment(s, sep="**") == s


def test_complex_separator():
    s = "**this** is a **test**"
    assert remove_fragment(s, sep="**") == ""
