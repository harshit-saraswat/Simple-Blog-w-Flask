# -*- coding: utf-8 -*-
"""
Created on Sat Aug  8 01:27:05 2020

@author: harshit-saraswat
"""

from flaskblog import create_app

app =create_app()

if __name__=="__main__":
    app.run(debug=True)
