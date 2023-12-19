import os
from flask import Flask



def make_app():
    from config import Config
    from flask import Blueprint

    app = Flask(__name__, instance_relative_config=True)
    app.config.from_object(Config)

    # register blueprints
    from .authorization.routes import authorization
    
