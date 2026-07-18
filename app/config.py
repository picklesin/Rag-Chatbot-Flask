import os
from dotenv import load_dotenv
load_dotenv()

class Config():
 
    GEMINI_API_KEY = os.getenv('GOOGLE_API_KEY')
    SECRET_KEY = os.getenv('SECRET_KEY')
    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER')