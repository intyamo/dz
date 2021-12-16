from pizza import find_entrance, find_floor, FLATS_PER_FLOOR

FLOORS = 5  # этажей


def test_first_flat():
    n = 1

    assert find_entrance(FLOORS, n) == 1
    assert find_floor(FLOORS, n) == 1


def test_first_entrance_middle_1():
    n = 13

    assert find_entrance(FLOORS, n) == 1
    assert find_floor(FLOORS, n) == 4


def test_first_entrance_middle_2():
    n = 16

    assert find_entrance(FLOORS, n) == 1
    assert find_floor(FLOORS, n) == 4


def test_first_entrance_last_flat():
    n = FLOORS * FLATS_PER_FLOOR

    assert find_entrance(FLOORS, n) == 1
    assert find_floor(FLOORS, n) == 5


def test_first_flat_of_entrance():
    # первая квартира 2 подъезда
    n = FLOORS * FLATS_PER_FLOOR + 1

    assert find_entrance(FLOORS, n) == 2
    assert find_floor(FLOORS, n) == 1


def test_somewhere_in_the_middle():
    # 2 подъезд, 2 этаж
    n = 25

    assert find_entrance(FLOORS, n) == 2
    assert find_floor(FLOORS, n) == 2


def test_last_flat_of_entrance():
    # последняя квартира 2 подъезда
    n = 2 * FLOORS * FLATS_PER_FLOOR

    assert find_entrance(FLOORS, n) == 2
    assert find_floor(FLOORS, n) == FLOORS
