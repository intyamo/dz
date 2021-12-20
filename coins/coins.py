#!/usr/bin/env python

# Бабушка Зина даёт своему любимому внуку Васе 3 монеты и разрешает оставить 2 из них.
# Найдите максимальную сумму из любых двух монет.
# Номинальная стоимость монет: a, b и с тугриков.

def max_sum_of_2(a: int, b: int, c: int) -> int:
    ab = a+b
    ac = a+c
    bc = b+c
    if ab > ac and ab > bc:
        return ab
    else:
        if bc > ac:
            return bc
        else:
            return ac

if __name__ == "__main__":
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))

    print(max_sum_of_2(a, b, c))
