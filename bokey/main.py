from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import FileField, SubmitField
from flask_wtf.file import FileAllowed
from werkzeug.utils import secure_filename
import cv2
import numpy as np
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'supersecretkey'
app.config['UPLOAD_FOLDER'] = 'static/files'

ALLOWED_EXTENSIONS = {'jpg', 'jpeg', 'png'}  # Define the allowed image file extensions

class UploadFileForm(FlaskForm):
    file = FileField("File", validators=[
        FileAllowed(ALLOWED_EXTENSIONS, 'Only image files are allowed!')
    ])
    submit = SubmitField("Upload File")

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def home():
    form = UploadFileForm()
    if form.validate_on_submit():
        file = form.file.data
        if file:
            file_ext = file.filename.rsplit('.', 1)[1].lower()
            if file_ext in ALLOWED_EXTENSIONS:
                file.save(os.path.join(os.path.abspath(os.path.dirname(__file__)), app.config['UPLOAD_FOLDER'], secure_filename(file.filename)))
                return "File has been uploaded."
            else:
                return "Only image files (JPG, JPEG, PNG) are allowed."
    return render_template('index.html', form=form)

def apply_bokey(file):
    
    return
if __name__ == '__main__':
    app.run(debug=True)
