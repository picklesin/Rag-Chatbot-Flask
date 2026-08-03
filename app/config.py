import os
from dotenv import load_dotenv
load_dotenv()

class BaseConfig():
    GEMINI_API_KEY = os.getenv("GOOGLE_API_KEY")
    SECRET_KEY = os.getenv("SECRET_KEY")
    

class DevelopmentConfig(BaseConfig):
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER")
    DEBUG = True


class ProductionConfig(BaseConfig):
    UPLOAD_FOLDER = os.getenv("UPLOAD_FOLDER_PRODUCTION")
    DATABASE_URL = os.getenv("DATABASE_URL")
    DEBUG = False


