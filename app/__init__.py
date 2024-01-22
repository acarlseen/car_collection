from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    from config import Config

    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(Config)

    #initialize plugins
    db.init_app(app)
    login_manager.init_app(app)

    with app.app_context():
        # Import blueprints
        from .site.routes import site
        from .authorization.auth import authorization

        # Register blueprints
        app.register_blueprint(site)
        app.register_blueprint(authorization)

        #Create database models
        db.create_all()

        return app