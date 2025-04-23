from flask import Blueprint, flash, session, redirect, url_for, request, render_template
from flask_login import current_user
from src.utils.db_utils import db
from src.models import ShoppingCart, ShoppingCartItem, Product, Inventory, Order, OrderItem, forms
from src.controllers.shop_controller import get_shop_item_by_id
from sqlalchemy.exc import SQLAlchemyError
import random

cart_bp = Blueprint('cart', __name__)


def generate_anonymous_user_id():
    return random.randint(100000, 999999)


@cart_bp.route('/add_to_cart/<int:item_id>', methods=['GET'])
def add_to_cart(item_id):
    session_id = request.cookies.get('session_id')

    if current_user.is_authenticated:
        customer_id = current_user.Customer_ID
    else:
        customer_id = generate_anonymous_user_id()

    if not session_id:
        flash('Your cart is empty!', 'info')
        return redirect(url_for('cart.view_cart'))

    try:
        if current_user.is_authenticated:
            shopping_cart = db.session.query(ShoppingCart).filter_by(
                Customer_ID=customer_id).first()
        else:
            shopping_cart = db.session.query(ShoppingCart).filter_by(
                Session_ID=session_id).first()

        if not shopping_cart:
            shopping_cart = ShoppingCart(
                Customer_ID=current_user.Customer_ID if current_user.is_authenticated else customer_id,
                Session_ID=session_id)
            db.session.add(shopping_cart)
            db.session.commit()

        cart_item = db.session.query(
            ShoppingCartItem
        ).filter_by(
            Cart_ID=shopping_cart.Cart_ID,
            Inventory_ID=item_id
        ).first()

        if cart_item:
            cart_item.Quantity += 1
            db.session.commit()
        else:
            cart_item = ShoppingCartItem(
                Cart_ID=shopping_cart.Cart_ID,
                Inventory_ID=item_id,
                Quantity=1
            )
            db.session.add(cart_item)
        db.session.commit()
        flash('Item added to cart!', 'success')

    except SQLAlchemyError as e:
        db.session.rollback()
        flash('An error occurred while adding the item to the cart.', 'danger')
        print(f"SQLAlchemy Error: {e}")

    return redirect(request.referrer or url_for('shop.view_shop'))


@cart_bp.route('/remove_from_cart/<int:item_id>', methods=['GET'])
def remove_from_cart(item_id):
    session_id = request.cookies.get('session_id')

    if current_user.is_authenticated:
        customer_id = current_user.Customer_ID
    else:
        customer_id = generate_anonymous_user_id()

    if not session_id and not current_user.is_authenticated:
        flash('Your cart is empty!', 'info')
        return redirect(url_for('cart.view_cart'))

    try:
        if current_user.is_authenticated:
            shopping_cart = db.session.query(ShoppingCart).filter_by(
                Customer_ID=customer_id).first()
        else:
            shopping_cart = db.session.query(ShoppingCart).filter_by(
                Session_ID=session_id).first()

        if not shopping_cart:
            flash('Your cart is empty!', 'info')
            return redirect(url_for('cart.view_cart'))

        cart_item = db.session.query(
            ShoppingCartItem
        ).filter_by(
            Cart_ID=shopping_cart.Cart_ID,
            Inventory_ID=item_id
        ).first()

        if cart_item:
            if cart_item.Quantity > 1:
                cart_item.Quantity -= 1
                db.session.commit()
                flash('Item removed from cart!', 'danger')
            else:
                db.session.delete(cart_item)
                db.session.commit()
                flash('Item removed from cart!', 'danger')
        else:
            flash('Item not found in cart!', 'warning')

    except SQLAlchemyError as e:
        db.session.rollback()
        flash('An error occurred while removing the item from the cart.', 'danger')
        print(f"SQLAlchemy Error: {e}")

    return redirect(url_for('cart.view_cart'))


@cart_bp.route('/remove_all_of_item/<int:item_id>', methods=['GET'])
def remove_all_of_item(item_id):
    session_id = request.cookies.get('session_id')
    if not session_id:
        flash('Your cart is empty!', 'info')
        return redirect(url_for('cart.view_cart'))

    try:
        shopping_cart = db.session.query(ShoppingCart).filter_by(
            Session_ID=session_id).first()

        if not shopping_cart:
            flash('Your cart is empty!', 'info')
            return redirect(url_for('cart.view_cart'))

        cart_item = db.session.query(
            ShoppingCartItem
        ).filter_by(
            Cart_ID=shopping_cart.Cart_ID,
            Inventory_ID=item_id
        ).first()

        if cart_item:
            db.session.delete(cart_item)
            db.session.commit()
            flash('Removed items from cart!', 'danger')
        else:
            flash('Item not found in cart!', 'warning')

    except SQLAlchemyError as e:
        db.session.rollback()
        flash('An error occurred while removing the item from the cart.', 'danger')
        print(f"SQLAlchemy Error: {e}")
    return redirect(url_for('cart.view_cart'))


