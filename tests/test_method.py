from __future__ import annotations

import numpy as np
import py_sample


def test_log_func():
    x = np.random.uniform(low=0, high=1, size=(2, 3))
    y = py_sample.log_func(x)
    z = np.log(x)
    assert (y == z).all()
