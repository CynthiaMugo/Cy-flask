from flask import Blueprint,jsonify,request

# create student blueprint
student_bp=Blueprint("student",__name__,url_prefix="/student")

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
def add_user_json():
    print("Add user was hit")
    data=request.get_json()
    print("Received Data", data)
    return "Adding a student json",200

@student_bp.route("/add/form",methods=["POST"])
def add_user_form():
    print("Add user was hit")
    return "Adding a student with form",200

@student_bp.route("/edit",methods=["PUT"])
def edit_user():
    print("User was edited")
    return "Editing a student"

@student_bp.route("/list",methods=["GET"])
def list_users():
    print("List Students")
    users=[{"name":"Maggie"}, {"name":"Cynthia"}]
    return jsonify(users)
    return "List ALL students FROM"