#Task 1 - Resolution, Histogram & Thresholding
#Task 1(a): Take a grayscale image of size 512x512, 
#decrease its spatial resolution by half every time 
#& observe it's change when displaying in the same window size

#Importing the Libraries
import cv2  # import OpenCV libary for image processing vision tasks 

import numpy as np  # import NumPy libary for effcient array manipulation and mathematical opearation 

import matplotlib.pyplot as plt # use the libary for creating and visualization the port

#Function for Decreasing Spatial Resolution by Half

def decrease_resolution(image): # take function dec_resolution  and input image 
    
    height, width = image.shape #retrives the height and width of input image 
    
    decreased_image = np.zeros((height // 2, width // 2)) #create new image half dimension of original image , other filled with zeros 

    for r in range(0, height, 2): #iterates the row of original image
        for c in range(0, width, 2): #iterates the column of original image 
            decreased_image[r // 2, c // 2] = image[r, c] #reducing the resolution of half
        
    return np.uint8(decreased_image) #returns the decreeased image as uint8 array

#Loading the Original Image

original_image = cv2.imread("./Rose 1024x1024.tif", cv2.IMREAD_GRAYSCALE) #read original image grayscale openCV function 

original_image = cv2.resize(original_image, (512, 512)) #resize image 512*512 pixel OpenCV function

#Decreasing the Spatial Resolution by Half
decreased_image = original_image.copy() # copy 512*512 image

plt.figure(figsize = (13, 13)) #specified size using Matplotlib 

for k in range (1, 5): #iterative four times 
    plt.subplot(2, 2, k) # create subplot for current iteration
    
    plt.imshow(decreased_image, cmap = 'gray') #display decrease grayscale image using image_function
    
    height, width = decreased_image.shape
    plt.title(f"{height}x{width}") #get dimension of decreased image 
    
    decreased_image = decrease_resolution(decreased_image) # call dec_resolution function for reduce the image for the next iteration 

plt.show() #display the final figure with all subplots 