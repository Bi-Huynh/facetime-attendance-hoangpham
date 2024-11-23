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


@app.route("/api/users")
def get_users():
  db = Database()
  result_select: list[User] = db.select_users()
  result = {
      "status": 200,
      "data-users": [user.__dict__ for user in result_select]
    }
  return jsonify(result)


@app.route("/api/users/<string:user_id>")
def get_user_by_userid(user_id: str):
  pass


@app.route("/api/user/insert", methods=["POST"])
def insert_user_db():
  data = request.get_json()
  user_insert = User()
  user_insert.Create_Data_Insert(**data)
  db = Database()
  db.insert_user(user_insert)
  return jsonify({"status": 200, "message": "Insert successful", "data_insert": user_insert.__dict__})


@app.route("/api/timesheets/<string:user_id>")
def get_timesheet_by_userid(user_id: str):
  pass


@app.route("/api/timesheets")
def get_timesheets():
  db = Database()
  result_select: list[TimeSheet] = db.select_timesheets()
  result = {
      "status": 200,
      "data-timesheets": [timesheet.__dict__ for timesheet in result_select]
    }
  return jsonify(result)


@app.route("/api/timesheet/insert", methods=["POST"])
def insert_timesheet_db():
  data = request.get_json()
  timesheet_insert = TimeSheet()
  timesheet_insert.Create_Data_Insert(**data)
  db = Database()
  db.insert_timesheet(timesheet_insert)
  return jsonify({"status": 200, "message": "Insert successful", "data_insert": timesheet_insert.__dict__})


if __name__ == "__main__":
  app.run("0.0.0.0", port=8080, debug=True)
