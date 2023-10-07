import os
from flask import Flask
from flask_cors import CORS

SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SECURE = True

APP_CONFIG = {
    "SECRET_KEY": os.environ.get("SECRET_KEY", "S3cr3t!"),
    "SESSION_TYPE": os.environ.get("SESSION_TYPE", "filesystem"),
    "UPLOAD_FOLDER": os.environ.get("UPLOAD_FOLDER", "uploads"),
    "SQLALCHEMY_DATABASE_URI": os.environ.get("DB_URI", "sqlite:///:memory:"),
}


def create_app():
    app = Flask(__name__)

    # Configure the application
    app.config.from_mapping(APP_CONFIG)

    # Initialize Flask extensions
    from app.extensions import db

    db.init_app(app)

    # Import external endpoints
    from app.controllers.api.book import api as book_api

    app.register_blueprint(book_api)

    # Ensure creation of database tables
    # NOTE: This will not apply changes to (migrate) existing tables
    with app.app_context():
        db.create_all()

    # TODO: Correct CORS configuration to a secure one
    CORS(app)

    return app
