import os
from dotenv import load_dotenv
load_dotenv()

class Config():
 
    GEMINI_API_KEY = os.getenv('GOOGLE_API_KEY')

    UPLOAD_FOLDER = os.getenv('UPLOAD_FOLDER')