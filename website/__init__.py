#initialization stuff for the Flask webapp

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

def create_app():
    #first thing to do when creating a flask application
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "dcu238rh%@29x3o"

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    

    return app