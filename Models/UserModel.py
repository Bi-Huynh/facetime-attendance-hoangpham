class User:

  def __init__(self, Id="", firstname="", lastname="", age=0, title="", department="") -> None:
    self.ID: str = Id
    self.FirstName: str = firstname
    self.LastName: str = lastname
    self.Age: int = age
    self.Title: str = title
    self.Department: str = department
