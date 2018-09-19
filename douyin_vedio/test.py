import cv2
import numpy as np

cap = cv2.VideoCapture(0)#打开摄像头
while(1):
    # get a frame
    ret, frame = cap.read()
    # show a frame
    cv2.imshow("capture", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'): #按q退出
        break
cap.release()
cv2.destroyAllWindows() 