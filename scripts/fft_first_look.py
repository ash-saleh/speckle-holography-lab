import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm

from speckle.fourier import (
    find_edge,
    fourier_magnitude,
    frequency_axes,
    power_spectrum,
    radial_average,
)
from speckle.image_io import load_gray

image = load_gray("data/test2.bmp")
image_ft = power_spectrum(image)
freq_x, freq_y = frequency_axes(image_ft.shape)
vmin = np.percentile(image_ft, 1)

fig, ax = plt.subplots()
im = ax.imshow(
    image_ft,
    extent=(freq_x[0], freq_x[-1], freq_y[0], freq_y[-1]),
    origin="lower",
    norm=LogNorm(vmin=vmin),
)
fig.colorbar(im, ax=ax)
ax.set_xlabel("cycles per pixel")
ax.set_ylabel("cycles per pixel")

horizontal_slice = image_ft[image_ft.shape[0] // 2]
vertical_slice = image_ft[:, image_ft.shape[1] // 2]

fig, ax = plt.subplots()
ax.semilogy(freq_x, horizontal_slice, marker="o", label="Horizontal Slice")
ax.semilogy(freq_y, vertical_slice, marker="s", linestyle="--", label="Vertical Slice")
ax.set_ylim(100)
ax.legend()

fig, ax = plt.subplots()
distances, averages = radial_average(image_ft, freq_x, freq_y)
ax.semilogy(distances, averages)
ax.set_xlabel("radial frequency (cycles per pixel)")
ax.set_ylabel("mean Fourier magnitude(arbitrary units)")
ax.axvline(x=0.065, label="x=0.065")
ax.set_xlim((0, 0.5))
ax.legend()

print(find_edge(distances, averages))

plt.show()
