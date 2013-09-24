
from flask import g, request, render_template, url_for
from werkzeug import secure_filename

from mocky import app
from mocky import api

@app.route("/", methods=["GET", "POST"])
def recommendations():
    if request.method == "GET":
        recommendations = api.recommendations() 
    elif request.method == "POST":
        recommendations = api.recommendations_like_this(request.form["data"])
    return render_template("index.html", recommendations=recommendations)
