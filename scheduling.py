from pprint import pprint
from googleapiclient import discovery
import numpy as np
import gspread
import pandas as pd
import random
import copy
from oauth2client.service_account import ServiceAccountCredentials

'''
On your terminal run the following commands for the code to run
pip install numpy
pip install pandas
pip install gspread
pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib
'''

session_num=2
class Student:
    def __init__(self, name, session, qb_exp, period2, period3, period4):
        self.name=name
        self.session=session
        self.qb_exp=qb_exp
        self.period2=period2
        self.period3=period3
        self.period4=period4
        #self.preference=preference
        self.classes=[]
class ClassSections:
    def __init__(self, name, teacher, enrollment):
        self.name=name
        self.teacher=teacher
        self.enrollment=enrollment
        self.max_priority=0
        self.highest=[]
        self.priorities=[]
        self.capacity=10
classEnrollment=[]

if (session_num==1):
    classEnrollment=[[ClassSections("Strategy", "Aarav", []),ClassSections("Geography", "Aarav", []),ClassSections("Geography", "Aarav", []),ClassSections("Geography", "Aarav", [])], 
    [ClassSections("Strategy", "Andy", []),ClassSections("American History", "Andy", []),ClassSections("Prose", "Andy", []),ClassSections("American History", "Andy", [])], 
    [ClassSections("How to QB", "Jason", []),ClassSections("Poetry", "Jason", []),ClassSections("Visual Art", "Jason", []),ClassSections("Drama", "Jason", [])], 
    [ClassSections("How to QB", "Jennifer", []),ClassSections("Biology", "Jennifer", []),ClassSections("Chemistry", "Jennifer", []),ClassSections("Biology", "Jennifer", [])], 
    [ClassSections("Strategy", "Kritika", []),ClassSections("Myth and Religion", "Kritika", []),ClassSections("World History", "Kritika", []),ClassSections("World History", "Kritika", [])], 
    [ClassSections("Strategy", "Vedul", []),ClassSections("Biology", "Vedul", []),ClassSections("Myth and Religion", "Vedul", []),ClassSections("Music", "Vedul", [])], 
    [ClassSections("Strategy", "Vishal", []),ClassSections("World History", "Vishal", []),ClassSections("Euro History", "Vishal", []),ClassSections("Euro History", "Vishal", [])]]
if (session_num==2):
    classEnrollment=[[ClassSections("Strategy", "Aarav", []),ClassSections("Geography II", "Aarav", []),"Break",ClassSections("Geography II", "Aarav", [])], 
    [ClassSections("Strategy", "Andy", []),"Break",ClassSections("Politics", "Andy", []), ClassSections("Authors", "Andy", [])], 
    [ClassSections("How to QB", "Jason", []), "Break" ,ClassSections("Poetry II", "Jason", []),"Break"], 
    [ClassSections("Strategy", "Jennifer", []), ClassSections("Biology II", "Jennifer", []),"Break",ClassSections("Earth and Space", "Jennifer", [])], 
    [ClassSections("Strategy", "Kritika", []),"Break","Break", "Break"], 
    ["Break",ClassSections("Myth and Religion II", "Vedul", []),ClassSections("Myth and Religion II", "Vedul", []),ClassSections("Music II", "Vedul", [])], 
    [ClassSections("How to QB", "Vishal", []),ClassSections("Military History", "Vishal", []), ClassSections("Monarchy", "Vishal", []), "Break"]]    

#change if instructors for classes changes
strategy=[classEnrollment[0][0], classEnrollment[1][0], classEnrollment[4][0], classEnrollment[5][0]]
howToQB=[classEnrollment[2][0], classEnrollment[6][0]]

scope=['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']        
credentials= ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client=gspread.authorize(credentials)
sheet=client.open('Copy of Scheduling Data')
campers_data=pd.DataFrame.from_dict(sheet.get_worksheet(0).get_all_records())
#instructors_data=pd.DataFrame.from_dict(sheet.get_worksheet(2).get_all_records())

