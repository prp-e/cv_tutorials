import cv2
import cvzone 

image = cv2.imread("ferrari.webp")
image = cv2.resize(image, (640, 480))

# 1. Art 
# 2. Simpler 
# 2.1. Training A.I is easier 
# 2.2. Training A.I is faster 
# 2.3. Finding details is faster and easier 
image_gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# 1. Standard in Photoshop, etc. 
# 2. OCR is easier. 
# 3. Transfer Learning made easier. 
image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)

# Hue, Saturation, Value
# Masking and color detection
image_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

stacked_images = cvzone.stackImages([image, image_gray, image_rgb, image_hsv], 2, 0.5)

cv2.imwrite("stacked_images.jpg", stacked_images)