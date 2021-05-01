from flask import Flask, session, render_template, request, url_for
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template("index.html", index = "index")