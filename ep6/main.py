import cv2
import time 

camera = cv2.VideoCapture(1) # camera = cv2.VideoCapture("video.mp4")

ctime = time.time()

while camera.isOpened():
    _, frame = camera.read()
    frame = cv2.flip(frame, 1)

    frame_rate = camera.get(cv2.CAP_PROP_FPS)
    cv2.putText(frame, "FPS: %.2f" % frame_rate, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow('Web Cam', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

camera.release()
cv2.destroyAllWindows()