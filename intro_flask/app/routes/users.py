from flask import Blueprint,jsonify,request,send_from_directory
from app.models import User
from app.db import db
import re
import os
from flask_bcrypt import Bcrypt
from flask_jwt_extended import create_access_token
from datetime import timedelta

bcrypt = Bcrypt()
# create student blueprint
user_bp=Blueprint("user",__name__,url_prefix="/user")

@user_bp.route("/add", methods=["POST"])
def add_user():
    data=request.get_json()

    name=data.get("name")
    email=data.get("email")
    password=data.get("password")

    # Validation
    if not name:
        return jsonify({"error":"Name is required"}),400
    if not email:
        return jsonify({"error":"Email is required"}),400
    email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not re.match(email_regex,email):
        return jsonify({"error":"Invalid email address"}),400
    if not password:
        return jsonify({"error":"Password is required"}),400

    # check for existing user
    existing_user=User.query.filter_by(email=email).first()
    if existing_user:
        return jsonify({"error":"User with this email already exists"}),400
    
    hashed_password=bcrypt.generate_password_hash(password).decode("utf-8")

    new_user=User(name=name,email=email,password=hashed_password)
    db.session.add(new_user)
    db.session.commit()

    return jsonify({
        "Message": "New user added",
        "User": {
            "id": new_user.id,
            "name": new_user.name,
            "email": new_user.email,
            "created_at": new_user.created_at
        }   
    }),201

@user_bp.route("/login", methods=["POST"])
def login_user():
    data=request.get_json()

    email=data.get("email")
    password=data.get("password")

    if not email or not password:
        return jsonify({"error":"Email and password are required"}),400

    user=User.query.filter_by(email=email).first()
    if not user:
        return jsonify({"error":"User not found"}),401
    
    check_password=bcrypt.check_password_hash(user.password,password)
    if not check_password:
        return jsonify({"error":"Invalid password"}),401

    access_token = create_access_token(
        identity={"id":user.id, "name":user.name},
        expires_delta=timedelta(hours=1))
    return jsonify({
        "token": access_token,
        "user": {
            "id": user.id,
            "name": user.name
    }
    }), 200