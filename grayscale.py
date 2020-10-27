# openCV stands for Open computer Vision
# We can write in code to control the cameras and what things may happen.

# importing the libraries
import numpy as np
import cv2


# selecting the webcam

cap = cv2.VideoCapture(0)

# This loop allows the cam to continue reading the frame and give output.

while True:
    ret, frame = cap.read()  # reading frame by frame

    # displaying the frame

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    cv2.imshow('frame', frame)
    cv2.imshow('gray', gray)
    if cv2.waitKey(20) & 0xFF == ord('q'):
        break
