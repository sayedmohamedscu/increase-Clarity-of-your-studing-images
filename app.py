import cv2
import numpy as np
x=cv2.imread('field lec. after mid-10.jpg')
img = cv2.cvtColor(x,cv2.COLOR_BGR2GRAY)

img[img < 235] = 0
img=255-img
kernel = np.ones((5,5),np.uint8)

ret,img = cv2.threshold(img,100,255,cv2.THRESH_BINARY)
ret,img1 = cv2.threshold(img,100,255,cv2.THRESH_BINARY_INV)

c =np.ones(x.shape)
c=c*255
c[:,:,1]=img1
c[:,:,2]=img1

cv2.imshow('x',c)

cv2.imwrite("1.jpg",c)
