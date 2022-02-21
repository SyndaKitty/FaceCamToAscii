import cv2
import sys

detector = cv2.CascadeClassifier('haarcascade_frontalface_alt2.xml')
img = cv2.imread('myface.jpg')
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
faces = detector.detectMultiScale(img_gray)

while True:
    cv2.imshow('img',img)
    for face in faces:
        (x,y,w,d) = face
        cv2.rectangle(img,(x,y),(x+w, y+d),(255, 255, 255), 2)
    key = cv2.waitKey(16)
    if key ==  ord('q'):
        break