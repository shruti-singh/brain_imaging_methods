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
print("Frequency corresponding to unique pixel values: ", Counter(brain_image.ravel()))
