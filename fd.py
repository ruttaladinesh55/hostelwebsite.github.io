import cv2
import numpy as np 
import os
import sys


camera = cv2.VideoCapture(0)

faceCascade = cv2.CascadeClassifier(r'C:\Users\G.Sushma\OneDrive\Desktop\opencv-3.4.8\data\haarcascades\haarcascade_frontalface_default.xml')

name = input("What's his/her rollno? ")
dirName = "C:\\images\\"
dirName=dirName+name
print(dirName)

if not os.path.exists(dirName):
	os.makedirs(dirName)
	print("Directory Created")
	
else:
	print("Name already exists")
	
	sys.exit()

count = 1
while count < 31:
# for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
	ret,frame = camera.read()
	if count > 30:
		break
	
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	faces = faceCascade.detectMultiScale(gray,scaleFactor=1.5, minNeighbors=5,minSize=(30, 30),)
	for (x, y, w, h) in faces:
		roiGray = gray[y:y+h, x:x+w]
		fileName = dirName + "/" + name + str(count) + ".jpg"
		cv2.imwrite(fileName, roiGray)
		cv2.imshow("face", roiGray)
		cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
		count += 1
	cv2.imshow('frame', frame)
	key = cv2.waitKey(1)
	#rawCapture.truncate(0)

	if key == 27:
		break

	cv2.destroyAllWindows()
	