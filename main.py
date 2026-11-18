from matplotlib import image
import numpy as np
import matplotlib.pyplot as plt
import tifffile as tf
import math

# SETUP BEGIN ==============================================================================

# Input
dataFilePath = "exampleData/data.tiff"
frameTime = 1/60 # Frame duration in seconds
rotationStartTime = 1 # Global time in seconds where the polarizer rotation begins
rotationEndTime = 5 # Global time in seconds where the polarizer rotation ends
rotationRange = 2 * math.pi # Total range rotated over


# Other
colorMap = "viridis" # gray also works
logLevel = 3 # 0 - none, 1 - errors, 2 - warnings, 3 - logs

# SETUP END =====================================================================================

def log(msg):
    if logLevel >= 3:
        print(f'[LOG] {msg}')

def warn(msg):
    if logLevel >= 2:
        print(f'[WARNING] {msg}')

def error(msg):
    if logLevel >= 1:
        print(f'[ERROR] {msg}')

image_data = tf.imread(dataFilePath)
log(f'Image Shape: {image_data.shape}')

log("Slicing image into frames")

images = []
for frame in range(image_data.shape[2]):
    images.append(image_data[:, :, frame])

log(f'{len(images)} frames')





plt.imshow(images[1], cmap=colorMap)
plt.show()
