import os
#import tensorflow
import cv2
import numpy as np

img = cv2.imread("C:\Users\minyu\Desktop\24716648.jpg")
cv2.namedWindow("lena")
cv2.imshow("lena",img)

cv2.waitKey(0)
cv2.destroyAllWindows()