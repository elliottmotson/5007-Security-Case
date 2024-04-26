import pathlib
from flask import (
    Flask,
    render_template,
    redirect,
    request,
    flash,
    url_for,
    session,
)  # noqa: E501
from dotenv import load_dotenv
import os
import time
import json
from pathlib import Path

load_dotenv(verbose=True)  # Take environment variables from .env.
SECRET_KEY = os.getenv("SECRET_KEY")


app = Flask(__name__)
app.config["SECRET_KEY"] = 'SECRET_KEY'

 


@app.route("/")
def index():
    if "username" in session:
        return render_template("index.html", username=session["username"])
    return render_template("index.html")


@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        session["username"] = request.form["username"]
        session["password"] = request.form["password"]
        if session["username"] == "admin" and session["password"] == "admin":
            return redirect(url_for("index"))
        else:
            flash("Invalid credentials")
            session.pop("username", None)
            return redirect(url_for("login"))
    return render_template("login.html")
    
@app.route("/logout")
def logout():
    session.pop("username", None)
    return redirect(url_for("index"))

