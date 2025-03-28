from flask import Blueprint, session, redirect, url_for, request, render_template
from src.controllers.inventory_controller import get_inventory_item_by_id

cart_bp = Blueprint('cart', __name__)


@cart_bp.route('/add_to_cart/<int:item_id>', methods=['GET'])
def add_to_cart(item_id):
    if 'cart' not in session:
        session['cart'] = []
    session['cart'].append(item_id)
    print(session['cart'])
    print(session.get('cart'))
    return redirect(url_for('inventory.view_inventory'))


@cart_bp.route('/remove_from_cart/<int:item_id>', methods=['GET'])
def remove_from_cart(item_id):
    print(session['cart'])
    if 'cart' in session:
        session['cart'].remove(item_id)
    return redirect(url_for('inventory.view_inventory'))


@cart_bp.route('/cart', methods=['GET'])
def view_cart():
    cart_item_ids = session.get('cart', [])
    print(f"Cart item IDs: {cart_item_ids}")
    # item = [get_inventory_item_by_id(item_id) for item_id in cart_item_ids]
    items = []
    for item_id in cart_item_ids:
        item = get_inventory_item_by_id(item_id)
        if item:
            items.append(item)
    
    # Calculate the total price
    total_price = sum(item.price * item.quantity for item in items)
    return render_template('cart.html', item=items, total_price=total_price)
