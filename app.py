from flask import Flask, flash, request, redirect, url_for, render_template
from flask_restful import Resource, Api
import os
import personDetect
from werkzeug.utils import secure_filename

app = Flask(__name__)
api = Api(app)

#Folder do którego zostają zapisane
#przesłane zdjęcia
UPLOAD_FOLDER = 'static/uploads/'

app.secret_key = "secret key"
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg'])

#Dozwolone pliki do przesłania
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/', methods=['POST'])
def upload_image():
    if 'file' not in request.files:
        flash('No file part')
        return redirect(request.url)
    file = request.files['file']
    if file.filename == '':
        flash('Nie wybrano zdjęcia do przesłania')
        return redirect(request.url)
    #Jeżeli załączono plik i posiada on
    #odpowiednie rozszerzenie
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        person_count = personDetect.personDetectionFromImage(filename)
        flash(person_count)
        return render_template('index.html', filename=filename)
    else:
        flash('Dozwolone rozszerzenia to - png, jpg, jpeg')
        return redirect(request.url)


@app.route('/display/<filename>')
def display_image(filename):
    return redirect(url_for('static', filename='uploads/' + filename), code=301)


if __name__ == '__main__':
    app.run()
