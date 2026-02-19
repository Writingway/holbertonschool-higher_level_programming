#!/usr/bin/python3
from flask import Flask
from flask import jsonify
from flask import request
import json

app = Flask(__name__)
users = {}


@app.route("/add_user", methods=["POST"])
def add_user():
    if request.method == "POST":
        content = json.loads(request.data)
        if "username" in content.keys():
            if content["username"] in users:
                return jsonify({
                    "error": "Username already exists"
                }), 409

            if jsonify(content) is None:
                return jsonify({"error": "Invalid JSON"}), 400

            user = {
                "username": content["username"],
                "name": content["name"],
                "age": content["age"],
                "city": content["city"]
            }
            users[content["username"]] = user
            message = "User added successfully"

            return jsonify({
                "message": message,
                "user": user
            }), 201
        else:
            return jsonify({"error": "Username is required"}), 400


@app.route("/users/<username>", methods=["GET"])
def get_user(username):
    user_info = users.get(username)

    if user_info:
        return jsonify(user_info)
    else:
        return jsonify({"error": "User not found"}), 404


@app.route("/status", methods=["GET"])
def status():
    return ("OK")


@app.route("/data", methods=["GET"])
def get_data():
    return jsonify(list(users.keys()))


@app.route("/", methods=["GET"])
def home():
    return "Welcome to the Flask API!"


if __name__ == "__main__":
    app.run()
