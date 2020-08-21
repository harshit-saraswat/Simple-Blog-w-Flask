 # -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 23:08:25 2020

@author: harshit-saraswat
"""

from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from flask_login import current_user
from wtforms import StringField, PasswordField, SubmitField, BooleanField, TextAreaField
from wtforms.validators import DataRequired,Length,Email, EqualTo, ValidationError
from flaskblog.models import User
