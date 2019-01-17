# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 09:10:15 2019

@author: Kate Sorotos
"""

from flask import Flask, render_template 
app = Flask("MyApp")

@app.route("/")
def home():
    message = "<body><h1 style = color:pink;>Hello World</h1><h2>This is an index page</h2></body>"
    return message

@app.route("/about")
def about_page():
#    return "<body><h1>About Me</h1><h2>My name is Kate</h2></body>"
    return render_template("grace-hopper-bootstrap.html")


@app.route("/news")
def news_page():
    return "<body><h1>News</h1><h2>This is a news page</h2></body>"

@app.route("/contact")
def contact_page():
    return "<body><h1>Contact</h1><h2>If you would like to get in touch please contact us - </h2></body>"


app.run(debug=True) #remember to have this at the end

