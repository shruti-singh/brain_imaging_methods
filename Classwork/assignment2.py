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
plt.savefig("./plots/a2/org_img_vis.png", dpi=200)

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
fig = plt.figure(figsize=(12, 6))


# First subplot in the 2x1 figure
plt.subplot(121)

# Plotting the histogram with a separate bin for all intensity values from 0-255
plt.hist(brain_image.ravel(), bins=list(range(0, 256)))
plt.xlabel('Pixel Intensity bins')
plt.ylabel('Frequency')
plt.title("256 bins")


# Second subplot in the 2x1 figure
plt.subplot(122)

# Plotting the histogram with 16 bins to group together high and low intensity pixel values and visualize the frequencies better
freq, bins, patches = plt.hist(brain_image.ravel(), bins=16, edgecolor='black')
plt.xlabel('Pixel Intensity bins')
plt.ylabel('Frequency')

# Annotate the frequency of each bin in the plot
for _, (fr, be, patch) in enumerate(zip(freq, bins, patches)):
    # To fix overlapping of freq labels
    if _ % 2 == 0:
        plt.annotate("{}".format(int(fr)), xy=(be, int(fr)+3000), fontsize=8) 
    else:
        plt.annotate("{}".format(int(fr)), xy=(be, int(fr)+10000), fontsize=8) 

plt.title("16 bins")

# Add title to the figure
fig.suptitle("Histogram of the original brain image")

# Save the figure and display on screen
plt.savefig('./plots/a2/hist_org_brain.png', dpi=200)
plt.show()



# ========================================================================================================================
# Plot histogram of the smoothed images
# ========================================================================================================================

sigma_values = [5, 10, 20, 30, 40, 50]

for sigma in sigma_values:
    smoothed_image = ndimage.gaussian_filter(brain_image, sigma=sigma)

    # Initialize a 5x5 plot for the smoothed image
    fig = plt.figure(figsize=(3, 3))

    # Plot the gaussian filtered brain image
    plt.imshow(smoothed_image, cmap="Greys_r")
    plt.title(r"Smoothed image with $\sigma$ = {}".format(sigma))
    plt.savefig("./plots/a2/smoothed_img_sigma_{}.png".format(sigma), dpi=200)
    plt.show()


    # Initialize a 10x5 plot
    fig = plt.figure(figsize=(12, 6))

    # Plot the histogram with 256 bins
    plt.subplot(121)
    freq, bins, patches = plt.hist(smoothed_image.ravel(), bins=list(range(0, 256)))
    plt.xlabel('Pixel Intensity bins')
    plt.ylabel('Frequency')
    plt.title(r"$\sigma$ = {} with 256 bins".format(sigma))


    # Plot the histogram with 16 bins
    plt.subplot(122)
    freq, bins, patches = plt.hist(smoothed_image.ravel(), bins=16, edgecolor='black')
    plt.xlabel('Pixel Intensity bins')
    plt.ylabel('Frequency')

    # Annotate the frequency of each bin in the plot
    for _, (fr, be, patch) in enumerate(zip(freq, bins, patches)):
        # To fix overlapping of freq labels
        if _ % 2 == 0:
            plt.annotate("{}".format(int(fr)), xy=(be, int(fr)+3000), fontsize=8) 
        else:
            plt.annotate("{}".format(int(fr)), xy=(be, int(fr)+10000), fontsize=8) 

    plt.title(r"$\sigma$ = {} with 16 bins".format(sigma))


    # Title of the figure
    fig.suptitle(r"Histogram of the gaussian filtered image $\sigma$ = {}".format(sigma))

    # Save and display on screen
    plt.savefig("./plots/a2/hist_smoothed_sigma_{}.png".format(sigma), dpi=200)
    plt.show()


    # Print the max and min intensity pixel values
    print(r"Pixel values for smoothed image with $\sigma$ = ", sigma)
    print("Max pixel value {} by {} pixels.".format(np.max(smoothed_image), np.count_nonzero(smoothed_image==np.max(smoothed_image))))
    print("Min pixel value {} by {} pixels.\n".format(np.min(smoothed_image), np.count_nonzero(smoothed_image==np.min(smoothed_image))))



# ========================================================================================================================
# Obtain edges and sharp features in the image
# ========================================================================================================================

plt.clf()
smoothed_image = ndimage.gaussian_filter(brain_image, sigma=5)
fig = plt.figure(figsize=(3, 3))
plt.imshow(np.subtract(brain_image, smoothed_image), cmap="Greys_r")
plt.savefig("./plots/a2/sharp_features_5.png")

smoothed_image = ndimage.gaussian_filter(brain_image, sigma=50)
fig = plt.figure(figsize=(3, 3))
plt.imshow(np.subtract(brain_image, smoothed_image), cmap="Greys_r")
plt.savefig("./plots/a2/sharp_features_50.png")