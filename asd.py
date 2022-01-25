import re

fen = "4r2k/q5bp/4R3/4P1P1/P1Qn3R/2N5/1r4KP/8 w - - 1 43"
fen_norm = re.sub(r'w.*', "", fen).replace('/', '').replace(' ', '')
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
fen_list = []
a = []
for i in fen_norm:
    fen_list.append(i)
for i in fen_list:
    if int(i) == int:
        a.append(1)
    else:
        pass

print(fen_norm)
print(fen_list)
print(a)
