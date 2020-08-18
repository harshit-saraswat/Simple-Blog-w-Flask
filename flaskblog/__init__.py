# -*- coding: utf-8 -*-
"""
Created on Wed Aug  12 11:45:05 2020

@author: harshit-saraswat
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flaskblog.secrets import Secrets
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail

app=Flask(__name__)
secretsObj=Secrets()
app.config['SECRET_KEY']=secretsObj.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///site.db"
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
loginManager=LoginManager(app)
loginManager.login_view='login'
loginManager.login_message_category='info'

app.config('MAIL_SERVER')='smtp.googlemail.com'
app.config('MAIL_PORT')=587
app.config('MAIL_USE_TLS')=True
app.config('MAIL_USERNAME')=secretsObj.EMAIL_ADDRESS
app.config('MAIL_PASSWORD')=secretsObj.PASSWORD
mail=Mail(app)


from flaskblog import routes
