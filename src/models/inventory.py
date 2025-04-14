from sqlalchemy import DECIMAL, CheckConstraint, Column, DateTime, ForeignKey, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from .base import Base


class Inventory(Base):
    __tablename__ = 'Inventory'
    Inventory_ID = Column(Integer, primary_key=True, autoincrement=True)
    Product_ID = Column(Integer, ForeignKey(
        "Product.Product_ID"), nullable=False)
    Quantity = Column(Integer, nullable=False)
    Unit_Price = Column(DECIMAL(8, 2), nullable=False)
    Deleted_At = Column(DateTime, nullable=True)

    # Define constraints to match the SQL script
    __table_args__ = (
        CheckConstraint('Quantity >= 0',
                        name='chk_inventory_quantity_non_negative'),
        CheckConstraint('Unit_Price >= 0',
                        name='chk_inventory_unit_price_non_negative'),
    )

    stored_product = relationship('Product', back_populates='inventory')
    cart_items_inv = relationship(
        "ShoppingCartItem", back_populates="inventory_item_cart")
    order_item_inv = relationship(
        "OrderItem", back_populates="inventory_item_order")

    def to_dict(self):
        return {
            'id': self.Inventory_ID,
            'product_id': self.Product_ID,
            'quantity': self.Quantity,
            'price': self.Unit_Price,
        }
