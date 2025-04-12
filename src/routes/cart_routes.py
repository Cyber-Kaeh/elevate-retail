from flask import Blueprint, session, redirect, url_for, request, render_template
from src.utils.db_utils import db
from src.models import ShoppingCart, ShoppingCartItem, Product, Inventory, forms
from src.controllers.inventory_controller import get_inventory_item_by_id
import random

cart_bp = Blueprint('cart', __name__)


def generate_anonymous_user_id():
    return random.randint(100000, 999999)


@cart_bp.route('/add_to_cart/<int:item_id>', methods=['GET'])
def add_to_cart(item_id):
    if 'cart' not in session:
        session['cart'] = []

    for item in session['cart']:
        if item['id'] == item_id:
            item['quantity'] += 1
            break
    else:
        session['cart'].append({'id': item_id, 'quantity': 1})
    session.modified = True
    print(session['cart'])
    return redirect(request.referrer or url_for('inventory.view_inventory'))


@cart_bp.route('/remove_from_cart/<int:item_id>', methods=['GET'])
def remove_from_cart(item_id):
    if 'cart' in session:
        for item in session['cart']:
            if item['id'] == item_id:
                item['quantity'] -= 1
                break
    session.modified = True
    return redirect(url_for('cart.view_cart'))


@cart_bp.route('/remove_all_of_item/<int:item_id>', methods=['GET'])
def remove_all_of_item(item_id):
    if 'cart' in session:
        session['cart'] = [item for item in session['cart']
                           if item['id'] != item_id]
    session.modified = True
    return redirect(url_for('cart.view_cart'))


@cart_bp.route('/clear_cart', methods=['GET'])
def clear_cart():
    session.pop('cart', None)
    session.modified = True
    return render_template('landing.html', items=[], total_price=0)


@cart_bp.route('/cart', methods=['GET'])
def view_cart():
    form = forms.LoginForm()
    session_id = request.cookies.get('session_id')
    anonymous_user = generate_anonymous_user_id()
    alert_message = session.pop('alert_message', None)

    shopping_cart = db.session.query(
        ShoppingCart).filter_by(Session_ID=session_id).first()
    if not shopping_cart:
        # return render_template('cart.html', items=[], total_price=0, form=form)
        shopping_cart = ShoppingCart(
            Cart_ID=anonymous_user, Customer_ID=anonymous_user, Session_ID=session_id)
        db.session.add(shopping_cart)
        db.session.commit()

    cart_items = db.session.query(
        ShoppingCartItem.Quantity.label('quantity'),
        Product.Product_ID.label('product_id'),
        Product.Product_Name.label('name'),
        Inventory.Unit_Price.label('price')
    ).join(
        Inventory, ShoppingCartItem.Inventory_ID == Inventory.Inventory_ID
    ).join(
        Product, Inventory.Product_ID == Product.Product_ID
    ).filter(
        ShoppingCartItem.Cart_ID == shopping_cart.Cart_ID
    ).all()

    items = []
    total_price = 0
    for cart_item in cart_items:
        item_total = cart_item.price * cart_item.quantity
        total_price += item_total
        items.append({
            'id': cart_item.product_id,
            'name': cart_item.name,
            'quantity': cart_item.quantity,
            'price': cart_item.price
        })
    # Calculate the total price
    # total_price = sum(item['price'] * item['quantity'] for item in items)
    return render_template('cart.html', items=items, total_price=total_price, alert_message=alert_message, form=form)


@cart_bp.app_context_processor
def inject_cart_item_count():
    cart_items = session.get('cart', [])
    return {'cart_item_count': sum([item['quantity'] for item in cart_items])}
