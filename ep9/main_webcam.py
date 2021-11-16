import cv2


camera = cv2.VideoCapture(1)

classifier = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

while camera.isOpened():
    _, frame = camera.read()
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = classifier.detectMultiScale(grey, 1.1, 4)

    for x, y, w, h in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 255), 4)
    
    cv2.imshow('Faces', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()