import cv2 as cv
import numpy as np

camera = cv.VideoCapture('car1.mp4')
car_cascade = cv.CascadeClassifier('cars.xml')

from pygame import mixer

mixer.init()
mixer.music.load('beep.wav')

while True:
    
    ret,frame = camera.read()

    if ret:
        
        gray = cv.cvtColor(frame,cv.COLOR_BGR2GRAY)
        car = car_cascade.detectMultiScale(gray,1.01,20,minSize=(100,100))
        
        cv.line(frame, (500,200), (80,800), (0,255,0), 2)
        cv.line(frame, (700,200), (1100,800), (0,255,0), 2)
        cv.line(frame, (360,400), (830,400), (0,0,255), 2)
        
        for (x,y,w,h) in car:
            
            cv.rectangle(frame,(x,y),(x+w,y+h),(255,0,255),3)
            cv.putText(frame, "Safe", (x + 5, y + 25), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            center = [(x+w)/2, (y+h)/2]
            print(center[0], center[1])
            
            if center[1]>100:
                if 300<center[0] and center[0]<400:
                    cv.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),5)
                    cv.putText(frame, "Danger!", (x + 5, y + 25), cv.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)
                    mixer.music.play()

    cv.namedWindow("Car detect", cv.WINDOW_NORMAL)
    cv.imshow("Car detect", frame)
    
    if cv.waitKey(1) & 0xFF == 32:
        break

camera.release()
cv.destroyAllWindows()