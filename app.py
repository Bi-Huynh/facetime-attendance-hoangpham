from flask import Flask, render_template, jsonify, request
from Models.UserModel import User
from Models.TimeSheetModel import TimeSheet
from Helper.DatabaseHelper import Database

app = Flask(__name__)


@app.route('/')
def home_page():
  db = Database()
  users = db.select_users()
  return render_template('home.html', users=users)


@app.route('/users')
def user_page():
  pass


@app.route('/user/<mssv>')          # Tại đây vừa trả thông tin user và trả luôn thông tin timesheet của user đó luôn
def user_by_id_page(mssv: str):
  pass


@app.post('/user')
def user_by_id_insert_page():
  data = request.get_data()   # làm sao để convert data from sang json để đưa dữ liệu vô trong class
  pass


@app.put('/user/<mssv>')
def user_by_id_edit_page(mssv: str):
  data = request.get_data()   # làm sao để convert data from sang json để đưa dữ liệu vô trong class
  pass


@app.delete('/user/<mssv>')
def user_by_id_delete_page(mssv: str):
  pass



# Api Users
@app.route("/api/users")
def get_users():
  db = Database()
  result_select: list[User] = db.select_users()
  result = {
      "status": 200,
      "data-users": [user.__dict__ for user in result_select]
    }
  return jsonify(result)


@app.route("/api/user/<user_id>")
def get_user_by_userid(user_id: str):
  pass


@app.post("/api/user")
def insert_user_db():
  data = request.get_json()
  user_insert = User()
  user_insert.Create_Data_Insert(**data)
  db = Database()
  db.insert_user(user_insert)
  return jsonify({"status": 200, "message": "Insert successful", "data_insert": user_insert.__dict__})


@app.put("/api/user/<user_id>")
def edit_user_by_userid(user_id: str):
  pass


@app.delete("/api/user/<user_id>")
def delete_user_by_userid(user_id: str):
  pass



# Api Timesheets
@app.route("/api/timesheets/user/<mssv>")     # Viết lại theo user
def get_timesheets(mssv: str):
  db = Database()
  result_select: list[TimeSheet] = db.select_timesheets()
  result = {
      "status": 200,
      "data-timesheets": [timesheet.__dict__ for timesheet in result_select]
    }
  return jsonify(result)


@app.post("/api/timesheet/user")          # Test lại
def insert_timesheet_db():
  data = request.get_json()
  timesheet_insert = TimeSheet()
  timesheet_insert.Create_Data_Insert(**data)
  db = Database()
  db.insert_timesheet(timesheet_insert)
  return jsonify({"status": 200, "message": "Insert successful", "data_insert": timesheet_insert.__dict__})


if __name__ == "__main__":
  app.run("0.0.0.0", port=8080, debug=True)
