import cv2
import numpy as np
import time
print(cv2.__version__)

raw_video=cv2.VideoCapture("E:\Sruthi\Open CV\Lesson 7\video.mp4")

time.sleep(1)
count=0
background=None

for i in range(60):
    return_val,background=raw_video.read()
    if return_val == False:
        continue
    #
    
if background is None:
    print("Error")
    raw_video.release()
    exit()
background=np.flip(background,axis=1)

while(raw_video.isOpened()):
    return_val,img=raw_video.read()
    if not return_val:
        break
    count+=1
    img=np.flip(img,axis=1)

    hsv=cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

    
    lower_green = np.array([35, 40, 40])  # Lower bound for green in HSV
    upper_green = np.array([85, 255, 255]) 

    mask1=cv2.inRange(hsv,lower_green,upper_green)

    lower_green=([90,40,40])
    upper_green=([180,255,255])

    mask2=cv2.inRange(hsv,lower_green,upper_green)
    mask1=mask1+mask2

    mask1=cv2.morphologyEx(mask1,cv2.MORPH_OPEN,np.ones((3,3),np.unit8),iterations=1)
    mask2=cv2.bitwise_not(mask1)

    res1 = cv2.bitwise_and(background, background, mask = mask1)
    res2 = cv2.bitwise_and(img, img, mask = mask2)
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)

    cv2.imshow("INVISIBLE MAN", final_output)
    k = cv2.waitKey(10)
    if k == 27:
        break

raw_video.release()
cv2.destroyAllWindows()