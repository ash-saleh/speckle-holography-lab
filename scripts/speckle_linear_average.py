import numpy as np
import matplotlib.pyplot as plt
import csv
from speckle.image_io import load_gray
from speckle.fourier import fourier_magnitude
from pathlib import Path

total_profile = 0
output_folder = Path(r"C:\Documents\Linear Speckle Results")
repeat_images = sorted(Path("data/10-11-2026").glob("iris2_m05_r*.bmp"))
print("Number of repeats found:",len(repeat_images))

for image_path in repeat_images:
    image = load_gray(image_path)

    magnitude = fourier_magnitude(image)
    power = magnitude**2

    middle = power.shape[0] // 2
    profile = np.zeros(power.shape[1])

    for row in range(middle - 5, middle + 6):
        profile += power[row]

    profile = profile/11
    total_profile += profile

average_profile = total_profile/len(repeat_images)

frequency = np.fft.fftshift(np.fft.fftfreq(len(average_profile)))

x = frequency
y = average_profile

fit_start = 0.003
fit_end = 0.008

right = (x >= fit_start) & (x <= fit_end)
left = (x >= -fit_end) & (x <= -fit_start)

m_right, c_right = np.polyfit(x[right], y[right], 1)
m_left, c_left = np.polyfit(x[left], y[left], 1)

left_edge = -c_left/m_left
right_edge = -c_right/m_right
width = right_edge-left_edge

print(f"Left extrapolated edge: {left_edge:.6f} cycles/pixel")
print(f"Right extrapolated edge: {right_edge:.6f} cycles/pixel")
print(f"Total extrapolated width {width:.6f} cycles/pixel")

plt.plot(x,y,label="Average Fourier Power Spectrum")

plt.plot(x[left], m_left*x[left] + c_left, "r", linewidth=3, label="Left linear fit")

plt.plot(x[right], m_right*x[right] + c_right, "g", linewidth=3, label="Right linear fit")

plt.plot([left_edge,-fit_end],[0,m_left*(-fit_end)+c_left],"r--")
plt.plot([fit_end,right_edge],[m_right*fit_end+c_right,0],"g--")
plt.scatter([left_edge,right_edge],[0,0],color="black")

plt.xlabel("Spatial Frequency (cycles/pixel)")
plt.ylabel("Average Fourier Power")
plt.title("iris2_m05 - Average of repeats")
plt.xlim(-0.03,0.03)
plt.legend()

plt.savefig(output_folder/"iris2_m05_average.png")
plt.close()