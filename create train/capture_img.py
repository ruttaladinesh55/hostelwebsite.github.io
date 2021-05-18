
import cv2
import csv



cam = cv2.VideoCapture(0)
detector = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
Enrollment = input("Enter student id : ")
Enrollment = Enrollment
Name = input("Enter your name : ")
Name=str(Name)
print('hello')
sampleNum = 0
while (True):
    ret, img = cam.read()
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = detector.detectMultiScale(gray, 1.3, 5)
    for (x, y, w, h) in faces:
        cv2.rectangle(img, (x, y), (x + w, y + h), (255, 0, 0), 2)
        # incrementing sample number
        sampleNum = sampleNum + 1
        # saving the captured face in the dataset folder
        cv2.imwrite("TrainingImage/ " + Name + "." + Enrollment + '.' + str(sampleNum) + ".jpg",
                    gray[y:y + h, x:x + w])
        cv2.imshow('Frame', img)
    # wait for 100 miliseconds
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    # break if the sample number is morethan 100
    elif sampleNum > 70:
        break
cam.release()
cv2.destroyAllWindows()
