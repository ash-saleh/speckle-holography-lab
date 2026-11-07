import numpy as np
from PIL import Image

from speckle.image_io import load_gray

io_image = load_gray("data/test2.bmp")

with Image.open("data/test2.bmp") as img:
    pil_grayscale = img.convert("L")
    pil_array = np.array(pil_grayscale).astype(float)

print(io_image.shape)
print(pil_array.shape)

difference = np.abs(io_image - pil_array)

print(np.max(difference))
print(np.mean(difference))
