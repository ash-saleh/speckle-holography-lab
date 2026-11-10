from pathlib import Path

from speckle.fourier import measure_edge
from speckle.image_io import load_gray
from speckle.records import read_images_csv

image_data = read_images_csv("data/2026-11-10")
session_dir = Path("data/2026-11-10")

for row in image_data:
    grayscale_image_data = load_gray(session_dir / row["filename"])
    edge = measure_edge(grayscale_image_data)
    print(
        f"Filename: {row['filename']}, measured edge: {edge}, predicted edge: {row['spot_measured_mm'] * 0.031}"
    )
