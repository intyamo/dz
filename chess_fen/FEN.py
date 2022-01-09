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
    a = fen.find(' ')
    srez = fen[:a]
    n = len(srez)
    wh = 0
    bl = 0
    for i in range(0, n):
        sim = srez[i]
        if sim == 'P':
            wh += PAWN_VAL
        elif sim == 'p':
            bl += PAWN_VAL
        elif sim == 'B' or sim == 'N':
            wh += KNIGHT_VAL
        elif sim == 'b' or sim == 'n':
            bl += KNIGHT_VAL
        elif sim == 'R':
            wh += ROOK_VAL
        elif sim == 'r':
            bl += ROOK_VAL
        elif sim == 'Q':
            wh += QUEEN_VAL
        elif sim == 'q':
            bl += QUEEN_VAL
    calc_chess_balance = wh - bl
    return calc_chess_balance


def chess_board(fen: str) -> str:
    chisl_s = fen.find(' ')
    matric = fen[:(chisl_s + 1)]
    chisl_matric = len(matric)
    board = ''
    aboard = ''
    for f in range(0, chisl_matric):
        simvol = matric[f]
        if len(aboard) == 16:
            board += aboard.lstrip() + '\n'
            aboard = ''
        else:
            if simvol.isdecimal() == True:
                aboard += ' .' * int(simvol)
            elif simvol == '/':
                aboard += ''
            else:
                aboard += ' ' + simvol
    chess = board.splitlines()
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
