import cv2

faceCascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

capture = cv2.VideoCapture(0)

while True: 
    _, frame = capture.read()
    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(gray,1.1,4)
    for x,y,w,h in faces: 
         cv2.rectangle(frame,(x,y), (x+w,y+h),(0,255,0),2)
    cv2.imshow('Image', frame)
    keyboard = cv2.waitKey(30 & 0xff)
    if keyboard == 27:
        break
capture.release()