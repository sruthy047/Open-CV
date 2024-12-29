import cv2

# Load the pre-trained Haar Cascade classifier
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

# Open the video source (0 for the webcam or replace with a video file path)
video_capture = cv2.VideoCapture(0)  # Change '0' to your video file path if needed

while True:
    # Read a frame from the video source
    ret, frame = video_capture.read()
    
    # Break the loop if the frame was not captured successfully
    if not ret:
        print("Failed to capture video frame. Exiting...")
        break

    # Convert the frame to grayscale (Haar Cascades work with grayscale images)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Detect faces in the frame
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))

    # Draw rectangles around the detected faces
    for (x, y, w, h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    # Display the resulting frame
    cv2.imshow('Face Detection', frame)

    # Exit the loop if the 'q' key is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the video capture object and close all OpenCV windows
video_capture.release()
cv2.destroyAllWindows()
