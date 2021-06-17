from pprint import pprint
from googleapiclient import discovery
import numpy as np
import gspread
import pandas as pd
import random
from oauth2client.service_account import ServiceAccountCredentials

session_num=1
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
        self.capacity=10
classEnrollment=[[ClassSections("Strategy", "Aarav", []),ClassSections("Geography", "Aarav", []),ClassSections("Geography", "Aarav", []),ClassSections("Geography", "Aarav", [])], 
[ClassSections("Strategy", "Andy", []),ClassSections("US History", "Andy", []),ClassSections("Prose", "Andy", []),ClassSections("US History", "Andy", [])], 
[ClassSections("How to QB", "Jason", []),ClassSections("Poetry", "Jason", []),ClassSections("Visual Art", "Jason", []),ClassSections("Drama", "Jason", [])], 
[ClassSections("How to QB", "Jennifer", []),ClassSections("Biology", "Jennifer", []),ClassSections("Chemistry", "Jennifer", []),ClassSections("Biology", "Jennifer", [])], 
[ClassSections("Strategy", "Kritika", []),ClassSections("Myth and Religion", "Kritika", []),ClassSections("World History", "Kritika", []),ClassSections("World History", "Kritika", [])], 
[ClassSections("Strategy", "Vedul"),ClassSections("Biology", "Vedul"),ClassSections("Myth and Religion", "Vedul"),ClassSections("Music", "Vedul")], 
[ClassSections("Strategy", "Vishal", []),ClassSections("World History", "Vishal", []),ClassSections("Euro History", "Vishal", []),ClassSections("Euro History", "Vishal", [])]]

strategy=[classEnrollment[0][0], classEnrollment[1][0], classEnrollment[4][0], classEnrollment[5][0], classEnrollment[6][0]]
howToQB=[classEnrollment[2][0], classEnrollment[3][0]]

scope=['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']        
credentials= ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client=gspread.authorize(credentials)
sheet=client.open('https://docs.google.com/spreadsheets/d/1Ev3R1HH_eNRTxhoy8a5dxAG0Bkk85-Ef1kpUK63UVUs/edit?usp=sharing')
campers_data=pd.DataFrame.from_dict(sheet.get_worksheet(1).get_all_records())
instructors_data=pd.DataFrame.from_dict(sheet.get_worksheet(2).get_all_records())

service=discovery.build('sheets', 'v4', credentials=credentials)
spreadsheet_id="1Ev3R1HH_eNRTxhoy8a5dxAG0Bkk85-Ef1kpUK63UVUs"
campers_sheet_id=2008186473
instructors_sheet_id=1244594342

session1Classes=["Myth and Religion", "Prose", "US History", "Chemistry", "Geography", "Poetry", "European History",
    "Biology", "Visual Art", "Drama", "World History", "Physics", "Music"]
session2Classes= ["Prose II", "Politics", "Myth and Religion II", "Biology II", "Poetry II", "Military History",
    "Philosophy and Society", "Chemistry II", "Authors", "Monarchy", "Geography II", "Earth and Space", "Music II"]

classPeriods={
    "Geography": [2,3,4],
    "Prose": [2],
    "World History": [2,3,4],
    "US History": [2,4],
    "European History": [2,4],
    "Myth and Religion": [2,3],
    "Chemistry": [3], 
    "Poetry": [3],
    "Biology": [2], 
    "Visual Art": [3], 
    "Drama": [4], 
    "Music": [4],
    "Prose II":[2],
    "Politics":[3],
    "Myth and Religion II":[2,3],
    "Biology II":[2],
    "Poetry II":[3],
    "Military History":[2],
    "Philosophy and Society":[3],
    "Chemistry II":[3],
    "Authors":[4],
    "Monarchy":[3],
    "Geography II":[2,4],
    "Earth and Space":[4],
    "Music II": [4],
}


session1Students=[]
session2Students=[]


def myFunc(e):
    return e.values()[0]

for ind in campers_data.index:
    p2=[]
    p3=[]
    p4=[]

    for i in range(1, 6):
        input='Class preference: ['+i+']'
        prefClass=campers_data[input][ind]
        for j in classPeriods[prefClass]:
            if(j==2):
                p2.append({prefClass, i})
            elif(j==3):
                p3.append({prefClass, i})
            elif(j==4):
                p4.append({prefClass,i})

    p2.sort(key=myFunc)
    p3.sort(key=myFunc)
    p4.sort(key=myFunc)
    s=Student(campers_data['Name'][ind], campers_data['Session 1 or 2'][ind], campers_data['QB Exp.'][ind], p2, p3, p4)

    
    if(s.session==1):
        session1Students.append(s)
    else:
        session2Students.append(s)


for i in range(1, 5):
    for s in session1Students:
        if(i==1):
            if(s.qb_exp=="None"):
                how=howToQB[randrange(len(howToQB))]
                how.enrollment.append(s)
                s.classes.append(how)
            else:
                strat=strategy[randrange(len(strategy))]
                strat.enrollment.append(s)
                s.classes.append(strat)                
        else:
            if(i==2):
                for j in s.period2:
                    if len(j.keys()[0].enrollment)<10:
                        j.keys()[0].enrollment.append(s)
                        s.classes.append(j.keys()[0])
                        if(j.values()[0]>j.keys()[0].max_priority):
                            j.keys()[0].max_priority=j.values()[0]
                        break
                    else:
                        if(j.values()<j.keys()[0].max_priority):
                            for k in j.keys[0].enrollment: #looping thorugh students to find one to remove
                                for x in k.period2:
                                    if x.keys()[0]==j.keys()[0]:
                                        if(x.values()[0]==j.keys()[0].max_priority):
                                            


            elif (i==3):
                for j in s.period3:
            else:
                for j in s.period4:


#for str in session1Classes:

#for str in session2Classes:

