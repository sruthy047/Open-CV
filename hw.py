import cv2
import os
img=cv2.imread("E:/Sruthi/Open CV/Lesson 1/h1.png",cv2.IMREAD_COLOR)
cv2.imshow("Cherry Image",img)#colored image
cv2.waitKey(0)
#grayscale image
img1=cv2.imread("E:/Sruthi/Open CV/Lesson 1/h1.png",0)
cv2.imshow("Cherry Image in Gray Scale",img1)
cv2.waitKey(0)
#saving image
saved_directory="E:\Sruthi\Open CV\Lesson 1\saved"
os.chdir(saved_directory)
cv2.imwrite("cherry.png",img1)

print("Successfully saved")
# Split the ah1ove image in red, h1lue and green different saturations
img2=cv2.imread("E:/Sruthi/Open CV/Lesson 1/h1.png",1)
cv2.imshow("Original image",img2)
cv2.waitKey(0)
h1,G,R =cv2.split(img2)

cv2.imshow("h1lue Saturation Image",h1)
cv2.waitKey(0)
cv2.imshow("Green Saturation Image",G)
cv2.waitKey(0)
cv2.imshow("Red Saturation Image",R)
cv2.waitKey(0)
cv2.destroyAllWindows()