import cv2
import os

def video_brightness(frame):
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    average_brightness = gray_frame.mean()
    return average_brightness

def pixel_info(frame):
    #find face using default frontal face machine learning thing
    cascadeClassifier = cv2.CascadeClassifier(os.path.join('','src\\haarcascade_frontalface_default.xml'))

    if cascadeClassifier.empty():
        print("Error loading the cascade classifier.")
    faces = cascadeClassifier.detectMultiScale(frame, scaleFactor=1.1, minNeighbors=5, minSize=(30,30), maxSize=(200,200))
    recog_face = frame.copy()
    #draw rectangle
    for (x, y, w, h) in faces:
        cv2.rectangle(recog_face, (x, y), (x+w, y+h), (0,255,0), 3)
    return recog_face

def findpixel(frame):
    cv2.calcCovarMatrix(frame, frame.mean())
    