"""
src/controllers/inventory_controller.py:
This file defines CRUD operations for Inventory.
(C)reate a new inventory item or (R)ead an
existing one.
- Anthony Allen
"""

from src.models.inventory import Inventory
from src.utils.db_utils import get_session


def create_inventory_item(name, quantity, price):
    session = get_session()
    new_item = Inventory(name=name, quantity=quantity, price=price)
    session.add(new_item)
    session.commit()


def get_inventory_items():
    session = get_session()
    items = session.query(Inventory).all()
    return items


def get_inventory_item_by_id(item_id):
    session = get_session()
    item = session.query(Inventory).filter(Inventory.id == item_id).first()
    return item
