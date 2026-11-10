import csv
from pathlib import Path

INT_COLUMNS = ("repeat", "gain")
FLOAT_COLUMNS = (
    "iris_mm",
    "magnification",
    "aperture_to_lens_mm",
    "lens_to_block_mm",
    "spot_measured_mm",
    "exposure_ms",
)


def read_images_csv(session_dir: str | Path) -> list[dict]:
    """Takes a directory with a images.csv file and returns a list of dictionaries with all values in the CSV. Numbers are converted to integers or floats depending on their type"""
    path = Path(session_dir) / "images.csv"

    records = []
    with path.open(newline="") as file:
        reader = csv.DictReader(file)
        for row in reader:
            for col in INT_COLUMNS:
                row[col] = int(row[col])
            for col in FLOAT_COLUMNS:
                row[col] = float(row[col])
            records.append(row)
    return records
