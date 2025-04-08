"""
outdated shopping cart models. should be able to delete this file
"""
from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from datetime import datetime

Base = declarative_base()


class Shopping_Cart(Base):
    __tablename__ = "Shopping_Cart"
    Cart_ID = Column(Integer, primary_key=True)
    Cust_ID = Column(Integer, ForeignKey("Customer.Cust_ID"), nullable=False)
    Created_At = Column(DateTime, default=lambda: datetime.now(
        datetime.timezone.utc), nullable=False)
    Updated_At = Column(DateTime, default=lambda: datetime.now(
        datetime.timezone.utc), onupdate=lambda: datetime.now(datetime.timezone.utc), nullable=False)
    items = relationship("Shopping_Cart_Item", back_populates="cart")
    shopping_cart = relationship("Customer", back_populates="shopping_cart")


class Shopping_Cart_Item(Base):
    __tablename__ = "Shopping_Cart_Item"
    Cart_ID = Column(Integer, ForeignKey(
        "Shopping_Cart.Cart_ID"), primary_key=True)
    Inventory_ID = Column(Integer, ForeignKey(
        "Inventory.Inventory_ID"), primary_key=True)
    Quantity = Column(Integer, nullable=False)
    Created_At = Column(DateTime, default=lambda: datetime.now(
        datetime.timezone.utc), nullable=False)
    Updated_At = Column(DateTime, default=lambda: datetime.now(
        datetime.timezone.utc), onupdate=lambda: datetime.now(datetime.timezone.utc), nullable=False)

    cart = relationship("Shopping_Cart", back_populates="items")
    inventory = relationship("Inventory", back_populates="items")
