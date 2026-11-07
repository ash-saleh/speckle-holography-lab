from pathlib import Path

import numpy as np
from PIL import Image


def get_image_array(image_path: str | Path) -> np.ndarray:
    path = Path(image_path).resolve()

    with Image.open(path) as img:
        # gray_image = img.convert("L")
        image_arr = np.array(img).astype(float)
        return image_arr
