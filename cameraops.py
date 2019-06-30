#!/usr/bin/python3

import cv2
# starting camera

cap=cv2.VideoCapture(0) #0 for internal camera

# to check camera is started or not
if cap.isOpened():
    print("camera is ready to take pictures")
        
else:
    print("check your web cam drivers")


# now we can take read pictures
status,img=cap.read() # it will take first picture

#now showing
cv2.imshow('liveimage',img)
cv2.waitKey(0)

#to close
cap.release()


