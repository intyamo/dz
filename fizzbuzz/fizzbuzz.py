#!/usr/bin/env python

"""
Напишите функцию, которая возвращает для чисел:

- кратных 3 - Fizz
- кратных 5 - Buzz
- одновременно кратных и 3 и 5 - FizzBuzz
- строковое представление этих чисел (т.е. "1" для 1)

https://en.wikipedia.org/wiki/Fizz_buzz
"""


def fizzbuzz(n: int) -> str:
    if int(n) % 3 == 0 and int(n) % 5 != 0:
        return 'Fizz'
    elif int(n) % 5 == 0 and int(n) % 3 != 0:
        return 'Buzz'
    elif int(n) % 5 == 0 and int(n) % 3 == 0:
        return 'FizzBuzz'
    else:
        return 'Ни то ни сё'


n = input('Введите число - ')
print('Число ', str(n), ' - ', fizzbuzz(int(n)))
