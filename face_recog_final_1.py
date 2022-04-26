import cv2
import numpy as np
import face_recognition
import os
import mysql.connector
import calendar
from pytz import timezone
from datetime import datetime
from datetime import date


#
def getdatabase_day():
    my_date = date.today()
    data_day = calendar.day_name[my_date.weekday()]
    return data_day.lower()


def get_time():
    ind_time = datetime.now(timezone("Asia/Kathmandu"))
    intt = ind_time.strftime("%H");
    return intt


def period_time(t):
    if (t == "08"):
        return "first";
    elif (t == "09"):
        return "second";
    elif (t == "10"):
        return "third";
    elif (t == "11"):
        return "fourth";
    elif (t == "12"):
        return "fifth";
    elif (t == "13"):
        return "sixth";
    elif (t == "14"):
        return "seventh";
    elif (t == "15"):
        return "eighth";
    elif (t == "16"):
        return "ninth";
    elif (t == "17"):
        return "tenth";
    elif (t == "18"):
        return "eleventh";


#
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="password",
    database="project_osp"
)
mycursor = mydb.cursor()


#
def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList


def markAttendance(name):
    with open('Attendance.csv', 'r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
        if name not in nameList:
            now = datetime.now()
            dtString = now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')


# storing in separate table;
def store_in_db(register):
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="password",
        database="project_osp"
    )
    mycursor = mydb.cursor()
    sql = "INSERT INTO attendance (register_no, time) VALUES (%s, %s)"
    # sql = "INSERT INTO view_info (register_no, time) VALUES (%s, %s)"
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    val = (register, current_time)
    mycursor.execute(sql, val)
    mydb.commit()


#
print("How do you want see your Today routine")
print("Choose the option with which you want to proceed further")
print("1.Show your face to system.")
print("2.Type your reg no")
selected = int(input())
register = ""

if selected == 1:
    print("Enter 1. For displaying current schedule")
    print("Enter 2. For displaying whole day routine.")
    mod = int(input())
    if mod == 1:
        condition = True
        counter = 0
        path = 'ImagesAttendance'
        images = []
        classNames = []
        myList = os.listdir(path)
        print("Processing..\nPlease wait till it connects with database...")
        for cl in myList:
            curImg = cv2.imread(f'{path}/{cl}')
            images.append(curImg)
            classNames.append(os.path.splitext(cl)[0])
        # print(classNames)
        encodeListKnown = findEncodings(images)
        # print('Encoding Complete')
        cap = cv2.VideoCapture(0)
        while (condition == True):
            success, img = cap.read()
            # img = captureScreen()
            imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
            imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

            facesCurFrame = face_recognition.face_locations(imgS)
            encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

            for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
                matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
                faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
                # print(faceDis)
                matchIndex = np.argmin(faceDis)

                if matches[matchIndex]:
                    name = classNames[matchIndex].upper()
                    # print(name)
                    y1, x2, y2, x1 = faceLoc
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                    markAttendance(name)
                    register = name
                    counter = counter + 1
                    # print(register)

            cv2.imshow('Webcam', img)
            cv2.waitKey(1)


            database_period = period_time(get_time())

           # database_table_name = getdatabase_day()
            database_table_name = 'monday';
            tim = "SELECT {} FROM {} WHERE id =\"{}\" ".format(database_period, database_table_name, register)
            mycursor.execute(tim)
            myresult = mycursor.fetchall()

            if counter == 1:
                for x in myresult:
                    if get_time() == "08" or get_time() == "09":
                        print("You have " + x[0] + " at " + str(get_time())[1] + " o'clock,morning" + getdatabase_day())
                    else:
                        if int(get_time()) > 12:
                            dump = (int(get_time()) - 12)
                            print("You have " + x[0] + " at " + str(dump) + " o'clock,afternoon " + getdatabase_day())
                        else:
                            print("You have " + x[0] + " at " + get_time() + " o'clock,afternoon " + getdatabase_day())
                    store_in_db(register)

            # condition = False

    else:
        condition = True
        counter = 0
        path = 'ImagesAttendance'
        images = []
        classNames = []
        myList = os.listdir(path)
        print("Processing..\nPlease wait till it connects with database...")
        for cl in myList:
            curImg = cv2.imread(f'{path}/{cl}')
            images.append(curImg)
            classNames.append(os.path.splitext(cl)[0])
        # print(classNames)
        encodeListKnown = findEncodings(images)
        # print('Encoding Complete')
        cap = cv2.VideoCapture(0)
        while (condition == True):
            success, img = cap.read()
            # img = captureScreen()
            imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
            imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

            facesCurFrame = face_recognition.face_locations(imgS)
            encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)

            for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
                matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
                faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
                # print(faceDis)
                matchIndex = np.argmin(faceDis)

                if matches[matchIndex]:
                    name = classNames[matchIndex].upper()
                    # print(name)
                    y1, x2, y2, x1 = faceLoc
                    y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4
                    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 2)
                    cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 255, 0), cv2.FILLED)
                    cv2.putText(img, name, (x1 + 6, y2 - 6), cv2.FONT_HERSHEY_COMPLEX, 1, (255, 255, 255), 2)
                    markAttendance(name)
                    register = name
                    counter = counter + 1
                    # print(register)

            cv2.imshow('Webcam', img)
            cv2.waitKey(1)
            database_table_name = getdatabase_day()
            tim = "SELECT * FROM {} WHERE id =\"{}\" ".format(database_table_name, register)
            mycursor.execute(tim)
            myresult = mycursor.fetchall()
            if counter == 1:
                print("Your today's timetable is")
                for x in myresult:
                    for y in x:
                        print(y)
                store_in_db(register)

else:
    register = input("Enter registration no. : ")
    mod = int(input("Enter 1. For displaying current schedule.\nEnter 2. For displaying whole day schedule.\n"))
    if mod == 1:
        database_period = period_time(get_time())
        database_table_name = getdatabase_day()
        tim = "SELECT {} FROM {} WHERE id =\"{}\" ".format(database_period, database_table_name, register)
        mycursor.execute(tim)
        myresult = mycursor.fetchall()
        for x in myresult:
            if get_time() == "08" or get_time() == "09":
                print("You have " + x[0] + " at " + str(get_time())[1] + " o'clock,morning " + getdatabase_day())
            else:
                if int(get_time()) > 12:
                    dump = (int(get_time()) - 12)
                    print("You have " + x[0] + " at " + str(dump) + " o'clock, afternoon " + getdatabase_day())
                else:
                    print("You have " + x[0] + " at " + get_time() + " o'clock, morning " + getdatabase_day())
            store_in_db(register)
    else:
        database_table_name = getdatabase_day()
        tim = "SELECT * FROM {} WHERE id =\"{}\" ".format(database_table_name, register)
        mycursor.execute(tim)
        myresult = mycursor.fetchall()
        print("Your today's timetable is")
        for x in myresult:
            for y in x:
                print(y)
        store_in_db(register)
