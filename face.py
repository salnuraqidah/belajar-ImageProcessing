import cv2
import numpy as np
import sys

# Create the haar cascade
faceCascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")

img = cv2.imread("a (15).JPG")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

resized = cv2.resize(gray, (int(gray.shape[1]/2), 
	int(gray.shape[0]/2)))

faces = faceCascade.detectMultiScale(
	resized,
	scaleFactor=1.1,
	minNeighbors=5,
	minSize=(30, 30)
	)


# Draw a rectangle around the faces
for (x, y, w, h) in faces:
    cv2.rectangle(resized, (x, y), (x+w, y+h), (0, 255, 0), 2)

cv2.imshow("sal",resized)
cv2.waitKey(0)

cv2.destroyAllWindows()