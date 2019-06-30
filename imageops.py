
#!/usr/bin/python3
import cv2
import sys

#version
#print(cv2._version_)

data=input("enter image name")

img=cv2.imread(data)
print(img)

print(img.shape)



cv2.imshow('windowname',img)


#saving image
cv2.imwrite('newdog.jpg',img)
cv2.waitKey(0)