service=discovery.build('sheets', 'v4', credentials=credentials)
spreadsheet_id="1Ev3R1HH_eNRTxhoy8a5dxAG0Bkk85-Ef1kpUK63UVUs"
campers_sheet_id=2008186473
instructors_sheet_id=1244594342

session1Classes=["Myth and Religion", "Prose", "US History", "Chemistry", "Geography", "Poetry", "European History",
    "Biology", "Visual Art", "Drama", "World History", "Physics", "Music"]
session2Classes= ["Politics", "Myth and Religion II", "Biology II", "Poetry II", "Military History",
"Authors", "Monarchy", "Geography II", "Earth and Space", "Music II"]

classPeriods={
    "Geography": [2,3,4],
    "Prose": [2],
    "World History": [2,3,4],
    "American History": [2,4],
    "European History": [2,4],
    "Myth and Religion": [2,3],
    "Chemistry": [3], 
    "Poetry": [3],
    "Biology": [2], 
    "Visual Art": [3], 
    "Drama": [4], 
    "Music": [4],
    "Politics":[3],
    "Myth and Religion II":[2,3],
    "Biology II":[2],
    "Poetry II":[3],
    "Military History":[2],
    "Authors":[4],
    "Monarchy":[3],
    "Geography II":[2,4],
    "Earth and Space":[4],
    "Music II": [4],
}
#change sexy dictionary if class order changes

session1Students=[]
session2Students=[]


def myFunc(e):
    return list(e.values())[0]

for ind in campers_data.index:
    p2=[]
    p3=[]
    p4=[]

    for i in range(1, 6):
        input='Preference '+str(i)
        prefClass=campers_data[input][ind]
        if (not(prefClass in classPeriods.keys())):
            continue
        for j in classPeriods[prefClass]:
            if(j==2):
                for x in classEnrollment:
                    for y in range(4):
                        classObj=None
                        if (x[y]!="Break") and (x[y].name==prefClass) and (y==1):
                            classObj=x[y]
                if(classObj!=None) and (classObj!="Break"):
                    p2.append({classObj: i})
            elif(j==3):
                for x in classEnrollment:
                    for y in range(4):
                        classObj=None
                        if (x[y]!="Break") and (x[y].name==prefClass) and (y==2):
                            classObj=x[y]
                if(classObj!=None) and (classObj!="Break"):
                    p3.append({classObj: i})
            elif(j==4):
                for x in classEnrollment:
                    for y in range(4):
                        classObj=None
                        if(x[y]!="Break") and (x[y].name==prefClass) and (y==3):
                            classObj=x[y]
                if(classObj!=None) and (classObj!="Break"):
                    p4.append({classObj: i})

    p2.sort(key=myFunc)
    p3.sort(key=myFunc)
    p4.sort(key=myFunc)
    s=Student(campers_data['Name'][ind], campers_data['Session'][ind], campers_data['Years'][ind], p2, p3, p4)

    
    if(s.session=="Session 1"):
        session1Students.append(s)
    else:
        session2Students.append(s)

