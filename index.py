from flask import *
import cv2
import mysql.connector
import cv2
import csv
import time

import numpy as np
#from flaskext.mysql import MySQL

#import MySQLdb

import pickle
from datetime import date
from time import sleep


app=Flask(__name__)



mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  passwd="",
  database="hostel"
)
cur =mydb.cursor()

def login_with_cam():
    try:
        now = time.time()
        future = now + 20
        recognizer = cv2.face.LBPHFaceRecognizer_create()
        tt='madhav'
        recognizer.read("static/images_work/TrainingImageLabel/Trainner.yml")
        harcascadePath = "static/images_work/haarcascade_frontalface_default.xml"
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
                    return redirect(url_for('studenthome'))
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
            elif time.time() > future:
                break
            cv2.imshow('Filling attedance..', im)
    except :
        print('hello world')

@app.route('/')
@app.route('/home')
def home():
	return render_template("sample.html")

@app.route('/breakfast_feedback')
def breakfast_feedback():
	if not UserID:
		return redirect(url_for('login'))
	else:
		return render_template("feedback.html")

@app.route('/submit_breakfast_feedback', methods=['POST'])
def submit_breakfast_feedback():
	name = request.form
	q1 = name['experience1']
	q2 = name['experience2']
	q3 = name['experience3']
	q4 = name['experience4']
	q5 = name['experience5']
	q6 = name['experience6']
	q7 = name['experience7']
	q8 = name['experience8']
	q9 = name['experience9']
	q10 = name['experience10']
	q11 = name['experience11']
	q12 = name['experience12']
	q13 = name['experience13']
	q14 = name['experience14']
	q15 = name['experience15']
	q16 = name['date']
	data=""
	sqlsel = "SELECT * FROM feedbackbreakfast where roll=%s and `date` =%s"
	val = (RollNo,q16)
	print(val)
	cur.execute(sqlsel,val)
	data=cur.fetchall()
	count=len(data)
	print(count)
	if count==0:
		sql="INSERT INTO `feedbackbreakfast` (`roll`,`feedbackitem1`,`feedbackitem2`,`feedbackitem3`,`feedbackitem4`,`feedbackitem5`,`feedbackitem6`, `feedbackitem7`,`feedbackitem8`,`feedbackitem9`,`feedbackitem10`,`feedbackitem11`,`feedbackitem12`,`feedbackitem13`,`feedbackitem14`, `feedbackitem15`,`date`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
		val=(RollNo,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16)
		cur.execute(sql,val)
		res = mydb.commit()
		return render_template("/feedback.html",error='success')
	else:
		return render_template("/feedback.html",error='You are already submitted')

@app.route('/lunch_feedback')
def lunch_feedback():
	if not UserID:
		return redirect(url_for('login'))
	else:
		return render_template("feedbacklunch.html")
@app.route('/submit_lunch_feedback', methods=['POST'])
def submit_lunch_feedback():
	name = request.form
	q1 = name['experience1']
	q2 = name['experience2']
	q3 = name['experience3']
	q4 = name['experience4']
	q5 = name['experience5']
	q6 = name['experience6']
	q7 = name['experience7']
	q8 = name['experience8']
	q9 = name['experience9']
	q10 = name['experience10']
	q11 = name['experience11']
	q12 = name['experience12']
	q13 = name['experience13']
	q14 = name['experience14']
	q15 = name['experience15']
	q16 = name['experience16']
	q17 = name['experience17']
	q18 = name['experience18']
	q19 = name['experience19']
	q20 = name['experience20']
	q21 = name['date']
	data=""
	sqlsel = "SELECT * FROM feedbacklunch where roll=%s and `date` =%s"
	val = (RollNo,q21)
	print(val)
	cur.execute(sqlsel,val)
	data=cur.fetchall()
	count=len(data)
	print(count)
	if count==0:
		sql="INSERT INTO `feedbacklunch` (`roll`,`feedbackitem1`,`feedbackitem2`,`feedbackitem3`,`feedbackitem4`,`feedbackitem5`,`feedbackitem6`, `feedbackitem7`,`feedbackitem8`,`feedbackitem9`,`feedbackitem10`,`feedbackitem11`,`feedbackitem12`,`feedbackitem13`,`feedbackitem14`, `feedbackitem15`,`feedbackitem16`,`feedbackitem17`,`feedbackitem18`,`feedbackitem19`,`feedbackitem20`,`date`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
		val=(RollNo,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21)
		cur.execute(sql,val)
		res = mydb.commit()
		return render_template("/feedbacklunch.html",error='success')
	else:
		return render_template("/feedbacklunch.html",error='You are already submitted')

@app.route('/dinner_feedback')
def dinner_feedback():
	if not UserID:
		return redirect(url_for('login'))
	else:
		return render_template("feedbackdinner.html")
@app.route('/submit_dinner_feedback', methods=['POST'])
def submit_dinner_feedback():
	name = request.form
	q1 = name['experience1']
	q2 = name['experience2']
	q3 = name['experience3']
	q4 = name['experience4']
	q5 = name['experience5']
	q6 = name['experience6']
	q7 = name['experience7']
	q8 = name['experience8']
	q9 = name['experience9']
	q10 = name['experience10']
	q11 = name['experience11']
	q12 = name['experience12']
	q13 = name['experience13']
	q14 = name['experience14']
	q15 = name['experience15']
	q16 = name['experience16']
	q17 = name['experience17']
	q18 = name['experience18']
	q19 = name['experience19']
	q20 = name['experience20']
	q21 = name['date']
	data=""
	sqlsel = "SELECT * FROM feedbackdinner where roll=%s and `date` =%s"
	val = (RollNo,q21)
	print(val)
	cur.execute(sqlsel,val)
	data=cur.fetchall()
	count=len(data)
	print(count)
	if count==0:
		sql="INSERT INTO `feedbackdinner` (`roll`,`feedbackitem1`,`feedbackitem2`,`feedbackitem3`,`feedbackitem4`,`feedbackitem5`,`feedbackitem6`, `feedbackitem7`,`feedbackitem8`,`feedbackitem9`,`feedbackitem10`,`feedbackitem11`,`feedbackitem12`,`feedbackitem13`,`feedbackitem14`, `feedbackitem15`,`feedbackitem16`,`feedbackitem17`,`feedbackitem18`,`feedbackitem19`,`feedbackitem20`,`date`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
		val=(RollNo,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21)
		cur.execute(sql,val)
		res = mydb.commit()
		return render_template("/feedbackdinner.html",error='success')
	else:
		return render_template("/feedbackdinner.html",error='You are already submitted')

@app.route('/attendance')
def attendance():
	if not UserID:
		return redirect(url_for('login'))
	else:
		return render_template("attendancestudent.html")
@app.route('/submit_student_attendance', methods=['POST'])
def submit_student_attendance():
	name = request.form.getlist('eat')
	q1 = ""
	q2 = ""
	q3 = ""
	q4 =request.form['date']
	data = ""
	for data in name:
		if data=="morning":
			q1 = data
		elif data=="afternoon":
			q2 = data
		else:
			q3 = data
	Sqlsel = "SELECT * FROM studentattendance where roll=%s and `date`=%s"
	val = (RollNo,q4)
	print(val)
	cur.execute(Sqlsel,val)
	data=cur.fetchall()
	count = len(data)
	print(count)
	if count==0:
		sql="INSERT INTO `studentattendance` (`roll`,`breakfast`,`lunch`,`dinner`,`date`) VALUES (%s,%s,%s,%s,%s)"
		val=(RollNo,q1,q2,q3,q4)
		cur.execute(sql,val)
		res = mydb.commit()
		return render_template("/attendancestudent.html",error='success')
	else:
		return render_template("/attendancestudent.html",error='You are alreay submitted')

All_data="hia"
UserID = ""
UserName = ""
RollNo = ""
@app.route('/login')
def login():
	if not UserID:
		return render_template("studentlogin.html", error='')
	else:
		return redirect(url_for('studenthome'))


@app.route('/studentlogout')
def studentlogout():
	global UserID
	global UserName
	global RollNo
	UserName = ""
	UserID=""
	RollNo=""
	return render_template("studentlogin.html")

@app.route('/logincam', methods=['POST'])
def login_with_cam():
    now = time.time()
    future = now + 20
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    tt='madhav'
    recognizer.read("static/images_work/TrainingImageLabel/Trainner.yml")
    harcascadePath = "static/images_work/haarcascade_frontalface_default.xml"
    faceCascade = cv2.CascadeClassifier(harcascadePath)
    cam = cv2.VideoCapture(0)
    font = cv2.FONT_HERSHEY_SIMPLEX
    while True:
        ret, im = cam.read()
        gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)
        faces = faceCascade.detectMultiScale(gray, 1.2, 5)
        for (x, y, w, h) in faces:
            Id, conf = recognizer.predict(gray[y:y + h, x:x + w])
            print(Id)
            if (conf <70):
                cv2.rectangle(im, (x, y), (x + w, y + h), (0, 260, 0), 7)
                print(Id+1)
                phone="16A91A0"+str(Id)
                cur.execute("select * from registrationformstudent where rollno=(%s) and rollno=(%s)",(phone,phone))
                print(Id)
                print("sucess")
                All=cur.fetchall()
                global All_data
                global UserID
                global RollNo
                global UserName
                print(All)
                All_data = All
                UserID = All_data[0][0]
                UserName = All_data[0][1]
                RollNo = All_data[0][2]
                count = len(All_data)
                return redirect(url_for('studenthome'))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cam.release()
            break
        elif time.time() > future:
            cam.release()
            break
        cv2.imshow('Login with camera..', im)
    cam.release()
    cv2.destroyAllWindows()
    return render_template("/studentlogin.html", error='Please enter valid details')

@app.route('/studentupdateprofile', methods=['POST'])
def studentupdateprofile1():
	if not UserID:
		return redirect(url_for('login'))
	else:
		oldpassword =  request.form['old']
		newpassword =  request.form['new']
		confirmnewpassword =  request.form['confirm']
		temp_id=str(UserID)
		print(UserID)
		cur.execute("select * from registrationformstudent where id=(%s) and id=(%s)",(temp_id,temp_id))
		All=cur.fetchone()
		print(All)
		if All:
			if str(All[9])!=str(oldpassword):
				return render_template("profilestudent.html", data="Old Password not matched")
			else:
				val=cur.execute("update registrationformstudent set password=(%s) where id=(%s)",(newpassword,UserID))
				res = mydb.commit()
				return render_template("profilestudent.html", data='Pssword update success')


@app.route('/facultyupdateprofile', methods=['POST'])
def facultyupdateprofile():
	if not UserID:
		return redirect(url_for('login'))
	else:
		oldpassword =  request.form['old']
		newpassword =  request.form['new']
		confirmnewpassword =  request.form['confirm']
		temp_id=str(UserID)
		print(UserID)
		print(UserID)
		print(UserID)
		print(UserID)
		print(UserID)
		cur.execute("select * from registrationformfaculty where id=(%s) and id=(%s)",(temp_id,temp_id))
		All=cur.fetchone()
		print(All)
		if All:
			if str(All[9])!=str(oldpassword):
				return render_template("profilefaculty.html", data="Old Password not matched")
			else:
				val=cur.execute("update registrationformfaculty set password=(%s) where id=(%s)",(newpassword,UserID))
				res = mydb.commit()
				return render_template("profilefaculty.html", data='Pssword update success')

def login_succ():
    return redirect(url_for('studenthome'))

@app.route('/login', methods=['POST'])
def login1():
	name =  request.form['rollno']
	password =  request.form['password']
	cur.execute("select * from registrationformstudent where rollno=(%s) and password=(%s)",(name,password))
	All=cur.fetchall()
	if not All:
		return render_template("/studentlogin.html", error='Please enter valid details')
		login_succ()
	global All_data
	global UserID
	global UserName
	global RollNo
	All_data = All
	UserID = All_data[0][0]
	UserName = All_data[0][1]
	RollNo = All_data[0][2]
	count = len(All_data)
	return redirect(url_for('studenthome'))

@app.route('/studenthome')
def studenthome():
	if not UserID:
		return redirect(url_for('login'))
	else:
		return render_template("/studenthome.html",data=All_data,UserName=UserName,UserID=UserID)

@app.route('/adminrequirementissues')
def adminrequirementissues():
	today=date.today()
	cur.execute("select * FROM `requirementissues` where date=(%s)",(today,))
	issues=cur.fetchall()
	return render_template("/adminissues.html",data=issues)


@app.route('/suggestions')
def suggestions():
	return render_template("studentsuggestion.html",error='')
@app.route('/suggestions', methods=['POST'])
def suggestions1():
	i1=request.form['suggestions']
	i2=request.form['date']
	sql="INSERT INTO `studentsuggestions` (`suggestions`,`date`) VALUES (%s,%s)"
	val=(i1,i2)
	cur.execute(sql,val)
	res = mydb.commit()
	return render_template("/studentsuggestion.html",error='success')

@app.route('/studentupdateprofile')
def studentupdateprofile():
	if not UserID:
		return redirect(url_for('login'))
	else:
		return render_template("profilestudent.html")
#chiefwarden start
@app.route('/chiefwardenlogin')
def chiefwardenlogin():
	if not UserID:
		return render_template("chiefwardenlogin.html", error='')
	else:
		return redirect(url_for('chiefwardenhome'))


@app.route('/chiefwardenlogin', methods=['POST'])
def chiefwardenlogin1():
	name =  request.form['username']
	password =  request.form['password']
	cur.execute("select * from cheif_warden where cheifwarden_user_name=(%s) and cheifwarden_user_password=(%s)",(name,password))
	All=cur.fetchall()
	if not All:
		return render_template("/chiefwardenlogin.html", error='Please enter valid details')
	global All_data
	global UserID
	global UserName
	All_data = All
	UserID = All_data[0][0]
	UserName = All_data[0][1]
	count = len(All_data)
	return redirect(url_for('chiefwardenhome'))

@app.route('/chiefwardenhome')
def chiefwardenhome():
	if not UserID:
		return redirect(url_for('chiefwardenlogin'))
	else:
		return render_template("/chiefwardenhome.html",data=All_data,UserName=UserName,UserID=UserID)

@app.route('/chiefwardenlogout')
def chiefwardenlogout():
	global UserID
	global UserName
	UserName = ""
	UserID=""
	return render_template("chiefwardenlogin.html")

