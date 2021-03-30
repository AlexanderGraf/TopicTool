
from flask import render_template, make_response, url_for, redirect
from TopicTool import app
from TopicTool.models import TopicToolDB

@app.route("/")
@app.route("/index.html")
def index():
    return render_template("index.html")

@app.route("/about.html")
def about():
    return render_template("about.html")