"""
src/routes/shop_routes.py:
This module is necessary for organizing and managing the routes for the shop
management system. It imports the shop controller functions to interact with
the database and render the appropriate templates.
- Anthony Allen
"""

from flask import Blueprint, render_template
from src.controllers.shop_controller import get_product_items_to_display, get_shop_items, get_shop_item_by_id

shop_bp = Blueprint('shop', __name__)
single_checkout_bp = Blueprint('single_checkout', __name__)


@shop_bp.route('/shop', methods=['GET'])
def view_shop():
    items = get_product_items_to_display()
    return render_template('shop.html', items=items)


@single_checkout_bp.route('/checkout/<int:item_id>', methods=['GET'])
def single_checkout(item_id):
    item = get_shop_item_by_id(item_id)
    return render_template('cart.html', item=item)
    """This function attaches the the item_id to url so we can grab
    it on the checkout page. - Anthony Allen"""
