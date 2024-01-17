#Task 1 - Resolution, Histogram & Thresholding
#Task 1(c): Take a grayscale image of size 512x512, illustrate the Histogram of the image & make Single Threshold Segmentation observed from the histogram

#Importing the Libraries

import cv2
import numpy as np
import matplotlib.pyplot as plt



#Function for generating Histogram

def generate_histogram(image):
    gray_levels_count = np.zeros(256) # Creates an array to store the count of each grayscale level (0-255), initially filled with zeros.
    
    height, width = image.shape

    for r in range (width):
        for c in range(height):
            gray_levels_count[image[c, r]] += 1 #Increments the count of the corresponding grayscale level in the gray_levels_count array.

    plt.bar(range(256), gray_levels_count, width = 1.0, color = "gray") #Creates a bar chart using Matplotlib, where the x-axis represents grayscale levels (0-255) and the y-axis represents the count of each level.
    
    plt.title("The Histogram of the Image")
    plt.show()
    
    
#Loading the Original Image

original_images = cv2.imread("./Skeleton 750x1482.tif", cv2.IMREAD_GRAYSCALE)

plt.imshow(cv2.cvtColor(original_images, cv2.COLOR_BGR2RGB))#Displays the image using Matplotlib, converting it to RGB format for visualization.

plt.title("The Skull Image")
plt.show()



# Showing the Histogram of the Original Image
generate_histogram(original_images)

# Making Single Threshold Segmentation observed from the Histogram
threshold_intensity = 27
segmented_image = np.where(original_images < threshold_intensity, 0, 255)
segmented_image = np.uint8(segmented_image)

plt.imshow(cv2.cvtColor(segmented_image, cv2.COLOR_BGR2RGB))
plt.title("Histogram of the Segmented Image")
plt.show()

# Showing the Histogram of the Segmented Image
generate_histogram(segmented_image)