# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 01:27:05 2020

@author: harshit-saraswat
"""

from flask import Flask, render_template, url_for, flash, redirect
from secrets import Secrets
from forms import RegistrationForm,LoginForm


app=Flask(__name__)
secretsObj=Secrets()
app.config['SECRET_KEY']=secretsObj.SECRET_KEY

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
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account Created for {form.username.data} Successfully!','success')
        return redirect(url_for('home'))
    return render_template("register.html", title="Register", form=form)

@app.route("/login",methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        if form.email.data == 'admin@blog.com' and form.password.data == 'Admin@123':
            flash(f'Welcome, {form.email.data}! You have been logged in successfully!','success')
            return redirect(url_for('home'))
        else:
            flash(f'Login Unsuccessful. Please check email and password!','danger')
    return render_template("login.html", title="Login", form=form)

if __name__=="__main__":
    app.run(debug=True)
