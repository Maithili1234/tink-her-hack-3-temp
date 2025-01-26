from flask import render_template, request, jsonify, Blueprint
from app.model.models import Product
from app import db
import os

retailer_bp = Blueprint('retailer', __name__)
UPLOAD_FOLDER = 'ap/static/uploads'  # Make sure this folder exists in your project

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@retailer_bp.route('/add-product', methods=['GET', 'POST'])


def add_product():
    if 'image' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['image']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    # Save the file
    filename = secure_filename(file.filename)
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)
    file.save(file_path)

    # Get other form data
    name = request.form.get('name')
    size = request.form.get('size')
    color = request.form.get('color')

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

    return render_template('add_product.html')
