from flask import Blueprint, render_template, redirect, flash
from flask_login import LoginManager, login_required, current_user, login_user, logout_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField, SubmitField
from wtforms.validators import InputRequired
from app import app
from models import db, User
from cryptography.fernet import Fernet
from flask_bcrypt import Bcrypt

#Initialize Blueprint
authbp = Blueprint("auth", __name__, url_prefix="/auth", template_folder="templates", static_folder="static")

#Login Manager
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login"

#Bcrypt
bcrypt = Bcrypt(app)

#Userloader
@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

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

#Fernet 
fernet = Fernet(app.config['SECRET_KEY'])

#Routes
@authbp.route('/')
def mainpage():
    return redirect('/dashboard')

@authbp.route('/login')
def login():
    if current_user.is_authenticated:
        return redirect('/dashboard')
    form = LoginForm()
    if form.validate_on_submit():
        try:
            check_user = User.query.filter_by(username=form.username.data).first()
            if bcrypt.check_password_hash(check_user.hashed_password, form.password.data):
                flash("Login Successful!", 'success')
                return redirect('/dashboard')
            else:
                flash("Wrong password!", 'error')
                return redirect('/auth/login')
        except AttributeError:
            db.session.rollback()
            flash("Incorrect Username or Password", 'error')
            return redirect('/auth/login')
        except Exception as e:
            db.session.rollback()
            flash("Something went wrong, try again!", 'error')
            return redirect('/auth/login')

