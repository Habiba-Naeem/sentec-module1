from flask import Flask, session, render_template, request, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from sqlalchemy_utils import *
app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://mownmbfgyxlpek:4b3ea0e203756ef6eecd8c5393123945d7757f95b6540b59a05656d1ea18b675@ec2-184-73-198-174.compute-1.amazonaws.com:5432/d83s5570udk9do'
db = SQLAlchemy(app)

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(120), nullable=False)
    last_name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    past_experience = db.Column(db.Text, nullable=False)
    reason = db.Column(db.Text, nullable=False)
    phone_number = db.Column(db.Unicode(11))
    department =  db.Column(db.String(120), nullable = False)
    year = db.Column(db.String(120), nullable = False)
    domain = db.Column(db.String(120), nullable=False)
    
    def __repr__(self):
        return f"User('{self.first_name}', '{self.email}', '{self.department}')"















@app.route('/')
def hello_world():
    return render_template("index.html", index = "index", )

@app.route('/submit', methods=["GET", "POST"])
def submit():
    if request.method == "POST":
        first_name = request.form.get("first_name")
        last_name = request.form.get("last_name")
        email = request.form.get("email")
        phone_number = request.form.get("phone_number")
        year = request.form.get("year")
        past_experience = request.form.get("past_experience")
        domain = request.form.get("domain")
        reason = request.form.get("reason")
        department = request.form.get("department")

        user = User(first_name = first_name, last_name = last_name, email = email,
        past_experience = past_experience, reason = reason, phone_number = phone_number, 
        department = department, year = year, domain = domain)
        db.session.add(user)
        db.session.commit()

        return render_template("index.html")