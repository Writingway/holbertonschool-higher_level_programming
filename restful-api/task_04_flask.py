#!/usr/bin/python3
from flask import Flask
from flask import jsonify
from flask import request
import json

app = Flask(__name__)
users = {}


@app.route("/add_user", methods=["POST"])
def add_user():
    payload = request.get_json(silent=True)
    if payload is None:
        return jsonify({"error": "Invalid JSON"}), 400

    username = payload.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    users[username] = payload

    return jsonify({"message": "User added", "user": payload}), 201


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
