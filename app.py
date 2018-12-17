import os
from flask import Flask, render_template, jsonify, request, redirect, url_for, flash, send_from_directory
from flask import request
import requests
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'static/images'
ALLOWED_EXTENSIONS = set(['png', 'jpg'])

#hi


app = Flask(__name__)
app.secret_key = b'n\xfc\xb5\x10\xca\xb1\xca\xf3\x89\xc8\x8b\x02\xc0\xfc\xf5\xd0'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
            filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)



@app.route('/',methods=['GET','POST'])
def index():

    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)

        file = request.files['file']

        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
            return redirect(url_for('uploaded_file', filename=filename))
                                                                                                                                                                                                                                                                                                                                                                                                                                

    return render_template("index.html")








if __name__ == "__main__":
  app.run(debug=True)
