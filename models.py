from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from app import app

#Initialize Database
db = SQLAlchemy(app)

#Tables
class User(UserMixin, db.Model()):
    id = db.Column(db.Integer(), primary_key=True, unique=True, nullable=False)
    username = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), unique=False, nullable=False)
    fullname = db.Column(db.String(), unique=False, nullable=False)
    gender = db.Column(db.String(), unique=False, nullable=False)
    user_id = db.Column(db.String(), unique=True, nullable=False)

class Invite(db.Model()):
    id = db.Column(db.Integer(), primary_key=True, unique=True, nullable=False)
    owner = db.Column(db.String(), unique=False, nullable=False)
    recipient = db.Column(db.String(), unique=False, nullable=False)
    message = db.Column(db.String(), unique=False, nullable=False)
    link = db.Column(db.String(), unique=True, nullable=False)