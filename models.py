from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import enum
from main import app

ENV = 'dev'

if ENV == 'dev':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://rzlnxwbqfcsmhw:dea826539982c006e53b3c6ad87fd6b467e2391c72be144b9d52a1ba88a37817@ec2-23-22-191-232.compute-1.amazonaws.com:5432/d6dqrvufk6jund'
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Departments(enum.Enum):
    software = 1
    mechanical = 2

class Year(enum.Enum):
    first_year = 1
    second_year = 2
    third_year = 3
    fourth_year = 4

class Domains(enum.Enum):
    documentation = 1
    rnd = 2
    promotions = 3

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.Column(db.String(100), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    past_experience = db.Column(db.Text, nullable=False)
    reason = db.Column(db.Text, nullable=False)
    phone_number = db.Column(db.Unicode(11))
    department = db.Column(db.Enum(Departments),  nullable=False)
    year = db.Column(db.Enum(Year),  nullable=False)
    domain = db.Column(db.Enum(Domains),  nullable=False)

    def __repr__(self):
        return f"User('{self.first_name}', '{self.email}', '{self.department}')"
