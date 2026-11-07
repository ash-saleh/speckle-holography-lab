import numpy as np

from speckle.fourier import fourier_magnitude, frequency_axes

column_positions = np.arange(1280)

row = np.sin(2 * np.pi * column_positions / 20)

image = np.tile(row, (960, 1))

fourier_image = fourier_magnitude(image)

freq_x, freq_y = frequency_axes(fourier_image.shape)

peak = np.argmax(fourier_image)
peak_row, peak_column = np.unravel_index(peak, fourier_image.shape)

assert np.isclose(abs(freq_x[peak_column]), 0.05)
assert np.isclose(freq_y[peak_row], 0)
