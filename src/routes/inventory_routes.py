"""
src/routes/inventory_routes.py:
This module is necessary for organizing and managing the routes for the inventory
management system. It imports the inventory controller functions to interact with
the database and render the appropriate templates.
- Anthony Allen
"""

from flask import Blueprint, render_template
from src.controllers.inventory_controller import get_product_items_to_display, get_inventory_items, get_inventory_item_by_id

inventory_bp = Blueprint('inventory', __name__)
single_checkout_bp = Blueprint('single_checkout', __name__)


@inventory_bp.route('/inventory', methods=['GET'])
def view_inventory():
    items = get_product_items_to_display()
    return render_template('inventory.html', items=items)


@single_checkout_bp.route('/checkout/<int:item_id>', methods=['GET'])
def single_checkout(item_id):
    item = get_inventory_item_by_id(item_id)
    return render_template('cart.html', item=item)
    """This function attaches the the item_id to url so we can grab
    it on the checkout page. - Anthony Allen"""
