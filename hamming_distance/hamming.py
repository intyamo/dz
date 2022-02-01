#!/usr/bin/env python

"""
Напишите программу, которая рассчитывает расстояние Хэмминга (Hamming distance) двух цепочек ДНК.

ДНК задаётся 4 нуклеотидами:

1. аденин - A
2. цитозин - C
3. гуанин - G
4. тимин - T

Расстояние Хэмминга оперделяет число отличающихся нуклеотидов, находящихся в одинаковой позиции:

strand_a = GAGCCTACTAACGGGAT
strand_b = CATCGTAATGACGGCCT
           ^ ^ ^  ^ ^    ^^

Расстояние Хэмминга для данных цепочек = 7.
"""


def hamming_distance(strand_a: str, strand_b: str) -> int:
    if len(strand_a) != len(strand_b):
        raise ValueError("Цепочки ДНК должны быть одинаковой длины")
    Hd = 0
    for i in range(len(strand_a)):
        if strand_a[i] != strand_b[i]:
            Hd += 1
    return Hd


strand_a = str(input('Введите первое ДНК - '))
strand_b = str(input('Введите второе ДНК - '))
print('Расстояние Хэмминга - ', hamming_distance(strand_a, strand_b))
