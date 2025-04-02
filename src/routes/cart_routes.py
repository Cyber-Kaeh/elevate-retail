from flask import Blueprint, session, redirect, url_for, request, render_template
from src.models.forms import LoginForm
from src.controllers.inventory_controller import get_inventory_item_by_id

cart_bp = Blueprint('cart', __name__)


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


@cart_bp.route('/cart', methods=['GET'])
def view_cart():
    form = LoginForm()
    cart_items = session.get('cart', [])
    alert_message = session.pop('alert_message', None)
    # item = [get_inventory_item_by_id(item_id) for item_id in cart_item_ids]
    items = []
    for cart_item in cart_items:
        item = get_inventory_item_by_id(cart_item['id'])
        if item:
            items.append({
                'id': item['id'],
                'name': item['name'],
                'quantity': cart_item['quantity'],
                'price': item['price']
            })
    # Calculate the total price
    total_price = sum(item['price'] * item['quantity'] for item in items)
    return render_template('cart.html', items=items, total_price=total_price, form=form, alert_message=alert_message)


@cart_bp.app_context_processor
def inject_cart_item_count():
    cart_items = session.get('cart', [])
    # print(cart_items)
    # count = 0
    # for item in cart_items:
    #     count += item['quantity']
    return {'cart_item_count': sum([item['quantity'] for item in cart_items])}
