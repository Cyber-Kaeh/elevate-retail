"""
src/controllers/inventory_controller.py:
This file defines CRUD operations for Inventory.
(C)reate a new inventory item or (R)ead an
existing one.
- Anthony Allen
"""

from src.models import Inventory, Product
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
        item = sess.query(Inventory).filter(
            Inventory.Inventory_ID == item_id).first()
        # return item
        return item.to_dict() if item else None


def get_product_items_to_display():
    with get_session() as sess:
        products = sess.query(
            Product.Product_ID.label('product_id'),
            Product.Product_Name.label('name'),
            Product.Product_Description.label('description'),
            Product.Image_URL.label('image_url'),
            Inventory.Unit_Price.label('price'),
        ).join(
            Inventory, Inventory.Product_ID == Product.Product_ID
        ).all()
        return [
            {
                'product_id': product.product_id,
                'name': product.name,
                'description': product.description,
                'image_url': product.image_url,
                'price': product.price,
            }
            for product in products
        ]


def get_product_by_inv_id(item_id):
    with get_session as sess:
        product = sess.query(Product).filter(
            Inventory.Inventory_ID == item_id
        ).join(
            Product, Inventory.Product_ID == Product.Product_ID
        ).first()
        return product.to_dict() if product else None
