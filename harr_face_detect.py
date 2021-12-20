import cv2 as cv
import matplotlib.pyplot as plt
img = cv.imread('group_1.jpg')
#cv.imshow('Group of 5 people', img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
#cv.imshow('Gray People', gray)

haar_cascade = cv.CascadeClassifier('harr_face.xml')

faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

print(f'Number of faces found = {len(faces_rect)}')

for (x,y,w,h) in faces_rect:
    cv.rectangle(img, (x,y), (x+w,y+h), (0,243,255), thickness=2)

cv.imshow('Detected Faces', img)

cv.waitKey(0)
