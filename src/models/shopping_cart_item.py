from sqlalchemy import Column, Integer, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base


class ShoppingCartItem(Base):
    __tablename__ = "Shopping_Cart_Item"
    Cart_ID = Column(Integer, ForeignKey(
        "Shopping_Cart.Cart_ID"), primary_key=True)
    Inventory_ID = Column(Integer, ForeignKey(
        "Inventory.Inventory_ID"), primary_key=True)
    Quantity = Column(Integer, nullable=False)
    Created_At = Column(DateTime, default=func.now(), nullable=False)
    Updated_At = Column(DateTime, onupdate=func.now(), nullable=True)

    cart = relationship("ShoppingCart", back_populates="cart_items")
    inventory_item_cart = relationship(
        "Inventory", back_populates="cart_items_inv")
