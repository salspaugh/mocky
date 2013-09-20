
from flask import g, render_template, url_for
from werkzeug import secure_filename

from mocky import app
from mocky import api

@app.route("/")
def index():
    recommendations = api.generate_recommendations() 
    return render_template("index.html", recommendations=recommendations)
