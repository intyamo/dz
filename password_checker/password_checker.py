#!/usr/bin/env python

"""
Напишите функцию, которая проверяет "силу" пароля.

Надёжный пароль:
    - не менее 10 символов
    - содержит буквы разного регистра
    - минимум одну цифру
    - минимум один знак пунктуации

Вам могут пригодиться константы из модуля `string`:

- `string.ascii_letters`
- `string.digits`
- `string.punctuation`
"""


def is_strong_password(pwd: str) -> bool:
    import string
    n = len(pwd)
    b = 0
    c = 0
    c1 = 0
    d = 0
    e = string.digits
    f = string.ascii_uppercase
    f1 = string.ascii_lowercase
    g = string.punctuation
    for i in range(0, n):
        a = pwd[i]
        if e.count(a):
            b += 1
        elif f.count(a):
            c += 1
        elif f1.count(a):
            c1 += 1
        elif g.count(a):
            d += 1
    if b >= 1 and c >= 1 and c1 >= 1 and d >= 1 and n >= 10:
        is_strong_password = True
    else:
        is_strong_password = False
    return is_strong_password
