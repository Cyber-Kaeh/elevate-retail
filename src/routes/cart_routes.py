from flask import Blueprint, session, redirect, url_for, request, render_template
from src.controllers.inventory_controller import get_inventory_item_by_id

cart_bp = Blueprint('cart', __name__)


@cart_bp.route('/add_to_cart/<int:item_id>', methods=['GET'])
def add_to_cart(item_id):
    if 'cart' not in session:
        session['cart'] = []
    session['cart'].append(item_id)
    return redirect(url_for('inventory.view_inventory'))


@cart_bp.route('/remove_from_cart/<int:item_id>', methods=['GET'])
def remove_from_cart(item_id):
    if 'cart' in session:
        session['cart'].remove(item_id)
    return redirect(url_for('inventory.view_inventory'))


@cart_bp.route('/cart', methods=['GET'])
def view_cart():
    return render_template('cart.html', cart=session.get('cart', []))
