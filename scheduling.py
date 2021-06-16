from pprint import pprint
from googleapiclient import discovery
import numpy as np
import gspread
import pandas as pd
from oauth2client.service_account import ServiceAccountCredentials

class Student:
    def __init__(self, name, session, qb_exp, preference):
        self.name=name
        self.session=session
        self.qb_exp=qb_exp
        self.preference=preference

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
mythReligion=[]
prose=[]
usHistory=[]
chemistry=[]
geography=[]
poetry=[]
euroHist=[]
biology=[]
visualArt=[]
drama=[]
worldHist=[]
physics=[]
music=[]
prose2=[]
politics=[]
mythReligion2=[]
biology2=[]
militaryHist=[]
philSociety=[]
chemistry2=[]
authors=[]
monarchy=[]
geography2=[]
earthSpace=[]
music2=[]

def getClassList(className):
    
    print(x)

students={}
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

