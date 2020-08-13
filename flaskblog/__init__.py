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

app=Flask(__name__)
secretsObj=Secrets()
app.config['SECRET_KEY']=secretsObj.SECRET_KEY
app.config['SQLALCHEMY_DATABASE_URI']="sqlite:///site.db"
db=SQLAlchemy(app)
bcrypt=Bcrypt(app)
loginManager=LoginManager(app)

from flaskblog import routes
