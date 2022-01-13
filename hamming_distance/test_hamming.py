from hamming import hamming_distance


def test_empty():
    assert hamming_distance("", "") == 0


def test_single():
    a = b = "A"
    assert hamming_distance(a, b) == 0


def test_long_identical_strands():
    a = b = "GGACTGAAATCTGACGT"
    assert hamming_distance(a, b) == 0


def test_long_strands_7():
    a = "GAGCCTACTAACGGGAT"
    b = "CATCGTAATGACGGCCT"

    assert hamming_distance(a, b) == 7


def test_long_strands_9():
    a = "GGACGGATTCTG"
    b = "AGGACGGATTCT"

    assert hamming_distance(a, b) == 9
