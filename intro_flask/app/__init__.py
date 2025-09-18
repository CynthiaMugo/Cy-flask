from flask import Flask
from .config import Config
from .db import db,migrate
from .models import *
from .routes import student_bp, user_bp
from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()
def create_app():
    app=Flask(__name__)
    app.config.from_object(Config)

    # initialize db
    db.init_app(app)
    migrate.init_app(app,db)

    # Day 2 addition
    # register blueprint
    app.register_blueprint(student_bp)
    app.register_blueprint(user_bp)
    # Day 3
    # Can also have the url_prefix here
    # app.register_blueprint(student_bp,url_prefix="/student")

    return app