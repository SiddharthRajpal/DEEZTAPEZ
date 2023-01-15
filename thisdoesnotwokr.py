import cv2 as cv
import numpy as np
cap= cv.VideoCapture(0)
while True:
    _,a= cap.read()
    
    
    
    
    img= cv.cvtColor(a, cv.COLOR_BGR2HSV)
    lower= np.array([0, 0, 0])
    upper = np.array([180, 255, 50])

    mask = cv.inRange(img,lower,upper)
    




    edged= cv.Canny(mask,30,200)
    
    ret, thresh1 = cv.threshold(img, 50, 500, cv.THRESH_BINARY)
    thresh1 = cv.cvtColor(thresh1, cv.COLOR_RGB2GRAY)
    contours, hiearchy = cv.findContours(thresh1,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
    def get_contour_areas(contours):

        all_areas= []

        for cnt in contours:
            area= cv.contourArea(cnt)
            all_areas.append(area)

        return all_areas


    sorted_contours= sorted(contours, key=cv.contourArea, reverse= True)
    cv .imshow('wao',mask)

    largest_item= sorted_contours[0]

    img = cv .drawContours(mask, largest_item, -1, (0,255,255), 3)
    
    cv.imshow('mask',thresh1)
    cv.imshow('img',img)
    key = cv.waitKey(5)

	# if the 'q' key is pressed, stop the loop
    if key == ord("q"):
        break
