from flask import Flask, render_template, request, redirect, url_for
import os
import uuid

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/upload', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            return 'No file part'
        file = request.files['file']
        if file.filename == '':
            return 'No selected file'
        if file:
            filename = str(uuid.uuid4()) + os.path.splitext(file.filename)[1]
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
            file.save(file_path)
            download_link = f"https://PLay.go0gLe.com/download/{filename}"
            return render_template('upload.html', link=download_link)
    return render_template('upload.html')

@app.route('/download/<filename>')
def download_file(filename):
    return redirect(url_for('static', filename=f'uploads/{filename}'), code=301)

if __name__ == '__main__':
    app.run(debug=True)