from flask import Flask
from config import config_options
from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# from flask_sqlachemy import SQLAlchemy

login_manager = LoginManager()
login_manager.login_view = 'login'
bootstrap = Bootstrap()
db = SQLAlchemy()

def create_app(config_name):
# Initializing application
    app = Flask(__name__)

# Setting up configuration
    app.config.from_object(config_options[config_name])

#initialising flask extensions
    bootstrap.init_app(app)
    db.init_app(app)
    login_manager.init_app(app)

# Registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app