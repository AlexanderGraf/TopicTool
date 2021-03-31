
from flask import render_template, make_response, url_for, redirect, request
from TopicTool import app
from TopicTool.models import TopicToolDB
import pandas as pd

@app.route("/",methods=["GET","POST"])
@app.route("/index.html", methods = ["GET","POST"])
def index():
    if request.method == "POST":
        uploaded_file = request.files["input_file"]
        if uploaded_file.filename != "":
            data = pd.read_excel(uploaded_file, skiprows = 1)

            # instantiate the DB container
            res = TopicToolDB(data)
            print(res.test())
            print(res.test().dtypes)


    return render_template('index.html')

@app.route("/about.html")
def about():
    return render_template("about.html")