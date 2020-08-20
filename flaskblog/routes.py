# -*- coding: utf-8 -*-
"""
Created on Wed Aug  12 11:49:05 2020

@author: harshit-saraswat
"""

import os
import secrets
from PIL import Image
from flask import render_template, url_for, flash, redirect, request, abort
from flaskblog import app, db, bcrypt, mail
from flaskblog.forms import RegistrationForm,LoginForm, UpdateAccountForm, PostForm, RequestResetForm, ResetPasswordForm
from flaskblog.models import User, Post
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message

@app.route("/")
@app.route("/home")
def home():
    page=request.args.get('page',1,type=int)
    posts=Post.query.order_by(Post.date_posted.desc()).paginate(page=page, per_page=5)
    return render_template("home.html",posts=posts)

@app.route("/about")
def about():
    return render_template("about.html",title="About")



@app.route("/posts/new",methods=['GET','POST'])
@login_required
def new_post():
    form = PostForm()
    if form.validate_on_submit():
        post=Post(title=form.title.data, content=form.content.data, author=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Your post has been created!', 'success')
        return redirect(url_for('home'))
    return render_template("create_post.html", title="New Post", legend="New Post", form= form)

@app.route("/posts/<int:post_id>",methods=['GET','POST'])
def post(post_id):
    post=Post.query.get_or_404(post_id)
    return render_template('post.html', title=post.title, post=post)

@app.route("/posts/<int:post_id>/update",methods=['GET','POST'])
@login_required
def update_post(post_id):
    post=Post.query.get_or_404(post_id)
    if post.author!=current_user:
        abort(403)
    form = PostForm()
    if form.validate_on_submit():
        post.title=form.title.data
        post.content=form.content.data
        db.session.commit()
        flash('Your post has been updated','success')
        return redirect(url_for('post',post_id=post.id))
    elif request.method=='GET':
        form.title.data = post.title
        form.content.data = post.content
    return render_template("create_post.html", title="Update Post", legend="Update Post", form= form)    

@app.route("/posts/<int:post_id>/delete",methods=['POST'])
@login_required
def delete_post(post_id):
    post=Post.query.get_or_404(post_id)
    if post.author!=current_user:
        abort(403)
    db.session.delete(post)
    db.session.commit()
    flash('Your post has been deleted.','success')
    return redirect(url_for('home'))

