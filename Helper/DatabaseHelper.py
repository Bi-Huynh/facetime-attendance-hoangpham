from dotenv import load_dotenv
import os
import mysql.connector
import uuid
from Models.UserModel import User


class Database():
    def __init__(self):
        host = os.getenv('HOST')
        user = os.getenv('USER')
        password = os.getenv('PASSWORD')
        database = os.getenv('DATABASE')
        
        self.db = mysql.connector.connect(host=host, user=user, passwd=password, database=database)
        
    def select_user(self) -> list[User]:
        cursor = self.db.cursor()
        query = "SELECT ID, FirstName, LastName, Age, Title, Department FROM tblUser"
        cursor.execute(query)
        
        result_execute = cursor.fetchall()
        result = []
        for row in result_execute:
            user = User(*row)
            result.append(user)
            
        cursor.close()
        return result
    
    def insert_user(self, user: User) -> bool:
        Id: str = str(uuid.uuid4())
        cursor = self.db.cursor()
        insert_str: str = "INSERT INTO tblUser (ID, FirstName, LastName, Age, Title, Department) VALUES (%s, %s, %s, %s, %s,%s)"
        val: tuple = (Id, user.FirstName, user.LastName, user.Age, user.Title, user.Department)
        cursor.execute(insert_str, val)
        
        self.db.commit()
        cursor.close()
        return True













