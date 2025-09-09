from flask import Blueprint,jsonify,request

# create student blueprint
student_bp=Blueprint("student",__name__)

# routes and controller logic
@student_bp.route("/student/add",methods=["POST"])
def add_user():
    print("Add user was hit")
    return "Adding a student"

@student_bp.route("/students",methods=["GET"])
def list_users():
    print("List Students")
    return "List ALL students"