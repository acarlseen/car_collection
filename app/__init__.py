from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from flask_migrate import Migrate


db = SQLAlchemy()
login_manager = LoginManager()
migrate = Migrate()

def create_app():
    from config import Config

    app = Flask(__name__, instance_relative_config=False)
    app.config.from_object(Config)

    #initialize plugins
    db.init_app(app)
    login_manager.init_app(app)
    migrate.init_app(app, db)

    with app.app_context():
        # Import blueprints
        from .site.routes import site
        from .authorization.auth import authorization
        from .api.routes import api

        # Register blueprints
        app.register_blueprint(site)
        app.register_blueprint(authorization)
        app.register_blueprint(api)

        #Create database models
        db.create_all()

        return app