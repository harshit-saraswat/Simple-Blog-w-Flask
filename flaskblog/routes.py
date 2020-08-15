# -*- coding: utf-8 -*-
"""
Created on Wed Aug  12 11:49:05 2020

@author: harshit-saraswat
"""

from flask import render_template, url_for, flash, redirect, request
from flaskblog import app, db, bcrypt
from flaskblog.forms import RegistrationForm,LoginForm, UpdateAccountForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required

posts = [
        {
            'author':'harshit-saraswat',
            'title':'Post 1',
            'content':'Lorem ipsum dolor sit amet, consectetur adipiscing elit. Quisque faucibus commodo venenatis. Fusce vel feugiat enim, in bibendum sapien. Proin vel cursus mi, in tincidunt sem. Curabitur consequat justo eget feugiat varius. Sed quis pellentesque metus, nec feugiat nunc. In hac habitasse platea dictumst. Duis arcu nunc, dapibus id bibendum eget, congue nec nunc. Vestibulum accumsan velit nisl, eget hendrerit purus pharetra ac. Morbi varius erat in pulvinar interdum.',
            'date_posted':'August 8th, 2020'
        }, 
        {
            'author':'jane-doe',
            'title':'Post 2',
            'content':'Aliquam est nulla, pellentesque vel suscipit eget, pharetra a tellus. Interdum et malesuada fames ac ante ipsum primis in faucibus. Aliquam lacinia elit a pulvinar malesuada. Nulla congue at mauris in luctus. Nunc porta dui id sapien convallis pretium. Morbi tempus magna mauris, eu commodo velit aliquam quis. Maecenas sagittis erat ac sagittis volutpat. Curabitur erat sapien, congue sed tincidunt in, pulvinar sed augue. In ipsum arcu, hendrerit vel nulla et, sagittis gravida quam.',
            'date_posted':'August 7th, 2020'
        }
    ]

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html",posts=posts)

@app.route("/about")
def about():
    return render_template("about.html",title="About")

@app.route("/register",methods=['GET','POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashedPassword=bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user=User(username=form.username.data,email=form.email.data,password=hashedPassword)
        db.session.add(user)
        db.session.commit()
        flash(f'Your account has been created successfully! Please Login to continue to your feed.','success')
        return redirect(url_for('login'))
    return render_template("register.html", title="Register", form=form)

@app.route("/login",methods=['GET','POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user=User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password,form.password.data):
            login_user(user,remember=form.remember.data)
            nextPage=request.args.get('next')
            return redirect(url_for(nextPage)) if nextPage else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password!','danger')
    return render_template("login.html", title="Login", form=form)

@app.route("/logout")
def logout():
    logout_user()
    flash('Logged out successfully!','info')
    return redirect(url_for('home'))


@app.route("/account",methods=['GET','POST'])
@login_required
def account():
    form = UpdateAccountForm()
    if form.validate_on_submit():
        current_user.username=form.username.data
        current_user.email=form.email.data
        db.session.commit()
        flash('Your account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method=='GET':
        form.username.data=current_user.username
        form.email.data=current_user.email
    image_file= url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template("account.html", title="Account", image_file=image_file, form = form)