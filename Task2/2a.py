#Task 2 - Enhancements with Point Processing
#Task 2(a): Take a grayscale image of size 512x512, perform the brightness enhancement of a specific range of gray levels & observe its result
#Importing the Libraries

import cv2
import numpy as np
import matplotlib.pyplot as plt

#Loading the Original Image
original_image = cv2.imread("./Fractured Spine 746x976.tif", cv2.IMREAD_GRAYSCALE)
plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB)) #Displays the image using Matplotlib, converting it to RGB format for visualization.
plt.title("The Original Image")
plt.show()



# Enhancing Brightness of a specific range of Gray Levels

range_start, range_end, add_brightness = 10, 50, 40
height, width = original_image.shape
image = original_image

for r in range(width):
    for c in range(height):
        if (image[c, r] >= range_start and image[c, r] <= range_end):
            image[c, r] += add_brightness
        image[c, r] = 255 if image[c, r] > 255 else image[c, r]

plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("The Enhanced Image") 
plt.show()