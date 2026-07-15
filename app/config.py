import os
from dotenv import load_dotenv
load_dotenv()

class Config():
    SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
    SECRET_KEY = os.getenv("SECRET_KEY")
    SQLALCHEMY_TRACK_MODIFICATIONS = os.getenv("SQLALCHEMY_TRACK_MODIFICATIONS")

    GEMINI_API_KEY = os.getenv('GEMINI_API_KEY')

    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER')