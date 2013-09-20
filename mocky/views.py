
from flask import g, render_template, url_for
from werkzeug import secure_filename
from mocky import app

@app.route('/')
def index():
    return render_template('index.html')
