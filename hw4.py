import cv2

image=cv2.imread("E:/Sruthi/Open CV/Lesson 4/3.jfif")

color=(255,0,0)
thickness=2

img=cv2.line(image,(100,50),(150,0),color,thickness)
img=cv2.line(image,(150,0),(200,50),color,thickness)
img=cv2.line(image,(100,50),(200,50),color,thickness)
img=cv2.rectangle(image,(100,50),(200,100),color,thickness)
cv2.imshow("Image",img)
cv2.waitKey(0)
cv2.destroyAllWindows(0)
