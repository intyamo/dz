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

# ready
def calc_chess_balance(fen: str) -> int:
    balance = 0
    for i in fen:
        if i == 'Q':
            balance += QUEEN_VAL
        elif i == 'R':
            balance += ROOK_VAL
        elif i == 'B' or i == 'N':
            balance += BISHOP_VAL
        elif i == 'P':
            balance += PAWN_VAL
        elif i == 'q':
            balance -= QUEEN_VAL
        elif i == 'r':
            balance -= ROOK_VAL
        elif i == 'b' or i == 'n':
            balance -= BISHOP_VAL
        elif i == 'p':
            balance -= PAWN_VAL
    return balance


def chess_board(fen: str) -> str:
    index_el = fen.find(' ')
    field = fen[:(index_el + 1)]
    chisl_matric = len(field)
    board = ''
    aboard = ''
    for f in range(0, chisl_matric):
        element_fen = field[f]
        if len(aboard) == 16:
            board += aboard.lstrip() + '\n'
            aboard = ''
        else:
            if element_fen.isdecimal() == True:
                aboard += ' .' * int(element_fen)
            elif element_fen == '/':
                aboard += ''
            else:
                aboard += ' ' + element_fen
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
print(chess_board("4r2k/q5bp/4R3/4P1P1/P1Qn3R/2N5/1r4KP/8 w - - 1 43"))
