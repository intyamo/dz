from fizzbuzz import fizzbuzz


def test_1():
    assert fizzbuzz(1) == "1"


def test_3_5_15():
    assert fizzbuzz(3) == "Fizz"
    assert fizzbuzz(5) == "Buzz"
    assert fizzbuzz(15) == "FizzBuzz"


def test_3_5_15_multiplied():
    MULTIPLIER = 7
    assert fizzbuzz(3 * MULTIPLIER) == "Fizz"
    assert fizzbuzz(5 * MULTIPLIER) == "Buzz"
    assert fizzbuzz(15 * MULTIPLIER) == "FizzBuzz"
