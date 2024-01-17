#Task 2 - Enhancements with Point Processing
#Task 2(a): Take a grayscale image of size 512x512, perform the brightness enhancement of a specific range of gray levels & observe its result
#Importing the Libraries
import cv2
import numpy as np
import matplotlib.pyplot as plt
#Loading the Original Image
original_image = cv2.imread("./Fractured Spine 746x976.tif", cv2.IMREAD_GRAYSCALE)
plt.imshow(cv2.cvtColor(original_image, cv2.COLOR_BGR2RGB))
plt.title("The Original Image")
plt.show()