@app.route('/viewbreakfast')
def viewbreakfast():
	today=date.today()
	cur.execute("select * from itemlist where date=(%s)",(today,))
	All=cur.fetchall()
	return render_template("/viewbreakfast.html",data=All)

@app.route('/viewlunch')
def viewlunch():
	today=date.today()
	cur.execute("select * from itemlistlunch where date=(%s)",(today,))
	All=cur.fetchall()
	return render_template("/viewlunch.html",data=All)

@app.route('/viewdinner')
def viewdinner():
	today=date.today()
	cur.execute("select * from itemlistdinner where date=(%s)",(today,))
	All=cur.fetchall()
	return render_template("/viewdinner.html",data=All)


@app.route('/addbreakfast')
def addbreakfast():
	return render_template("/addbreakfast.html")
@app.route('/addbreakfast1', methods=['POST'])
def addbreakfast1():
	i1=request.form['item1']
	i2=request.form['item2']
	i3=request.form['item3']
	i4=request.form['item4']
	i5=request.form['item5']
	i6=request.form['date']
	sql="INSERT INTO `itemlist`(`item1`, `item2`, `item3`, `item4`, `item5`,`date`) VALUES (%s,%s,%s,%s,%s,%s)"
	val=(i1,i2,i3,i4,i5,i6)
	cur.execute(sql,val)
	res = mydb.commit()
	return render_template("/addbreakfast.html",error='success')

@app.route('/addlunch')
def addlunch():
	return render_template("/addlunch.html")
@app.route('/addlunch1', methods=['POST'])
def addlunch1():
	i1=request.form['item1']
	i2=request.form['item2']
	i3=request.form['item3']
	i4=request.form['item4']
	i5=request.form['item5']
	i6=request.form['item6']
	i7=request.form['item7']
	i8=request.form['item8']
	i9=request.form['item9']
	i10=request.form['item10']
	i11=request.form['date']


	sql="INSERT INTO `itemlistlunch`(`item1`, `item2`, `item3`, `item4`, `item5`,`item6`, `item7`, `item8`, `item9`, `item10`,`date`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
	val=(i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11)
	cur.execute(sql,val)
	res = mydb.commit()
	return render_template("/addlunch.html",error='success')

@app.route('/adddinner')
def adddinner():
	return render_template("/adddinner.html")
@app.route('/adddinner1', methods=['POST'])
def adddinner1():
	i1=request.form['item1']
	i2=request.form['item2']
	i3=request.form['item3']
	i4=request.form['item4']
	i5=request.form['item5']
	i6=request.form['item6']
	i7=request.form['item7']
	i8=request.form['item8']
	i9=request.form['item9']
	i10=request.form['item10']
	i11=request.form['date']

	sql="INSERT INTO `itemlistdinner`(`item1`, `item2`, `item3`, `item4`, `item5`,`item6`, `item7`, `item8`, `item9`, `item10`,`date`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
	val=(i1,i2,i3,i4,i5,i6,i7,i8,i9,i10,i11)
	cur.execute(sql,val)
	res = mydb.commit()
	return render_template("/adddinner.html",error='success')


@app.route('/breakfast')
def breakfast():
	today=date.today()
	#t1=today.strftime("%Y-%m-%d")
	cur.execute("select * from itemlist where date=(%s)",(today,))
	all=cur.fetchall()
	return render_template("/breakfast.html",data=all)

@app.route('/lunch')
def lunch():
	today=date.today()
	cur.execute("select * from itemlistlunch where date=(%s)",(today,))
	All=cur.fetchall()
	return render_template("/lunch.html",data=All)
@app.route('/dinner')
def dinner():
	today=date.today()
	cur.execute("select * from itemlistdinner where date=(%s)",(today,))
	All=cur.fetchall()
	return render_template("/dinner.html",data=All)


@app.route('/checkfeedbackbreakfast')
def checkfeedbackbreakfast():
	today=date.today()
	cur.execute("select count(*), feedbackitem1 FROM `feedbackbreakfast` where date=(%s) group by feedbackitem1",(today,))
	feedbackitem1=cur.fetchall()
	cur.execute("select count(*), feedbackitem2 FROM `feedbackbreakfast`  where date=(%s) group by feedbackitem2",(today,))
	feedbackitem2=cur.fetchall()
	cur.execute("select count(*), feedbackitem3 FROM `feedbackbreakfast`  where date=(%s) group by feedbackitem3",(today,))
	feedbackitem3=cur.fetchall()
	cur.execute("select count(*), feedbackitem4 FROM `feedbackbreakfast`  where date=(%s) group by feedbackitem4",(today,))
	feedbackitem4=cur.fetchall()
	cur.execute("select count(*), feedbackitem5 FROM `feedbackbreakfast`  where date=(%s) group by feedbackitem5",(today,))
	feedbackitem5=cur.fetchall()
	cur.execute("select count(*), feedbackitem6 FROM `feedbackbreakfast`  where date=(%s) group by feedbackitem6",(today,))
	feedbackitem6=cur.fetchall()
	cur.execute("select count(*), feedbackitem7 FROM `feedbackbreakfast`  where date=(%s) group by feedbackitem7",(today,))
	feedbackitem7=cur.fetchall()
	cur.execute("select count(*), feedbackitem8 FROM `feedbackbreakfast`  where date=(%s) group by feedbackitem8",(today,))
	feedbackitem8=cur.fetchall()
	cur.execute("select count(*), feedbackitem9 FROM `feedbackbreakfast`  where date=(%s) group by feedbackitem9",(today,))
	feedbackitem9=cur.fetchall()
	cur.execute("select count(*), feedbackitem10 FROM `feedbackbreakfast`  where date=(%s) group by feedbackitem10",(today,))
	feedbackitem10=cur.fetchall()
	cur.execute("select count(*), feedbackitem11 FROM `feedbackbreakfast`  where date=(%s) group by feedbackitem11",(today,))
	feedbackitem11=cur.fetchall()
	cur.execute("select count(*), feedbackitem12 FROM `feedbackbreakfast`  where date=(%s) group by feedbackitem12",(today,))
	feedbackitem12=cur.fetchall()
	cur.execute("select count(*), feedbackitem13 FROM `feedbackbreakfast`  where date=(%s) group by feedbackitem13",(today,))
	feedbackitem13=cur.fetchall()
	cur.execute("select count(*), feedbackitem14 FROM `feedbackbreakfast`  where date=(%s) group by feedbackitem14",(today,))
	feedbackitem14=cur.fetchall()
	cur.execute("select count(*), feedbackitem15 FROM `feedbackbreakfast`  where date=(%s) group by feedbackitem15",(today,))
	feedbackitem15=cur.fetchall()

	return render_template("/checkfeedbackbreakfast.html",feedbackitem1=feedbackitem1,feedbackitem2=feedbackitem2,feedbackitem3=feedbackitem3,feedbackitem4=feedbackitem4,feedbackitem5=feedbackitem5,feedbackitem6=feedbackitem6,feedbackitem7=feedbackitem7,feedbackitem8=feedbackitem8,feedbackitem9=feedbackitem9,feedbackitem10=feedbackitem10,feedbackitem11=feedbackitem11,feedbackitem12=feedbackitem12,feedbackitem13=feedbackitem13,feedbackitem14=feedbackitem14,feedbackitem15=feedbackitem15,)

@app.route('/checkfeedbacklunch')
def checkfeedbacklunch():
	today=date.today()
	cur.execute("select count(*), feedbackitem1 FROM `feedbacklunch` where date=(%s) group by feedbackitem1",(today,))
	feedbackitem1=cur.fetchall()
	cur.execute("select count(*), feedbackitem2 FROM `feedbacklunch` where date=(%s) group by feedbackitem2",(today,))
	feedbackitem2=cur.fetchall()
	cur.execute("select count(*), feedbackitem3 FROM `feedbacklunch` where date=(%s) group by feedbackitem3",(today,))
	feedbackitem3=cur.fetchall()
	cur.execute("select count(*), feedbackitem4 FROM `feedbacklunch` where date=(%s) group by feedbackitem4",(today,))
	feedbackitem4=cur.fetchall()
	cur.execute("select count(*), feedbackitem5 FROM `feedbacklunch` where date=(%s) group by feedbackitem5",(today,))
	feedbackitem5=cur.fetchall()
	cur.execute("select count(*), feedbackitem6 FROM `feedbacklunch` where date=(%s) group by feedbackitem6",(today,))
	feedbackitem6=cur.fetchall()
	cur.execute("select count(*), feedbackitem7 FROM `feedbacklunch` where date=(%s) group by feedbackitem7",(today,))
	feedbackitem7=cur.fetchall()
	cur.execute("select count(*), feedbackitem8 FROM `feedbacklunch` where date=(%s) group by feedbackitem8",(today,))
	feedbackitem8=cur.fetchall()
	cur.execute("select count(*), feedbackitem9 FROM `feedbacklunch` where date=(%s) group by feedbackitem9",(today,))
	feedbackitem9=cur.fetchall()
	cur.execute("select count(*), feedbackitem10 FROM `feedbacklunch` where date=(%s) group by feedbackitem10",(today,))
	feedbackitem10=cur.fetchall()
	cur.execute("select count(*), feedbackitem11 FROM `feedbacklunch` where date=(%s) group by feedbackitem11",(today,))
	feedbackitem11=cur.fetchall()
	cur.execute("select count(*), feedbackitem12 FROM `feedbacklunch` where date=(%s) group by feedbackitem12",(today,))
	feedbackitem12=cur.fetchall()
	cur.execute("select count(*), feedbackitem13 FROM `feedbacklunch` where date=(%s) group by feedbackitem13",(today,))
	feedbackitem13=cur.fetchall()
	cur.execute("select count(*), feedbackitem14 FROM `feedbacklunch` where date=(%s) group by feedbackitem14",(today,))
	feedbackitem14=cur.fetchall()
	cur.execute("select count(*), feedbackitem15 FROM `feedbacklunch` where date=(%s) group by feedbackitem15",(today,))
	feedbackitem15=cur.fetchall()
	cur.execute("select count(*), feedbackitem16 FROM `feedbacklunch` where date=(%s) group by feedbackitem16",(today,))
	feedbackitem16=cur.fetchall()
	cur.execute("select count(*), feedbackitem17 FROM `feedbacklunch` where date=(%s) group by feedbackitem17",(today,))
	feedbackitem17=cur.fetchall()
	cur.execute("select count(*), feedbackitem18 FROM `feedbacklunch` where date=(%s) group by feedbackitem18",(today,))
	feedbackitem18=cur.fetchall()
	cur.execute("select count(*), feedbackitem19 FROM `feedbacklunch` where date=(%s) group by feedbackitem19",(today,))
	feedbackitem19=cur.fetchall()
	cur.execute("select count(*), feedbackitem20 FROM `feedbacklunch` where date=(%s) group by feedbackitem20",(today,))
	feedbackitem20=cur.fetchall()

	return render_template("/checkfeedbacklunch.html",feedbackitem1=feedbackitem1,feedbackitem2=feedbackitem2,feedbackitem3=feedbackitem3,feedbackitem4=feedbackitem4,feedbackitem5=feedbackitem5,feedbackitem6=feedbackitem6,feedbackitem7=feedbackitem7,feedbackitem8=feedbackitem8,feedbackitem9=feedbackitem9,feedbackitem10=feedbackitem10,feedbackitem11=feedbackitem11,feedbackitem12=feedbackitem12,feedbackitem13=feedbackitem13,feedbackitem14=feedbackitem14,feedbackitem15=feedbackitem15,feedbackitem16=feedbackitem16,feedbackitem17=feedbackitem17,feedbackitem18=feedbackitem18,feedbackitem19=feedbackitem19,feedbackitem20=feedbackitem20,)

@app.route('/checkfeedbackdinner')
def checkfeedbackdinner():
	today=date.today()
	cur.execute("select count(*), feedbackitem1 FROM `feedbackdinner` where date=(%s) group by feedbackitem1",(today,))
	feedbackitem1=cur.fetchall()
	cur.execute("select count(*), feedbackitem2 FROM `feedbackdinner` where date=(%s) group by feedbackitem2",(today,))
	feedbackitem2=cur.fetchall()
	cur.execute("select count(*), feedbackitem3 FROM `feedbackdinner` where date=(%s) group by feedbackitem3",(today,))
	feedbackitem3=cur.fetchall()
	cur.execute("select count(*), feedbackitem4 FROM `feedbackdinner` where date=(%s) group by feedbackitem4",(today,))
	feedbackitem4=cur.fetchall()
	cur.execute("select count(*), feedbackitem5 FROM `feedbackdinner` where date=(%s) group by feedbackitem5",(today,))
	feedbackitem5=cur.fetchall()
	cur.execute("select count(*), feedbackitem6 FROM `feedbackdinner` where date=(%s) group by feedbackitem6",(today,))
	feedbackitem6=cur.fetchall()
	cur.execute("select count(*), feedbackitem7 FROM `feedbackdinner` where date=(%s) group by feedbackitem7",(today,))
	feedbackitem7=cur.fetchall()
	cur.execute("select count(*), feedbackitem8 FROM `feedbackdinner` where date=(%s) group by feedbackitem8",(today,))
	feedbackitem8=cur.fetchall()
	cur.execute("select count(*), feedbackitem9 FROM `feedbackdinner` where date=(%s) group by feedbackitem9",(today,))
	feedbackitem9=cur.fetchall()
	cur.execute("select count(*), feedbackitem10 FROM `feedbackdinner` where date=(%s) group by feedbackitem10",(today,))
	feedbackitem10=cur.fetchall()
	cur.execute("select count(*), feedbackitem11 FROM `feedbackdinner` where date=(%s) group by feedbackitem11",(today,))
	feedbackitem11=cur.fetchall()
	cur.execute("select count(*), feedbackitem12 FROM `feedbackdinner` where date=(%s) group by feedbackitem12",(today,))
	feedbackitem12=cur.fetchall()
	cur.execute("select count(*), feedbackitem13 FROM `feedbackdinner` where date=(%s) group by feedbackitem13",(today,))
	feedbackitem13=cur.fetchall()
	cur.execute("select count(*), feedbackitem14 FROM `feedbackdinner` where date=(%s) group by feedbackitem14",(today,))
	feedbackitem14=cur.fetchall()
	cur.execute("select count(*), feedbackitem15 FROM `feedbackdinner` where date=(%s) group by feedbackitem15",(today,))
	feedbackitem15=cur.fetchall()
	cur.execute("select count(*), feedbackitem16 FROM `feedbackdinner` where date=(%s) group by feedbackitem16",(today,))
	feedbackitem16=cur.fetchall()
	cur.execute("select count(*), feedbackitem17 FROM `feedbackdinner` where date=(%s) group by feedbackitem17",(today,))
	feedbackitem17=cur.fetchall()
	cur.execute("select count(*), feedbackitem18 FROM `feedbackdinner` where date=(%s) group by feedbackitem18",(today,))
	feedbackitem18=cur.fetchall()
	cur.execute("select count(*), feedbackitem19 FROM `feedbackdinner` where date=(%s) group by feedbackitem19",(today,))
	feedbackitem19=cur.fetchall()
	cur.execute("select count(*), feedbackitem20 FROM `feedbackdinner` where date=(%s) group by feedbackitem20",(today,))
	feedbackitem20=cur.fetchall()

	return render_template("/checkfeedbackdinner.html",feedbackitem1=feedbackitem1,feedbackitem2=feedbackitem2,feedbackitem3=feedbackitem3,feedbackitem4=feedbackitem4,feedbackitem5=feedbackitem5,feedbackitem6=feedbackitem6,feedbackitem7=feedbackitem7,feedbackitem8=feedbackitem8,feedbackitem9=feedbackitem9,feedbackitem10=feedbackitem10,feedbackitem11=feedbackitem11,feedbackitem12=feedbackitem12,feedbackitem13=feedbackitem13,feedbackitem14=feedbackitem14,feedbackitem15=feedbackitem15,feedbackitem16=feedbackitem16,feedbackitem17=feedbackitem17,feedbackitem18=feedbackitem18,feedbackitem19=feedbackitem19,feedbackitem20=feedbackitem20,)


