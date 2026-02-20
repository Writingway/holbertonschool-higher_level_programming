from flask import Flask, jsonify, request
from werkzeug.security import generate_password_hash, check_password_hash
from flask_jwt_extended import JWTManager, jwt_required, create_access_token
from flask_jwt_extended import get_jwt_identity
from flask_httpauth import HTTPDigestAuth

app = Flask(__name__)
app.config['SECRET_KEY'] = '0c688cae24884016b406a7f9ed93e7ac'
jwt = JWTManager(app)
auth = HTTPDigestAuth()

users = {
    "user1": {
        "username": "user1",
        "password": generate_password_hash("password"),
        "role": "user"
    },
    "admin1": {
        "username": "admin1",
        "password": generate_password_hash("password"),
        "role": "admin"
    }
}


@app.route("/basic-protected", methods=["GET"])
@auth.login_required
def basic_protected():
    user = request.authorization
    if user and user.username in users:
        stored_user = users[user.username]
        if check_password_hash(stored_user["password"], user.password):
            return jsonify({"message": "Basic Auth: Access Granted"}), 200

    return jsonify({"error": "401 Unauthorized"}), 401


@app.route("/login", methods=["POST"])
def login():
    data = request.get_json(silent=True)
    if not data:
        return jsonify({"error": "Invalid JSON"}), 400

    username = data.get("username")
    password = data.get("password")
    if not username or not password:
        return jsonify({"error": "Invalid credentials"}), 401

    user = users.get(username)
    if user and check_password_hash(user["password"], password):
        token = create_access_token(identity=username, additional_claims={
            "role": user["role"]
        })
        return jsonify({"access_token": token}), 200


@app.route("/jwt-protected", methods=["GET"])
@jwt_required()
def jwt_protected():
    return "JWT Auth: Access Granted"


@app.route("/admin-only", methods=["GET"])
@jwt_required()
def admin_only():
    username = get_jwt_identity()
    user = users.get(username)

    if user and user["role"] == "admin":
        return jsonify({"message": "Admin Access: Granted"}), 403

    return "Admin access required"


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401


@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401


@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401


@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401


@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401


if __name__ == "__main__":
    app.run()
