from flask import Flask
from app.routes import auth_bp  # Import the routes (blueprints)
from app.config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)  # Apply the configuration from Config class
    # Register blueprints
    app.register_blueprint(auth_bp, url_prefix='/auth')  # Register the authentication blueprint
    return app
