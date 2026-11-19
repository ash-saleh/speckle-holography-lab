import numpy as np
import matplotlib.pyplot as plt
import csv
from speckle.image_io import load_gray
from speckle.fourier import fourier_magnitude
from pathlib import Path

results = []
output_folder = Path(r"C:\Documents\Linear Speckle Results")
images = sorted(Path("data").rglob("iris*_m*_r*.bmp"))
print("Number of images found:",len(images))

for image_path in images[:3]:
    image = load_gray(image_path)

    magnitude = fourier_magnitude(image)
    power = magnitude**2

    middle = power.shape[0] // 2
    profile = np.zeros(power.shape[1])

    for row in range(middle - 5, middle + 6):
        profile += power[row]

    frequency = np.fft.fftshift(np.fft.fftfreq(power.shape[1]))

    x = frequency
    y = profile

    #y = y / np.max(y)

    # Choose the frequency range to fit on each side
    fit_start = 0.003
    fit_end = 0.008

    right = (x >= fit_start) & (x <= fit_end)
    left = (x >= -fit_end) & (x <= -fit_start)

    m_right, c_right = np.polyfit(x[right], y[right], 1)
    m_left, c_left = np.polyfit(x[left], y[left], 1)

    plot_name = image_path.parent.name + "_" + image_path.stem + ".png"

    plt.plot(x, y, label="Fourier power spectrum")

    plt.plot(x[left], m_left*x[left] + c_left, "r", linewidth=3, label="Left linear fit")

    plt.plot(x[right], m_right*x[right] + c_right, "g", linewidth=3, label="Right linear fit")

    plt.xlabel("Spatial frequency (cycles/pixel)")
    plt.ylabel("Fourier power")
    plt.xlim(-0.03,0.03)
    plt.legend()

    plt.savefig(output_folder/plot_name)
    plt.close()
    print("Processed:", image_path.name)

    results.append([image_path.name, m_left, c_left, m_right, c_right])

with open(output_folder/"linear_fit_data.csv","w",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Image","Left Gradient","Left Intercept","Right Gradient","Right Intercept"])
    writer.writerows(results)