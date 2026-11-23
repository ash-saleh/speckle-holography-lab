import numpy as np


def difference_image(before, after) -> np.ndarray:
    after = np.asarray(after, dtype=float)
    before = np.asarray(before, dtype=float)
    if before.ndim != 2:
        raise ValueError(f"expected a 2D array, got {before.shape}")
    if after.ndim != 2:
        raise ValueError(f"expected a 2D array, got {before.shape}")
    return np.abs(after - before)
