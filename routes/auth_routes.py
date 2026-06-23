from flask import Blueprint, request, jsonify, session
from models.user import User
from database.db import db

auth_bp = Blueprint("auth", __name__, url_prefix="/api")


def get_json_or_400():
    data = request.get_json(silent=True)
    if not data:
        return None
    return data


@auth_bp.post("/register")
def register():
    data = get_json_or_400()
    if not data:
        return jsonify({"error": "Missing JSON body"}), 400

    username = (data.get("username") or "").strip()
    email = (data.get("email") or "").strip()
    password = data.get("password")

    if not username or not email or not password:
        return jsonify({"error": "username, email, password are required"}), 400

    if User.query.filter((User.username == username) | (User.email == email)).first():
        return jsonify({"error": "Username or email already exists"}), 409

    user = User(username=username, email=email)
    user.set_password(password)

    db.session.add(user)
    db.session.commit()

    return jsonify({"message": "User registered", "user_id": user.id}), 201


@auth_bp.post("/login")
def login():
    data = get_json_or_400()

    if not data:
        return jsonify({"error": "Missing JSON body"}), 400

    username = (data.get("username") or "").strip()
    password = data.get("password")

    if not username or not password:
        return jsonify({"error": "username and password are required"}), 400

    user = User.query.filter_by(username=username).first()
    if not user or not user.check_password(password):
        return jsonify({"error": "Invalid credentials"}), 401

    session["user_id"] = user.id
    session["username"] = user.username

    return jsonify({"message": "Login successful"}), 200


@auth_bp.post("/logout")
def logout():

    session.clear()
    return jsonify({"message": "Logged out"}), 200

