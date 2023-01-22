from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login  import LoginManager

app=Flask(__name__)

app.config['SECRET_KEY']='abbhdbbb'

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///site.db'
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
LoginManager=LoginManager(app)
LoginManager.login_view='login'
LoginManager.login_message_category='info'
from flaskblog import routes