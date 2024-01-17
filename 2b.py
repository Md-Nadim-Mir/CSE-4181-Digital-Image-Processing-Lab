#Task 2 - Enhancements with Point Processing
#Task 2(b): Take a grayscale image of size 512x512, differentiate the results of power law & inverse logarithmic transformation
#Importing the Libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt
#Function for Power Law Transformation
def power_law_transformation(image, gamma):
    transformed_image = image.copy()
    height, width = image.shape

    for r in range(height):
        for c in range(width):
            pixel = float(image[r, c]) / 255.0
            transformed_image[r, c] = (pixel ** gamma) * 255
    
    return np.uint8(transformed_image)
#Function for Inverse Logarithmic Transformation
def inverse_log_transformation(image):
    c = 255 / np.log(256)
    transformed_image = np.exp(image / c) - 1
    
    return np.uint8(transformed_image)
#Applying Power Law Transformation (γ < 0)
spine_image = cv2.imread("./Fractured Spine 746x976.tif", cv2.IMREAD_GRAYSCALE)
gammas, subplot_number = [1, 0.6, 0.4, 0.3], 1
plt.figure(figsize = (14, 17))

for gamma in (gammas):
    transformed_image = power_law_transformation(spine_image, gamma)
    plt.subplot(2, 2, subplot_number)
    plt.imshow(cv2.cvtColor(transformed_image, cv2.COLOR_BGR2RGB))
    plt.title(f"Power Law Transformation with γ = {gamma}")
    subplot_number += 1

plt.show()