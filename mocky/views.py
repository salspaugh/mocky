
from flask import g, request, render_template, send_from_directory, url_for
from werkzeug import secure_filename

from mocky import app
from mocky import api

import json

@app.route("/", methods=["GET", "POST"])
def recommendations():
    if request.method == "GET":
        recommendations = api.recommendations() 
    elif request.method == "POST":
        selected = json.loads(request.form["data"])
        if request.form["remove"]:
            api.remove_recommendation(selected)
            recommendations = api.recommendations()
        elif request.form["samefields"]:
            recommendations = api.recommendations_with_these_fields(selected)
        elif request.form["samemarks"]:
            recommendations = api.recommendations_with_these_marks(selected)
    return render_template("index.html", recommendations=recommendations)

@app.route("/data/<path:filename>")
def data(filename):
    return send_from_directory("data", filename) 


    
