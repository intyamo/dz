from golden_ratio import fib_phi_calc


def test_micro():
    assert fib_phi_calc(0.000_001) == (987, 1597)


def test_nano():
    assert fib_phi_calc(0.000_000_001) == (28657, 46368)


def test_pico():
    assert fib_phi_calc(10e-12) == (317811, 514229)


def test_femto():
    assert fib_phi_calc(10e-15) == (9227465, 14930352)
