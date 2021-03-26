
from flask import render_template, url_for, redirect
from TopicTool import app

@app.route("/")
def index():
    return render_template("index.html")