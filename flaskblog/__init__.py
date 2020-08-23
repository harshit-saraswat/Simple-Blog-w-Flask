# -*- coding: utf-8 -*-
"""
Created on Wed Aug  12 11:45:05 2020

@author: harshit-saraswat
"""

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_mail import Mail
from flaskblog.config import Config


db=SQLAlchemy()
bcrypt=Bcrypt()
loginManager=LoginManager()
loginManager.login_view='users.login'
loginManager.login_message_category='info'
mail=Mail()


def create_app(config_class=Config):
	app=Flask(__name__)
	app.config.from_object(Config)

	db.init_app(app)
	bcrypt.init_app(app)
	loginManager.init_app(app)
	mail.init_app(app)

	from flaskblog.users.routes import users
	from flaskblog.posts.routes import posts
	from flaskblog.main.routes import main
	from flaskblog.errors.handlers import errors

	app.register_blueprint(users)
	app.register_blueprint(posts)
	app.register_blueprint(main)
	app.register_blueprint(errors)

	return app