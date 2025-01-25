from flask import Flask
from app.routes.retailer import retailer_bp
from app.routes.customer import customer_bp

def create_app():
    app = Flask(__name__)

    # Register Blueprints for retailer and customer routes
    app.register_blueprint(retailer_bp, url_prefix='/retailer')
    app.register_blueprint(customer_bp, url_prefix='/customer')

    # Configure your app, e.g., database
    app.config['SECRET_KEY'] = 'your-secret-key'
    
    return app
