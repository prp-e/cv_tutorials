import cv2 
import cvzone 

image = cv2.imread("Lenna.png")
blue_image = image[:, :, 0]
green_image = image[:, :, 1]
red_image = image[:, :, 2]

image_list = [image, blue_image, green_image, red_image]
final_image = cvzone.stackImages(image_list, 2, 0.5)

print(image.shape) # (512, 512, 3)

cv2.imshow("Grid", final_image)
if cv2.waitKey(0) & 0xFF == ord('q'):
    cv2.destroyAllWindows()