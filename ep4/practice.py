import cv2 
import numpy as np

image = np.zeros((720, 1080,3), np.uint8)

# Making the image white
for i in range(0,720):
    for j in range(0,1080):
        image[i,j] = (255,255,255)

x, y = 270, 140
w, h = 400, 400 

cv2.rectangle(image, (x,y), (x+w, y+h), (200,155,0), 2)
cv2.circle(image, (x, y), 20, (0,0,255), -1)
cv2.circle(image, (x + w, y + h), 20, (0,0,255), -1)
cv2.line(image, (x, y), (x + w, y + h), (0, 0, 0), 2)

cv2.imshow('Canvas', image)
cv2.waitKey(0)