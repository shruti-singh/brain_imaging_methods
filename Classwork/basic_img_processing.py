### Basic Image processing codes ###

# import blocks for plotting and image processing
import matplotlib.pyplot as plt
from scipy import misc, ndimage

# face array
face = misc.face()

# using gaussian kernels for smoothing. 
blurred_face = ndimage.gaussian_filter(face, sigma=5)
very_blurred_face = ndimage.gaussian_filter(face, sigma=25)

# initialize a 2x2 subplot to plot the original face and the blurred face arrays
fig, ax = plt.subplots(2, 2, figsize=(10, 10))

# draw the original image first
ax[0, 0].imshow(face)
ax[0, 1].imshow(face[:,:,0])

# draw the blurred images on the corresponding subplots
ax[1, 0].imshow(blurred_face)
ax[1, 1].imshow(very_blurred_face)

# add labels to the subplots
ax[0, 0].set_xlabel("Original face iamge")
ax[0, 1].set_xlabel("Face image: First color channel")
ax[1, 0].set_xlabel("sigma = 5")
ax[1, 1].set_xlabel("sigma = 25")

# add title to the figure
fig.suptitle("Gaussian filtering to blur image")

# show the image
plt.show()

# save the figure
plt.savefig('plots/gaussian_filter_on_face.png')
