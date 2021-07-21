import glob
import os
import zipfile
from flask import Flask, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename
ROOT_DIR = os.path.dirname(os.path.abspath(os.curdir))
ROOT = ROOT_DIR.replace("\\","/")

UPLOAD_FOLDER = ROOT + '/app/Uploads'
ZIP_FOLDER = ROOT + '/app/Zips'
UPLOAD_EXTENSIONS = set(['zip'])
app = Flask(__name__, static_folder=ROOT + '/app/static', static_url_path='/static')



def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in UPLOAD_EXTENSIONS


@app.route('/', methods=['GET', 'POST'])
def main():
    if request.method == 'POST':

        if 'files[]' not in request.files:
            return redirect(request.url)

        files = request.files.getlist('files[]')

        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(ZIP_FOLDER, filename))
                zip_ref = zipfile.ZipFile(os.path.join(ZIP_FOLDER, filename), 'r')
                zip_ref.extractall(UPLOAD_FOLDER)
                zip_ref.close()
                return redirect(url_for('main',
                                        filename=filename))
    return render_template('index.html')


@app.route('/train', methods=['POST'])
def train():
    from src import trainer as trainer
    trainer.train(ROOT + "/app/Uploads")
    print("--------------TRAINING COMPLETEE ------------")
    return render_template('index.html')


@app.route('/recognize', methods=['POST'])

def recognize():
    from src import screengrabber
    import attendancechecker as ac
    ac.check()
    print("ATTENDANCE CHECKED!")
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
