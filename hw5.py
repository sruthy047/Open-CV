import cv2
import numpy as np

image=cv2.imread("E:/Sruthi/Open CV/Lesson 5/p.jfif",cv2.IMREAD_COLOR)
cv2.imshow("Original image",image)

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
gray_blurred=cv2.blur(gray,(3,3))
cv2.waitKey(0)

detected_circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, 1, 20, param1 = 50, param2 = 30, minRadius = 1, maxRadius = 40)
print(detected_circles)

if detected_circles is not None:
    detected_circles = np.uint16(np.around(detected_circles))
    for pt in detected_circles[0, :] :
        a, b, r = pt[0], pt[1], pt[2]
        cv2.circle(image, (a,b), r, (0, 255, 0), 2)
        cv2.circle(image, (a, b), 1, (0, 0, 255), 3)
        cv2.imshow("Detected Circles", image)
        cv2.waitKey(0)


'''# Give a basic overview of the SimpleBlobDetecter function, Why it is used and What are the parameters required.

# Set our filtering parameters Initialize parameter settiing using cv2.SimpleBlobDetector
image=cv2.imread("E:/Sruthi/Open CV/Lesson 5/p.jfif",cv2.IMREAD_COLOR)

params = cv2.SimpleBlobDetector_Params()

# Set Area filtering parameters
params.filterByArea = True
params.minArea = 100
# Set Circularity filtering parameters
params.filterByCircularity = True
params.minCircularity = 0.9
# Set Convexity filtering parameters
params.filterByConvexity = True
params.minConvexity = 0.2
# Set inertia filtering parameters
params.filterByInertia = True
params.minInertiaRatio = 0.01
# Create a detector with the parameters
detector = cv2.SimpleBlobDetector_create(params)
	
# Detect blobs
keypoints = detector.detect(image)

# Draw blobs on our image as red circles
blank = np.zeros((1, 1))
blobs = cv2.drawKeypoints(image, keypoints, blank, (0, 0, 255), cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

number_of_blobs = len(keypoints)
print(number_of_blobs)
text = "People: " + str(len(keypoints))
cv2.putText(blobs, text, (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 100, 255), 2)
cv2.imshow("nNumber",blobs)
cv2.waitKey(0)

# Show blobs
cv2.imshow("People", blobs)
cv2.waitKey(0)'''

cv2.destroyAllWindows()