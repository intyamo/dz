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
import string


def atbash_encode(text: str) -> str:
    text3 = text.lower()
    text4 = text3.replace('\n', '')
    text_l = text4.replace('\t', '')
    baza = string.ascii_lowercase
    baza1 = string.punctuation
    chislo_t = len(text_l)
    text1 = ''
    for i in range(0, chislo_t):
        simvol = text_l[i]
        if simvol.islower() == True:
            simvol_a = baza.find(simvol)
            baza_r = baza[::-1]
            text1 += baza_r[simvol_a]
        elif simvol == ' ' or baza1.count(simvol) >= 1:
            text1 += ''
        else:
            text1 += simvol

    textx = ' '.join([text1[j:j + 5] for j in range(0, len(text1), 5)])
    atbash_encode = textx
    return atbash_encode


def atbash_decode(cipher: str) -> str:
    chiper1 = cipher.replace(' ', '')
    baza = string.ascii_lowercase
    baza1 = string.punctuation
    chislo_z = len(chiper1)
    texty = ''
    for y in range(0, chislo_z):
        simvoly = chiper1[y]
        if simvoly.islower() == True:
            simvol_y = baza.find(simvoly)
            baza_r = baza[::-1]
            texty += baza_r[simvol_y]
        else:
            texty += simvoly
    atbash_decode = texty
    return atbash_decode

# cipher = input()
# z = atbash_decode(cipher)
# print(z)
