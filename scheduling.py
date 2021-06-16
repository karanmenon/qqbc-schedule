from pprint import pprint
from googleapiclient import discovery
import numpy as np
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

session_num=1
class Student:
    def __init__(self, name, session, qb_exp, preference):
        self.name=name
        self.session=session
        self.qb_exp=qb_exp
        self.preference=preference
        self.classes=[]
class ClassSections:
    def __init__(self, name, teacher, enrollment, max_priority):
        self.name=name
        self.teacher=teacher
        self.enrollment=enrollment
        self.max_priority=max_priority
        self.capacity=10
classEnrollment=[[ClassSections(),ClassSections(),ClassSections(),ClassSections()], 
[ClassSections(),ClassSections(),ClassSections(),ClassSections()], 
[ClassSections(),ClassSections(),ClassSections(),ClassSections()], 
[ClassSections(),ClassSections(),ClassSections(),ClassSections()], 
[ClassSections(),ClassSections(),ClassSections(),ClassSections()], 
[ClassSections(),ClassSections(),ClassSections(),ClassSections()], 
[ClassSections(),ClassSections(),ClassSections(),ClassSections()]]

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
for ind in campers_data.index:
    preference_list=[]
    preference_list.append(campers_data['Class preference: [1]'][ind])
    preference_list.append(campers_data['Class preference: [2]'][ind])
    preference_list.append(campers_data['Class preference: [3]'][ind])
    preference_list.append(campers_data['Class preference: [4]'][ind])
    preference_list.append(campers_data['Class preference: [5]'][ind])

    s=Student(campers_data['Name'][ind], campers_data['Session 1 or 2'][ind], campers_data['QB Exp.'][ind], preference_list)
    students.append(s)
classEnrollment={}
studentSchedule={}

service=discovery.build('sheets', 'v4', credentials=credentials)
spreadsheet_id="1Ev3R1HH_eNRTxhoy8a5dxAG0Bkk85-Ef1kpUK63UVUs"
campers_sheet_id=2008186473
instructors_sheet_id=1244594342
#for str in session1Classes:

#for str in session2Classes:

