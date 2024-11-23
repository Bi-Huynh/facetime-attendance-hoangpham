from datetime import datetime
import uuid

class TimeSheet:
    def __init__(self):
        self.ID: str = ""
        self.UserID: str = ""
        self.TimeStamp: str = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
    def Create_Data_Insert(self, UserID):
        self.ID = str(uuid.uuid4())
        self.UserID = UserID
    
    def Create_Data_Select(self, ID="", UserID="", TimeStamp:datetime=None):
        self.ID = ID
        self.UserID = UserID
        self.TimeStamp = TimeStamp.strftime("%Y-%m-%d %H:%M:%S")
        
    
        