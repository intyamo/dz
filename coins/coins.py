#!/usr/bin/env python

# Бабушка Зина даёт своему любимому внуку Васе 3 монеты и разрешает оставить 2 из них.
# Найдите максимальную сумму из любых двух монет.
# Номинальная стоимость монет: a, b и с тугриков.
from unittest import result


def max_sum_of_2(a: int, b: int, c: int) -> int:
    sum = max(a+b, b+c, a+c)



    return sum


if __name__ == "__main__":
    a = int(input("a = "))
    b = int(input("a = "))
    c = int(input("a = "))




    print(max_sum_of_2(a, b, c))
