from flask import Flask
from config import DevConfig
from flask_sqlachemy import SQLAlchemy

# Initializing application
app = Flask(__name__)

# Setting up configuration
app.config.from_object(DevConfig)

from app import views