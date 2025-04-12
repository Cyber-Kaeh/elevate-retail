from sqlalchemy import Column, Integer, DateTime, ForeignKey, func, NVARCHAR
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base


class ShoppingCart(Base):
    __tablename__ = 'Shopping_Cart'
    Cart_ID = Column(Integer, primary_key=True)
    Customer_ID = Column(Integer, ForeignKey(
        'Customer.Customer_ID'), nullable=False)
    Session_ID = Column(NVARCHAR(50), nullable=True)
    Created_At = Column(DateTime, default=func.now(), nullable=False)
    Updated_At = Column(DateTime, onupdate=func.utc_timestamp(), nullable=True)

    customer = relationship("Customer", back_populates="shopping_carts")
    cart_items = relationship(
        "ShoppingCartItem", back_populates="cart", cascade="all, delete-orphan")
