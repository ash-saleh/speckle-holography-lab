import matplotlib.pyplot as plt
import numpy as np

from speckle.espi import difference_image
from speckle.image_io import load_gray

before = load_gray("data/2026-11-19/more/Baseline.bmp")
after = load_gray("data/2026-11-19/more/Tiny.bmp")

difference = difference_image(before, after)
vmax = np.percentile(difference, 99)

fig, axes = plt.subplots(1, 3)
image = axes[0].imshow(before, cmap="gray")
axes[0].set_title("Baseline")
image1 = axes[1].imshow(after, cmap="gray")
axes[1].set_title("Second image")
image2 = axes[2].imshow(difference, vmax=vmax, vmin=0, cmap="gray")
axes[2].set_title("Difference image (tiny rotation)")

after = load_gray("data/2026-11-19/more/BitMore.bmp")
difference = difference_image(before, after)
fig, axes = plt.subplots(1, 3)
image = axes[0].imshow(before, cmap="gray")
axes[0].set_title("Baseline")
image1 = axes[1].imshow(after, cmap="gray")
axes[1].set_title("Second image")
image2 = axes[2].imshow(difference, vmax=vmax, vmin=0, cmap="gray")
axes[2].set_title("Difference image after a tiny + a bit more")

after = load_gray("data/2026-11-19/more/BitMore2.bmp")
difference = difference_image(before, after)
fig, axes = plt.subplots(1, 3)
image = axes[0].imshow(before, cmap="gray")
axes[0].set_title("Baseline")
image1 = axes[1].imshow(after, cmap="gray")
axes[1].set_title("Second image")
image2 = axes[2].imshow(difference, vmax=vmax, vmin=0, cmap="gray")
axes[2].set_title("Difference image after tiny + bit more 2")

after = load_gray("data/2026-11-19/more/BitMore3.bmp")
difference = difference_image(before, after)
fig, axes = plt.subplots(1, 3)
image = axes[0].imshow(before, cmap="gray")
axes[0].set_title("Baseline")
image1 = axes[1].imshow(after, cmap="gray")
axes[1].set_title("Second image")
image2 = axes[2].imshow(difference, vmax=vmax, vmin=0, cmap="gray")
axes[2].set_title("Difference image after tiny + bit more 3")

after = load_gray("data/2026-11-19/more/BitMore4.bmp")
difference = difference_image(before, after)
fig, axes = plt.subplots(1, 3)
image = axes[0].imshow(before, cmap="gray")
axes[0].set_title("Baseline")
image1 = axes[1].imshow(after, cmap="gray")
axes[1].set_title("Second image")
image2 = axes[2].imshow(difference, vmax=vmax, vmin=0, cmap="gray")
axes[2].set_title("Difference image after tiny + bit more 4")
plt.show()
