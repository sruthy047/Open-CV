import cv2
cap=cv2.VideoCapture('E://Sruthi//Open CV//Lesson 10//LP//Cars.mp4')

plate_cascade=cv2.CascadeClassifier('E://Sruthi//Open CV//Lesson 10//LP//haarcascade_russian_plate_number.xml')

while True:
    ret,frames=cap.read()
    if not ret:
        break
    gray=cv2.cvtColor(frames,cv2.COLOR_BGR2GRAY)

    plates = plate_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1, minSize=(20, 20))
    


    for (x,y,w,h) in plates:  
        cv2.rectangle(frames,(x,y),(x+w,y+h),(0,0,255),2)

    cv2.imshow('video2', frames)
	
	#  Esc key to stop
    if cv2.waitKey(33) == 27:
        break


cv2.destroyAllWindows()