@app.route('/checkattendance')
def checkattendance():
	today=date.today()
	cur.execute("select count(*) FROM `studentattendance` where breakfast='morning' and date=(%s)",(today,))
	feedbackitem1=cur.fetchall()
	cur.execute("select count(*) FROM `studentattendance` where lunch='afternoon' and date=(%s)",(today,))
	feedbackitem2=cur.fetchall()
	cur.execute("select count(*) FROM `studentattendance` where dinner='night' and date=(%s)",(today,))
	feedbackitem3=cur.fetchall()

	return render_template("/checkattendance.html", data1=feedbackitem1, data2=feedbackitem2, data3=feedbackitem3)

@app.route('/checkattendancefaculty')
def checkattendancefaculty():
	today=date.today()
	cur.execute("select count(*) FROM `facultyattendance` where breakfast='morning' and date=(%s)",(today,))
	feedbackitem1=cur.fetchall()

	cur.execute("select count(*) FROM `facultyattendance` where lunch='afternoon' and date=(%s)",(today,))
	feedbackitem2=cur.fetchall()
	
	cur.execute("select count(*) FROM `facultyattendance` where dinner='night' and date=(%s)",(today,))
	feedbackitem3=cur.fetchall()
	

	return render_template("/checkattendancefaculty.html", data1=feedbackitem1, data2=feedbackitem2, data3=feedbackitem3)


@app.route('/requirementissues')
def requirementissues():
	return render_template("requirement.html",error='')
@app.route('/requirement', methods=['POST'])
def requirement():
	i1=request.form['issues']
	i2=request.form['date']
	sql="INSERT INTO `requirementissues` (`issues`,`date`) VALUES (%s,%s)"
	val=(i1,i2)
	cur.execute(sql,val)
	res = mydb.commit()
	return render_template("/requirement.html",error='success')

@app.route('/chiefwardenupdateprofile')
def chiefwardenupdateprofile1():
	if not UserID:
		return redirect(url_for('chiefwardenlogin'))
	else:
		return render_template("profilechiefwarden.html")

@app.route('/chiefwardenupdateprofile', methods=['POST'])
def chiefwardenupdateprofile():
	if not UserID:
		return redirect(url_for('chiefwardenlogin'))
	else:
		oldpassword =  request.form['old']
		newpassword =  request.form['new']
		confirmnewpassword =  request.form['confirm']
		temp_id=str(UserID)
		print(UserID)
		print(UserID)
		print(UserID)
		print(UserID)
		print(UserID)
		cur.execute("select * from cheif_warden where cheifwarden_id=(%s) and cheifwarden_id=(%s)",(temp_id,temp_id))
		All=cur.fetchone()
		print(All)
		if All:
			if str(All[2])!=str(oldpassword):
				return render_template("profilechiefwarden.html", data="Old Password not matched")
			else:
				val=cur.execute("update cheif_warden set cheifwarden_user_password=(%s) where cheifwarden_id=(%s)",(newpassword,UserID))
				res = mydb.commit()
				return render_template("profilechiefwarden.html", data='Password update success')


#chiefwarden end

#facu
@app.route('/facultylogin')
def facultylogin():
	return render_template("facultylogin.html", error='')

@app.route('/logincam_fac', methods=['POST'])
def login_with_cam_fac():
    now = time.time()
    future = now + 20
    recognizer = cv2.face.LBPHFaceRecognizer_create()
    tt='madhav'
    recognizer.read("static/images_work/TrainingImageLabel/Trainner.yml")
    harcascadePath = "static/images_work/haarcascade_frontalface_default.xml"
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
                phone=str(Id)
                cur.execute("select * from registrationformfaculty where rollno=(%s) and rollno=(%s)",(phone,phone))
                print(Id)
                All=cur.fetchall()
                if All:
                	global All_data
                	global UserID
                	global UserName
                	All_data = All
                	UserID = All_data[0][0]
                	UserName = All_data[0][1]
                	count = len(All_data)
                	return redirect(url_for('facultyhome'))
        if cv2.waitKey(1) & 0xFF == ord('q'):
            cam.release()
            break
        elif time.time() > future:
            cam.release()
            break
        cv2.imshow('Login with camera..', im)
    cam.release()
    cv2.destroyAllWindows()
    return render_template("/facultylogin.html", error='Please enter valid details')

@app.route('/facultylogin', methods=['POST'])
def facultylogin1():
	name =  request.form['rollno']
	password =  request.form['password']
	cur.execute("select * from registrationformfaculty where rollno=(%s) and password=(%s)",(name,password))
	All=cur.fetchall()
	print(All)
	if not All:
		return render_template("/facultylogin.html", error='Please enter valid details')
		login_succ()
	global All_data
	global UserID
	global UserName
	global RollNo
	All_data = All
	UserID = All_data[0][0]
	UserName = All_data[0][1]
	RollNo = All_data[0][2]
	count = len(All_data)
	return redirect(url_for('facultyhome'))

@app.route('/facultyhome')
def facultyhome():
	if UserID=="":
		return redirect(url_for('facultylogin'))
	else:
		return render_template("/facultyhome.html",data=All_data,UserName=UserName,UserID=UserID)

@app.route('/facultylogout')
def facultylogout():
	global UserID
	global UserName
	global RollNo
	UserName = ""
	UserID=""
	RollNo=""
	return render_template("facultylogin.html")


@app.route('/facultybreakfast')
def facultybreakfast():
	today=date.today()
	t1=today.strftime("%Y-%m-%d")
	sql = "select * from itemlist where date LIKE %s"
	adr = (t1,)
	cur.execute(sql, adr)
	All=cur.fetchall()
	print(len(All))
	return render_template("/facultybreakfast.html",data=All)

@app.route('/facultyupdateprofile')
def facultyupdateprofile1():
	if not UserID:
		return redirect(url_for('facultylogin'))
	else:
		return render_template("profilefaculty.html")

@app.route('/facultylunch')
def facultylunch():
	today=date.today()
	t1=today.strftime("%Y-%m-%d")
	sql = "select * from itemlistlunch where date LIKE %s"
	adr = (t1,)
	cur.execute(sql, adr)
	All=cur.fetchall()
	print(len(All))
	return render_template("/facultylunch.html",data=All)

@app.route('/facultydinner')
def facultydinner():
	today=date.today()
	t1=today.strftime("%Y-%m-%d")
	sql = "select * from itemlistdinner where date LIKE %s"
	adr = (t1,)
	cur.execute(sql, adr)
	All=cur.fetchall()
	print(len(All))
	return render_template("/facultydinner.html",data=All)

@app.route('/facultybreakfast_feedback')
def facultybreakfast_feedback():
	if not UserID:
		return redirect(url_for('facultylogin'))
	else:
		return render_template("facultyfeedback.html")

@app.route('/facultysubmit_breakfast_feedback', methods=['POST'])
def facultysubmit_breakfast_feedback():
	name = request.form
	q1 = name['experience1']
	q2 = name['experience2']
	q3 = name['experience3']
	q4 = name['experience4']
	q5 = name['experience5']
	q6 = name['experience6']
	q7 = name['experience7']
	q8 = name['experience8']
	q9 = name['experience9']
	q10 = name['experience10']
	q11 = name['experience11']
	q12 = name['experience12']
	q13 = name['experience13']
	q14 = name['experience14']
	q15 = name['experience15']
	q16 = name['date']
	data=""
	sqlsel = "SELECT * FROM feedbackbreakfast where roll=%s and `date` =%s"
	val = (RollNo,q16)
	print(val)
	cur.execute(sqlsel,val)
	data=cur.fetchall()
	count=len(data)
	print(count)
	if count==0:
		sql="INSERT INTO `feedbackbreakfast` (`roll`,`feedbackitem1`,`feedbackitem2`,`feedbackitem3`,`feedbackitem4`,`feedbackitem5`,`feedbackitem6`, `feedbackitem7`,`feedbackitem8`,`feedbackitem9`,`feedbackitem10`,`feedbackitem11`,`feedbackitem12`,`feedbackitem13`,`feedbackitem14`, `feedbackitem15`,`date`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
		val=(RollNo,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16)
		cur.execute(sql,val)
		res = mydb.commit()
		return render_template("/facultyfeedback.html",error='success')
	else:
		return render_template("/facultyfeedback.html",error='You are already submitted')

@app.route('/facultylunch_feedback')
def facultylunch_feedback():
	if not UserID:
		return redirect(url_for('facultylogin'))
	else:
		return render_template("facultyfeedbacklunch.html")
@app.route('/facultysubmit_lunch_feedback', methods=['POST'])
def facultysubmit_lunch_feedback():
	name = request.form
	q1 = name['experience1']
	q2 = name['experience2']
	q3 = name['experience3']
	q4 = name['experience4']
	q5 = name['experience5']
	q6 = name['experience6']
	q7 = name['experience7']
	q8 = name['experience8']
	q9 = name['experience9']
	q10 = name['experience10']
	q11 = name['experience11']
	q12 = name['experience12']
	q13 = name['experience13']
	q14 = name['experience14']
	q15 = name['experience15']
	q16 = name['experience16']
	q17 = name['experience17']
	q18 = name['experience18']
	q19 = name['experience19']
	q20 = name['experience20']
	q21 = name['date']
	data=""
	sqlsel = "SELECT * FROM feedbacklunch where roll=%s and `date` =%s"
	val = (RollNo,q21)
	print(val)
	cur.execute(sqlsel,val)
	data=cur.fetchall()
	count=len(data)
	print(count)
	if count==0:
		sql="INSERT INTO `feedbacklunch` (`roll`,`feedbackitem1`,`feedbackitem2`,`feedbackitem3`,`feedbackitem4`,`feedbackitem5`,`feedbackitem6`, `feedbackitem7`,`feedbackitem8`,`feedbackitem9`,`feedbackitem10`,`feedbackitem11`,`feedbackitem12`,`feedbackitem13`,`feedbackitem14`, `feedbackitem15`,`feedbackitem16`,`feedbackitem17`,`feedbackitem18`,`feedbackitem19`,`feedbackitem20`,`date`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
		val=(RollNo,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21)
		cur.execute(sql,val)
		res = mydb.commit()
		return render_template("/facultyfeedbacklunch.html",error='success')
	else:
		return render_template("/facultyfeedbacklunch.html",error='You are already submitted')

	
@app.route('/facultydinner_feedback')
def facultydinner_feedback():
	if not UserID:
		return redirect(url_for('facultylogin'))
	else:
		return render_template("facultyfeedbackdinner.html")
@app.route('/facultysubmit_dinner_feedback', methods=['POST'])
def facultysubmit_dinner_feedback():
	name = request.form
	q1 = name['experience1']
	q2 = name['experience2']
	q3 = name['experience3']
	q4 = name['experience4']
	q5 = name['experience5']
	q6 = name['experience6']
	q7 = name['experience7']
	q8 = name['experience8']
	q9 = name['experience9']
	q10 = name['experience10']
	q11 = name['experience11']
	q12 = name['experience12']
	q13 = name['experience13']
	q14 = name['experience14']
	q15 = name['experience15']
	q16 = name['experience16']
	q17 = name['experience17']
	q18 = name['experience18']
	q19 = name['experience19']
	q20 = name['experience20']
	q21 = name['date']
	data=""
	sqlsel = "SELECT * FROM feedbackdinner where roll=%s and `date` =%s"
	val = (RollNo,q21)
	print(val)
	cur.execute(sqlsel,val)
	data=cur.fetchall()
	count=len(data)
	print(count)
	if count==0:
		sql="INSERT INTO `feedbackdinner` (`roll`,`feedbackitem1`,`feedbackitem2`,`feedbackitem3`,`feedbackitem4`,`feedbackitem5`,`feedbackitem6`, `feedbackitem7`,`feedbackitem8`,`feedbackitem9`,`feedbackitem10`,`feedbackitem11`,`feedbackitem12`,`feedbackitem13`,`feedbackitem14`, `feedbackitem15`,`feedbackitem16`,`feedbackitem17`,`feedbackitem18`,`feedbackitem19`,`feedbackitem20`,`date`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"
		val=(RollNo,q1,q2,q3,q4,q5,q6,q7,q8,q9,q10,q11,q12,q13,q14,q15,q16,q17,q18,q19,q20,q21)
		cur.execute(sql,val)
		res = mydb.commit()
		return render_template("/facultyfeedbackdinner.html",error='success')
	else:
		return render_template("/facultyfeedbackdinner.html",error='You are already submitted')

@app.route('/facultysuggestions')
def facultysuggestions():
	return render_template("facultysuggestions.html",error='')
@app.route('/facultysuggestions', methods=['POST'])
def facultysuggestions1():
	i1=request.form['suggestions']
	i2=request.form['date']
	sql="INSERT INTO `facultysuggestions` (`suggestions`,`date`) VALUES (%s,%s)"
	val=(i1,i2)
	cur.execute(sql,val)
	res = mydb.commit()
	return render_template("/facultysuggestions.html",error='success')

