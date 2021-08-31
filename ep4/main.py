import cv2 
import numpy as np

image = np.zeros((720, 1080,3), np.uint8)

# Making the image white
for i in range(0,720):
    for j in range(0,1080):
        image[i,j] = (255,255,255)

# cv2.rectangle(image, start_point, end_point, color, thickness)

x, y = 100, 100
w, h = 150, 150 

cv2.rectangle(image, (x,y), (x + w, y + h), (255, 0, 0), 2)

x, y = 300, 100
w, h = 150, 150 

cv2.rectangle(image, (x,y), (x + w, y + h), (255, 0, 0), -1) # cv2.FILLED

# cv2.circle(image, center_coordinates, radius, color, thickness)

x , y = 600, 150
cv2.circle(image, (x, y), 25, (0, 0, 255), 2)

x , y = 600, 250
cv2.circle(image, (x, y), 25, (0, 0, 255), -1)

# cv2.line(image, start_point, end_point, color, thickness)

x, y = 100, 600
x2, y2 = 1000, 0

cv2.line(image, (x, y), (x2, y + 0), (0, 0, 0), 2)

# cv2.putText(image, text, org, font, fontScale, color, thickness)

x, y = 50, 50 
text = "Hello, World!"

cv2.putText(image, text, (x, y), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 0, 0), 1)

cv2.imshow('Canvas', image)
cv2.waitKey(0)