from dotenv import load_dotenv
import os
import mysql.connector
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
        return result
        













