from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Initialize the database
db = SQLAlchemy()

# Define the Product model (for the products available in the store)
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)  # Primary Key
    name = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(500))
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0)  # Available stock
    image_url = db.Column(db.String(200))  # URL for product image
    
    def __repr__(self):
        return f"<Product {self.name}>"

# Define the User model (for customer information)
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(100), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password_hash = db.Column(db.String(200), nullable=False)
    
    def __repr__(self):
        return f"<User {self.username}>"

# Define the Retailer model (for retailer information)
class Retailer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    store_name = db.Column(db.String(100), nullable=False)
    contact = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(200), nullable=False)
    products = db.relationship('Product', backref='retailer', lazy=True)  # Link to products
    
    def __repr__(self):
        return f"<Retailer {self.store_name}>"
