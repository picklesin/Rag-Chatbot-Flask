import os
from flask import render_template, url_for, redirect, Blueprint, request, flash, current_app, jsonify
from dotenv import load_dotenv
from werkzeug.utils import secure_filename
from app.rag_agent import ingest_pdf, chat_response


main = Blueprint("main", __name__)

load_dotenv()


@main.route("/")
def home():
    return render_template("index.html")

ALLOWED_EXTENSIONS = {'pdf'}
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS 



@main.route("/", methods=['GET', 'POST'])
def upload():
  
    if request.method == 'POST':

        if 'file' not in request.files:
            flash('No file part')
            return redirect(url_for('main.home'))

        file = request.files['file']
    
        if file.filename == '':
            flash('No selected file')
            return redirect(url_for('main.home'))
        

        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file_path = os.path.join(current_app.config['UPLOAD_FOLDER'], filename)
        
            file.save(file_path)
            ingest_pdf(file_path)
          
            flash("PDF uploaded!")
            return redirect(url_for('main.home'))
        
        else:
            flash("Only PDF files are allowed.")
            return redirect(url_for('main.home'))
        
   

@main.route("/chatbot", methods=["POST"])
def chat_bot():

    data = request.get_json()
    question= data.get('data')
    response = "".join(chat_response(question))

    try:
        return jsonify({"message":response})
    
    except Exception as e:
        error_msg = f"Error: {str(e)}"
        return jsonify({"response":True, "message":error_msg})
    



