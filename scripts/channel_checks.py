import matplotlib.pyplot as plt
import numpy as np

from speckle.image_io import get_image_array

pro_image = get_image_array("../data/test2.bmp")

print(pro_image.shape)

r_channel = pro_image[:, :, 0]
g_channel = pro_image[:, :, 1]
b_channel = pro_image[:, :, 2]

print(r_channel.shape)
print(g_channel.shape)
print(b_channel.shape)

print(np.array_equal(r_channel, g_channel))
print(np.array_equal(g_channel, b_channel))
print(np.array_equal(r_channel, b_channel))

print(np.mean(r_channel))
print(np.mean(g_channel))
print(np.mean(b_channel))

print(np.max(r_channel))
print(np.max(g_channel))
print(np.max(b_channel))

print(np.abs(r_channel - g_channel).mean())
print(np.abs(g_channel - b_channel).mean())
print(np.abs(r_channel - b_channel).mean())

# Channel Histograms
# matplotlib.use("Agg")
r_1d = r_channel.ravel()
g_1d = g_channel.ravel()
b_1d = b_channel.ravel()
bin_edges = np.linspace(-0.5, 255.5, 257).tolist()
channels_1d = [r_1d, g_1d, b_1d]
channel_names = ["R channel", "G channel", "B Channel"]

fig, axes = plt.subplots(3, 1, sharex=True)
for channel, name, ax in zip(channels_1d, channel_names, axes):
    ax.hist(channel, bins=bin_edges, log=True, histtype="step")
    ax.set_title(name)

fig.tight_layout()
# plt.savefig("./plots/channel_histograms.png")

difference = r_channel - g_channel
limit = np.abs(difference[400:500, 600:700]).max()
fig, axes = plt.subplots(1, 2)
axes[0].set_title("Difference")
axes[1].set_title("Red Channel")
image = axes[0].imshow(
    difference[400:500, 600:700],
    cmap="gray",
    interpolation="nearest",
    vmin=-limit,
    vmax=limit,
)
image2 = axes[1].imshow(
    r_channel[400:500, 600:700],
    cmap="gray",
    interpolation="nearest",
)
fig.colorbar(image, ax=axes[0])
fig.colorbar(image2, ax=axes[1])
plt.show()
