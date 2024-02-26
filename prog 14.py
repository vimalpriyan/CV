import cv2
import numpy as np
img=cv2.imread("C:/Users/farid/OneDrive/Pictures/dogyy.png")
p1=np.float32([[141,131],[480,159],[493,690],[64,601]])
p2=np.float32([[318,256],[534,372],[316,670],[73,473]])
h,_=cv2.findHomography(p1,p2)
img2=cv2.warpPerspective(img,h,(600,600))
cv2.imshow("original",img)
cv2.imshow("homography",img2)
