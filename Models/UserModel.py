class User:

  def __init__(self, ID="", FirstName="", LastName="", Age=0, Title="", Department="") -> None:
    self.ID: str = ID
    self.FirstName: str = FirstName
    self.LastName: str = LastName
    self.Age: int = Age
    self.Title: str = Title
    self.Department: str = Department
