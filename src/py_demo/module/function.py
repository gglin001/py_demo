from __future__ import annotations

import numpy as np
import numpy.typing as npt


def exp_func(x: npt.NDArray) -> npt.NDArray:
    y = np.exp(x)
    return y
