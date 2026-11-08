# Speckle holography lab

Analysis code for experiment 2.4, Electronic Speckle Holography, in the Year 3 Laser Lab at the University of Birmingham.

## The experiment

**Part 1: characteristics of laser speckle.** A lens images a circular aperture onto a sand-blasted aluminium plate, giving an evenly lit disc of diameter *D*. A bare camera at distance *L* records the scattered light, which forms a speckle pattern. Theory predicts that the finest structure in the pattern has spatial frequency *D*/(λ*L*). So the width of the pattern's Fourier transform should be proportional to *D*. We vary *D* and test this prediction.

**Part 2: electronic speckle pattern interferometry.** Measure how far the diaphragm of a partly evacuated drum moves, by taking the difference between speckle images recorded before and after it flexes.

<!-- Expand each part as the work progresses. -->

The lab script suggests Matlab. This repository uses Python instead.

## Status

- [x] Load camera images and convert them to greyscale (`speckle.image_io`)
- [x] Check the camera's colour channels and intensity histograms
- [x] Fourier transform and frequency axes (`speckle.fourier`)
- [ ] Measure the Fourier-transform width for each spot diameter
- [ ] Plot the width against *D* and fit a line
- [ ] Analyse the electronic speckle pattern interferometry data (Part 2)
- [ ] Extension: real-time processing

## Setup

Requires [uv](https://docs.astral.sh/uv/).

```
git clone https://github.com/ash-saleh/speckle-holography-lab.git
cd speckle-holography-lab
uv sync
```

`uv sync` creates `.venv`, installs the exact package versions pinned in `uv.lock`, and installs the `speckle` package itself.

## Layout

```
src/speckle/   the package: reusable functions, imported by scripts and tests
scripts/       analysis and exploration scripts
tests/         checks that the package's functions give known answers
data/          camera images (not tracked by git)
plots/         generated figures (not tracked by git)
```

## Running

Run everything from the repository root, so that paths such as `data/...` resolve:

```
uv run scripts/<name>.py
uv run tests/<name>.py
```

### Modules

| Module | Contents |
|---|---|
| `speckle.image_io` | `load_image`, `to_gray`, `load_gray`: read a camera file and return a 2D float greyscale array |
| `speckle.fourier` | `fourier_magnitude`, `frequency_axes`, `radial_average`, `find_edge` : find magnitude of FT, label axes with frequency, average radially and find the edge of the speckle FT |

<!-- Add a row for each new module. -->

### Scripts

| Script | What it does |
|---|---|
| `channel_checks.py` | Compares the camera's three colour channels: equality, means, histograms and a difference image |
| `image_io_checks.py` | Checks `load_gray` against PIL's `convert("L")`; they agree to within rounding (maximum difference 0.5) |
| `fft_first_look.py` | checks `speckle.fourier` on generated sine data and then on actual image `test2.bmp` |
<!-- Add a row for each new script. -->

## Data

Images are not tracked by git, because they are large and never change. They are shared separately at: <!-- link to the shared folder -->

Each lab session gets its own folder, named by date:

```
data/
└── 2026-11-10/
    ├── images.csv
    ├── notes.md
    └── *.bmp
```

`images.csv` and `notes.md` are tracked by git; the images are not.

**`images.csv`** has one row per image:

| Column | Meaning |
|---|---|
| `filename` | image file in this folder |
| `repeat` | repeat number at the same settings |
| `iris_mm` | iris setting (mm) |
| `magnification` | magnification of the aperture image on the block |
| `aperture_to_lens_mm` | aperture-to-lens distance (mm) |
| `lens_to_block_mm` | lens-to-block distance (mm) |
| `spot_measured_mm` | spot diameter measured on the block (mm) |
| `exposure_ms` | camera exposure (ms) |
| `gain` | camera gain |
| `notes` | anything else; wrap in double quotes if it contains a comma |

**`notes.md`** records what stays the same for the whole session: camera model, pixel format, white balance, wavelength λ, block-to-camera distance *L*, and the dark-frame filename, plus free-text observations.

Records for each lab week are added on a branch named for that week (e.g. `week2`) and merged once checked.

## Camera notes

- The camera was set to save RGB images, though it is believed to be a mono model (DMK series). The three channels have equal means and identical histograms but differ pixel by pixel, by up to about 60 counts, mostly where the speckle is bright. `to_gray` combines them with the luma weights 0.299, 0.587 and 0.114, matching PIL's `convert("L")`. To do: switch the capture software to an 8-bit mono format (Y800 or Mono8).
- Images taken before the light-shielding tube was fitted have a background of about 40 counts.

<!-- Record camera model, pixel pitch and settings here once confirmed. -->

## Results

<!-- One line per key result: what was found, which script produced it, and the plot file. -->

## Conventions

- **Names:** `snake_case` for modules, functions and variables; `UPPER_CASE` for constants. SI units unless the name says otherwise (e.g. `distance_mm`).
- **Commits:** an imperative summary under about 50 characters ("Add frequency_axes"), a blank line, then why the change was made.
- **Decisions:** recorded in `decision-log.md`, with the date, what was chosen, why, and how it was checked.

## Collaborating

- Pull before starting work: `git pull`.
- Put each new piece of work on its own branch and open a pull request, so the other person can review it before it is merged.
- Commit small and often.
