#Task 1 - Resolution, Histogram & Thresholding
#Task 1(c): Take a grayscale image of size 512x512, illustrate the Histogram of the image & make Single Threshold Segmentation observed from the histogram
#Importing the Libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt
#Function for generating Histogram
def generate_histogram(image):
    gray_levels_count = np.zeros(256)
    height, width = image.shape

    for r in range (width):
        for c in range(height):
            gray_levels_count[image[c, r]] += 1

    plt.bar(range(256), gray_levels_count, width = 1.0, color = "gray")
    plt.title("The Histogram of the Image")
    plt.show()
#Loading the Original Image
original_images = cv2.imread("./Skeleton 750x1482.tif", cv2.IMREAD_GRAYSCALE)
plt.imshow(cv2.cvtColor(original_images, cv2.COLOR_BGR2RGB))
plt.title("The Skull Image")
plt.show()