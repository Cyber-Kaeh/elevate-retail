import os
from flask import Blueprint, request, jsonify

# Environment-specific import handling
if os.getenv("FLASK_ENV") == "pos":
    from src.utils.db_utils import db
else:
    from database import db

from models import Customer, Order

# Define the shipping blueprint
shipping_bp = Blueprint('shipping', __name__)


def calculate_shipping_cost(customer_type, shipping_option):
    """
    Calculate the shipping cost based on customer type and shipping option.

    :param customer_type: Type of the customer (e.g., 'Prime', 'Regular').
    :param shipping_option: Chosen shipping option (e.g., 'FedEx', 'UPS').
    :return: Calculated shipping cost, or 0.0 for Prime members.
    """
    shipping_rates = {"fedex": 10.0, "ups": 8.0}
    if customer_type.lower() == "prime":
        return 0.0
    shipping_option = shipping_option.lower()
    return shipping_rates.get(shipping_option, 0.0)


@shipping_bp.route('/orders', methods=['POST'])
def create_order():
    """
    Flask route to create a new order.

    :return: A success message with shipping cost, or an error response.
    """
    data = request.get_json()

    # Validate required fields
    required_fields = ['Customer_ID', 'Type', 'Shipping_Option']
    for field in required_fields:
        if field not in data:
            return jsonify({"error": f"Missing required field: {field}"}), 400

    # Validate and fetch customer from the database
    customer = Customer.query.get(data['Customer_ID'])
    if not customer:
        return jsonify({"error": "Customer not found"}), 404

    # Calculate shipping cost
    shipping_cost = calculate_shipping_cost(customer.Type, data['Shipping_Option'])

    # Create new order
    new_order = Order(
        Customer_ID=data['Customer_ID'],
        Type=data['Type'],
        Shipping_Option=data['Shipping_Option'],
        Shipping_Cost=shipping_cost
    )

    # Add to session and commit
    db.session.add(new_order)
    db.session.commit()

    # Respond with success message
    return jsonify({
        "message": "Order created successfully.",
        "Shipping_Cost": shipping_cost
    }), 201

