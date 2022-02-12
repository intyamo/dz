#!/usr/bin/env python

"""
Напишите функции для вывода ходов шахматных фигур на пустой доске.

Например, для коня на поле a1 доступны 2 поля: b3 и с2,
а для ладьи на поле a1 будут доступны вся вертикаль a и 1-ая горизонталь.
"""


def rook_moves(square: str) -> list:
    square_1 = list(square)
    square_1[0] = ord(square_1[0]) - 97
    square_1[1] = ord(square_1[1]) - 49
    moves = [-7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7]
    AA = []
    for dx in moves:
        x = square_1[0] + dx
        if 0 <= x <= 7:
            AA.append([x, square_1[1]])
    for dy in moves:
        y = square_1[1] + dy
        if 0 <= y <= 7:
            AA.append([square_1[0], y])
    result = []
    for i in range(len(AA)):
        result.append(str(chr(AA[i][0] + 97) + str(chr(AA[i][1] + 49))))
    return result


def bishop_moves(square: str) -> list:
    square_1 = list(square)
    square_1[0] = ord(square_1[0]) - 97
    square_1[1] = ord(square_1[1]) - 49
    moves = [-7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7]
    AA = []
    for dx in moves:
        x = square_1[0] + dx
        y = square_1[1] + dx
        if 0 <= x <= 7 and 0 <= y <= 7:
            AA.append([x, y])
    for dx in moves:
        x = square_1[0] + dx
        y = square_1[1] - dx
        if 0 <= x <= 7 and 0 <= y <= 7:
            AA.append([x, y])
    result = []
    for i in range(len(AA)):
        result.append(str(chr(AA[i][0] + 97) + str(chr(AA[i][1] + 49))))
    return result


def queen_moves(square: str) -> list:
    square_1 = list(square)
    square_1[0] = ord(square_1[0]) - 97
    square_1[1] = ord(square_1[1]) - 49
    moves = [-7, -6, -5, -4, -3, -2, -1, 1, 2, 3, 4, 5, 6, 7]
    AA = []
    for dx in moves:
        x = square_1[0] + dx
        y = square_1[1] + dx
        if 0 <= x <= 7 and 0 <= y <= 7:
            AA.append([x, y])
    for dx in moves:
        x = square_1[0] + dx
        y = square_1[1] - dx
        if 0 <= x <= 7 and 0 <= y <= 7:
            AA.append([x, y])
    for dx in moves:
        x = square_1[0] + dx
        if 0 <= x <= 7:
            AA.append([x, square_1[1]])
    for dy in moves:
        y = square_1[1] + dy
        if 0 <= y <= 7:
            AA.append([square_1[0], y])
    result = []
    for i in range(len(AA)):
        result.append(str(chr(AA[i][0] + 97) + str(chr(AA[i][1] + 49))))
    return result


def knight_moves(square: str) -> list:
    square_1 = list(square)
    square_1[0] = ord(square_1[0]) - 97
    square_1[1] = ord(square_1[1]) - 49
    moves = [[1, 2], [1, -2], [-1, 2], [-1, -2], [2, 1], [2, -1], [-2, 1], [-2, -1]]
    AA = []
    for dx, dy in moves:
        x = square_1[0] + dx
        y = square_1[1] + dy
        if 0 <= x <= 7 and 0 <= y <= 7:
            AA.append([x, y])
    result = []
    for i in range(len(AA)):
        result.append(str(chr(AA[i][0] + 97) + str(chr(AA[i][1] + 49))))
    return result


def king_moves(square: str) -> list:
    square_1 = list(square)
    square_1[0] = ord(square_1[0]) - 97
    square_1[1] = ord(square_1[1]) - 49
    moves = [[1, 0], [1, -1], [0, -1], [-1, -1], [-1, 0], [-1, 1], [0, 1], [1, 1]]
    AA = []
    for dx, dy in moves:
        x = square_1[0] + dx
        y = square_1[1] + dy
        if 0 <= x <= 7 and 0 <= y <= 7:
            AA.append([x, y])
    result = []
    for i in range(len(AA)):
        result.append(str(chr(AA[i][0] + 97) + str(chr(AA[i][1] + 49))))
    return result


square = input('Введите положение фигуры - ')
print('Ходы ладьи -', rook_moves(square))
print('Ходы слона -', bishop_moves(square))
print('Ходы ферзя -', queen_moves(square))
print('Ходы коня -', knight_moves(square))
print('Ходы короля -', king_moves(square))
