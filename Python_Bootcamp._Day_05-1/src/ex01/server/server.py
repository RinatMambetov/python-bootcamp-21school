from flask import Flask, render_template, request, redirect, url_for, send_from_directory
import os
import mimetypes

app = Flask(__name__)
UPLOAD_FOLDER = os.path.basename('uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in {'mp3', 'wav', 'ogg'}


def get_mime_type(filename):
    return mimetypes.guess_type(filename)[0]


@app.route('/')
def index():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('index.html', files=files, mimetypes=mimetypes)


@app.route('/upload', methods=['POST'])
def upload():
    file = request.files['file']
    if file and allowed_file(file.filename):
        filename = file.filename
        file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        # redirect to homepage after successful upload
        return redirect(url_for('index'))
    else:
        return "Non-audio file detected"


@app.route('/uploads/<filename>')
def serve_file(filename):
    # check if file exists in upload folder
    if os.path.isfile(os.path.join(app.config['UPLOAD_FOLDER'], filename)):
        # serve file with correct MIME type
        mimetype = get_mime_type(filename)
        return send_from_directory(app.config['UPLOAD_FOLDER'], filename, mimetype=mimetype)
    else:
        return "File not found", 404


@app.route('/uploads')
def list_files():
    files = os.listdir(app.config['UPLOAD_FOLDER'])
    return render_template('uploads.html', files=files)


if __name__ == '__main__':
    app.run(port=8888, debug=True)
