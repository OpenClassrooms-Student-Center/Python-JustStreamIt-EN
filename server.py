#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from flask import Flask, render_template
app = Flask(__name__)



### The variables to display in the interface

messageWelcome = "Future Python Developer"
objective = "The objective of this project is to create an interface for a Python web application."


### The variables to display in the interface

@app.route("/")
def index():
    return render_template("index.html", text = messageWelcome, message = objective )

if __name__ == "__main__":
    app.run(debug=True)
