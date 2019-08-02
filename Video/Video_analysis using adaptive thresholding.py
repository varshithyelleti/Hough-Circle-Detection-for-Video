
import numpy as np
import cv2 as cv
import xlsxwriter 

cam = cv.VideoCapture('Video path')

while(True):
    ret,img = cam.read() 
    
    if(ret!=True):
        break
    
    output=img.copy()
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
	
	
    gray = cv.GaussianBlur(gray,(5,5),0);
    gray = cv.medianBlur(gray,5)
	    gray = cv.adaptiveThreshold(gray,255,cv.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv.THRESH_BINARY,11,3.5)
	
    kernel = np.ones((3,3),np.uint8)
    gray = cv.erode(gray,kernel,iterations = 1)

    gray = cv.dilate(gray,kernel,iterations = 1)

    circles = cv.HoughCircles(gray, cv.HOUGH_GRADIENT, 1, 20, param1=73, param2=76, minRadius=0, maxRadius=0)

    if circles is None:
        continue
    
    circles = np.uint16(np.around(circles))

    for i in circles[0,:]:
        cv.circle(output,(i[0],i[1]),i[2],(0,255,0),2)
    frame = cv.resize(output, (900,500))
    cv.imshow('detected circles',frame)
    if (cv.waitKey(1) == ord('q')):
        break
    
    
cam.release()
cv.destroyAllWindows()
 
workbook.close()
