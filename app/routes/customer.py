from flask import Blueprint, render_template, request, redirect, url_for

from app.model.models import Product

customer_bp = Blueprint('customer', __name__)


# Route to display the home page with product listings
@customer_bp.route('/')
def home():
    products = Product.query.all()  # Fetch all products for display
    return render_template('index.html', products=products)

# Route to view a specific product's details
@customer_bp.route('/product/<int:id>')
def product_page(id):
    product = Product.query.get_or_404(id)
    return render_template('product_page.html', product=product)

# Route to add a product to the wishlist
@customer_bp.route('/add_to_wishlist/<int:id>')
def add_to_wishlist(id):
    # Add the product to the wishlist (this would involve user session or a database)
    return redirect(url_for('customer.home'))