for i in range(1, 5):
    sesh1=list(session2Students) #change session1Students to session2Students or vice versa if applicable
    for s in sesh1:
        if(i==1):
            if(s.qb_exp=="none"):
                how=howToQB[random.randrange(len(howToQB))]
                how.enrollment.append(s)
                s.classes.append(how)
            else:
                strat=strategy[random.randrange(len(strategy))]
                strat.enrollment.append(s)
                s.classes.append(strat)                
        else:
            if(i==2):
                skip=False
                for j in s.period2: #looping through classes in period by priority
                    for clas in s.classes:
                        if (clas.name==list(j.keys())[0].name):
                            skip=True
                    if (skip==True):
                        print("continue")
                        continue                       
                    if len(list(j.keys())[0].enrollment)<10:
                        list(j.keys())[0].enrollment.append(s)
                        s.classes.append(list(j.keys())[0])
                        if(list(j.values())[0]>list(j.keys())[0].max_priority):
                            list(j.keys())[0].max_priority=list(j.values())[0]
                            list(j.keys())[0].highest.insert(0, s)
                            list(j.keys())[0].priorities.insert(0, list(j.values())[0])
                        sesh1=[stu for stu in sesh1 if stu!=s]
                        break
                    else:
                        if(list(j.values())[0]<list(j.keys())[0].max_priority):
                            for k in list(j.keys())[0].enrollment: #looping thorugh students to find one to remove
                                for x in k.period2:
                                    if list(x.keys())[0]==list(j.keys())[0]:
                                        if(list(x.values())[0]==list(j.keys())[0].max_priority):
                                            x.classes.remove(j)
                                            list(j.keys())[0].enrollment.remove({x, list(j.keys())[0].max_priority})
                                            s.classes.append(list(j.keys())[0])
                                            list(j.keys())[0].enrollment.append()
                                            list(j.keys())[0].highest.pop(0)
                                            list(j.keys())[0].priorities.pop(0)
                                            if(list(j.values())[0]>list(j.keys())[0].max_priority):
                                                list(j.keys())[0].max_priority=list(j.values())[0]
                                                list(j.keys())[0].highest.insert(0, s)
                                                list(j.keys())[0].priorities.insert(0, list(j.values())[0])
                                            list(j.keys())[0].max_priority=list(j.keys())[0].priorities[0]
                                            sesh1.append(x)
                                            break
                if(len(s.classes)<2): #if they are not able to get any of their top 5 within a certain timeslot
                    min_enrollment=11
                    min_row=0
                    for y in range(0, 7):
                        skip-False
                        if(classEnrollment[y][1]=="Break"):
                            continue
                        if(len(classEnrollment[y][1].enrollment)<min_enrollment):
                            for clas in s.classes:
                                if (clas.name==classEnrollment[y][1].name) or (clas=="Break"):
                                    skip=True
                            if (skip==True):
                                continue
                            min_enrollment=len(classEnrollment[y][1].enrollment)
                            min_row=y    
                    classEnrollment[min_row][1].enrollment.append(s)
                    s.classes.append(classEnrollment[min_row][1])
            elif (i==3):
                skip=False
                for j in s.period3: #looping through classes in period by priority
                    for clas in s.classes:
                        if (clas.name==list(j.keys())[0].name):
                            print(clas.name)
                            skip=True
                    if (skip==True):
                        continue                        
                    if len(list(j.keys())[0].enrollment)<10:
                        list(j.keys())[0].enrollment.append(s)
                        s.classes.append(list(j.keys())[0])
                        if(list(j.values())[0]>list(j.keys())[0].max_priority):
                            list(j.keys())[0].max_priority=list(j.values())[0]
                            list(j.keys())[0].highest.insert(0, s)
                            list(j.keys())[0].priorities.insert(0, list(j.values())[0])
                        sesh1=[stu for stu in sesh1 if stu!=s]
                        break
                    else:
                        if(list(j.values())[0]<list(j.keys())[0].max_priority):
                            for k in list(j.keys())[0].enrollment: #looping thorugh students to find one to remove
                                for x in k.period3:
                                    if list(x.keys())[0]==list(j.keys())[0]:
                                        if(x.values()[0]==list(j.keys())[0].max_priority):
                                            x.classes.remove(j)
                                            list(j.keys())[0].enrollment.remove({x, list(j.keys())[0].max_priority})
                                            s.classes.append(list(j.keys())[0])
                                            list(j.keys())[0].enrollment.append()
                                            list(j.keys())[0].highest.pop(0)
                                            list(j.keys())[0].priorities.pop(0)
                                            if(list(j.values())[0]>list(j.keys())[0].max_priority):
                                                list(j.keys())[0].max_priority=list(j.values())[0]
                                                list(j.keys())[0].highest.insert(0, s)
                                                list(j.keys())[0].priorities.insert(0, list(j.values())[0])
                                            list(j.keys())[0].max_priority=list(j.keys())[0].priorities[0]
                                            sesh1.append(x)
                                            break
                if(len(s.classes)<3): #if they are not able to get any of their top 5 within a certain timeslot
                    min_enrollment=11
                    min_row=0
                    for y in range(0, 7):
                        skip=False
                        if(classEnrollment[y][2]=="Break"):
                            continue
                        if(len(classEnrollment[y][2].enrollment)<min_enrollment):
                            for clas in s.classes:
                                if (clas.name==classEnrollment[y][2].name) or (clas=="Break"):
                                    skip=True
                            if (skip==True):
                                continue
                            min_enrollment=len(classEnrollment[y][2].enrollment)
                            min_row=y   
                    classEnrollment[min_row][2].enrollment.append(s)
                    s.classes.append(classEnrollment[min_row][2])
            else:
                skip=False
                for j in s.period4: #looping through classes in period by priority
                    for clas in s.classes:
                        if (clas.name==list(j.keys())[0].name):
                            skip=True
                    if (skip==True):
                        continue     
                    if len(list(j.keys())[0].enrollment)<10:
                        list(j.keys())[0].enrollment.append(s)
                        s.classes.append(list(j.keys())[0])
                        if(list(j.values())[0]>list(j.keys())[0].max_priority):
                            list(j.keys())[0].max_priority=list(j.values())[0]
                            list(j.keys())[0].highest.insert(0, s)
                            list(j.keys())[0].priorities.insert(0, list(j.values())[0])
                        sesh1=[stu for stu in sesh1 if stu!=s]
                        break
                    else:
                        if(j.values()<list(j.keys())[0].max_priority):
                            for k in list(j.keys())[0].enrollment: #looping thorugh students to find one to remove
                                for x in k.period4:
                                    if list(x.keys())[0]==list(j.keys())[0]:
                                        if(list(x.values())[0]==list(j.keys())[0].max_priority):
                                            x.classes.remove(j)
                                            list(j.keys())[0].enrollment.remove({x, list(j.keys())[0].max_priority})
                                            s.classes.append(list(j.keys())[0])
                                            list(j.keys())[0].enrollment.append()
                                            list(j.keys())[0].highest.pop(0)
                                            list(j.keys())[0].priorities.pop(0)
                                            if(list(j.values())[0]>list(j.keys())[0].max_priority):
                                                list(j.keys())[0].max_priority=list(j.values())[0]
                                                list(j.keys())[0].highest.insert(0, s)
                                                list(j.keys())[0].priorities.insert(0, list(j.values())[0])
                                            list(j.keys())[0].max_priority=list(j.keys())[0].priorities[0]
                                            sesh1.append(x)
                                            break
                if(len(s.classes)<4): #if they are not able to get any of their top 5 within a certain timeslot
                    min_enrollment=11
                    min_row=0
                    for y in range(0, 7):
                        skip=False
                        if(classEnrollment[y][3]=="Break"):
                            continue
                        if(len(classEnrollment[y][3].enrollment)<min_enrollment):
                            for clas in s.classes:
                                if (clas.name==classEnrollment[y][3].name) or (clas=="Break"):
                                    skip=True
                            if (skip==True):
                                continue
                            min_enrollment=len(classEnrollment[y][3].enrollment)
                            min_row=y   
                    classEnrollment[min_row][3].enrollment.append(s)
                    s.classes.append(classEnrollment[min_row][3])

#for str in session1Classes:

#for str in session2Classes:
print("Teacher's Schedules: ")


for i in range(0, 7):
    if(classEnrollment[i][0]=="Break"):
        print(classEnrollment[i][1].teacher, ": ")
    else:    
        print(classEnrollment[i][0].teacher, ": ")
    for j in range(0, 4):
        num=str(j+1)
        if(classEnrollment[i][j]=="Break"):
            print("Period "+num+": Break")
        else: 
            print("Period "+num+": " + classEnrollment[i][j].name + " Enrollment: " + str(len(classEnrollment[i][j].enrollment))+ " students")

print("Student's Schedules")

for s in session2Students: #changes session1Students to session2Students if applicable or vice versa
    print("Name: " + s.name)
    for i in range(0, 4):
        num=str(i+1)
        print("Period "+ num + ": "+ s.classes[i].name + " Teacher: " + s.classes[i].teacher)


