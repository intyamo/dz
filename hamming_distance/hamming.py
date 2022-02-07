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
    res = [(x, y) for x, y in zip(strand_a, strand_b) if x != y]
    return len(res)

