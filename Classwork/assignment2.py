# Import statements
import matplotlib.pyplot as plt
from scipy import ndimage
import numpy as np
from collections import Counter

brain_image = plt.imread('Brain.jpg') 

# Initialize a 10x5 plot
fig = plt.figure(figsize=(10, 5))

# We use the first subplot in a 1x2 plot. The argument 121 stands for num_rows, num_cols, plot_index_in_use.
plt.subplot(121)
brain_image = plt.imread('Brain.jpg')
plt.imshow(brain_image)
plt.title('Original image')

# Using the second subplot.
plt.subplot(122)
plt.imshow(brain_image, cmap="Greys_r")
plt.title('Using Greys_r colormap')

fig.suptitle("Visualizing the brain image")

# Save the figure 
plt.savefig("./plots/a2/org_img_vis.png", dpi=500)

# Display on screen
plt.show()


print("Dimension/Shape of the image: ", brain_image.shape)
print("Pixel values: ")
print("Max pixel value {} by {} pixels.".format(np.max(brain_image), np.count_nonzero(brain_image==np.max(brain_image))))
print("Min pixel value {} by {} pixels.\n".format(np.min(brain_image), np.count_nonzero(brain_image==np.min(brain_image))))
# print("Frequency corresponding to unique pixel values: ", Counter(brain_image.ravel()))


# ========================================================================================================================
# Plot histogram of the original image
# ========================================================================================================================

# Initialize a 16x16 plot
fig = plt.figure(figsize=(16, 16))

# First subplot in the 2x1 figure
plt.subplot(121)
# Plotting the histogram with a separate bin for all intensity values from 0-255
plt.hist(brain_image.ravel(), bins=list(range(0, 256)))
plt.xlabel('Pixel Intensity bins')
plt.ylabel('Frequency')
plt.title("Histogram with 256 bins, one bin for each intensity value")

# Second subplot in the 2x1 figure
plt.subplot(122)
# Plotting the histogram with 16 bins to group together high and low intensity pixel values and visualize the frequencies better
freq, bins, patches = plt.hist(brain_image.ravel(), bins=16, edgecolor='black')
plt.xlabel('Pixel Intensity bins')
plt.ylabel('Frequency')
# Annotate the frequency of each bin
for fr, be, patch in zip(freq, bins, patches):
    plt.annotate("{}".format(int(fr)), xy=(be, int(fr)+1000)) 
plt.title("Histogram with 16 bins")

# Save the figure and display on screen
plt.savefig('./plots/a2/hist_org_brain.png', dpi=500)
plt.show()
