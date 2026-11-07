from pathlib import Path

import numpy as np
from PIL import Image

LUMA_WEIGHTS = np.array([0.299, 0.587, 0.114])


def load_image(image_path: str | Path) -> np.ndarray:
    """Reads file and returns its pixels as float array, unchanged in every other way. Returns 2D for a mono file, 3D for an RGB one."""
    path = Path(image_path).resolve()

    with Image.open(path) as img:
        image_arr = np.array(img).astype(float)
        return image_arr


def to_gray(image: np.ndarray) -> np.ndarray:
    """Takes an array from load_image and returns it if already grayscale or converts it to grayscale if RGB. Raises ValueError otherwise."""
    if image.ndim == 2:
        return image
    if image.ndim == 3 and image.shape[-1] == 3:
        return image @ LUMA_WEIGHTS
    raise ValueError(
        f"expected a 2D gray image or a 3D image with 3 channels, got shape {image.shape}"
    )


def load_gray(path: str | Path) -> np.ndarray:
    """A convenience function that takes an image file and calls both processing functions at once to return a grayscale image"""
    raw = load_image(path)
    gray_scale = to_gray(raw)
    return gray_scale
