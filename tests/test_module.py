from __future__ import annotations

import numpy as np
from py_demo.module import exp_func


def test_log_func():
    x = np.random.uniform(low=0, high=1, size=(2, 3))
    y = exp_func(x)
    z = np.exp(x)
    assert (y == z).all()
