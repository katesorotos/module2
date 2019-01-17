# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 19:19:58 2019

@author: Kate Sorotos
"""

from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def index():
    message = 'Hello World!'
    return render_template("index.html", title="Home", **locals())

@app.route("/about")
def about():
   	return render_template("about.html", title="about")        

@app.route("/confirmation", methods=["POST"])
def confirmation():
	form_data = request.form
	email = form_data["email"]
	result="ALL OK"
	return render_template("confirmation.html", title="Form confirmation", **locals())

if __name__ == "__main__":
    
    app.run(debug=True)