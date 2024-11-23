import uuid

class User:

  def __init__(self) -> None:
    self.ID: str = ""
    self.FirstName: str = ""
    self.LastName: str = ""
    self.Age: int = 0
    self.Title: str = ""
    self.Department: str = ""
  
  def Create_Data_Insert(self, FirstName="", LastName="", Age=0, Title="", Department=""):
    self.ID = str(uuid.uuid4())
    self.FirstName = FirstName
    self.LastName = LastName
    self.Age = Age
    self.Title = Title
    self.Department = Department
  
  def Create_Data_Select(self, ID="", FirstName="", LastName="", Age=0, Title="", Department=""):
    self.ID = ID
    self.FirstName = FirstName
    self.LastName = LastName
    self.Age = Age
    self.Title = Title
    self.Department = Department
