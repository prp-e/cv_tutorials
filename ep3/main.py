import cv2 

image = cv2.imread("ferrari.webp")

cv2.imshow("Original Image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()