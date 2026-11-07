import numpy as np


def fourier_magnitude(image: np.ndarray) -> np.ndarray:
    """Takes a 2D image and returns the magnitude of its Fourier transform with zero frequency at the centre, the same shape as the input"""
    if image.ndim != 2:
        raise ValueError(f"expected a 2D array, got {image.shape}")
    image_minus_mean = image - np.mean(image)
    image_c_transform = np.fft.fft2(image_minus_mean)
    image_magnitude = np.abs(image_c_transform)
    return np.fft.fftshift(image_magnitude)


def frequency_axes(
    shape: tuple[int, int], pixel_pitch: float = 1.0
) -> tuple[np.ndarray, np.ndarray]:
    """Takes the shape of Fourier transformed and shifted image and returns frequency labels. freq_x for the columns, freq_y for the rows. Units of cycle per pixel by default; cycles per metre when pixel_pitch is given in metres. Returns (freq_x, freq_y)"""
    freq_x = np.fft.fftfreq(shape[1], d=pixel_pitch)
    freq_y = np.fft.fftfreq(shape[0], d=pixel_pitch)
    return np.fft.fftshift(freq_x), np.fft.fftshift(freq_y)


def radial_average(
    magnitude: np.ndarray, freq_x: np.ndarray, freq_y: np.ndarray
) -> tuple[np.ndarray, np.ndarray]:
    fx, fy = np.meshgrid(freq_x, freq_y)
    r = np.sqrt(fx**2 + fy**2)
    spacing_y = freq_y[1] - freq_y[0]
    spacing_x = freq_x[1] - freq_x[0]
    spacing = max(spacing_x, spacing_y)
    ring = np.floor(r / spacing).astype(int)
    sums = np.bincount(ring.ravel(), weights=magnitude.ravel())
    counts = np.bincount(ring.ravel())
    averages = sums / counts
    k_vals = np.arange(len(averages))
    radii = (k_vals + 0.5) * spacing
    return (radii, averages)
