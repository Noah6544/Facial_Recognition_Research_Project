import cv2 as cv
import argparse
import numpy as np
#path to haarcascades
face_cascade_default = cv.CascadeClassifier("C:\\Users\\pathhaarcascade_frontalface_default.xml")
eye_cascade = cv.CascadeClassifier("C:\\Users\\user\\haarcascades\\haarcascade_eye.xml")

def find_face(frame):
    find_face = face_cascade_default.detectMultiScale(frame, 1.3, minNeighbors=5)
    for (x, y, w, h) in find_face:
        frame = cv.rectangle(frame, (x, y), (x + w, y + h), (0, 0, 0), 15)
        frame = cv.putText(frame,"Face",(x,y),cv.FONT_ITALIC,1,(255,255,255),2)

    return frame

def find_eye(frame):
    find_eye = eye_cascade.detectMultiScale(frame, 1.3, minNeighbors=5)
    for (x1, y1, x2, y2) in find_eye:
        left_pupil = int(x1+(y2/2))
        right_pupil = int(y1+(x2/2))
        frame = cv.circle(frame, (left_pupil,right_pupil), 2, (255, 255, 255), 15)

#change this argument to 0 if you have a single primary video camera, I'm on laptop which has 2 cameras.
vid = cv.VideoCapture(1)

#copied this from somewebsite
while (True):

    # Capture the video frame
    # by frame
    ret, frame = vid.read()

    # Display the resulting frame
    find_face(frame)
    find_eye(frame)

    cv.imshow('frame', frame)

    # the 'q' button is set as the
    # quitting button you may use any
    # desired button of your choice
    if cv.waitKey(1) & 0xFF == ord('q'):
        break




# After the loop release the cap object
vid.release()
# Destroy all the windows
cv.destroyAllWindows()
