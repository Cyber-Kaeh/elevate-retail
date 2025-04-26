import random
from flask import Blueprint, session, jsonify, render_template, request, flash, redirect, url_for
from ..models import Order
from ..utils.db_utils import db

from datetime import datetime, timedelta

# Make sure this matches what you use in login_view
order_bp = Blueprint('order', __name__)

@order_bp.route('/orders', methods=['GET'])
def orders():
    """
    Flask route to get all orders by customer ID.
    """
    if 'session_id' not in session:
        flash('You must be logged in to view orders.', 'danger')
        return redirect(url_for('login.login'))

    customer_id = session['session_id']
    if not customer_id:
        return jsonify({"error": "Customer ID is required"}), 400

    orders = db.session.query(Order).filter(Order.Customer_ID == customer_id).all()
    if not orders:
        return jsonify({"error": "No orders found for this customer"}), 404

    order_list = []
    for order in orders:
        order_list.append({
            "Order_ID": order.Order_ID,
            "Order_Date": order.Order_Date,
        })

    return render_template('manage_orders.html', orders=order_list)

@order_bp.route('/track_order', methods=['POST'])
def track_order():
    """
    Flask route to render the shipping landing page.
    """
    order_id = request.form['order_id']

    shipping = {
        'Order_ID': order_id,
        'Cost': random.uniform(5.0, 20.0),
        'Shipped_On': datetime.now() + timedelta(days=1),
        'Expected_By': random.choice([datetime.now() + timedelta(days=3), datetime.now() + timedelta(days=5), datetime.now() + timedelta(days=7)]),
        'Ship_Status': random.choice(['Pending', 'Shipped', 'Delivered']),
        'Carrier': random.choice(['FedEx', 'UPS', 'Amazon', 'USPS']),
        'Tracking_Number': random.randint(1000000000, 9999999999),
        'Shipping_Address_ID': random.randint(1, 100),
        'Billing_Address_ID': random.randint(1, 100)
    }
    print(shipping)
    return render_template('shipping.html', order_id=order_id, shipping=shipping)