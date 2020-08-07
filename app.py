# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 01:27:05 2020

@author: harshit-saraswat
"""

from flask import Flask

app=Flask(__name__)


@app.route("/")
def home():
    return "<h1>Hello World!</h1>"

if __name__=="__main__":
    app.run(debug=True)
