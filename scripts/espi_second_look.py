import matplotlib.pyplot as plt
import numpy as np

from speckle.espi import difference_image
from speckle.image_io import load_gray

before = load_gray("data/2026-11-24/s1_baseline_a.bmp")
after = load_gray("data/2026-11-24/s1_baseline_b.bmp")

difference = difference_image(before, after)
vmax = np.percentile(difference, 99)
print("The ratio of the means is ", difference.mean() / before.mean())

fig, axes = plt.subplots(1, 3)
image = axes[0].imshow(before, cmap="gray")
axes[0].set_title("Baseline")
image1 = axes[1].imshow(after, cmap="gray")
axes[1].set_title("Second Baseline image")
image2 = axes[2].imshow(difference, vmax=vmax, vmin=0, cmap="gray")
axes[2].set_title("Difference image (baselines)")

after = load_gray("data/2026-11-24/s1_05.bmp")
difference = difference_image(before, after)
vmax = np.percentile(difference, 99)
fig, axes = plt.subplots(1, 3)
image = axes[0].imshow(before, cmap="gray")
axes[0].set_title("Baseline")
image1 = axes[1].imshow(after, cmap="gray")
axes[1].set_title("Second image")
image2 = axes[2].imshow(difference, vmax=vmax, vmin=0, cmap="gray")
axes[2].set_title("Difference image 5mm rotation")


after = load_gray("data/2026-11-24/s1_10.bmp")
difference = difference_image(before, after)
vmax = np.percentile(difference, 99)
fig, axes = plt.subplots(1, 3)
image = axes[0].imshow(before, cmap="gray")
axes[0].set_title("Baseline")
image1 = axes[1].imshow(after, cmap="gray")
axes[1].set_title("Second image")
image2 = axes[2].imshow(difference, vmax=vmax, vmin=0, cmap="gray")
axes[2].set_title("Difference image 10mm rotation")

after = load_gray("data/2026-11-24/s1_15.bmp")
difference = difference_image(before, after)
vmax = np.percentile(difference, 99)
fig, axes = plt.subplots(1, 3)
image = axes[0].imshow(before, cmap="gray")
axes[0].set_title("Baseline")
image1 = axes[1].imshow(after, cmap="gray")
axes[1].set_title("Second image")
image2 = axes[2].imshow(difference, vmax=vmax, vmin=0, cmap="gray")
axes[2].set_title("Difference image 15mm rotation")


after = load_gray("data/2026-11-24/s1_25.bmp")
difference = difference_image(before, after)
vmax = np.percentile(difference, 99)
fig, axes = plt.subplots(1, 3)
image = axes[0].imshow(before, cmap="gray")
axes[0].set_title("Baseline")
image1 = axes[1].imshow(after, cmap="gray")
axes[1].set_title("Second image")
image2 = axes[2].imshow(difference, vmax=vmax, vmin=0, cmap="gray")
axes[2].set_title("Difference image 25mm rotation")

plt.show()
