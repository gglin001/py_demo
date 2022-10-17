import sample


def test_mul():
    x0, x1 = 2, 3
    y = sample.mul(x0, x1)
    z = x0 * x1
    assert y == z