@app.route('/facultyattendance')
def facultyattendance():
	if not UserID:
		return redirect(url_for('facultylogin'))
	else:
		return render_template("attendancefaculty.html")
@app.route('/submit_faculty_attendance', methods=['POST'])
def submit_faculty_attendance():
	name = request.form.getlist('eat')
	q1 = ""
	q2 = ""
	q3 = ""
	q4 =request.form['date']
	data = ""
	for data in name:
		if data=="morning":
			q1 = data
		elif data=="afternoon":
			q2 = data
		else:
			q3 = data
	sqlsel= "SELECT * FROM `facultyattendance` where roll=%s and `date` =%s"
	val= (RollNo,q4)
	print(val)
	cur.execute(sqlsel,val)
	data=cur.fetchall()
	count = len(data)
	print(count)
	if count==0:
		sql="INSERT INTO `facultyattendance` (`roll`,`breakfast`,`lunch`,`dinner`,`date`) VALUES (%s,%s,%s,%s,%s)"
		val=(RollNo,q1,q2,q3,q4)
		cur.execute(sql,val)
		res = mydb.commit()
		return render_template("/attendancefaculty.html",error='success')
	else:
		return render_template("/attendancefaculty.html",error='you are already submitted')


#faculty end

#admin start

@app.route('/adminlogin')
def adminlogin():
	if not UserID:
		return render_template("adminlogin.html", error='')
	else:
		return redirect(url_for('adminhome'))


@app.route('/adminlogin', methods=['POST'])
def adminlogin1():
	name =  request.form['username']
	password =  request.form['password']
	cur.execute("select * from admin where admin_user_name=(%s) and admin_user_password=(%s)",(name,password))
	All=cur.fetchall()
	if not All:
		return render_template("/adminlogin.html", error="Enter valid details")
	global All_data
	global UserID
	global UserName
	All_data = All
	UserID = All_data[0][0]
	UserName = All_data[0][1]
	count = len(All_data)
	if count==1:
		return redirect(url_for('adminhome' , UserName=UserName))
		
@app.route('/forget_error_student')
def forget_error_student():
	return render_template("studentlogin.html", error='Please contact admin')

@app.route('/forget_error_facul')
def forget_error_facul():
	return render_template("facultylogin.html", error='Please contact admin')

@app.route('/adminhome')
def adminhome():
	if not UserID:
		return redirect(url_for('adminlogin'))
	else:
		return render_template("/adminhome.html",data=All_data,UserName=UserName,UserID=UserID)

@app.route('/adminlogout')
def adminlogout():
	global UserID
	global UserName
	UserName = ""
	UserID=""
	return render_template("adminlogin.html")


@app.route('/registrationformstudent')
def registrationformstudent():
	return render_template("registrationformstudent.html")

