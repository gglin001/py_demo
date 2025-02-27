from __future__ import annotations

import py_sample


def test_mul():
    x0, x1 = 2, 3
    y = py_sample.mul(x0, x1)
    z = x0 * x1
    assert y == z
