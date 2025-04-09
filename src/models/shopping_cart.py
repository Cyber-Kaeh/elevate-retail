from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base


class ShoppingCart(Base):
    __tablename__ = 'shopping_cart'
    cart_id = Column(Integer, primary_key=True)
    cust_id = Column(Integer, ForeignKey('customer.id'), nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(
        datetime.timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=lambda: datetime.now(
        datetime.timezone.utc), onupdate=lambda: datetime.now(datetime.timezone.utc), nullable=False)

    customer = relationship("Customer", back_populates="shopping_carts")
