import os
from dotenv import load_dotenv
load_dotenv()

class TestConfig():
    GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY")
    SECRET_KEY = os.getenv("SECRET_KEY")
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER")
    DEBUG = True


class Production():
    GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY")
    SECRET_KEY = os.getenv("SECRET_KEY")
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER_PRODUCTION")

