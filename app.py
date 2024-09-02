from flask import Flask, request, send_file, render_template
from pytube import YouTube
import re

app = Flask(__name__)

def safe_filename(title):
    # Remove any characters that are not allowed in file names
    return re.sub(r'[\/:*?"<>|]', '', title) + '.mp4'

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/download', methods=['POST'])
def download():
    url = request.form['url']
    yt = YouTube(url)
    stream = yt.streams.get_highest_resolution()
    title = yt.title
    filename = safe_filename(title)
    file_path = stream.download(filename=filename)
    return send_file(file_path, as_attachment=True)

if __name__ == '__main__':
    app.run(debug=True)
