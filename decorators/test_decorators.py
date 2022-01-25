from decorators import repeat, html


# Repeater

def test_repeater():
    var = 0
    n = 10

    @repeat(n)
    def modify_var():
        nonlocal var
        var += 1

    modify_var()

    assert var == n


# HTML tag

def test_basic():
    bold = html("b")
    italic = html("i")

    @bold
    @italic
    def champion():
        return "Вася Пупкин - чемпион"

    assert champion() == "<b><i>Вася Пупкин - чемпион</i></b>"


def test_html_with_attributes():
    @html("a", href="https://vpupk.in", target="_blank", hidden=True)
    def vpupkin():
        return "V. Pupkin"

    assert vpupkin() == '<a href="https://vpupk.in" target="_blank" hidden>V. Pupkin</a>'
