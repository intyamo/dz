#!/usr/bin/env python

"""
Напишите функции для вывода ходов шахматных фигур на пустой доске.

Например, для коня на поле a1 доступны 2 поля: b3 и с2,
а для ладьи на поле a1 будут доступны вся вертикаль a и 1-ая горизонталь.
"""


def rook_moves(square: str) -> list:
    a_1 = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h'}
    a_2 = {a_1[i]: i for i in a_1}
    square_0 = square
    res = []
    square = list(square)
    square = [a_2[square[0]], int(square[1])]
    for j in a_1.keys():
        for k in a_1.keys():
            if square[0] == j or square[1] == k:
                if (a_1[j] + str(k)) != square_0:
                    res.append(a_1[j] + str(k))
    return res


def bishop_moves(square: str) -> list:
    a_1 = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h'}
    a_2 = {a_1[i]: i for i in a_1}
    square_0 = square
    res = []
    square = list(square)
    square = [a_2[square[0]], int(square[1])]
    for j in a_1.keys():
        for k in a_1.keys():
            if abs(square[0] - j) == abs(square[1] - k):
                if (a_1[j] + str(k)) != square_0:
                    res.append(a_1[j] + str(k))
    return res


def queen_moves(square: str) -> list:
    a_1 = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h'}
    a_2 = {a_1[i]: i for i in a_1}
    square_0 = square
    res = []
    square = list(square)
    square = [a_2[square[0]], int(square[1])]
    for j in a_1.keys():
        for k in a_1.keys():
            if (abs(square[0] - j) == abs(square[1] - k)) or (square[0] == j or square[1] == k):
                if (a_1[j] + str(k)) != square_0:
                    res.append(a_1[j] + str(k))
    return res


def knight_moves(square: str) -> list:
    a_1 = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h'}
    a_2 = {a_1[i]: i for i in a_1}
    square_0 = square
    res = []
    square = list(square)
    square = [a_2[square[0]], int(square[1])]
    for j in a_1.keys():
        for k in a_1.keys():
            if (abs(square[0] - j) == 2 and abs(square[1] - k) == 1) or (
                    abs(square[1] - k) == 2 and abs(square[0] - j) == 1):
                if (a_1[j] + str(k)) != square_0:
                    res.append(a_1[j] + str(k))
    return res


def king_moves(square: str) -> list:
    a_1 = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e', 6: 'f', 7: 'g', 8: 'h'}
    a_2 = {a_1[i]: i for i in a_1}
    square_0 = square
    res = []
    square = list(square)
    square = [a_2[square[0]], int(square[1])]
    for j in a_1.keys():
        for k in a_1.keys():
            if abs(square[0] - j) <= 1 and abs(square[1] - k) <= 1:
                if (a_1[j] + str(k)) != square_0:
                    res.append(a_1[j] + str(k))
    return res
