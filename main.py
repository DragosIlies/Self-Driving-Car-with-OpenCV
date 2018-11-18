from imutils.video import VideoStream
from imutils.video import FPS
from multiprocessing import Process
from multiprocessing import Queue
from picamera.array import PiRGBArray
from picamera import PiCamera

import numpy as np
import argparse
import imutils
import time
from piCar import *
import cv2
import math

print("[INFO] starting video stream...")
#vs = VideoStream(src=0).start()
vs = VideoStream(usePiCamera=True).start()
time.sleep(2.0)
fps = FPS().start()

face_cascade = cv2.CascadeClassifier('/home/pi/Desktop/IP_ASSIGMENT/shortCV.xml')



print("Starting detection process...")

turn_meter = 0

def get_direction(objX,centerX,turn_meter,distance):
    if objX > centerX:
        distance = (objX - centerX)
        print(distance)
       
        turn_meter = distance * 0.002
        pivot_right(turn_meter)
        print("Moving right accordingly with ",turn_meter )
    elif objX < centerX:
        distance = -(objX - centerX)
        print(distance)
        turn_meter = distance * 0.002
        pivot_left(turn_meter)
        print("Moving left accordingly with ",turn_meter )
        
    else:
        print("I guess it is fine")
        
        print("Distance is:",distance)
        reverse(0.1)
        
        return True
        
while True:
        # grab the frame from the threaded video stream, resize it, and
        # grab its imensions
        frame = vs.read()

        frame = imutils.resize(frame, width=400)
        (fH, fW) = frame.shape[:2]
        centerY = fH/2
        centerX = fW/2
        

        

        #print("Center is..",centerY,centerX)
        
        
        
        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.3, 5)
       
        for (x,y,w,h) in faces:
            distancei = (2*3.14 * 180)/(w+h*360)*1000 + 3
            print(distancei)
            cmDist = round(distancei * 2.54,1)
            #forward(1)
            #distance = x - centerX
            #print(distance)
            get_direction(x,centerX,turn_meter,cmDist)
            print(x,y)
            cv2.rectangle(frame,(x,y), (x+w, y+h),(255,0,0),2)
        
        # show the output frame
        cv2.imshow("Frame", frame)
        key = cv2.waitKey(1) & 0xFF

        # if the `q` key was pressed, break from the loop
        if key == ord("q"):
                break

        # update the FPS counter
        fps.update()

# stop the timer and display FPS information
fps.stop()
print("[INFO] elapsed time: {:.2f}".format(fps.elapsed()))
print("[INFO] approx. FPS: {:.2f}".format(fps.fps()))
        
