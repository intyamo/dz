#!/usr/bin/env python

# В. Пупкин развозит пиццу. Ему сообщают адрес доствки в виде
# <улица> <номер дома>-<номер квартиры>
#
# Приезжая по указанному адресу, Вася видит здание с числом этажей `floors`.
# Для простоты будем считать, что на каждом этаже в подъезде находятся 4 квартиры.
#
# Помогите Васе посчитать, в каком подъезде и на каком этаже находится нужная квартира n.
#
# Для решения понадобится использовать деление по модулю %
# или целочисленное деление //.
import math

FLATS_PER_FLOOR = 4




def find_entrance(floors, n):
    """
    floors - число этажей в доме
    n - номер квартиры
    """
    a = 4 * floors  # получим число кв в одном под
    math.ceil(n / a)  # получим подъезд
    return math.ceil(n / a)  # получим подъезд


def find_floor(floors, n):
    entrance = math.ceil(n / (floors*4)) # падик
    flats = floors * 4 # число кв в подъезде
    floor = (entrance-1) * flats # предыдущий падик

    """
    floors - число этажей в доме
    n - номер квартиры
    """


    return math.ceil((n-floor)/4)


if __name__ == "__main__":
    floors = int(input("Число этажей: "))
    flat_num = int(input("Номер квартиры: "))

    entrance = find_entrance(floors, flat_num)
    floor = find_floor(floors, flat_num)
    print(entrance, floor)
