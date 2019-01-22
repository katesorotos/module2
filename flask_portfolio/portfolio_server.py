# -*- coding: utf-8 -*-
"""
Created on Wed Jan 16 15:01:51 2019

@author: Kate Sorotos
"""

from flask import Flask, render_template
app = Flask("MyApp")


@app.route("/")
def portfolio():
    return render_template("index.html")

app.run(debug=True) #remember to have this at the end

