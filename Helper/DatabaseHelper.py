from dotenv import load_dotenv
import os
import mysql.connector
import uuid
from Models.UserModel import User
from Models.TimeSheetModel import TimeSheet


class Database():
    def __init__(self):
        host = os.getenv('HOST')
        user = os.getenv('USER')
        password = os.getenv('PASSWORD')
        database = os.getenv('DATABASE')
        
        self.db = mysql.connector.connect(host=host, user=user, passwd=password, database=database)
        
    def select_users(self) -> list[User]:
        cursor = self.db.cursor()
        query = "SELECT ID, FirstName, LastName, Age, Title, Department FROM tblUser"
        cursor.execute(query)
        
        result_execute = cursor.fetchall()
        result = []
        for row in result_execute:
            user = User()
            user.Create_Data_Select(*row)
            result.append(user)
            
        cursor.close()
        return result
    
    def insert_user(self, user: User) -> bool:
        insert_str: str = "INSERT INTO tblUser (ID, FirstName, LastName, Age, Title, Department) VALUES (%s, %s, %s, %s, %s,%s)"
        val: tuple = (user.ID, user.FirstName, user.LastName, user.Age, user.Title, user.Department)
        cursor = self.db.cursor()
        cursor.execute(insert_str, val)
        
        self.db.commit()
        cursor.close()
        return True
    
    
    def select_timesheets(self) -> list[TimeSheet]:
        cursor = self.db.cursor()
        query = "SELECT ID, UserID, TimeStamp FROM tblTimesheet"
        cursor.execute(query)
        
        result_execute = cursor.fetchall()
        result = []
        for row in result_execute:
            timesheet = TimeSheet()
            timesheet.Create_Data_Select(*row)
            result.append(timesheet)
            
        cursor.close()
        return result
    
    
    def insert_timesheet(self, timesheet: TimeSheet) -> bool:
        insert_str: str = "INSERT INTO tblTimesheet (ID, UserID) VALUES (%s, %s)"
        val: tuple = (timesheet.ID, timesheet.UserID)
        cursor = self.db.cursor()
        cursor.execute(insert_str, val)
        
        self.db.commit()
        cursor.close()
        return True













