from flask import Blueprint, render_template
from src.controllers.inventory_controller import get_inventory_items

inventory_bp = Blueprint('inventory', __name__)

@inventory_bp.route('/inventory', methods=['GET'])
def view_inventory():
    items = get_inventory_items()
    return render_template('inventory.html', items=items)