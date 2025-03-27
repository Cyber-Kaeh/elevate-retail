from flask import Blueprint, session, redirect, url_for, request
from src.controllers.session_controller import create_session, get_session_data, update_session, delete_session

cart_bp = Blueprint('cart', __name__)


@cart_bp.route('/add_to_cart/<int:item_id>', methods=['GET'])
def add_to_cart(item_id):
    cart = session.get('cart', [])
    cart.append(item_id)
    session['cart'] = cart
    # Store the session in the database
    update_session(session.sid, str(session))
    return redirect(url_for('inventory.view_inventory'))


@cart_bp.route('/remove_from_cart/<int:item_id>', methods=['GET'])
def remove_from_cart(item_id):
    cart = session.get('cart', [])
    cart.remove(item_id)
    session['cart'] = cart
    # Store the session in the database
    update_session(session.sid, str(session))
    return redirect(url_for('inventory.view_inventory'))


@cart_bp.route('/cart', methods=['GET'])
def view_cart():
    cart = session.get('cart', [])
    return render_template('cart.html', cart=cart)
