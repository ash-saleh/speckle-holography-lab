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
    """Average the Fourier magnitude over thin rings centred on zero frequency.

    Every point is assigned to a ring by its distance from the centre,
    r = sqrt(freq_x**2 + freq_y**2). Ring width is the larger of the two
    frequency spacings, so every ring contains at least one point.

    Args:
        magnitude: shifted Fourier magnitude, from fourier_magnitude.
        freq_x: column frequencies, from frequency_axes.
        freq_y: row frequencies, from frequency_axes.

    Returns:
        (distances, averages): the centre radius of each ring, in the same
        units as freq_x and freq_y, and the mean magnitude in that ring.
        Rings beyond 0.5 cycles per pixel are only partly filled (corners).
    """
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
    distances = (k_vals + 0.5) * spacing
    return (distances, averages)


def find_edge(
    distances: np.ndarray, averages: np.ndarray, r_max: float = 0.5, r_min: float = 0.01
) -> float:
    """Find the radius where the radial profile drops most steeply.

    Takes the log of the averages, differentiates with respect to distance,
    and returns the distance of the most negative slope within
    r_min < distance < r_max. This is the speckle cutoff frequency.

    Args:
        distances: ring radii, from radial_average.
        averages: mean magnitude per ring, from radial_average.
        r_max: upper limit of the search. The default assumes cycles per
            pixel; rings beyond 0.5 run into the corners.
        r_min: lower limit of the search. The default assumes cycles per
            pixel; rings near the centre hold few points and are noisy.

    Returns:
        The cutoff radius, in the same units as distances.
    """

    log_avg = np.log(averages)
    gradient = np.gradient(
        log_avg,
        distances,
    )
    in_range = (distances > r_min) & (distances < r_max)
    grad_in_range = gradient[in_range]
    dist_in_range = distances[in_range]
    steepest_drop = np.argmin(grad_in_range)
    return dist_in_range[steepest_drop]
