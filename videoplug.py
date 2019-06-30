import cv2

#videocapture module of cv2 to include video
cap=cv2.VideoCapture(0)
#we need to add plugin
plugin=cv2.VideoWriter_fourcc(*'XVID')
# for saving video
output=cv2.VideoWriter('class.mp4',plugin,20,(640,480))

while cap.isOpened():
    status,frame=cap.read() #status and frames are reading
          
    print(frame)

    cv2.imshow('live',frame)
    output.write(frame)

    if cv2.waitKey(10) & 0xff == ord('p'): #ascii code of p to stop
        break

cv2.destroyAllWindows()

cap.release()
