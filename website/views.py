#views.py will have all the views concerning the core blog application:
#home page, profile page, creative post page, etc.
from flask import Blueprint, render_template

views = Blueprint("views", __name__)

@views.route("/")
@views.route("/home")
def home():
    return render_template("home.html", name="Eman")