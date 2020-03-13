import numpy as np
import cv2
from matplotlib import pyplot as plt


# CasacdeClassifier Object Create
face_cascade = cv2.CascadeClassifier('../opencv/haarcascades/haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier("../opencv/haarcascades/haarcascade_eye.xml") # find eyes

img = cv2.imread('test2.jpg')
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # convert image color : RGB -> GRAY scale

# face scale alignment
# second argument number bigger, detect smaller face
faces = face_cascade.detectMultiScale(gray, 1.7, 3)

eye_detect = True

for (x,y,w,h) in faces:
	cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2) # (R,G,B) brightness
	roi_gray = gray[y:y+h, x:x+w]
	roi_color = img[y:y+h, x:x+w]
	if eye_detect:
		roi_gray = gray[y:y + h, x:x + w]
		roi_color = img[y:y + h, x:x + w]
		eyes = eye_cascade.detectMultiScale(roi_gray)
		for (ex, ey, ew, eh) in eyes:
			cv2.rectangle(roi_color, (ex, ey), (ex + ew, ey + eh), (0, 255, 0), 2)


cv2.imshow('img',img)
cv2.waitKey(0)
cv2.destroyAllWindows()



