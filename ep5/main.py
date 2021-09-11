import cv2
from zarnevis import Zarnevis

image = cv2.imread('azadisq.jpg')

processor = Zarnevis(image=image, text="میدان آزادی - شهر تهران", font_file='vazir.ttf', font_size=36, text_coords=(225,20), color=(255,0,0))
image = processor.draw_text()

cv2.imshow('image', image)
cv2.waitKey(0) 
