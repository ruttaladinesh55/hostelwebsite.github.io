import cv2
import csv
import time



def login():

    now = time.time()
    future = now + 20
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    tt='madhav'
    recognizer.read("TrainingImageLabel/Trainner.yml")
    harcascadePath = "haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath)
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        global Id
        for (x, y, w, h) in faces:
            Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
            if (conf <70):
                cv2.rectangle(im, (x, y), (x + w, y + h), (0, 260, 0), 7)
                print(Id+1)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
        elif time.time() > future:
            break
        cv2.imshow('Filling attedance..', im)


login()
