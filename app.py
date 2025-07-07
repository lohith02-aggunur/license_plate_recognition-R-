from flask import Flask, render_template, request
import pytesseract
import cv2
import os
import numpy as np

pytesseract.pytesseract.tesseract_cmd = "/usr/bin/tesseract"

app = Flask(__name__, static_folder='static', template_folder='templates')
app.config['UPLOAD_FOLDER'] = 'uploads'

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/success', methods=['POST'])
def success():
    if 'file' not in request.files:
        return 'No file part'
    file = request.files['file']
    if file.filename == '':
        return 'No selected file'
    if file:
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(filepath)

        img = cv2.imread(filepath)
        img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        text = pytesseract.image_to_string(img_gray)
        return render_template('success.html', text=text, image_path=filepath)
    return 'Something went wrong'

if __name__ == '__main__':
    app.run(debug=True)
