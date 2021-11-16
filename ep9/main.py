import cv2

image = cv2.imread('trump.jpg')
image_grey = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
faces = classifier.detectMultiScale(image_grey, 1.1, 4)

for x,y,w,h in faces:
    cv2.rectangle(image, (x,y), (x+w, y+h), (0, 255, 255), 4)

cv2.imshow('Original', image)
cv2.waitKey(0)