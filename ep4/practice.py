import cv2 
import numpy as np

image = np.zeros((720, 1080,3), np.uint8)

# Making the image white
for i in range(0,720):
    for j in range(0,1080):
        image[i,j] = (255,255,255)


cv2.imshow('Canvas', image)
cv2.waitKey(0)