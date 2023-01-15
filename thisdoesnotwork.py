import cv2 as cv
import numpy as np
cap= cv.VideoCapture(0)
while True:
    _,a= cap.read()
    
    
    
    
    img= cv.cvtColor(a, cv.COLOR_BGR2HSV)
    lower= np.array([0, 0, 0])
    upper = np.array([180, 255, 50])

    mask = cv.inRange(img,lower,upper)
    cv .imshow('wao',mask)




    edged= cv.Canny(mask,30,200)
    
    ret, thresh1 = cv.threshold(img, 50, 200, cv.THRESH_BINARY)
    contours, hiearchy = cv.findContours(thresh1,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
    img = cv .drawContours(thresh1, contours, -1, (0,255,255), 3)
    cv.imshow('mask',thresh1)
    cv.imshow('img',img)
    key = cv.waitKey(5)

	# if the 'q' key is pressed, stop the loop
    if key == ord("q"):
        break
