import cv2

#videocapture module of cv2 to include video
cap=cv2.VideoCapture(0)

while cap.isOpened():
    status,frame=cap.read() #status and frames are reading
    #grayimg=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY) #converting image to gray
    #cv2.imshow('live.gray',grayimg)

    #now we can draw all shapes
    #line
    cv2.line(frame,(10,10),(200,250),(14,56,123),3)
    #rectangle
    cv2.rectangle(frame,(50,100),(245,295),(0,0,189),2)

        
    print(frame)

    cv2.imshow('live',frame)

    if cv2.waitKey(10) & 0xff == ord('p'): #ascii code of p to stop
        break

cv2.destroyAllWindows()

cap.release()
