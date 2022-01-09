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



def atbash_encode(text: str) -> str:
    text1 = text.lower()
    text2 = text1.replace('\n', '')
    text3 = text2.replace('\t', '')
    aph = string.ascii_lowercase
    pun = string.punctuation
    num = len(text3)
    text1 = ''
    for i in range(0, num):
        simbol = text3[i]
        if simbol.islower() == True:
            simbol1 = aph.find(simbol)
            aph1 = aph[::-1]
            text1 += aph1[simbol1]
        elif simbol == ' ' or pun.count(simbol) >= 1:
            text1 += ''
        else:
            text1 += simbol

    text4 = ' '.join([text1[j:j + 5] for j in range(0, len(text1), 5)])
    atbash_encode = text4
    return atbash_encode


def atbash_decode(cipher: str) -> str:
    chiper1 = cipher.replace(' ', '')
    aph = string.ascii_lowercase
    num2 = len(chiper1)
    text5 = ''
    for y in range(0, num2):
        simbol = chiper1[y]
        if simbol.islower() == True:
            simbol1 = aph.find(simbol)
            aph1 = aph[::-1]
            text5 += aph1[simbol1]
        else:
            text5 += simbol
    atbash_decode = text5
    return atbash_decode
