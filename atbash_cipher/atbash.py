#!/usr/bin/env python

"""
Напишите программу, которая кодирует и декодирует текст шифром Атбаш.
В этом шифре каждая i-ая буква алфавита заменяется i-ой буквой с его конца, например, для латинского алфавита: a - z, b - y и т.д.

- заглавные буквы переводятся в строчные
- пробельные символы и знаки препинания опускаются
- шифр идёт блоками по 5 символов, между ними пробел

Пример:

`Bambarbia, Kirgudu` -> `yznyz iyrzp ritfw f`
"""

BLOCK_SIZE = 5


alph = "abcdefghijklmnopqrstuvwxyz"
reverse_alph = "zyxwvutsrqponmlkjihgfedcba"


def atbash_encode(text: str) -> str:
    del_ = text.replace(' ', '').replace(',', '').replace('\n', '').replace('\t', '').replace('.', '').lower()
    a = str.maketrans(alph, reverse_alph)
    b = del_.translate(a)
    new_text = " ".join([b[i:i +5] for  i in range(0,len(b),5)])
    return new_text


def atbash_decode(cipher: str) -> str:
    a = str.maketrans(reverse_alph,alph)
    text = cipher.replace(' ', '').translate(a)
    return text
