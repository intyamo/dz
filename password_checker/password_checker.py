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
import string
STRONG_PWD = "даLadno?$123.4"
symbols_ru = 'йцукеёнгшщзхъфывапролджэячсмитьбю'
def is_strong_password(pwd: str) -> bool:
    n = 0
    n_digits = 0
    n_punctuation = 0
    n_upper = 0
    n_lower = 0
    n_ru = 0
    if len(pwd) >= 10:
        for i in pwd:
            if pwd[n] in string.ascii_lowercase:
                n += 1
                n_lower = 1
            elif pwd[n] in string.ascii_uppercase:
                n += 1
                n_upper = 1
            elif pwd[n] in string.digits:
                n += 1
                n_digits = 1
            elif pwd[n] in string.punctuation:
                n += 1
                n_punctuation = 1
            elif pwd[n] in symbols_ru:
                n += 1
                n_ru = 1
    else:
        return False

    if n_ru == 1 and n_lower == 1 and n_upper == 1 and n_digits == 1 and n_punctuation == 1:
        return True


print(is_strong_password(STRONG_PWD))
