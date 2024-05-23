#auth.py will have all the routes concerning authentication:
#login, sign-up, sign-out, etc.
from flask import Blueprint, render_template

auth = Blueprint("auth", __name__)

@auth.route("/login")
def login():
    return "Login"

@auth.route("/signup")
def signup():
    return "Sign-up"

@auth.route("/signout")
def signout():
    return "Sign-out"