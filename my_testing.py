GOLDEN = (1 + 5 ** 0.5) / 2


def fib_pair_gen():
    """
    Generator to produce Fibonacci numbers indefinitely.
    """
    fib1, fib2 = 0, 1
    for i in range(2):
        fib1, fib2 = fib2, fib1 + fib2
        yield fib1, fib2

a = (28657, 46368)
precision = 0.000_000_001
# def fib_phi_calc(precision: float, n) -> (int, int):
#     """
#     Returns 2 consecutive Fibonacci numbers to calculate Golden Ratio with a given precision.
#     """

