from FEN import calc_chess_balance, chess_board


# --- diff ---


def test_starting_pos():
    fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    assert calc_chess_balance(fen) == 0


def test_karpov_kasparov_1985_16_octopus():
    fen = "8/5pk1/7p/8/1p4P1/1P1R2P1/3N1qBP/3Nr2K w - - 1 41"
    assert calc_chess_balance(fen) == 1


def test_karpov_kasparov_1985_24_champ():
    fen = "4r2k/q5bp/4R3/4P1P1/P1Qn3R/2N5/1r4KP/8 w - - 1 43"
    assert calc_chess_balance(fen) == 0


def test_kasparov_karpov_1990_20_queen_sac():
    fen = "r3Rb1k/8/p2p3q/3n1bN1/Pn6/6RP/1p3PPK/1B6 w - - 0 35"
    assert calc_chess_balance(fen) == -9


# --- boards ---


def test_board_starting_pos():
    fen = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1"
    board = """\
r n b q k b n r
p p p p p p p p
. . . . . . . .
. . . . . . . .
. . . . . . . .
. . . . . . . .
P P P P P P P P
R N B Q K B N R\
"""

    assert chess_board(fen) == board


def test_board_kasparov_karpov_1985_24_champ():
    fen = "4r2k/q5bp/4R3/4P1P1/P1Qn3R/2N5/1r4KP/8 w - - 1 43"
    board = """\
. . . . r . . k
q . . . . . b p
. . . . R . . .
. . . . P . P .
P . Q n . . . R
. . N . . . . .
. r . . . . K P
. . . . . . . .\
"""

    assert chess_board(fen) == board
