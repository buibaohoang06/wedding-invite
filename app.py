from flask import Flask
from cryptography.fernet import Fernet

#Initialize Flask App
app = Flask(__name__)

#Configs
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///database.db"
app.config['SECRET_KEY'] = Fernet.generate_key()

