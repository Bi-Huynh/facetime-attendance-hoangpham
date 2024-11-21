from flask import Flask, render_template, jsonify, request
from Models.UserModel import User
from Helper import FileHelper

app = Flask(__name__)


@app.route('/')
def home_page():
  users = [User("John", 25), User("Jane", 30), User("Bob", 35)]
  return render_template('home.html', users=users)


@app.route("/api/users")
def get_users():
  users = [User("John", 25), User("Jane", 30), User("Bob", 35)]
  return jsonify([user.__dict__ for user in users])


@app.route("/api/user/insert", methods=["POST"])
def insert_attendace_db():
  return jsonify({"status": 404, "message": "API is not available"})


if __name__ == "__main__":
  app.run("0.0.0.0", port=8080, debug=True)
