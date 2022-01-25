from chess_moves import *


# --- HELPER FUNCTIONS ---


def cmp(result, expected):
    return set(result) == expected


def moves(s: str) -> set:
    return set(s.split())


# --- TESTS ---


def test_rook_a1():
    expected = moves("a2 a3 a4 a5 a6 a7 a8") | moves("b1 c1 d1 e1 f1 g1 h1")

    assert cmp(rook_moves("a1"), expected)


def test_rook_e4():
    expected = moves("e1 e2 e3 e5 e6 e7 e8") | moves("a4 b4 c4 d4 f4 g4 h4")

    assert cmp(rook_moves("e4"), expected)


def test_bishop_h8():
    expected = moves("a1 b2 c3 d4 e5 f6 g7")

    assert cmp(bishop_moves("h8"), expected)


def test_bishop_e4():
    expected = moves("b1 c2 d3 f5 g6 h7") | moves("h1 g2 f3 d5 c6 b7 a8")

    assert cmp(bishop_moves("e4"), expected)


def test_queen_a1():
    expected = (
        moves("a2 a3 a4 a5 a6 a7 a8")
        | moves("b1 c1 d1 e1 f1 g1 h1")
        | moves("b2 c3 d4 e5 f6 g7 h8")
    )

    assert cmp(queen_moves("a1"), expected)


def test_queen_e4():
    expected = (
        moves("e1 e2 e3 e5 e6 e7 e8")
        | moves("a4 b4 c4 d4 f4 g4 h4")
        | moves("b1 c2 d3 f5 g6 h7")
        | moves("h1 g2 f3 d5 c6 b7 a8")
    )

    assert cmp(queen_moves("e4"), expected)


def test_knight_a1():
    expected = moves("b3 c2")

    assert cmp(knight_moves("a1"), expected)


def test_knight_e4():
    expected = moves("c3 c5 d2 d6 f2 f6 g3 g5")

    assert cmp(knight_moves("e4"), expected)


def test_knight_g8():
    expected = moves("e7 f6 h6")

    assert cmp(knight_moves("g8"), expected)


def test_king_e4():
    expected = moves("d3 d4 d5 e5 f5 f4 f3 e3")

    assert cmp(king_moves("e4"), expected)


def test_king_a1():
    expected = moves("a2 b2 b1")

    assert cmp(king_moves("a1"), expected)
