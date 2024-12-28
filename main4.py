import cv2
image=cv2.imread("E:/Sruthi/Open CV/Lesson 4/3.jfif")
start_point=(0,0)
end_point=(250,250)
color=(0,255,0)
thickness=9

img=cv2.line(image,start_point,end_point,color,thickness)

cv2.imshow("Line",img)
cv2.waitKey(0)



#Draw rectangle
image=cv2.imread("E:/Sruthi/Open CV/Lesson 4/3.jfif")

start_point=(5,5)
end_point=(200,200)
color=(255,0,0)
thickness=5

img=cv2.rectangle(image,start_point,end_point,color,thickness)

cv2.imshow("Rectangle",img)
cv2.waitKey(0)


#Using thickness of -1px to fill the rectangle by black color

image=cv2.imread("E:/Sruthi/Open CV/Lesson 4/3.jfif")
start_point = (100,100)
end_point = (150,150)
color=(0,0,0)
thickness = -1

img=cv2.rectangle(image,start_point,end_point,color,thickness)
cv2.imshow("coloured",img)
cv2.waitKey(0)


#Circle

image=cv2.imread("E:/Sruthi/Open CV/Lesson 4/3.jfif")

center_cor = (150,150)
radius=15
color=(255,150,0)
thickness=2

img=cv2.circle(image,center_cor,radius,color,thickness)
cv2.imshow("Circle",img)
cv2.waitKey(0)

#Filled circle

#Circle

image=cv2.imread("E:/Sruthi/Open CV/Lesson 4/3.jfif")

center_cor = (150,150)
radius=15
color=(255,150,0)
thickness=-1

img=cv2.circle(image,center_cor,radius,color,thickness)
cv2.imshow(" Filled Circle",img)
cv2.waitKey(0)

#Draw some text on image

image=cv2.imread("E:/Sruthi/Open CV/Lesson 4/3.jfif")

font=cv2.FONT_HERSHEY_COMPLEX
org=(50,50)
fontScale=1
color=(120,200,50)
thickness=2
img=cv2.putText(image,"OpenCV",org,font,fontScale,color,thickness,cv2.LINE_AA)

cv2.imshow("Text on image",img)
cv2.waitKey(0)



cv2.destroyAllWindows()