# Session notes: Tue 10 Nov 2026
Preliminary experiment: speckle size against spot diameter D. Images listed in `images.csv`, dark frames in `darks.csv`.

## Fixed for the whole session

- **Laser:** Thorlabs HNLS008R-EC HeNe, λ = 632.8 nm
- **Camera:** The Imaging Source DMK 42BUC03 (mono, Aptina MT9M021 sensor, 3.75 µm square pixels)
- **Pixel format:** Y800 (8-bit mono), [1280 × 960 — confirm]
- **Auto exposure / auto gain:** off; set by hand for each setting (values in `images.csv`)
- **White balance:** [auto / off]. No effect: mono camera, single channel.
- **Block-to-sensor distance L:** 190 ± [fill in] mm. Block and camera not moved all session.
- **Light-shielding tube:** fitted between block and camera

## Optics

laser → L1 (f = 20 mm) → ~120 mm → L2 (f = 200 mm) → mirror → iris → L3 (f = 100 mm) → sand-blasted Al block → bare camera

- L1–L2 spaced ~120 mm (not 220), so the beam diverges and overfills the iris. The iris edge defines the spot.
- Iris scale checked against calipers: reads correctly.
- Spot diameter D = iris setting × magnification.
- Lens and iris positions, measured from the block:

| m | lens → block | iris → block |
|---|---|---|
| 1 | 200 mm | 400 mm |
| 0.5 | 150 mm | 450 mm |
| 0.25 | 125 mm | 625 mm |

- Magnification and focus checked with graph paper in the iris holder at each lens position.

## Method

- At each setting: checked the iris clips the beam; set exposure and gain so the histogram max is below 255 with no pile-up at 0.
- 3 images per setting. Block slid ~10 mm sideways in its own plane between repeats (L unchanged), so each repeat lights a fresh patch of surface.
- Dark frames: beam blocked with a card (laser left on), tube on, room lighting unchanged. 3 frames for each gain/exposure combination used.

## Observations and problems

- **1 mm iris at m = 1 too dim to use.** Max ~20 counts with many pixels at 0 at long exposure; max ~75 even at maximum gain. Light through the iris scales with its area.
  - **Fix:** made the small spots by demagnifying a larger iris instead: iris 2 and 3 mm at m = 0.5, iris 3 and 4 mm at m = 0.25 (4–16× more light into the same spot size).
- **Gain and exposure varied between settings** to keep each image well exposed. This does not affect the measured edge: scaling an image by a constant c adds log c to the log profile, leaving its slope unchanged.
- **D = 1 mm measured by two routes** (iris 2 mm at m = 0.5; iris 4 mm at m = 0.25). Theory says only D matters, so both should give the same edge.
- Speckle at small D looks like large, soft blobs. Expected: there is no lens on the camera, and small D gives large speckle.

## Expected result

Predicted edge ≈ D/(λL) × pixel pitch = 0.031 × D cycles per pixel (D in mm), from 0.023 (D = 0.75 mm) to 0.25 (D = 8 mm).
