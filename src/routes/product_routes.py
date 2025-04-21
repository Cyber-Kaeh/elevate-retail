from flask import Blueprint, render_template, request, redirect, url_for
from src.controllers.shop_controller import get_product_by_inv_id

# Create a new blueprint for product-related routes
product_bp = Blueprint('product', __name__)


@product_bp.route('/product/<int:item_id>', methods=['GET'])
def view_product(item_id):
    # Fetch the product details from the database
    product = get_product_by_inv_id(item_id)
    if not product:
        return "Product not found", 404
    return render_template('product.html', product=product)


# @product_bp.route('/product/<int:product_id>/review', methods=['POST'])
# def product_review(item_id):
#     # Extract form values from the POST request
#     username = request.form.get('username')
#     rating = int(request.form.get('rating'))
#     comment = request.form.get('comment')

#     # Insert the review into the database
#     add_review(item_id, username, rating, comment)

#     # Redirect back to the product page after submission
#     return redirect(url_for('product.view_product', item_id=item_id))
"""Commented out the review route for now.
    Currently there is no place to store reviews in the database."""
