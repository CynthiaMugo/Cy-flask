import os
from dotenv import load_dotenv

# loading environmental variables

load_dotenv()

class Config:
    SQLALCHEMY_DATABASE_URI=os.getenv("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    SECRET_KEY="secret"