@cart_bp.route('/clear_cart', methods=['GET'])
def clear_cart():
    session_id = request.cookies.get('session_id')
    if not session_id:
        flash('Your cart is already empty!', 'info')
        return redirect(url_for('cart.view_cart'))

    shopping_cart = db.session.query(ShoppingCart).filter_by(
        Session_ID=session_id).first()

    if shopping_cart:
        db.session.query(ShoppingCartItem).filter_by(
            Cart_ID=shopping_cart.Cart_ID).delete()
        db.session.commit()
        flash('Your cart has been cleared!', 'success')
    else:
        flash('Your cart is already empty!', 'info')

    return redirect(url_for('cart.view_cart'))


@cart_bp.route('/cart', methods=['GET'])
def view_cart():
    form = forms.LoginForm()
    session_id = request.cookies.get('session_id')
    anonymous_user = generate_anonymous_user_id()
    alert_message = session.pop('alert_message', None)

    if current_user.is_authenticated:
        customer_id = current_user.Customer_ID
        shopping_cart = db.session.query(
            ShoppingCart).filter_by(Customer_ID=customer_id).first()
    else:
        shopping_cart = db.session.query(
            ShoppingCart).filter_by(Session_ID=session_id).first()

    if not shopping_cart:
        anonymous_user = generate_anonymous_user_id()
        shopping_cart = ShoppingCart(
            Cart_ID=anonymous_user,
            Customer_ID=current_user.id if current_user.is_authenticated else anonymous_user,
            Session_ID=session_id)
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
    return render_template('cart.html', items=items, total_price=total_price, alert_message=alert_message, form=form)


@cart_bp.route('/confirm_purchase', methods=['GET'])
def confirm_purchase():
    if current_user.is_authenticated:
        # If the user is logged in, redirect to the checkout page
        return redirect(url_for('cart.checkout'))
    else:
        # If the user is not logged in, redirect to the login page
        flash('Please log in to proceed to checkout.', 'info')
        return redirect(url_for('login.login', next=url_for('cart.process_checkout')))


@cart_bp.route('/process_checkout', methods=['POST'])
def process_checkout():
    if current_user.is_authenticated:
        customer_id = current_user.Customer_ID
    else:
        flash('You must be logged in to complete the purchase.', 'danger')
        return redirect(url_for('login.login'))

    # Create a new order
    new_order = Order(Customer_ID=customer_id)
    db.session.add(new_order)
    db.session.commit()

    # Get the user's shopping cart
    shopping_cart = db.session.query(ShoppingCart).filter_by(
        Customer_ID=customer_id).first()

    if not shopping_cart:
        flash('Your cart is empty.', 'danger')
        return redirect(url_for('cart.view_cart'))

    # Add items from the cart to the Order_Item table
    cart_items = db.session.query(ShoppingCartItem).filter_by(
        Cart_ID=shopping_cart.Cart_ID).all()
    for item in cart_items:
        order_item = OrderItem(
            Order_ID=new_order.Order_ID,
            Inventory_ID=item.Inventory_ID,
            Quantity=item.Quantity,
            Amount=item.Quantity * item.inventory_item_cart.Unit_Price,
            Tax=0.0  # Add tax calculation logic if needed
        )
        db.session.add(order_item)

    # Clear the shopping cart
    db.session.query(ShoppingCartItem).filter_by(
        Cart_ID=shopping_cart.Cart_ID).delete()
    db.session.commit()

    flash('Your order has been placed successfully!', 'success')
    return redirect(url_for('home'))


@cart_bp.route('/checkout', methods=['GET'])
def checkout():
    if not current_user.is_authenticated:
        flash('Please log in to proceed to checkout.', 'info')
        return redirect(url_for('login.login', next=url_for('cart.checkout')))
    return render_template('checkout.html')


@cart_bp.app_context_processor
def inject_cart_item_count():
    if current_user.is_authenticated:
        shopping_cart = db.session.query(
            ShoppingCart).filter_by(Customer_ID=current_user.Customer_ID).first()
    else:
        session_id = request.cookies.get('session_id')
        if not session_id:
            return {'cart_item_count': 0}
        shopping_cart = db.session.query(
            ShoppingCart).filter_by(Session_ID=session_id).first()

    if shopping_cart:
        cart_items_count = db.session.query(
            db.func.sum(ShoppingCartItem.Quantity)
        ).filter(
            ShoppingCartItem.Cart_ID == shopping_cart.Cart_ID
        ).scalar()
        return {'cart_item_count': cart_items_count or 0}
    else:
        return {'cart_item_count': 0}
