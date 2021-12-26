#!/usr/bin/env python

"""
Реализуйте функцию, которая использует шахматную нотацию Форсайта-Эдвардса (FEN - Forsyth–Edwards Notation)
для подсчёта баланса материала между белыми и чёрными.

- https://en.wikipedia.org/wiki/Forsyth–Edwards_Notation
- https://ru.wikipedia.org/wiki/Нотация_Форсайта_—_Эдвардса
- https://www.chessprogramming.org/Forsyth-Edwards_Notation

FEN задаёт полное расположение фигур на доске.
Относительная ценность фигур задана константами.
Короли с доски не снимаются, они бесценны и поэтому их учитывать не надо.

---

Также реализуйте функцию, которая возвращает строковое представление доски.

Например, для FEN начальной позиции

`rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1`

таким представлением будет

```
r n b q k b n r
p p p p p p p p
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
P P P P P P P P
R N B Q K B N R
```
"""

PAWN_VAL = 1  # пешка
KNIGHT_VAL = BISHOP_VAL = 3  # конь и слон
ROOK_VAL = 5  # ладья
QUEEN_VAL = 9  # ферзь


def calc_chess_balance(fen: str) -> int:
    pass


def chess_board(fen: str) -> str:
    pass
