#!/usr/bin/env python

# Бабушка Зина даёт своему любимому внуку Васе 3 монеты и разрешает оставить 2 из них.
# Найдите максимальную сумму из любых двух монет.
# Номинальная стоимость монет: a, b и с тугриков.

def max_sum_of_2(a: int, b: int, c: int) -> int:
    pass


if __name__ == "__main__":
    a = int(input("a = "))
    b = int(input("b = "))
    c = int(input("c = "))

if a >= b and b >= c:
    max_sum_of_2 = a + b
    print(max_sum_of_2)
elif a >= b and c >= b:
    max_sum_of_2 = a + c
    print(max_sum_of_2)
else:
    max_sum_of_2 = b + c
    print(max_sum_of_2)

