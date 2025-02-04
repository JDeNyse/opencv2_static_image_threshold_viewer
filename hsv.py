#based on code from Aruldd on stackoverflow, converted for use on static images

import cv2
import numpy as np

#put file name here
cap = cv2.imread("img.jpg")

def nothing(x):
    pass
# Creating a window for later use
cv2.namedWindow('result')

# Starting with values to prevent error while masking
h,s,v = 100,100,100
h1,s1,v2 = 100,100,100

# Creating track bar
cv2.createTrackbar('h', 'result',0,179,nothing)
cv2.createTrackbar('s', 'result',0,255,nothing)
cv2.createTrackbar('v', 'result',0,255,nothing)
cv2.createTrackbar('h1', 'result',179,179,nothing)
cv2.createTrackbar('s1', 'result',255,255,nothing)
cv2.createTrackbar('v1', 'result',255,255,nothing)

while(1):

    frame = cap
    #converting to HSV
    hsv = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)

    # get info from track bar and appy to result
    h = cv2.getTrackbarPos('h','result')
    s = cv2.getTrackbarPos('s','result')
    v = cv2.getTrackbarPos('v','result')
    h1 = cv2.getTrackbarPos('h1','result')
    s1 = cv2.getTrackbarPos('s1','result')
    v1 = cv2.getTrackbarPos('v1','result')

    # Normal masking algorithm
    lower_color = np.array([h,s,v])
    upper_color = np.array([h1,s1,v1])

    mask = cv2.inRange(hsv,lower_color, upper_color)

    result = cv2.bitwise_and(frame,frame,mask = mask)

    cv2.imshow('result',result)

    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break

cap.release()

cv2.destroyAllWindows()
