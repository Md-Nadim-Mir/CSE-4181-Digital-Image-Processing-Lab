#Task 2 - Enhancements with Point Processing
#Task 2(c): Take a grayscale image of size 512x512, find the difference image between the original & the image obtained by last three MSBs
#Importing the Libraries

import cv2
import numpy as np
import matplotlib.pyplot as plt

#Loading the Original Image
dollar_image = cv2.imread("./Dollar 1192x500.tif", cv2.IMREAD_GRAYSCALE)
plt.imshow(cv2.cvtColor(dollar_image, cv2.COLOR_BGR2RGB))
plt.title("The 100 Dollar Image")
plt.show()


# Image obtained by Last 3-Bits (MSBs)

mask = "11100000"
three_bit_image = dollar_image & int(mask, 2)
plt.imshow(cv2.cvtColor(three_bit_image, cv2.COLOR_BGR2RGB))
plt.title("Image using Last 3-Bits")
plt.show()

# Finding the Difference Image

difference_image = cv2.absdiff(np.array(dollar_image), np.array(three_bit_image))
plt.imshow(cv2.cvtColor(difference_image, cv2.COLOR_BGR2RGB))
plt.title("The Difference Image")
plt.show()
