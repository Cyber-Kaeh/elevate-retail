from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base


class ShoppingCartItem(Base):
    __tablename__ = "shopping_cart_item"
    cart_id = Column(Integer, ForeignKey(
        "shopping_sart.id"), primary_key=True)
    inventory_id = Column(Integer, ForeignKey(
        "inventory.id"), primary_key=True)
    quantity = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(
        datetime.timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=lambda: datetime.now(
        datetime.timezone.utc), onupdate=lambda: datetime.now(datetime.timezone.utc), nullable=False)

    cart = relationship("ShoppingCart", back_populates="items")
    inventory = relationship("Inventory", back_populates="cart_items")
