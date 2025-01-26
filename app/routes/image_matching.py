from flask import Flask, request, jsonify

app = Flask(__name__)

# Sample product data
products = [
    {"name": "T-Shirt", "color": "Red", "size": "M"},
    {"name": "Jeans", "color": "Blue", "size": "L"},
    {"name": "Hat", flask run


@app.route('/api/products', methods=['GET'])
def search_products():
    query = request.args.get('q', '').lower()
    filtered_products = [
        product for product in products
        if query in product['name'].lower() or query in product['color'].lower() or query in product['size'].lower()
    ]
    return jsonify(filtered_products)

if __name__ == '__main__':
    app.run(debug=True)

