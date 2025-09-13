from flask import Blueprint,jsonify,request,send_from_directory
from app.models import Student
from app.db import db
import re
import os

# create student blueprint
student_bp=Blueprint("student",__name__,url_prefix="/student")

UPLOAD_FOLDER="uploads"

# @student_bp.route("/", methods=["GET"])
# def home():
#     # return "Welcome to my API"
#     return """
#     <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Flask API</title>
# </head>
# <body>
#     <h1>Welcome to our site</h1>
# </body>
# </html>

# """

# routes and controller logic
@student_bp.route("/",methods=["GET"])
def single_student():
    print("Single student")
    return "Single student"

@student_bp.route("/add/json",methods=["POST"])
def add_student_json():
    print("Add user was hit")
    data=request.get_json()

    name=data.get("name")
    email=data.get("email")

    # Validation
    if not name:
        return jsonify({"error":"Name is required"}),400
    if not email:
        return jsonify({"error":"Email is required"}),400
    email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not re.match(email_regex,email):
        return jsonify({"error":"Invalid email address"})
    # check for existing student
    exists = Student.query.filter_by(email=email).first()
    if exists:
        return jsonify({"error":"Email in use"}),400
    new_student=Student(name=name,email=email)
    db.session.add(new_student)
    db.session.commit()

    return jsonify({
        "message":"Student added",
        "student":{
            "id":new_student.id,
            "name":new_student.name,
            "email":new_student.email,
            "created_at":new_student.created_at
        }
    }),201
    print("Received Data", data)
    return "Adding a student json",200

@student_bp.route("/add/form",methods=["POST"])
def add_student_form():
    print("Add user was hit")
    # data=request.get_json()

    name=request.form.get("name")
    email=request.form.get("email")

    # Validation
    if not name:
        return jsonify({"error":"Name is required"}),400
    if not email:
        return jsonify({"error":"Email is required"}),400
    email_regex = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not re.match(email_regex,email):
        return jsonify({"error":"Invalid email address"})
    # check for existing student
    exists = Student.query.filter_by(email=email).first()
    if exists:
        return jsonify({"error":"Email in use"}),400
    new_student=Student(name=name,email=email)
    db.session.add(new_student)
    db.session.commit()

    return jsonify({
        "message":"Student added",
        "student":{
            "id":new_student.id,
            "name":new_student.name,
            "email":new_student.email,
            "created_at":new_student.created_at
        }
    }),201
    return "Adding a student with form",200

@student_bp.route("/picture",methods=["POST"])
def add_student_picture():
    ALLOWED_EXTENSIONS={"png","jpg","jpeg"}
    os.makedirs(UPLOAD_FOLDER, exist_ok=True)

    if "pic" not in request.files:
        return jsonify({"error":"No file"}),400
    file=request.files["pic"]
    if file.filename =="":
        return jsonify({"error":"No file selected"}),400
    filename=file.filename
    ext=filename.rsplit(".",1)[1].lower()

    if ext not in ALLOWED_EXTENSIONS:
        return jsonify({"error":"Invalid file type"}),400
    
    filepath=os.path.join(UPLOAD_FOLDER,filename)
    file.save(filepath)

    return jsonify({
        "message":"File uploaded succefully",
        "filename":filename,
        "path":filepath
    }),201

#dynamic route :REACT<>
#---file serving --
@student_bp.route("/picture/<filename>",methods=["GET"])
def serve_file(filename):
    cwd=os.path.dirname(__file__)
    uploads=os.path.join(cwd,"../../uploads")
    return send_from_directory(uploads,filename)

@student_bp.route("/edit",methods=["PUT"])
def edit_user():
    print("User was edited")
    return "Editing a student"

@student_bp.route("/list",methods=["GET"])
def list_users():
    print("List Students")
    # users=[{"name":"Maggie"}, {"name":"Cynthia"}]
    # return jsonify(users)
    students = Student.query.all()
    students_list = [{"id": s.id, "name": s.name, "email": s.email, "created_at": s.created_at} for s in students]
    return jsonify(students_list), 200

    return "List ALL students FROM"