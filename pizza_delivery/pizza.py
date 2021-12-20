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
    all_flats = floors * 4
    return math.ceil(n / all_flats)


def find_floor(floors, n):
    """
    floors - число этажей в доме
    n - номер квартиры
    """
    entrance = math.ceil(n / (floors * 4))
    flats = floors * 4
    floor = (entrance - 1) * flats
    return math.ceil((n - floor) / 4)


if __name__ == "__main__":
    floors = int(input("Число этажей: "))
    flat_num = int(input("Номер квартиры: "))

    entrance = find_entrance(floors, flat_num)
    floor = find_floor(floors, flat_num)
    print(entrance, floor)