@app.route('/capture_imgs',methods=['POST'])
def capture_imgs():
    cam = cv2.VideoCapture(0)
    detector = cv2.CascadeClassifier('static/images_work/haarcascade_frontalface_default.xml')
    Enrollment = input("Enter student mobilenumber : ")
    Enrollment = Enrollment
    Name = input("Enter your name : ")
    Name=str(Name)
    print('Capturing images please wait......')
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
            cv2.imwrite("static/images_work/TrainingImage/ " + Name + "." + Enrollment + '.' + str(sampleNum) + ".jpg",
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
    return redirect(url_for('adminlogin'))

@app.route('/registrationformstudent', methods=['POST'])
def registrationformstudent1():
	i1=request.form['name']
	i2=request.form['rollno']
	i3=request.form['gender']
	i4=request.form['mailid']
	i5=request.form['phoneno']
	i6=request.form['course']
	i7=request.form['specalization']
	i8=request.form['messtype']
	i9=request.form['password']
	sql="INSERT INTO `registrationformstudent`(`name`, `rollno`, `gender`, `mailid` ,`phoneno`, `course`, `specialization`, `messtype`, `password`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
	val=(i1,i2,i3,i4,i5,i6,i7,i8,i9)
	cur.execute(sql,val)
	res = mydb.commit()
	return render_template("/registrationformstudent.html",error='success')

@app.route('/registrationformfaculty')
def registrationformfaculty():
	return render_template("registrationformfaculty.html")

@app.route('/registrationformfaculty', methods=['POST'])
def registrationformfaculty1():
	i1=request.form['name']
	i2=request.form['rollno']
	i3=request.form['gender']
	i4=request.form['mailid']
	i5=request.form['phoneno']
	i6=request.form['course']
	i7=request.form['specalization']
	i8=request.form['messtype']
	i9=request.form['password']
	sql="INSERT INTO `registrationformfaculty`(`name`, `rollno`, `gender`, `mailid` ,`phoneno`, `course`, `specialization`, `messtype`, `password`) VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)"
	val=(i1,i2,i3,i4,i5,i6,i7,i8,i9)
	cur.execute(sql,val)
	res = mydb.commit()
	return render_template("/registrationformfaculty.html",error='success')

@app.route('/adminbreak')
def adminbreak():
	today=date.today()
	cur.execute("select * from itemlist where date=(%s)",(today,))
	All=cur.fetchall()
	return render_template("/adminbreak.html",data=All)
@app.route('/adminlunch')
def adminlunch():
	today=date.today()
	cur.execute("select * from itemlistlunch where date=(%s)",(today,))
	All=cur.fetchall()
	return render_template("/adminlunch.html",data=All)
@app.route('/admindinner')
def admindinner():
	today=date.today()
	cur.execute("select * from itemlistdinner where date=(%s)",(today,))
	All=cur.fetchall()
	return render_template("/admindinner.html",data=All)


@app.route('/admincheckbreakfast')
def admincheckbreakfast():
	today=date.today()
	cur.execute("select count(*), feedbackitem1 FROM `feedbackbreakfast` where date=(%s) group by feedbackitem1",(today,))
	feedbackitem1=cur.fetchall()
	cur.execute("select count(*), feedbackitem2 FROM `feedbackbreakfast`  where date=(%s) group by feedbackitem2",(today,))
	feedbackitem2=cur.fetchall()
	cur.execute("select count(*), feedbackitem3 FROM `feedbackbreakfast`  where date=(%s) group by feedbackitem3",(today,))
	feedbackitem3=cur.fetchall()
	cur.execute("select count(*), feedbackitem4 FROM `feedbackbreakfast`  where date=(%s) group by feedbackitem4",(today,))
	feedbackitem4=cur.fetchall()
	cur.execute("select count(*), feedbackitem5 FROM `feedbackbreakfast`  where date=(%s) group by feedbackitem5",(today,))
	feedbackitem5=cur.fetchall()
	cur.execute("select count(*), feedbackitem6 FROM `feedbackbreakfast`  where date=(%s) group by feedbackitem6",(today,))
	feedbackitem6=cur.fetchall()
	cur.execute("select count(*), feedbackitem7 FROM `feedbackbreakfast`  where date=(%s) group by feedbackitem7",(today,))
	feedbackitem7=cur.fetchall()
	cur.execute("select count(*), feedbackitem8 FROM `feedbackbreakfast`  where date=(%s) group by feedbackitem8",(today,))
	feedbackitem8=cur.fetchall()
	cur.execute("select count(*), feedbackitem9 FROM `feedbackbreakfast`  where date=(%s) group by feedbackitem9",(today,))
	feedbackitem9=cur.fetchall()
	cur.execute("select count(*), feedbackitem10 FROM `feedbackbreakfast`  where date=(%s) group by feedbackitem10",(today,))
	feedbackitem10=cur.fetchall()
	cur.execute("select count(*), feedbackitem11 FROM `feedbackbreakfast`  where date=(%s) group by feedbackitem11",(today,))
	feedbackitem11=cur.fetchall()
	cur.execute("select count(*), feedbackitem12 FROM `feedbackbreakfast`  where date=(%s) group by feedbackitem12",(today,))
	feedbackitem12=cur.fetchall()
	cur.execute("select count(*), feedbackitem13 FROM `feedbackbreakfast`  where date=(%s) group by feedbackitem13",(today,))
	feedbackitem13=cur.fetchall()
	cur.execute("select count(*), feedbackitem14 FROM `feedbackbreakfast`  where date=(%s) group by feedbackitem14",(today,))
	feedbackitem14=cur.fetchall()
	cur.execute("select count(*), feedbackitem15 FROM `feedbackbreakfast`  where date=(%s) group by feedbackitem15",(today,))
	feedbackitem15=cur.fetchall()

	return render_template("/admincheckbreakfast.html",feedbackitem1=feedbackitem1,feedbackitem2=feedbackitem2,feedbackitem3=feedbackitem3,feedbackitem4=feedbackitem4,feedbackitem5=feedbackitem5,feedbackitem6=feedbackitem6,feedbackitem7=feedbackitem7,feedbackitem8=feedbackitem8,feedbackitem9=feedbackitem9,feedbackitem10=feedbackitem10,feedbackitem11=feedbackitem11,feedbackitem12=feedbackitem12,feedbackitem13=feedbackitem13,feedbackitem14=feedbackitem14,feedbackitem15=feedbackitem15,)


@app.route('/adminchecklunch')
def adminchecklunch():
	today=date.today()
	cur.execute("select count(*), feedbackitem1 FROM `feedbacklunch`  where date=(%s) group by feedbackitem1",(today,))
	feedbackitem1=cur.fetchall()
	cur.execute("select count(*), feedbackitem2 FROM `feedbacklunch`  where date=(%s) group by feedbackitem2",(today,))
	feedbackitem2=cur.fetchall()
	cur.execute("select count(*), feedbackitem3 FROM `feedbacklunch`  where date=(%s) group by feedbackitem3",(today,))
	feedbackitem3=cur.fetchall()
	cur.execute("select count(*), feedbackitem4 FROM `feedbacklunch`  where date=(%s) group by feedbackitem4",(today,))
	feedbackitem4=cur.fetchall()
	cur.execute("select count(*), feedbackitem5 FROM `feedbacklunch`  where date=(%s) group by feedbackitem5",(today,))
	feedbackitem5=cur.fetchall()
	cur.execute("select count(*), feedbackitem6 FROM `feedbacklunch`  where date=(%s) group by feedbackitem6",(today,))
	feedbackitem6=cur.fetchall()
	cur.execute("select count(*), feedbackitem7 FROM `feedbacklunch`  where date=(%s) group by feedbackitem7",(today,))
	feedbackitem7=cur.fetchall()
	cur.execute("select count(*), feedbackitem8 FROM `feedbacklunch`  where date=(%s) group by feedbackitem8",(today,))
	feedbackitem8=cur.fetchall()
	cur.execute("select count(*), feedbackitem9 FROM `feedbacklunch`  where date=(%s) group by feedbackitem9",(today,))
	feedbackitem9=cur.fetchall()
	cur.execute("select count(*), feedbackitem10 FROM `feedbacklunch`  where date=(%s) group by feedbackitem10",(today,))
	feedbackitem10=cur.fetchall()
	cur.execute("select count(*), feedbackitem11 FROM `feedbacklunch`  where date=(%s) group by feedbackitem11",(today,))
	feedbackitem11=cur.fetchall()
	cur.execute("select count(*), feedbackitem12 FROM `feedbacklunch`  where date=(%s) group by feedbackitem12",(today,))
	feedbackitem12=cur.fetchall()
	cur.execute("select count(*), feedbackitem13 FROM `feedbacklunch` where date=(%s) group by feedbackitem13",(today,))
	feedbackitem13=cur.fetchall()
	cur.execute("select count(*), feedbackitem14 FROM `feedbacklunch` where date=(%s) group by feedbackitem14",(today,))
	feedbackitem14=cur.fetchall()
	cur.execute("select count(*), feedbackitem15 FROM `feedbacklunch` where date=(%s) group by feedbackitem15",(today,))
	feedbackitem15=cur.fetchall()
	cur.execute("select count(*), feedbackitem16 FROM `feedbacklunch` where date=(%s) group by feedbackitem16",(today,))
	feedbackitem16=cur.fetchall()
	cur.execute("select count(*), feedbackitem17 FROM `feedbacklunch` where date=(%s) group by feedbackitem17",(today,))
	feedbackitem17=cur.fetchall()
	cur.execute("select count(*), feedbackitem18 FROM `feedbacklunch` where date=(%s) group by feedbackitem18",(today,))
	feedbackitem18=cur.fetchall()
	cur.execute("select count(*), feedbackitem19 FROM `feedbacklunch` where date=(%s) group by feedbackitem19",(today,))
	feedbackitem19=cur.fetchall()
	cur.execute("select count(*), feedbackitem20 FROM `feedbacklunch` where date=(%s) group by feedbackitem20",(today,))
	feedbackitem20=cur.fetchall()

	return render_template("/adminchecklunch.html",feedbackitem1=feedbackitem1,feedbackitem2=feedbackitem2,feedbackitem3=feedbackitem3,feedbackitem4=feedbackitem4,feedbackitem5=feedbackitem5,feedbackitem6=feedbackitem6,feedbackitem7=feedbackitem7,feedbackitem8=feedbackitem8,feedbackitem9=feedbackitem9,feedbackitem10=feedbackitem10,feedbackitem11=feedbackitem11,feedbackitem12=feedbackitem12,feedbackitem13=feedbackitem13,feedbackitem14=feedbackitem14,feedbackitem15=feedbackitem15,feedbackitem16=feedbackitem16,feedbackitem17=feedbackitem17,feedbackitem18=feedbackitem18,feedbackitem19=feedbackitem19,feedbackitem20=feedbackitem20,)

@app.route('/admincheckdinner')
def admincheckdinner():
	today=date.today()
	cur.execute("select count(*), feedbackitem1 FROM `feedbackdinner`  where date=(%s) group by feedbackitem1",(today,))
	feedbackitem1=cur.fetchall()
	cur.execute("select count(*), feedbackitem2 FROM `feedbackdinner` where date=(%s) group by feedbackitem2",(today,))
	feedbackitem2=cur.fetchall()
	cur.execute("select count(*), feedbackitem3 FROM `feedbackdinner` where date=(%s) group by feedbackitem3",(today,))
	feedbackitem3=cur.fetchall()
	cur.execute("select count(*), feedbackitem4 FROM `feedbackdinner` where date=(%s) group by feedbackitem4",(today,))
	feedbackitem4=cur.fetchall()
	cur.execute("select count(*), feedbackitem5 FROM `feedbackdinner` where date=(%s) group by feedbackitem5",(today,))
	feedbackitem5=cur.fetchall()
	cur.execute("select count(*), feedbackitem6 FROM `feedbackdinner` where date=(%s) group by feedbackitem6",(today,))
	feedbackitem6=cur.fetchall()
	cur.execute("select count(*), feedbackitem7 FROM `feedbackdinner` where date=(%s) group by feedbackitem7",(today,))
	feedbackitem7=cur.fetchall()
	cur.execute("select count(*), feedbackitem8 FROM `feedbackdinner` where date=(%s) group by feedbackitem8",(today,))
	feedbackitem8=cur.fetchall()
	cur.execute("select count(*), feedbackitem9 FROM `feedbackdinner` where date=(%s) group by feedbackitem9",(today,))
	feedbackitem9=cur.fetchall()
	cur.execute("select count(*), feedbackitem10 FROM `feedbackdinner` where date=(%s) group by feedbackitem10",(today,))
	feedbackitem10=cur.fetchall()
	cur.execute("select count(*), feedbackitem11 FROM `feedbackdinner` where date=(%s) group by feedbackitem11",(today,))
	feedbackitem11=cur.fetchall()
	cur.execute("select count(*), feedbackitem12 FROM `feedbackdinner` where date=(%s) group by feedbackitem12",(today,))
	feedbackitem12=cur.fetchall()
	cur.execute("select count(*), feedbackitem13 FROM `feedbackdinner` where date=(%s) group by feedbackitem13",(today,))
	feedbackitem13=cur.fetchall()
	cur.execute("select count(*), feedbackitem14 FROM `feedbackdinner` where date=(%s) group by feedbackitem14",(today,))
	feedbackitem14=cur.fetchall()
	cur.execute("select count(*), feedbackitem15 FROM `feedbackdinner` where date=(%s) group by feedbackitem15",(today,))
	feedbackitem15=cur.fetchall()
	cur.execute("select count(*), feedbackitem16 FROM `feedbackdinner` where date=(%s) group by feedbackitem16",(today,))
	feedbackitem16=cur.fetchall()
	cur.execute("select count(*), feedbackitem17 FROM `feedbackdinner` where date=(%s) group by feedbackitem17",(today,))
	feedbackitem17=cur.fetchall()
	cur.execute("select count(*), feedbackitem18 FROM `feedbackdinner` where date=(%s) group by feedbackitem18",(today,))
	feedbackitem18=cur.fetchall()
	cur.execute("select count(*), feedbackitem19 FROM `feedbackdinner` where date=(%s) group by feedbackitem19",(today,))
	feedbackitem19=cur.fetchall()
	cur.execute("select count(*), feedbackitem20 FROM `feedbackdinner` where date=(%s) group by feedbackitem20",(today,))
	feedbackitem20=cur.fetchall()

	return render_template("/admincheckdinner.html",feedbackitem1=feedbackitem1,feedbackitem2=feedbackitem2,feedbackitem3=feedbackitem3,feedbackitem4=feedbackitem4,feedbackitem5=feedbackitem5,feedbackitem6=feedbackitem6,feedbackitem7=feedbackitem7,feedbackitem8=feedbackitem8,feedbackitem9=feedbackitem9,feedbackitem10=feedbackitem10,feedbackitem11=feedbackitem11,feedbackitem12=feedbackitem12,feedbackitem13=feedbackitem13,feedbackitem14=feedbackitem14,feedbackitem15=feedbackitem15,feedbackitem16=feedbackitem16,feedbackitem17=feedbackitem17,feedbackitem18=feedbackitem18,feedbackitem19=feedbackitem19,feedbackitem20=feedbackitem20)


@app.route('/admincheckattendance')
def admincheckattendance():
	today=date.today()
	cur.execute("select count(*) FROM `studentattendance` where breakfast='morning' and date=(%s)",(today,))
	feedbackitem1=cur.fetchall()

	cur.execute("select count(*) FROM `studentattendance` where lunch='afternoon' and date=(%s)",(today,))
	feedbackitem2=cur.fetchall()
	
	cur.execute("select count(*) FROM `studentattendance` where dinner='night' and date=(%s)",(today,))
	feedbackitem3=cur.fetchall()
	

	return render_template("/admincheckattendance.html", data1=feedbackitem1, data2=feedbackitem2, data3=feedbackitem3)

@app.route('/admincheckattendancefaculty')
def admincheckattendancefaculty():
	today=date.today()
	cur.execute("select count(*) FROM `facultyattendance` where breakfast='morning' and date=(%s)",(today,))
	feedbackitem1=cur.fetchall()

	cur.execute("select count(*) FROM `facultyattendance` where lunch='afternoon' and date=(%s)",(today,))
	feedbackitem2=cur.fetchall()
	
	cur.execute("select count(*) FROM `facultyattendance` where dinner='night' and date=(%s)",(today,))
	feedbackitem3=cur.fetchall()
	

	return render_template("/admincheckattendancefaculty.html", data1=feedbackitem1, data2=feedbackitem2, data3=feedbackitem3)

@app.route('/adminupdatestudentfaculty')
def adminupdatestudentfaculty():
	return redirect(url_for('managementhome'))

@app.route('/studentsuggestionsadmin')
def studentsuggestionsadmin():
	today=date.today()
	cur.execute("select * FROM `studentsuggestions` where date=(%s)",(today,))
	suggestions=cur.fetchall()
	return render_template("/suggestionsadmin.html",data=suggestions)

@app.route('/facultysuggestionsadmin')
def facultysuggestionsadmin():
	today=date.today()
	cur.execute("select * FROM `facultysuggestions`where date=(%s)",(today,))
	suggestions=cur.fetchall()
	return render_template("/suggestionsadmin.html",data=suggestions)

@app.route('/adminreportfeedback')
def adminreportfeedback():
	return render_template("/adminreport.html")
@app.route('/adminreportfeedback1', methods=['POST'])
def adminreportfeedback1():
	i1=request.form['from']
	i2=request.form['to']
	cur.execute("select count(*), feedbackitem1 FROM `feedbackbreakfast` where date BETWEEN %s AND %s group by feedbackitem1",(i1,i2))
	feedbackitem1=cur.fetchall()
	cur.execute("select count(*), feedbackitem2 FROM `feedbackbreakfast`  where date BETWEEN %s AND %s group by feedbackitem2",(i1,i2))
	feedbackitem2=cur.fetchall()
	cur.execute("select count(*), feedbackitem3 FROM `feedbackbreakfast`  where date BETWEEN %s AND %s group by feedbackitem3",(i1,i2))
	feedbackitem3=cur.fetchall()
	cur.execute("select count(*), feedbackitem4 FROM `feedbackbreakfast`  where date BETWEEN %s AND %s group by feedbackitem4",(i1,i2))
	feedbackitem4=cur.fetchall()
	cur.execute("select count(*), feedbackitem5 FROM `feedbackbreakfast`  where date BETWEEN %s AND %s group by feedbackitem5",(i1,i2))
	feedbackitem5=cur.fetchall()
	cur.execute("select count(*), feedbackitem6 FROM `feedbackbreakfast`  where date BETWEEN %s AND %s group by feedbackitem6",(i1,i2))
	feedbackitem6=cur.fetchall()
	cur.execute("select count(*), feedbackitem7 FROM `feedbackbreakfast`  where date BETWEEN %s AND %s group by feedbackitem7",(i1,i2))
	feedbackitem7=cur.fetchall()
	cur.execute("select count(*), feedbackitem8 FROM `feedbackbreakfast`  where date BETWEEN %s AND %s group by feedbackitem8",(i1,i2))
	feedbackitem8=cur.fetchall()
	cur.execute("select count(*), feedbackitem9 FROM `feedbackbreakfast`  where date BETWEEN %s AND %s group by feedbackitem9",(i1,i2))
	feedbackitem9=cur.fetchall()
	cur.execute("select count(*), feedbackitem10 FROM `feedbackbreakfast`  where date BETWEEN %s AND %s group by feedbackitem10",(i1,i2))
	feedbackitem10=cur.fetchall()
	cur.execute("select count(*), feedbackitem11 FROM `feedbackbreakfast`  where date BETWEEN %s AND %s group by feedbackitem11",(i1,i2))
	feedbackitem11=cur.fetchall()
	cur.execute("select count(*), feedbackitem12 FROM `feedbackbreakfast`  where date BETWEEN %s AND %s group by feedbackitem12",(i1,i2))
	feedbackitem12=cur.fetchall()
	cur.execute("select count(*), feedbackitem13 FROM `feedbackbreakfast`  where date BETWEEN %s AND %s group by feedbackitem13",(i1,i2))
	feedbackitem13=cur.fetchall()
	cur.execute("select count(*), feedbackitem14 FROM `feedbackbreakfast`  where date BETWEEN %s AND %s group by feedbackitem14",(i1,i2))
	feedbackitem14=cur.fetchall()
	cur.execute("select count(*), feedbackitem15 FROM `feedbackbreakfast`  where date BETWEEN %s AND %s group by feedbackitem15",(i1,i2))
	feedbackitem15=cur.fetchall()

	return render_template("/admincheckbreakfast.html",feedbackitem1=feedbackitem1,feedbackitem2=feedbackitem2,feedbackitem3=feedbackitem3,feedbackitem4=feedbackitem4,feedbackitem5=feedbackitem5,feedbackitem6=feedbackitem6,feedbackitem7=feedbackitem7,feedbackitem8=feedbackitem8,feedbackitem9=feedbackitem9,feedbackitem10=feedbackitem10,feedbackitem11=feedbackitem11,feedbackitem12=feedbackitem12,feedbackitem13=feedbackitem13,feedbackitem14=feedbackitem14,feedbackitem15=feedbackitem15,)


@app.route('/adminreportfeedbacklunch')
def adminreportfeedbacklunch():
	return render_template("/adminreportlunch.html")
@app.route('/adminreportfeedbacklunch1', methods=['POST'])
def adminreportfeedbacklunch1():
	i1=request.form['from']
	i2=request.form['to']
	cur.execute("select count(*), feedbackitem1 FROM `feedbacklunch`  where date BETWEEN %s AND %s group by feedbackitem1",(i1,i2,))
	feedbackitem1=cur.fetchall()
	cur.execute("select count(*), feedbackitem2 FROM `feedbacklunch`  where date BETWEEN %s AND %s group by feedbackitem2",(i1,i2))
	feedbackitem2=cur.fetchall()
	cur.execute("select count(*), feedbackitem3 FROM `feedbacklunch`  where date BETWEEN %s AND %s group by feedbackitem3",(i1,i2))
	feedbackitem3=cur.fetchall()
	cur.execute("select count(*), feedbackitem4 FROM `feedbacklunch`  where date BETWEEN %s AND %s group by feedbackitem4",(i1,i2))
	feedbackitem4=cur.fetchall()
	cur.execute("select count(*), feedbackitem5 FROM `feedbacklunch`  where date BETWEEN %s AND %s group by feedbackitem5",(i1,i2))
	feedbackitem5=cur.fetchall()
	cur.execute("select count(*), feedbackitem6 FROM `feedbacklunch`  where date BETWEEN %s AND %s group by feedbackitem6",(i1,i2))
	feedbackitem6=cur.fetchall()
	cur.execute("select count(*), feedbackitem7 FROM `feedbacklunch`  where date BETWEEN %s AND %s group by feedbackitem7",(i1,i2))
	feedbackitem7=cur.fetchall()
	cur.execute("select count(*), feedbackitem8 FROM `feedbacklunch`  where date BETWEEN %s AND %s group by feedbackitem8",(i1,i2))
	feedbackitem8=cur.fetchall()
	cur.execute("select count(*), feedbackitem9 FROM `feedbacklunch`  where date BETWEEN %s AND %s group by feedbackitem9",(i1,i2))
	feedbackitem9=cur.fetchall()
	cur.execute("select count(*), feedbackitem10 FROM `feedbacklunch`  where date BETWEEN %s AND %s group by feedbackitem10",(i1,i2))
	feedbackitem10=cur.fetchall()
	cur.execute("select count(*), feedbackitem11 FROM `feedbacklunch`  where date BETWEEN %s AND %s group by feedbackitem11",(i1,i2))
	feedbackitem11=cur.fetchall()
	cur.execute("select count(*), feedbackitem12 FROM `feedbacklunch`  where date BETWEEN %s AND %s group by feedbackitem12",(i1,i2))
	feedbackitem12=cur.fetchall()
	cur.execute("select count(*), feedbackitem13 FROM `feedbacklunch` where date BETWEEN %s AND %s group by feedbackitem13",(i1,i2))
	feedbackitem13=cur.fetchall()
	cur.execute("select count(*), feedbackitem14 FROM `feedbacklunch` where date BETWEEN %s AND %s group by feedbackitem14",(i1,i2))
	feedbackitem14=cur.fetchall()
	cur.execute("select count(*), feedbackitem15 FROM `feedbacklunch` where date BETWEEN %s AND %s group by feedbackitem15",(i1,i2))
	feedbackitem15=cur.fetchall()
	cur.execute("select count(*), feedbackitem16 FROM `feedbacklunch` where date BETWEEN %s AND %s group by feedbackitem16",(i1,i2))
	feedbackitem16=cur.fetchall()
	cur.execute("select count(*), feedbackitem17 FROM `feedbacklunch` where date BETWEEN %s AND %s group by feedbackitem17",(i1,i2))
	feedbackitem17=cur.fetchall()
	cur.execute("select count(*), feedbackitem18 FROM `feedbacklunch` where date BETWEEN %s AND %s group by feedbackitem18",(i1,i2))
	feedbackitem18=cur.fetchall()
	cur.execute("select count(*), feedbackitem19 FROM `feedbacklunch` where date BETWEEN %s AND %s group by feedbackitem19",(i1,i2))
	feedbackitem19=cur.fetchall()
	cur.execute("select count(*), feedbackitem20 FROM `feedbacklunch` where date BETWEEN %s AND %s group by feedbackitem20",(i1,i2))
	feedbackitem20=cur.fetchall()

	return render_template("/adminchecklunch.html",feedbackitem1=feedbackitem1,feedbackitem2=feedbackitem2,feedbackitem3=feedbackitem3,feedbackitem4=feedbackitem4,feedbackitem5=feedbackitem5,feedbackitem6=feedbackitem6,feedbackitem7=feedbackitem7,feedbackitem8=feedbackitem8,feedbackitem9=feedbackitem9,feedbackitem10=feedbackitem10,feedbackitem11=feedbackitem11,feedbackitem12=feedbackitem12,feedbackitem13=feedbackitem13,feedbackitem14=feedbackitem14,feedbackitem15=feedbackitem15,feedbackitem16=feedbackitem16,feedbackitem17=feedbackitem17,feedbackitem18=feedbackitem18,feedbackitem19=feedbackitem19,feedbackitem20=feedbackitem20,)


@app.route('/adminreportfeedbackdinner')
def adminreportfeedbackdinner():
	return render_template("/adminreportdinner.html")
@app.route('/adminreportfeedbackdinner1', methods=['POST'])
def adminreportfeedbackdinner1():
	i1=request.form['from']
	i2=request.form['to']
	cur.execute("select count(*), feedbackitem1 FROM `feedbackdinner`  where date BETWEEN %s AND %s group by feedbackitem1",(i1,i2,))
	feedbackitem1=cur.fetchall()
	cur.execute("select count(*), feedbackitem2 FROM `feedbackdinner`  where date BETWEEN %s AND %s group by feedbackitem2",(i1,i2))
	feedbackitem2=cur.fetchall()
	cur.execute("select count(*), feedbackitem3 FROM `feedbackdinner`  where date BETWEEN %s AND %s group by feedbackitem3",(i1,i2))
	feedbackitem3=cur.fetchall()
	cur.execute("select count(*), feedbackitem4 FROM `feedbackdinner`  where date BETWEEN %s AND %s group by feedbackitem4",(i1,i2))
	feedbackitem4=cur.fetchall()
	cur.execute("select count(*), feedbackitem5 FROM `feedbackdinner`  where date BETWEEN %s AND %s group by feedbackitem5",(i1,i2))
	feedbackitem5=cur.fetchall()
	cur.execute("select count(*), feedbackitem6 FROM `feedbackdinner`  where date BETWEEN %s AND %s group by feedbackitem6",(i1,i2))
	feedbackitem6=cur.fetchall()
	cur.execute("select count(*), feedbackitem7 FROM `feedbackdinner`  where date BETWEEN %s AND %s group by feedbackitem7",(i1,i2))
	feedbackitem7=cur.fetchall()
	cur.execute("select count(*), feedbackitem8 FROM `feedbackdinner`  where date BETWEEN %s AND %s group by feedbackitem8",(i1,i2))
	feedbackitem8=cur.fetchall()
	cur.execute("select count(*), feedbackitem9 FROM `feedbackdinner`  where date BETWEEN %s AND %s group by feedbackitem9",(i1,i2))
	feedbackitem9=cur.fetchall()
	cur.execute("select count(*), feedbackitem10 FROM `feedbackdinner`  where date BETWEEN %s AND %s group by feedbackitem10",(i1,i2))
	feedbackitem10=cur.fetchall()
	cur.execute("select count(*), feedbackitem11 FROM `feedbackdinner`  where date BETWEEN %s AND %s group by feedbackitem11",(i1,i2))
	feedbackitem11=cur.fetchall()
	cur.execute("select count(*), feedbackitem12 FROM `feedbackdinner`  where date BETWEEN %s AND %s group by feedbackitem12",(i1,i2))
	feedbackitem12=cur.fetchall()
	cur.execute("select count(*), feedbackitem13 FROM `feedbackdinner` where date BETWEEN %s AND %s group by feedbackitem13",(i1,i2))
	feedbackitem13=cur.fetchall()
	cur.execute("select count(*), feedbackitem14 FROM `feedbackdinner` where date BETWEEN %s AND %s group by feedbackitem14",(i1,i2))
	feedbackitem14=cur.fetchall()
	cur.execute("select count(*), feedbackitem15 FROM `feedbackdinner` where date BETWEEN %s AND %s group by feedbackitem15",(i1,i2))
	feedbackitem15=cur.fetchall()
	cur.execute("select count(*), feedbackitem16 FROM `feedbackdinner` where date BETWEEN %s AND %s group by feedbackitem16",(i1,i2))
	feedbackitem16=cur.fetchall()
	cur.execute("select count(*), feedbackitem17 FROM `feedbackdinner` where date BETWEEN %s AND %s group by feedbackitem17",(i1,i2))
	feedbackitem17=cur.fetchall()
	cur.execute("select count(*), feedbackitem18 FROM `feedbackdinner` where date BETWEEN %s AND %s group by feedbackitem18",(i1,i2))
	feedbackitem18=cur.fetchall()
	cur.execute("select count(*), feedbackitem19 FROM `feedbackdinner` where date BETWEEN %s AND %s group by feedbackitem19",(i1,i2))
	feedbackitem19=cur.fetchall()
	cur.execute("select count(*), feedbackitem20 FROM `feedbackdinner` where date BETWEEN %s AND %s group by feedbackitem20",(i1,i2))
	feedbackitem20=cur.fetchall()

	return render_template("/admincheckdinner.html",feedbackitem1=feedbackitem1,feedbackitem2=feedbackitem2,feedbackitem3=feedbackitem3,feedbackitem4=feedbackitem4,feedbackitem5=feedbackitem5,feedbackitem6=feedbackitem6,feedbackitem7=feedbackitem7,feedbackitem8=feedbackitem8,feedbackitem9=feedbackitem9,feedbackitem10=feedbackitem10,feedbackitem11=feedbackitem11,feedbackitem12=feedbackitem12,feedbackitem13=feedbackitem13,feedbackitem14=feedbackitem14,feedbackitem15=feedbackitem15,feedbackitem16=feedbackitem16,feedbackitem17=feedbackitem17,feedbackitem18=feedbackitem18,feedbackitem19=feedbackitem19,feedbackitem20=feedbackitem20,)




#@app.route('/studentdata')
#def studentdata():
#	return render_template("studentdata.html")
@app.route('/studentdata')
def studentdata():
	cur.execute("select * from registrationformstudent")
	All=cur.fetchall()
	return render_template("/studentdata.html",data=All)

@app.route('/studentdatadelete', methods=['POST'])
def studentdatadelete():
	i1=request.form['studentid']
	val=cur.execute("Delete from registrationformstudent where id=(%s)",(i1,))
	res = mydb.commit()
	cur.execute("select * from registrationformstudent")
	All=cur.fetchall()
	return render_template("/studentdata.html",data=All)

@app.route('/breakfastdelete', methods=['POST'])
def breakfastdelete():
	today=date.today()
	i1=request.form['studentid']
	val=cur.execute("Delete from itemlist where id=(%s)",(i1,))
	res = mydb.commit()
	cur.execute("select * from itemlist where date=(%s)",(today,))
	All=cur.fetchall()
	return render_template("/viewbreakfast.html",data=All)

@app.route('/lunchdelete', methods=['POST'])
def lunchdelete():
	today=date.today()
	i1=request.form['studentid']
	val=cur.execute("Delete from itemlistlunch where id=(%s)",(i1,))
	res = mydb.commit()
	cur.execute("select * from itemlistlunch where date=(%s)",(today,))
	All=cur.fetchall()
	return render_template("/viewlunch.html",data=All)

@app.route('/dinnerdelete', methods=['POST'])
def dinnerdelete():
	today=date.today()
	i1=request.form['studentid']
	val=cur.execute("Delete from itemlistdinner where id=(%s)",(i1,))
	res = mydb.commit()
	cur.execute("select * from itemlistdinner where date=(%s)",(today,))
	All=cur.fetchall()
	return render_template("/viewdinner.html",data=All)

@app.route('/facultydatadelete', methods=['POST'])
def facultydatadelete():
	i1=request.form['facultyid']
	val=cur.execute("Delete from registrationformfaculty where id=(%s)",(i1,))
	res = mydb.commit()
	cur.execute("select * from registrationformfaculty")
	All=cur.fetchall()
	return render_template("/facultydata.html",data=All)
	
#@app.route('/facultydata')
#def facultydata():
	#return render_template("facultydata.html")
@app.route('/facultydata')
def facultydata():
	cur.execute("select * from registrationformfaculty")
	All=cur.fetchall()
	return render_template("/facultydata.html",data=All)

@app.route('/adminupdateprofile')
def adminupdateprofile1():
	if not UserID:
		return redirect(url_for('adminlogin'))
	else:
		return render_template("profileadmin.html")

@app.route('/adminupdateprofile', methods=['POST'])
def adminupdateprofile():
	if not UserID:
		return redirect(url_for('adminlogin'))
	else:
		oldpassword =  request.form['old']
		newpassword =  request.form['new']
		confirmnewpassword =  request.form['confirm']
		temp_id=str(UserID)
		print(UserID)
		print(UserID)
		print(UserID)
		print(UserID)
		print(UserID)
		cur.execute("select * from admin where admin_id=(%s) and admin_id=(%s)",(temp_id,temp_id))
		All=cur.fetchone()
		print(All)
		if All:
			if str(All[2])!=str(oldpassword):
				return render_template("profileadmin.html", data="Old Password not matched")
			else:
				val=cur.execute("update admin set admin_user_password=(%s) where admin_id=(%s)",(newpassword,UserID))
				res = mydb.commit()
				return render_template("profileadmin.html", data='Password update success')

	






#admin end

#management start

@app.route('/managementlogin')
def managementlogin():
	return render_template("managementlogin.html")

@app.route('/managementlogin', methods=['POST'])
def managementlogin1():
	name =  request.form['username']
	password =  request.form['password']
	cur.execute("select * from management where management_user_name=(%s) and management_user_password=(%s)",(name,password))
	All=cur.fetchall()
	global All_data
	global UserID
	global UserName
	All_data = All
	UserID = All_data[0][0]
	UserName = All_data[0][1]
	count = len(All_data)
	if count==1:
		return redirect(url_for('managementhome'))
	else:
		return render_template("/managementlogin.html", error='Please enter valid details')

@app.route('/managementhome')
def managementhome():
	if UserID=="":
		return redirect(url_for('managementlogin'))
	else:
		return render_template("/managementhome.html",data=All_data,UserName=UserName,UserID=UserID)

@app.route('/managementlogout')
def managementlogout():
	global UserID
	global UserName
	UserName = ""
	UserID=""
	return render_template("managementlogin.html")

@app.route('/managementbreak')
def managementbreak():
	today=date.today()
	cur.execute("select * from itemlist where date=(%s)",(today,))
	All=cur.fetchall()
	return render_template("/managementbreak.html",data=All)
@app.route('/managementlunch')
def managementlunch():
	today=date.today()
	cur.execute("select * from itemlistlunch where date=(%s)",(today,))
	All=cur.fetchall()
	return render_template("/managementlunch.html",data=All)
@app.route('/managementdinner')
def managementdinner():
	today=date.today()
	cur.execute("select * from itemlistdinner where date=(%s)",(today,))
	All=cur.fetchall()
	return render_template("/managementdinner.html",data=All)

@app.route('/managementstudent')
def managementstudent():
	cur.execute("select * from registrationformstudent")
	All=cur.fetchall()
	return render_template("/studentmanagement.html",data=All)


@app.route('/managementfaculty')
def managementfaculty():
	cur.execute("select * from registrationformfaculty")
	All=cur.fetchall()
	return render_template("/facultymanagement.html",data=All)

@app.route('/managementcheckbreakfast')
def managementcheckbreakfast():
	today=date.today()
	cur.execute("select count(*), feedbackitem1 FROM `feedbackbreakfast` where date=(%s) group by feedbackitem1",(today,))
	feedbackitem1=cur.fetchall()
	cur.execute("select count(*), feedbackitem2 FROM `feedbackbreakfast`  where date=(%s) group by feedbackitem2",(today,))
	feedbackitem2=cur.fetchall()
	cur.execute("select count(*), feedbackitem3 FROM `feedbackbreakfast`  where date=(%s) group by feedbackitem3",(today,))
	feedbackitem3=cur.fetchall()
	cur.execute("select count(*), feedbackitem4 FROM `feedbackbreakfast`  where date=(%s) group by feedbackitem4",(today,))
	feedbackitem4=cur.fetchall()
	cur.execute("select count(*), feedbackitem5 FROM `feedbackbreakfast`  where date=(%s) group by feedbackitem5",(today,))
	feedbackitem5=cur.fetchall()
	cur.execute("select count(*), feedbackitem6 FROM `feedbackbreakfast`  where date=(%s) group by feedbackitem6",(today,))
	feedbackitem6=cur.fetchall()
	cur.execute("select count(*), feedbackitem7 FROM `feedbackbreakfast`  where date=(%s) group by feedbackitem7",(today,))
	feedbackitem7=cur.fetchall()
	cur.execute("select count(*), feedbackitem8 FROM `feedbackbreakfast`  where date=(%s) group by feedbackitem8",(today,))
	feedbackitem8=cur.fetchall()
	cur.execute("select count(*), feedbackitem9 FROM `feedbackbreakfast`  where date=(%s) group by feedbackitem9",(today,))
	feedbackitem9=cur.fetchall()
	cur.execute("select count(*), feedbackitem10 FROM `feedbackbreakfast`  where date=(%s) group by feedbackitem10",(today,))
	feedbackitem10=cur.fetchall()
	cur.execute("select count(*), feedbackitem11 FROM `feedbackbreakfast`  where date=(%s) group by feedbackitem11",(today,))
	feedbackitem11=cur.fetchall()
	cur.execute("select count(*), feedbackitem12 FROM `feedbackbreakfast`  where date=(%s) group by feedbackitem12",(today,))
	feedbackitem12=cur.fetchall()
	cur.execute("select count(*), feedbackitem13 FROM `feedbackbreakfast`  where date=(%s) group by feedbackitem13",(today,))
	feedbackitem13=cur.fetchall()
	cur.execute("select count(*), feedbackitem14 FROM `feedbackbreakfast`  where date=(%s) group by feedbackitem14",(today,))
	feedbackitem14=cur.fetchall()
	cur.execute("select count(*), feedbackitem15 FROM `feedbackbreakfast`  where date=(%s) group by feedbackitem15",(today,))
	feedbackitem15=cur.fetchall()

	return render_template("/managementcheckbreakfast.html",feedbackitem1=feedbackitem1,feedbackitem2=feedbackitem2,feedbackitem3=feedbackitem3,feedbackitem4=feedbackitem4,feedbackitem5=feedbackitem5,feedbackitem6=feedbackitem6,feedbackitem7=feedbackitem7,feedbackitem8=feedbackitem8,feedbackitem9=feedbackitem9,feedbackitem10=feedbackitem10,feedbackitem11=feedbackitem11,feedbackitem12=feedbackitem12,feedbackitem13=feedbackitem13,feedbackitem14=feedbackitem14,feedbackitem15=feedbackitem15,)

@app.route('/managementchecklunch')
def managementchecklunch():
	today=date.today()
	cur.execute("select count(*), feedbackitem1 FROM `feedbacklunch`  where date=(%s) group by feedbackitem1",(today,))
	feedbackitem1=cur.fetchall()
	cur.execute("select count(*), feedbackitem2 FROM `feedbacklunch`  where date=(%s) group by feedbackitem2",(today,))
	feedbackitem2=cur.fetchall()
	cur.execute("select count(*), feedbackitem3 FROM `feedbacklunch`  where date=(%s) group by feedbackitem3",(today,))
	feedbackitem3=cur.fetchall()
	cur.execute("select count(*), feedbackitem4 FROM `feedbacklunch`  where date=(%s) group by feedbackitem4",(today,))
	feedbackitem4=cur.fetchall()
	cur.execute("select count(*), feedbackitem5 FROM `feedbacklunch`  where date=(%s) group by feedbackitem5",(today,))
	feedbackitem5=cur.fetchall()
	cur.execute("select count(*), feedbackitem6 FROM `feedbacklunch`  where date=(%s) group by feedbackitem6",(today,))
	feedbackitem6=cur.fetchall()
	cur.execute("select count(*), feedbackitem7 FROM `feedbacklunch`  where date=(%s) group by feedbackitem7",(today,))
	feedbackitem7=cur.fetchall()
	cur.execute("select count(*), feedbackitem8 FROM `feedbacklunch`  where date=(%s) group by feedbackitem8",(today,))
	feedbackitem8=cur.fetchall()
	cur.execute("select count(*), feedbackitem9 FROM `feedbacklunch`  where date=(%s) group by feedbackitem9",(today,))
	feedbackitem9=cur.fetchall()
	cur.execute("select count(*), feedbackitem10 FROM `feedbacklunch`  where date=(%s) group by feedbackitem10",(today,))
	feedbackitem10=cur.fetchall()
	cur.execute("select count(*), feedbackitem11 FROM `feedbacklunch`  where date=(%s) group by feedbackitem11",(today,))
	feedbackitem11=cur.fetchall()
	cur.execute("select count(*), feedbackitem12 FROM `feedbacklunch`  where date=(%s) group by feedbackitem12",(today,))
	feedbackitem12=cur.fetchall()
	cur.execute("select count(*), feedbackitem13 FROM `feedbacklunch` where date=(%s) group by feedbackitem13",(today,))
	feedbackitem13=cur.fetchall()
	cur.execute("select count(*), feedbackitem14 FROM `feedbacklunch` where date=(%s) group by feedbackitem14",(today,))
	feedbackitem14=cur.fetchall()
	cur.execute("select count(*), feedbackitem15 FROM `feedbacklunch` where date=(%s) group by feedbackitem15",(today,))
	feedbackitem15=cur.fetchall()
	cur.execute("select count(*), feedbackitem16 FROM `feedbacklunch` where date=(%s) group by feedbackitem16",(today,))
	feedbackitem16=cur.fetchall()
	cur.execute("select count(*), feedbackitem17 FROM `feedbacklunch` where date=(%s) group by feedbackitem17",(today,))
	feedbackitem17=cur.fetchall()
	cur.execute("select count(*), feedbackitem18 FROM `feedbacklunch` where date=(%s) group by feedbackitem18",(today,))
	feedbackitem18=cur.fetchall()
	cur.execute("select count(*), feedbackitem19 FROM `feedbacklunch` where date=(%s) group by feedbackitem19",(today,))
	feedbackitem19=cur.fetchall()
	cur.execute("select count(*), feedbackitem20 FROM `feedbacklunch` where date=(%s) group by feedbackitem20",(today,))
	feedbackitem20=cur.fetchall()


	return render_template("/managementchecklunch.html",feedbackitem1=feedbackitem1,feedbackitem2=feedbackitem2,feedbackitem3=feedbackitem3,feedbackitem4=feedbackitem4,feedbackitem5=feedbackitem5,feedbackitem6=feedbackitem6,feedbackitem7=feedbackitem7,feedbackitem8=feedbackitem8,feedbackitem9=feedbackitem9,feedbackitem10=feedbackitem10,feedbackitem11=feedbackitem11,feedbackitem12=feedbackitem12,feedbackitem13=feedbackitem13,feedbackitem14=feedbackitem14,feedbackitem15=feedbackitem15,feedbackitem16=feedbackitem16,feedbackitem17=feedbackitem17,feedbackitem18=feedbackitem18,feedbackitem19=feedbackitem19,feedbackitem20=feedbackitem20,)

@app.route('/managementcheckdinner')
def managementcheckdinner():
	today=date.today()
	cur.execute("select count(*), feedbackitem1 FROM `feedbackdinner`  where date=(%s) group by feedbackitem1",(today,))
	feedbackitem1=cur.fetchall()
	cur.execute("select count(*), feedbackitem2 FROM `feedbackdinner` where date=(%s) group by feedbackitem2",(today,))
	feedbackitem2=cur.fetchall()
	cur.execute("select count(*), feedbackitem3 FROM `feedbackdinner` where date=(%s) group by feedbackitem3",(today,))
	feedbackitem3=cur.fetchall()
	cur.execute("select count(*), feedbackitem4 FROM `feedbackdinner` where date=(%s) group by feedbackitem4",(today,))
	feedbackitem4=cur.fetchall()
	cur.execute("select count(*), feedbackitem5 FROM `feedbackdinner` where date=(%s) group by feedbackitem5",(today,))
	feedbackitem5=cur.fetchall()
	cur.execute("select count(*), feedbackitem6 FROM `feedbackdinner` where date=(%s) group by feedbackitem6",(today,))
	feedbackitem6=cur.fetchall()
	cur.execute("select count(*), feedbackitem7 FROM `feedbackdinner` where date=(%s) group by feedbackitem7",(today,))
	feedbackitem7=cur.fetchall()
	cur.execute("select count(*), feedbackitem8 FROM `feedbackdinner` where date=(%s) group by feedbackitem8",(today,))
	feedbackitem8=cur.fetchall()
	cur.execute("select count(*), feedbackitem9 FROM `feedbackdinner` where date=(%s) group by feedbackitem9",(today,))
	feedbackitem9=cur.fetchall()
	cur.execute("select count(*), feedbackitem10 FROM `feedbackdinner` where date=(%s) group by feedbackitem10",(today,))
	feedbackitem10=cur.fetchall()
	cur.execute("select count(*), feedbackitem11 FROM `feedbackdinner` where date=(%s) group by feedbackitem11",(today,))
	feedbackitem11=cur.fetchall()
	cur.execute("select count(*), feedbackitem12 FROM `feedbackdinner` where date=(%s) group by feedbackitem12",(today,))
	feedbackitem12=cur.fetchall()
	cur.execute("select count(*), feedbackitem13 FROM `feedbackdinner` where date=(%s) group by feedbackitem13",(today,))
	feedbackitem13=cur.fetchall()
	cur.execute("select count(*), feedbackitem14 FROM `feedbackdinner` where date=(%s) group by feedbackitem14",(today,))
	feedbackitem14=cur.fetchall()
	cur.execute("select count(*), feedbackitem15 FROM `feedbackdinner` where date=(%s) group by feedbackitem15",(today,))
	feedbackitem15=cur.fetchall()
	cur.execute("select count(*), feedbackitem16 FROM `feedbackdinner` where date=(%s) group by feedbackitem16",(today,))
	feedbackitem16=cur.fetchall()
	cur.execute("select count(*), feedbackitem17 FROM `feedbackdinner` where date=(%s) group by feedbackitem17",(today,))
	feedbackitem17=cur.fetchall()
	cur.execute("select count(*), feedbackitem18 FROM `feedbackdinner` where date=(%s) group by feedbackitem18",(today,))
	feedbackitem18=cur.fetchall()
	cur.execute("select count(*), feedbackitem19 FROM `feedbackdinner` where date=(%s) group by feedbackitem19",(today,))
	feedbackitem19=cur.fetchall()
	cur.execute("select count(*), feedbackitem20 FROM `feedbackdinner` where date=(%s) group by feedbackitem20",(today,))
	feedbackitem20=cur.fetchall()

	return render_template("/managementcheckdinner.html",feedbackitem1=feedbackitem1,feedbackitem2=feedbackitem2,feedbackitem3=feedbackitem3,feedbackitem4=feedbackitem4,feedbackitem5=feedbackitem5,feedbackitem6=feedbackitem6,feedbackitem7=feedbackitem7,feedbackitem8=feedbackitem8,feedbackitem9=feedbackitem9,feedbackitem10=feedbackitem10,feedbackitem11=feedbackitem11,feedbackitem12=feedbackitem12,feedbackitem13=feedbackitem13,feedbackitem14=feedbackitem14,feedbackitem15=feedbackitem15,feedbackitem16=feedbackitem16,feedbackitem17=feedbackitem17,feedbackitem18=feedbackitem18,feedbackitem19=feedbackitem19,feedbackitem20=feedbackitem20,)

@app.route('/managementcheckattendance')
def managementcheckattendance():
	today=date.today()
	cur.execute("select count(*) FROM `studentattendance` where breakfast='morning' and date=(%s)",(today,))
	feedbackitem1=cur.fetchall()
	cur.execute("select count(*) FROM `studentattendance` where lunch='afternoon' and date=(%s)",(today,))
	feedbackitem2=cur.fetchall()
	cur.execute("select count(*) FROM `studentattendance` where dinner='night' and date=(%s)",(today,))
	feedbackitem3=cur.fetchall()
	return render_template("/managementcheckattendance.html", data1=feedbackitem1, data2=feedbackitem2, data3=feedbackitem3)


@app.route('/managementcheckattendancefaculty')
def managementcheckattendancefaculty():
	today=date.today()
	cur.execute("select count(*) FROM `facultyattendance` where breakfast='morning' and date=(%s)",(today,))
	feedbackitem1=cur.fetchall()

	cur.execute("select count(*) FROM `facultyattendance` where lunch='afternoon' and date=(%s)",(today,))
	feedbackitem2=cur.fetchall()
	
	cur.execute("select count(*) FROM `facultyattendance` where dinner='night' and date=(%s)",(today,))
	feedbackitem3=cur.fetchall()
	

	return render_template("/managementcheckattendancefaculty.html", data1=feedbackitem1, data2=feedbackitem2, data3=feedbackitem3)

@app.route('/managementrequirementissues')
def managementrequirementissues():
	today=date.today()
	cur.execute("select * FROM `requirementissues` where date=(%s)",(today,))
	issues=cur.fetchall()
	return render_template("/managementissues.html",data=issues)

@app.route('/studentsuggestionsmanagement')
def studentsuggestionsmanagement():
	today=date.today()
	cur.execute("select * FROM `studentsuggestions` where date=(%s)",(today,))
	suggestions=cur.fetchall()
	return render_template("/suggestionsmanagement.html",data=suggestions)

@app.route('/facultysuggestionsmanagement')
def facultysuggestionsmanagement():
	today=date.today()
	cur.execute("select * FROM `facultysuggestions` where date=(%s)",(today,))
	suggestions=cur.fetchall()
	return render_template("/suggestionsmanagement.html",data=suggestions)

@app.route('/managementupdateprofile')
def managementupdateprofile1():
	if not UserID:
		return redirect(url_for('managementlogin'))
	else:
		return render_template("profilemanagement.html")

@app.route('/managementupdateprofile', methods=['POST'])
def managementupdateprofile():
	if not UserID:
		return redirect(url_for('managementlogin'))
	else:
		oldpassword =  request.form['old']
		newpassword =  request.form['new']
		confirmnewpassword =  request.form['confirm']
		temp_id=str(UserID)
		print(UserID)
		print(UserID)
		print(UserID)
		print(UserID)
		print(UserID)
		cur.execute("select * from management where management_id=(%s) and management_id=(%s)",(temp_id,temp_id))
		All=cur.fetchone()
		print(All)
		if All:
			if str(All[2])!=str(oldpassword):
				return render_template("profilemanagement.html", data="Old Password not matched")
			else:
				val=cur.execute("update management set management_user_password=(%s) where management_id=(%s)",(newpassword,UserID))
				res = mydb.commit()
				return render_template("profilemanagement.html", data='Password update success')

@app.route('/managementreportfeedback')
def managementreportfeedback():
	return render_template("/managementfeedbackreport.html")
@app.route('/managementreportfeedback1', methods=['POST'])
def managementreportfeedback1():
	i1=request.form['from']
	i2=request.form['to']
	cur.execute("select count(*), feedbackitem1 FROM `feedbackbreakfast` where date BETWEEN %s AND %s group by feedbackitem1",(i1,i2))
	feedbackitem1=cur.fetchall()
	cur.execute("select count(*), feedbackitem2 FROM `feedbackbreakfast`  where date BETWEEN %s AND %s group by feedbackitem2",(i1,i2))
	feedbackitem2=cur.fetchall()
	cur.execute("select count(*), feedbackitem3 FROM `feedbackbreakfast`  where date BETWEEN %s AND %s group by feedbackitem3",(i1,i2))
	feedbackitem3=cur.fetchall()
	cur.execute("select count(*), feedbackitem4 FROM `feedbackbreakfast`  where date BETWEEN %s AND %s group by feedbackitem4",(i1,i2))
	feedbackitem4=cur.fetchall()
	cur.execute("select count(*), feedbackitem5 FROM `feedbackbreakfast`  where date BETWEEN %s AND %s group by feedbackitem5",(i1,i2))
	feedbackitem5=cur.fetchall()
	cur.execute("select count(*), feedbackitem6 FROM `feedbackbreakfast`  where date BETWEEN %s AND %s group by feedbackitem6",(i1,i2))
	feedbackitem6=cur.fetchall()
	cur.execute("select count(*), feedbackitem7 FROM `feedbackbreakfast`  where date BETWEEN %s AND %s group by feedbackitem7",(i1,i2))
	feedbackitem7=cur.fetchall()
	cur.execute("select count(*), feedbackitem8 FROM `feedbackbreakfast`  where date BETWEEN %s AND %s group by feedbackitem8",(i1,i2))
	feedbackitem8=cur.fetchall()
	cur.execute("select count(*), feedbackitem9 FROM `feedbackbreakfast`  where date BETWEEN %s AND %s group by feedbackitem9",(i1,i2))
	feedbackitem9=cur.fetchall()
	cur.execute("select count(*), feedbackitem10 FROM `feedbackbreakfast`  where date BETWEEN %s AND %s group by feedbackitem10",(i1,i2))
	feedbackitem10=cur.fetchall()
	cur.execute("select count(*), feedbackitem11 FROM `feedbackbreakfast`  where date BETWEEN %s AND %s group by feedbackitem11",(i1,i2))
	feedbackitem11=cur.fetchall()
	cur.execute("select count(*), feedbackitem12 FROM `feedbackbreakfast`  where date BETWEEN %s AND %s group by feedbackitem12",(i1,i2))
	feedbackitem12=cur.fetchall()
	cur.execute("select count(*), feedbackitem13 FROM `feedbackbreakfast`  where date BETWEEN %s AND %s group by feedbackitem13",(i1,i2))
	feedbackitem13=cur.fetchall()
	cur.execute("select count(*), feedbackitem14 FROM `feedbackbreakfast`  where date BETWEEN %s AND %s group by feedbackitem14",(i1,i2))
	feedbackitem14=cur.fetchall()
	cur.execute("select count(*), feedbackitem15 FROM `feedbackbreakfast`  where date BETWEEN %s AND %s group by feedbackitem15",(i1,i2))
	feedbackitem15=cur.fetchall()

	return render_template("/managementcheckbreakfast.html",feedbackitem1=feedbackitem1,feedbackitem2=feedbackitem2,feedbackitem3=feedbackitem3,feedbackitem4=feedbackitem4,feedbackitem5=feedbackitem5,feedbackitem6=feedbackitem6,feedbackitem7=feedbackitem7,feedbackitem8=feedbackitem8,feedbackitem9=feedbackitem9,feedbackitem10=feedbackitem10,feedbackitem11=feedbackitem11,feedbackitem12=feedbackitem12,feedbackitem13=feedbackitem13,feedbackitem14=feedbackitem14,feedbackitem15=feedbackitem15,)


@app.route('/managementreportfeedbacklunch')
def managementreportfeedbacklunch():
	return render_template("/managementreportfeedbacklunch.html")
@app.route('/managementreportfeedbacklunch1', methods=['POST'])
def managementreportfeedbacklunch1():
	i1=request.form['from']
	i2=request.form['to']
	cur.execute("select count(*), feedbackitem1 FROM `feedbacklunch`  where date BETWEEN %s AND %s group by feedbackitem1",(i1,i2,))
	feedbackitem1=cur.fetchall()
	cur.execute("select count(*), feedbackitem2 FROM `feedbacklunch`  where date BETWEEN %s AND %s group by feedbackitem2",(i1,i2))
	feedbackitem2=cur.fetchall()
	cur.execute("select count(*), feedbackitem3 FROM `feedbacklunch`  where date BETWEEN %s AND %s group by feedbackitem3",(i1,i2))
	feedbackitem3=cur.fetchall()
	cur.execute("select count(*), feedbackitem4 FROM `feedbacklunch`  where date BETWEEN %s AND %s group by feedbackitem4",(i1,i2))
	feedbackitem4=cur.fetchall()
	cur.execute("select count(*), feedbackitem5 FROM `feedbacklunch`  where date BETWEEN %s AND %s group by feedbackitem5",(i1,i2))
	feedbackitem5=cur.fetchall()
	cur.execute("select count(*), feedbackitem6 FROM `feedbacklunch`  where date BETWEEN %s AND %s group by feedbackitem6",(i1,i2))
	feedbackitem6=cur.fetchall()
	cur.execute("select count(*), feedbackitem7 FROM `feedbacklunch`  where date BETWEEN %s AND %s group by feedbackitem7",(i1,i2))
	feedbackitem7=cur.fetchall()
	cur.execute("select count(*), feedbackitem8 FROM `feedbacklunch`  where date BETWEEN %s AND %s group by feedbackitem8",(i1,i2))
	feedbackitem8=cur.fetchall()
	cur.execute("select count(*), feedbackitem9 FROM `feedbacklunch`  where date BETWEEN %s AND %s group by feedbackitem9",(i1,i2))
	feedbackitem9=cur.fetchall()
	cur.execute("select count(*), feedbackitem10 FROM `feedbacklunch`  where date BETWEEN %s AND %s group by feedbackitem10",(i1,i2))
	feedbackitem10=cur.fetchall()
	cur.execute("select count(*), feedbackitem11 FROM `feedbacklunch`  where date BETWEEN %s AND %s group by feedbackitem11",(i1,i2))
	feedbackitem11=cur.fetchall()
	cur.execute("select count(*), feedbackitem12 FROM `feedbacklunch`  where date BETWEEN %s AND %s group by feedbackitem12",(i1,i2))
	feedbackitem12=cur.fetchall()
	cur.execute("select count(*), feedbackitem13 FROM `feedbacklunch` where date BETWEEN %s AND %s group by feedbackitem13",(i1,i2))
	feedbackitem13=cur.fetchall()
	cur.execute("select count(*), feedbackitem14 FROM `feedbacklunch` where date BETWEEN %s AND %s group by feedbackitem14",(i1,i2))
	feedbackitem14=cur.fetchall()
	cur.execute("select count(*), feedbackitem15 FROM `feedbacklunch` where date BETWEEN %s AND %s group by feedbackitem15",(i1,i2))
	feedbackitem15=cur.fetchall()
	cur.execute("select count(*), feedbackitem16 FROM `feedbacklunch` where date BETWEEN %s AND %s group by feedbackitem16",(i1,i2))
	feedbackitem16=cur.fetchall()
	cur.execute("select count(*), feedbackitem17 FROM `feedbacklunch` where date BETWEEN %s AND %s group by feedbackitem17",(i1,i2))
	feedbackitem17=cur.fetchall()
	cur.execute("select count(*), feedbackitem18 FROM `feedbacklunch` where date BETWEEN %s AND %s group by feedbackitem18",(i1,i2))
	feedbackitem18=cur.fetchall()
	cur.execute("select count(*), feedbackitem19 FROM `feedbacklunch` where date BETWEEN %s AND %s group by feedbackitem19",(i1,i2))
	feedbackitem19=cur.fetchall()
	cur.execute("select count(*), feedbackitem20 FROM `feedbacklunch` where date BETWEEN %s AND %s group by feedbackitem20",(i1,i2))
	feedbackitem20=cur.fetchall()

	return render_template("/managementchecklunch.html",feedbackitem1=feedbackitem1,feedbackitem2=feedbackitem2,feedbackitem3=feedbackitem3,feedbackitem4=feedbackitem4,feedbackitem5=feedbackitem5,feedbackitem6=feedbackitem6,feedbackitem7=feedbackitem7,feedbackitem8=feedbackitem8,feedbackitem9=feedbackitem9,feedbackitem10=feedbackitem10,feedbackitem11=feedbackitem11,feedbackitem12=feedbackitem12,feedbackitem13=feedbackitem13,feedbackitem14=feedbackitem14,feedbackitem15=feedbackitem15,feedbackitem16=feedbackitem16,feedbackitem17=feedbackitem17,feedbackitem18=feedbackitem18,feedbackitem19=feedbackitem19,feedbackitem20=feedbackitem20,)


@app.route('/managementreportfeedbackdinner')
def managementreportfeedbackdinner():
	return render_template("/managementreportfeedbackdinner.html")
@app.route('/managementreportfeedbackdinner1', methods=['POST'])
def managementreportfeedbackdinner1():
	i1=request.form['from']
	i2=request.form['to']
	cur.execute("select count(*), feedbackitem1 FROM `feedbackdinner`  where date BETWEEN %s AND %s group by feedbackitem1",(i1,i2,))
	feedbackitem1=cur.fetchall()
	cur.execute("select count(*), feedbackitem2 FROM `feedbackdinner`  where date BETWEEN %s AND %s group by feedbackitem2",(i1,i2))
	feedbackitem2=cur.fetchall()
	cur.execute("select count(*), feedbackitem3 FROM `feedbackdinner`  where date BETWEEN %s AND %s group by feedbackitem3",(i1,i2))
	feedbackitem3=cur.fetchall()
	cur.execute("select count(*), feedbackitem4 FROM `feedbackdinner`  where date BETWEEN %s AND %s group by feedbackitem4",(i1,i2))
	feedbackitem4=cur.fetchall()
	cur.execute("select count(*), feedbackitem5 FROM `feedbackdinner`  where date BETWEEN %s AND %s group by feedbackitem5",(i1,i2))
	feedbackitem5=cur.fetchall()
	cur.execute("select count(*), feedbackitem6 FROM `feedbackdinner`  where date BETWEEN %s AND %s group by feedbackitem6",(i1,i2))
	feedbackitem6=cur.fetchall()
	cur.execute("select count(*), feedbackitem7 FROM `feedbackdinner`  where date BETWEEN %s AND %s group by feedbackitem7",(i1,i2))
	feedbackitem7=cur.fetchall()
	cur.execute("select count(*), feedbackitem8 FROM `feedbackdinner`  where date BETWEEN %s AND %s group by feedbackitem8",(i1,i2))
	feedbackitem8=cur.fetchall()
	cur.execute("select count(*), feedbackitem9 FROM `feedbackdinner`  where date BETWEEN %s AND %s group by feedbackitem9",(i1,i2))
	feedbackitem9=cur.fetchall()
	cur.execute("select count(*), feedbackitem10 FROM `feedbackdinner`  where date BETWEEN %s AND %s group by feedbackitem10",(i1,i2))
	feedbackitem10=cur.fetchall()
	cur.execute("select count(*), feedbackitem11 FROM `feedbackdinner`  where date BETWEEN %s AND %s group by feedbackitem11",(i1,i2))
	feedbackitem11=cur.fetchall()
	cur.execute("select count(*), feedbackitem12 FROM `feedbackdinner`  where date BETWEEN %s AND %s group by feedbackitem12",(i1,i2))
	feedbackitem12=cur.fetchall()
	cur.execute("select count(*), feedbackitem13 FROM `feedbackdinner` where date BETWEEN %s AND %s group by feedbackitem13",(i1,i2))
	feedbackitem13=cur.fetchall()
	cur.execute("select count(*), feedbackitem14 FROM `feedbackdinner` where date BETWEEN %s AND %s group by feedbackitem14",(i1,i2))
	feedbackitem14=cur.fetchall()
	cur.execute("select count(*), feedbackitem15 FROM `feedbackdinner` where date BETWEEN %s AND %s group by feedbackitem15",(i1,i2))
	feedbackitem15=cur.fetchall()
	cur.execute("select count(*), feedbackitem16 FROM `feedbackdinner` where date BETWEEN %s AND %s group by feedbackitem16",(i1,i2))
	feedbackitem16=cur.fetchall()
	cur.execute("select count(*), feedbackitem17 FROM `feedbackdinner` where date BETWEEN %s AND %s group by feedbackitem17",(i1,i2))
	feedbackitem17=cur.fetchall()
	cur.execute("select count(*), feedbackitem18 FROM `feedbackdinner` where date BETWEEN %s AND %s group by feedbackitem18",(i1,i2))
	feedbackitem18=cur.fetchall()
	cur.execute("select count(*), feedbackitem19 FROM `feedbackdinner` where date BETWEEN %s AND %s group by feedbackitem19",(i1,i2))
	feedbackitem19=cur.fetchall()
	cur.execute("select count(*), feedbackitem20 FROM `feedbackdinner` where date BETWEEN %s AND %s group by feedbackitem20",(i1,i2))
	feedbackitem20=cur.fetchall()

	return render_template("/managementcheckdinner.html",feedbackitem1=feedbackitem1,feedbackitem2=feedbackitem2,feedbackitem3=feedbackitem3,feedbackitem4=feedbackitem4,feedbackitem5=feedbackitem5,feedbackitem6=feedbackitem6,feedbackitem7=feedbackitem7,feedbackitem8=feedbackitem8,feedbackitem9=feedbackitem9,feedbackitem10=feedbackitem10,feedbackitem11=feedbackitem11,feedbackitem12=feedbackitem12,feedbackitem13=feedbackitem13,feedbackitem14=feedbackitem14,feedbackitem15=feedbackitem15,feedbackitem16=feedbackitem16,feedbackitem17=feedbackitem17,feedbackitem18=feedbackitem18,feedbackitem19=feedbackitem19,feedbackitem20=feedbackitem20,)





#management end

#
#def login():
#	with open('../labels', 'rb') as f:
#		dicti = pickle.load(f)
#
#	# camera = PiCamera()
#	camera = cv2.VideoCapture(0)
#
#
#	faceCascade = cv2.CascadeClassifier(r'C:\Users\G.Sushma\OneDrive\Desktop\opencv-3.4.8\data\haarcascades\haarcascade_frontalface_default.xml')
#
#	recognizer = cv2.face.LBPHFaceRecognizer_create()
#	recognizer.read(r'C:\Users\G.Sushma\Documents\trainer.yml')
#
#	font = cv2.FONT_HERSHEY_SIMPLEX
#	la=''
#	s=0
#
#	#for frame in camera.capture_continuous(rawCapture, format="bgr", use_video_port=True):
#	while True:
#		ret,frame = camera.read()
#		gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#		faces = faceCascade.detectMultiScale(gray, scaleFactor = 1.5, minNeighbors = 5)
#		for (x, y, w, h) in faces:
#			roiGray = gray[y:y+h, x:x+w]
#
#			id_, conf = recognizer.predict(roiGray)
#
#			for name, value in dicti.items():
#				if value == id_:
#					print(name)
#					cv2.putText(frame, name, (x, y), font, 2, (0, 0 ,255), 2,cv2.LINE_AA)
#					s=1
#
#					break
#					if name!=la :
#						la=name
#
#
#			if conf <= 80:
#
#				cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
#				# cv2.putText(frame, name + str(conf), (x, y), font, 2, (0, 0 ,255), 2,cv2.LINE_AA)
#
#			else:
#				cv2.imshow('frame', frame)
#				key = cv2.waitKey(1)
#
#		if cv2.waitKey(1) & 0xFF == ord('q'):
#				break
#		if s==1:
#
#				break
#
#	cv2.destroyAllWindows()
#	return render_template("home.html",data=name)

if __name__ == "__main__":
	app.run(debug=True)
