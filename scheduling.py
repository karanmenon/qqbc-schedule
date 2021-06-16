from pprint import pprint
from googleapiclient import discovery
import numpy as np
import gspread
import pandas as pd
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

scope=['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']        
credentials= ServiceAccountCredentials.from_json_keyfile_name('credentials.json', scope)
client=gspread.authorize(credentials)
sheet=client.open('https://docs.google.com/spreadsheets/d/1Ev3R1HH_eNRTxhoy8a5dxAG0Bkk85-Ef1kpUK63UVUs/edit?usp=sharing')
campers_data=pd.DataFrame.from_dict(sheet.get_worksheet(1).get_all_records())
instructors_data=pd.DataFrame.from_dict(sheet.get_worksheet(2).get_all_records())

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

strategy=[]
howToQB=[]
session1Students=[]
session2Students=[]

p2=[]
p3=[]
p4=[]

for ind in campers_data.index:
    for i in range(1, 6):
        input='Class preference: ['+i+']'
        prefClass=campers_data[input][ind]
        for j in classPeriods[prefClass]:
            if(j==2):
                p2.append({prefClass, i})
            else if(j==3):
                p3.append({prefClass, i})
            else if(j==4):
                p4.append({prefClass,i})

    preference_list=[]
    preference_list.append(campers_data['Class preference: [1]'][ind])
    preference_list.append(campers_data['Class preference: [2]'][ind])
    preference_list.append(campers_data['Class preference: [3]'][ind])
    preference_list.append(campers_data['Class preference: [4]'][ind])
    preference_list.append(campers_data['Class preference: [5]'][ind])


    s=Student(campers_data['Name'][ind], campers_data['Session 1 or 2'][ind], campers_data['QB Exp.'][ind], preference_list)

    if(s.qb_exp=="none"):
        howToQB.append(s)
    else:
        strategy.append(s)
    
    if(s.session==1):
        session1Students.append(s)
    else:
        session2Students.append(s)


service=discovery.build('sheets', 'v4', credentials=credentials)
spreadsheet_id="1Ev3R1HH_eNRTxhoy8a5dxAG0Bkk85-Ef1kpUK63UVUs"
campers_sheet_id=2008186473
instructors_sheet_id=1244594342
#for str in session1Classes:

#for str in session2Classes:

