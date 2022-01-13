import random

from not_last import last_but_one

PUPILS_LIST = [
    ("Вася Пупкин", 3.2),
    ("Петя Дудкин", 3.9),
    ('Юра Баранкин', 4.100_01),
    ("Костя Малинин", 3.141_592),
    ("Зина Фокина", 4.8),
    ("Артур Пирожков", 3.2),
    ("Гадя Петрович", 3.141_592)
]


def test_vasya_wins():
    pupils = list(PUPILS_LIST)
    for _ in range(3):
        random.shuffle(pupils)

        assert last_but_one(pupils) == ["Артур Пирожков", "Вася Пупкин"]


def test_petya_wins():
    pupils = list(PUPILS_LIST)
    assert pupils.pop(3) == ("Костя Малинин", 3.141_592)  # Костя Малинин
    assert pupils.pop() == ("Гадя Петрович", 3.141_592)  # Гадя Петрович

    for _ in range(3):
        random.shuffle(pupils)

        assert last_but_one(pupils) == ["Петя Дудкин"]
