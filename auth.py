from flask import Blueprint, render_template, redirect, flash
from flask_login import LoginManager, login_required, current_user, login_user, logout_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField, SubmitField
from wtforms.validators import InputRequired
from app import app
from models import User

#Initialize Blueprint
authbp = Blueprint("auth", __name__, url_prefix="/auth", template_folder="templates", static_folder="static")

#Login Manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login"

#Forms
class LoginForm(FlaskForm):
    username = StringField(validators=[InputRequired()], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired()], render_kw={"placeholder": "Password"})
    submit = SubmitField()

class RegisterForm(FlaskForm):
    options = ['Male', 'Female']
    fullname = StringField(validators=[InputRequired()], render_kw={"placeholder": "Fullname"})
    gender = SelectField(label="Gender", options=options)
    username = StringField(validators=[InputRequired()], render_kw={"placeholder": "Username"})
    password = PasswordField(validators=[InputRequired()], render_kw={"placeholder": "Password"})
    submit = SubmitField()
