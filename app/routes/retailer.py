<<<<<<< HEAD
from flask import render_template, request, jsonify, Blueprint
from app.model.models import Product
from app import db
import os

retailer_bp = Blueprint('retailer', __name__)
UPLOAD_FOLDER = 'ap/static/uploads'  # Make sure this folder exists in your project

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
=======
from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from app import db, app  # Importing app configuration from the main file
from app.models import Retailer, Product
import os

# Folder to store uploaded images (make sure the directory is created in the correct location)
UPLOAD_FOLDER = os.path.join(app.config['STATIC_FOLDER'], 'uploads')  # Fix path
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER  # You can configure the app's upload folder here

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Blueprint for retailer routes
retailer_bp = Blueprint('retailer', __name__)
>>>>>>> 4328d71871504b29f62c1339706fd812a78b4572

# Add product route to handle product form submission
@retailer_bp.route('/add-product', methods=['GET', 'POST'])


def add_product():
    if 'image' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

<<<<<<< HEAD
    # Save the file
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    # Get other form data
    name = request.form.get('name')
    size = request.form.get('size')
    color = request.form.get('color')
=======
        # Save the image to the uploads folder
        file_path = os.path.join(UPLOAD_FOLDER, file.filename)
        file.save(file_path)

        # Create a new product and add it to the database
        new_product = Product(
            name=name,
            description=description,
            price=price,
            stock=stock,
            retailer_id=retailer_id,
            image_url=file_path  # Storing the file path of the uploaded image
        )
        db.session.add(new_product)
        db.session.commit()
>>>>>>> 4328d71871504b29f62c1339706fd812a78b4572

    if not all([name, size, color]):
        return jsonify({"error": "Missing fields"}), 400

    # Simulate saving product info to a database
    product = {
        "name": name,
        "size": size,
        "color": color,
        "image_url": file_path
    }
    # In a real app, you'd save this to your database
    print(f"Product added: {product}")

    return jsonify({"message": "Product uploaded successfully!", "product": product}), 200

    # If GET request, show the form to add a product
    return render_template('add_product.html')
