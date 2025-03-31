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
    with get_session() as sess:
        new_item = Inventory(name=name, quantity=quantity, price=price)
        sess.add(new_item)
        sess.commit()
        return new_item


def get_inventory_items():
    with get_session() as sess:
        items = sess.query(Inventory).all()
        # return items
        return [item.to_dict() for item in items]


def get_inventory_item_by_id(item_id):
    with get_session() as sess:
        item = sess.query(Inventory).filter(Inventory.id == item_id).first()
        # return item
        return item.to_dict() if item else None
