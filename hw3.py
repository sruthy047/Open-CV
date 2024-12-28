import cv2

#Grayscaling of an image

image=cv2.imread("E:/Sruthi/Open CV/Lesson 3/2.jfif")
cv2.imshow("Original Image",image)
cv2.waitKey(0)

gray_image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Gray Scale Image",gray_image)
cv2.waitKey(0)

# Using averaging of pixels method to grayscale the image
# Without using the library to grayscale the image

img=cv2.imread("E:/Sruthi/Open CV/Lesson 3/2.jfif")
(row,col)=image.shape[0:2]
for i in range(row):
    for j in range(col):
        img[i,j]=sum(img[i,j])*0.33

cv2.imshow("GrayScale Image using averaging",img)
cv2.waitKey(0)

#Rotating an image

image=cv2.imread("E:/Sruthi/Open CV/Lesson 3/2.jfif")
(rows,cols)=image.shape[:2]

# getRotationMatrix2D creates a matrix needed for transformation.
# We want matrix for rotation w.r.t center to 45 degree without scaling.
M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 45, 1)
res = cv2.warpAffine(image, M, (cols, rows))

cv2.imwrite('result.jpg', res)
cv2.imshow("Rotated Image",res)
cv2.waitKey(0)


#Edge Detection

image=cv2.imread("E:/Sruthi/Open CV/Lesson 3/2.jfif")
#uisng Canny edge detection algorithm

edge=cv2.Canny(image,100,200)
cv2.imshow("Edge Detection",edge)
cv2.waitKey(0)

#Convert image from one color frame to other
#Convert image from RGB to HSV

image=cv2.imread("E:/Sruthi/Open CV/Lesson 3/2.jfif")
hsvImg=cv2.cvtColor(image,cv2.COLOR_BGR2HSV)
cv2.imshow("HSV Image",hsvImg)
cv2.waitKey(0)

cv2.destroyAllWindows()