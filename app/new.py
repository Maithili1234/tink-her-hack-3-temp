from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os

# Initialize the database
db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    
    
    # Configuration settings
    app.config['UPLOAD_FOLDER'] = 'ap/static/uploads'
    CORS(app)  # Enable CORS
    app.register_blueprint(retailer_bp)
    app.config['SECRET_KEY'] = 'your-secret-key'  # Set your secret key for session management
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///site.db'  # Database URI (change for production)
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['UPLOAD_FOLDER'] = 'app/static/uploads'  # Folder to store uploaded images

    # Initialize extensions
    db.init_app(app)  # Initialize the database with the app
    CORS(app)  # Enable CORS for the app (optional but useful if you have a frontend)

    # Register blueprints here (optional if you have multiple blueprints)
    # For example:
    from app.routes.retailer import retailer_bp
    app.register_blueprint(retailer_bp, url_prefix='/retailer')

    return app
