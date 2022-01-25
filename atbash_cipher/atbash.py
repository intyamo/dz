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
alf = 'abcdefghijklmnopqrstuvwxyz'
alf_rev = 'zyxwvutsrqponmlkjihgfedcba'


def atbash_encode(text: str) -> str:
    ttab = str.maketrans(alf, alf_rev)
    text = str(text.replace('.', '').replace('\n', '').replace('\t', '').replace(',', '').replace(' ', '').lower()
                     .translate(ttab)
                     )
    ready_text = ' '.join([text[i:i+5] for i in range(0, len(text), 5)])
    print(ready_text)
    return ready_text


def atbash_decode(cipher: str) -> str:
    ttab = str.maketrans(alf_rev, alf)
    text = cipher.replace(' ', '').translate(ttab)

    return text



