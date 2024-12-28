import cv2
import numpy as np
#resizing image

img1=cv2.imread("E:/Sruthi/Open CV/Lesson 2/3.jfif",1)
cv2.imshow("Original Image1",img1)
cv2.waitKey(0)

r1=cv2.resize(img1,(500,250))
cv2.imshow("Resized image1",r1)
cv2.waitKey(0)

img2=cv2.imread("E:/Sruthi/Open CV/Lesson 2/4.jfif",1)
cv2.imshow("Original Image2",img2)
cv2.waitKey(0)

r2=cv2.resize(img2,(500,250))
cv2.imshow("Resized image2",r2)
cv2.waitKey(0)


# 0.5 and 0.4 are weights to be multiplied for each pixel, 0 is gamma_value (measurement of light)
weightedsum=cv2.addWeighted(r1,0.5,r2,0.4,0)
  
cv2.imshow('Weighted Image', weightedsum)

cv2.waitKey(0) 

#Subtraction

sub = cv2.subtract(r1, r2)
  
cv2.imshow('Subtracted Image', sub)
  
cv2.waitKey(0)

# Erosion of an image, corners are trimmed in erosion

# kernel is used for erosion as an input
kernel = np.ones((5, 5), np.uint8)

image = cv2.erode(img1, kernel) 
cv2.imshow("Eroded Image", image)

cv2.waitKey(0) 


#Blurring an image

cv2.imshow("Original image",img1)
cv2.waitKey(0)
Gaussian=cv2.GaussianBlur(img1,(7,7),0)
cv2.imshow('Gaussian Blurring',Gaussian)
cv2.waitKey(0)

#Median Blur - used in digital processing preserves edges but removes noise
median=cv2.medianBlur(img1,5)
cv2.imshow("Median Blurring",median)
cv2.waitKey(0)

#Bilateral Blur-only sharp edges are preserved here
bilateral=cv2.bilateralFilter(img1,9,75,75)
cv2.imshow("Bilateral Blurring",bilateral)
cv2.waitKey(0)

# Bordering an image
#cv2.copyMakeBorder(image, top, bottom, left, right, borderType, colorValue)
# SOLID Border around an image

borderedimage=cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_CONSTANT,value=1)
cv2.imshow("Bordered Image",borderedimage)
cv2.waitKey(0)

#Reflective border

borderedimage=cv2.copyMakeBorder(img1,10,10,10,10,cv2.BORDER_REFLECT,value=1)
cv2.imshow("Bordered Image",borderedimage)
cv2.waitKey(0)


cv2.destroyAllWindows()