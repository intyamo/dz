from itertools import permutations

from coins import max_sum_of_2


def test_2_3_6():
    coins = [2, 3, 6]

    for perm in permutations(coins):
        assert max_sum_of_2(*perm) == 9


def test_3_2_2():
    coins = [3, 2, 2]

    for perm in permutations(coins):
        assert max_sum_of_2(*perm) == 5
