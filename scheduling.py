from pprint import pprint
from googleapiclient import discovery
import numpy as np

class Student:
    def __init__(self, name, session, qb_exp, preference):
        self.name=name
        self.session=session
        self.qb_exp=qb_exp
        self.preference=preference
    
    
        
credentials=None
session1Classes=["Myth and Religion", "Prose", "US History", "Chemistry", "Geography", "Poetry", "European History",
    "Biology", "Visual Art", "Drama", "World History", "Physics", "Music"]
session2Classes= ["Prose II", "Politics", "Myth and Religion II", "Biology II", "Poetry II", "Military History",
    "Philosophy and Society", "Chemistry II", "Authors", "Monarchy", "Geography II", "Earth and Space", "Music II"]
studentPreferences={}
classEnrollment={}
studentSchedule={}

service=discovery.build('sheets', 'v4', credentials=credentials)
spreadsheet_id="1Ev3R1HH_eNRTxhoy8a5dxAG0Bkk85-Ef1kpUK63UVUs"
campers_sheet_id=2008186473
instructors_sheet_id=1244594342
for str in session1Classes:

for str in session2Classes:

