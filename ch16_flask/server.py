# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 09:10:15 2019

@author: Kate Sorotos
"""

from flask import Flask, render_template
app = Flask("MyApp")


@app.route("/")
def home():
    message = "<body><h1 style='color:pink;'>Hello World!</h1><h2>This is an index page</h2></body>"
    return message

@app.route("/hello")
def hello():
    return render_template("grace-hopper-bootstrap.html") 

@app.route("/<name>")
def hello_someone(name):
    return render_template("hello.html", name=name.title())

app.run(debug=True) #remember to have this at the end


