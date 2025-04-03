from sqlalchemy import Column, Integer, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from src.models import Inventory

Base = declarative_base()


class Shopping_Cart(Base):
    __tablename__ = "Shopping_Cart"
    Cart_ID = Column(Integer, primary_key=True)
    Cust_ID = Column(Integer, ForeignKey("Customer.Cust_ID"), nullable=False)
    Created_At = Column(Date, nullable=False)
    Updated_At = Column(Date, nullable=False)

    items = relationship("Shopping_Cart_Item", back_populates="cart")


class Shopping_Cart_Item(Base):
    __tablename__ = "Shopping_Cart_Item"
    Cart_ID = Column(Integer, ForeignKey(
        "Shopping_Cart.Cart_ID"), primary_key=True)
    Inventory_ID = Column(Integer, ForeignKey(
        "Inventory.Inventory_ID"), primary_key=True)
    Quantity = Column(Integer, nullable=False)
    Created_At = Column(Date, nullable=False)
    Updated_At = Column(Date, nullable=False)

    cart = relationship("Shopping_Cart", back_populates="items")
    inventory = relationship("Inventory", back_populates="items")
