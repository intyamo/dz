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
    a = string.ascii_lowercase
    b = string.ascii_uppercase
    c = string.digits
    d = string.punctuation
    n = len(pwd)
    lc = 0
    uc = 0
    dc = 0
    pc = 0
    for i in range(0, n):
        f = pwd[i]
        if a.count(f) >= 1:
            lc += 1
        elif b.count(f) >= 1:
            uc += 1
        elif c.count(f) >= 1:
            dc += 1
        elif d.count(f) >= 1:
            pc += 1
    if lc >= 1 and uc >= 1 and dc >= 1 and pc >= 1 and n >= 10:
        pwd = True
    else:
        pwd = False
    return pwd
