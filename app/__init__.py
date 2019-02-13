# third party imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# local imports
from config import app_config

# db variable initialization
db = SQLAlchemy()
loginmanager = LoginManager()


def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(app_config[config_name])
    db.init_app(app)
    loginmanager.init_app(app)
    loginmanager.login_message = 'You must be logged in to access this page'
    loginmanager.login_view = 'auth.login'

    return app
