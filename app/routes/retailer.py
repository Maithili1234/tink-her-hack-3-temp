from flask import render_template, request, redirect, url_for, jsonify, Blueprint
from app import db
from app.models import Retailer, Product
import os

# Folder to store uploaded images
UPLOAD_FOLDER = 'ap/static/uploads'  # Make sure this folder exists in your project
#app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)
retailer_bp = Blueprint('retailer', __name__)

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
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
        file.save(file_path)

        # Create a new product
        new_product = Product(name=name, description=description, price=price, stock=stock, retailer_id=retailer_id, image_url=file_path)
        db.session.add(new_product)
        db.session.commit()

        return redirect(url_for('main.retailer_dashboard'))

    return render_template('add_product.html')
