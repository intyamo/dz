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

import string

BLOCK_SIZE = 5
ABC = string.ascii_lowercase
CBA = ABC[::-1]
ABC1 = string.punctuation
def atbash_encode(text: str) -> str:
    text1 = text.lower()
    text2 = text1.replace('\t', '')
    text3 = text2.replace('\n', '')
    size = len(text3)
    encode = ''
    for i in range(0, size):
        char = text3[i]
        if char.isalpha():
            char1 = ABC.find(char)
            encode += CBA[char1]
        elif char == ' ' or ABC1.count(char) >= 1:
            encode += ''
        else:
            encode += char

    text4 = ' '.join([encode[n:n +5] for n in range(0, len(encode), BLOCK_SIZE)])
    return text4

def atbash_decode(cipher: str) -> str:
    chiper1 = cipher.replace(" ", "")
    size1 = len(chiper1)
    decode = ""
    for y in range(0, size1):
        char2 = chiper1[y]
        if char2.isalpha():
            char3 = ABC.find(char2)
            decode += CBA[char3]
        else:
            decode += char2
    return decode

