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
import re



# ready
def calc_chess_balance(fen: str) -> int:
    PAWN_VAL = 1  # пешка
    KNIGHT_VAL = BISHOP_VAL = 3  # конь и слон
    ROOK_VAL = 5  # ладья
    QUEEN_VAL = 9  # ферзь
    a = fen.find(' ')
    slice = fen[:a]
    n = len(slice)
    while_ = 0
    black = 0
    for i in range(0, n):
        sim = slice[i]
        if sim == 'P':
            while_ += PAWN_VAL
        elif sim == 'p':
            black += PAWN_VAL
        elif sim == 'B' or sim == 'N':
            while_ += KNIGHT_VAL
        elif sim == 'b' or sim == 'n':
            black += KNIGHT_VAL
        elif sim == 'R':
            while_ += ROOK_VAL
        elif sim == 'r':
            black += ROOK_VAL
        elif sim == 'Q':
            while_ += QUEEN_VAL
        elif sim == 'q':
            black += QUEEN_VAL
    chess_balance = while_ - black
    return chess_balance


def chess_board(fen: str) -> str:
    search = fen.find(' ')
    slice = fen[:(search + 1)]
    chisl_matric = len(slice)
    new_text = ''
    string = ''
    for f in range(0, chisl_matric):
        simvol = slice[f]
        if len(string) == 16:
            new_text += string.lstrip() + '\n'
            string = ''
        else:
            if simvol.isdecimal() == True:
                string += ' .' * int(simvol)
            elif simvol == '/':
                string += ''
            else:
                string += ' ' + simvol
    chess = new_text.splitlines()
    chess_board = f'''\
{chess[0]}
{chess[1]}
{chess[2]}
{chess[3]}
{chess[4]}
{chess[5]}
{chess[6]}
{chess[7]}\
'''
    return chess_board


