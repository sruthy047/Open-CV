import cv2
import numpy as np
import time

print(cv2.__version__)

# Open the video file
raw_video = cv2.VideoCapture("E:\\Sruthi\\Open CV\\Lesson 7\\video.mp4")

time.sleep(1)
count = 0
background = None  # Initialize to None

# Capture the background (assume the video loads successfully)
for i in range(60):
    return_val, frame = raw_video.read()
    if not return_val:
        print(f"Frame {i} could not be read, skipping.")
        continue
    background = frame

# Check if the background was successfully captured
if background is None:
    print("Error: Unable to read any frame from the video.")
    raw_video.release()
    exit()

# Flip the background
background = np.flip(background, axis=1)

# Process video frames
while raw_video.isOpened():
    return_val, img = raw_video.read()
    if not return_val:
        print("No more frames to read, exiting.")
        break

    count += 1
    img = np.flip(img, axis=1)

    # Convert BGR to HSV
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Define the range for detecting red
    lower_red = np.array([100, 40, 40])
    upper_red = np.array([100, 255, 255])
    mask1 = cv2.inRange(hsv, lower_red, upper_red)

    lower_red = np.array([155, 40, 40])
    upper_red = np.array([180, 255, 255])
    mask2 = cv2.inRange(hsv, lower_red, upper_red)

    # Combine masks
    mask1 = mask1 + mask2

    # Perform morphological operations
    mask1 = cv2.morphologyEx(mask1, cv2.MORPH_OPEN, np.ones((3, 3), np.uint8), iterations=1)
    mask2 = cv2.bitwise_not(mask1)

    # Segment the background and the current frame
    res1 = cv2.bitwise_and(background, background, mask=mask1)
    res2 = cv2.bitwise_and(img, img, mask=mask2)

    # Combine results
    final_output = cv2.addWeighted(res1, 1, res2, 1, 0)

    # Display the output
    cv2.imshow("INVISIBLE MAN", final_output)
    k = cv2.waitKey(10)
    if k == 27:  # Exit on pressing 'ESC'
        break

# Release resources
raw_video.release()
cv2.destroyAllWindows()
