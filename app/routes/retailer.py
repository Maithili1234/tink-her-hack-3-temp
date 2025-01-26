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

# Add product route to handle product form submission
@retailer_bp.route('/add-product', methods=['GET', 'POST'])
def add_product():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        price = request.form['price']
        stock = request.form['stock']
        retailer_id = request.form['retailer_id']

        # Image upload handling
        if 'image' not in request.files:
            return jsonify({"error": "No image part"}), 400
        file = request.files['image']
        if file.filename == '':
            return jsonify({"error": "No selected file"}), 400

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

        return redirect(url_for('main.retailer_dashboard'))

    # If GET request, show the form to add a product
    return render_template('add_product.html')
