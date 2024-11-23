from flask import Flask, render_template, jsonify, request
from Models.UserModel import User
from Helper.DatabaseHelper import Database

app = Flask(__name__)


@app.route('/')
def home_page():
  db = Database()
  users = db.select_user()
  return render_template('home.html', users=users)


@app.route("/api/users")
def get_users():
  db = Database()
  result_select: list[User] = db.select_user()
  result = {
      "status": 200,
      "data-users": [user.__dict__ for user in result_select]
    }
  return jsonify(result)


@app.route("/api/user/insert", methods=["POST"])
def insert_attendace_db():
  data = request.get_json()
  user_insert = User(**data)
  db = Database()
  db.insert_user(user_insert)
  return jsonify({"status": 200, "message": "Insert successful", "data_insert": user_insert.__dict__})


if __name__ == "__main__":
  app.run("0.0.0.0", port=8080, debug=True)
