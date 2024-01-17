#Task 1 - Resolution, Histogram & Thresholding
#Task 1(b): Take a grayscale image of size 512x512, decrease its intensity level resolution by one bit up to reach its binary format & observe its change when displaying in the same window size
#Importing the Libraries


import cv2
import numpy as np
import matplotlib.pyplot as plt

#Function for Decreasing Intensity Level Resolution by 1-Bit

def decrease_resolution(image, number_of_bits):
    
    step = 255 / (2**number_of_bits - 1)
    #Calculates the step size between intensity levels based on the number of bits.
    
    height, width = image.shape
    decreased_image = image.copy()
    
    

    for r in range(height): #Iterates over each row of the image.
        for c in range(width): #Iterates over each column of the image.
            decreased_image[r, c] = round(image[r, c] / step) * step #Rounds the pixel value to the nearest multiple of the step size, effectively reducing the number of possible intensity levels.
        
    return decreased_image


#Loading the Original Image
original_image = cv2.imread("./Skull 374x452.tif", 0)

#Decreasing Intensity Level Resolution by 1-Bit
decreased_image = original_image.copy()
plt.figure(figsize = (13, 8)) # Creates a figure for displaying multiple images.
 
for k in range(1, 9): # Iterates 8 times to create 8 images with different intensity resolutions.
    
    plt.subplot(2, 4, k) #Creates a subplot within the figure for the current iteration.
    
    number_of_bits = 9 - k #Sets the number of bits for the current image.
    
    decreased_image = decrease_resolution(decreased_image, number_of_bits) #Calls the decrease_resolution function to reduce the intensity resolution.
    
    plt.imshow(cv2.cvtColor(decreased_image, cv2.COLOR_BGR2RGB)) # Displays the image, converting it to RGB format for visualization.
    
    plt.title(f"{number_of_bits}-Bits Image") #Sets the title of the subplot to indicate the number of bits used.

plt.show() #Displays the final figure with all subplots.