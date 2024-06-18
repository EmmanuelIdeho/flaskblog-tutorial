#initialization stuff for the Flask webapp

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import path
from flask_login import LoginManager

db = SQLAlchemy()
DB_NAME = "database.db"

def create_app():
    #first thing to do when creating a flask application
    app = Flask(__name__)
    app.config['SECRET_KEY'] = "dcu238rh%@29x3o"
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{DB_NAME}'
    db.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User, Post, Comment

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    create_database(app)

    

    return app

#checks if the database already exists, if it doesn't then create it.
def create_database(app):
    with app.app_context():
        db.create_all()
        print("EMMAN THE CHIEF CREATED DATABASE!")