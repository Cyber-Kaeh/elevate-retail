from sqlalchemy import Column, Integer, DECIMAL, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base


class OrderItem(Base):
    __tablename__ = 'Order_Item'
    Order_ID = Column(Integer, ForeignKey('Order.Order_ID'), primary_key=True)
    Inventory_ID = Column(Integer, ForeignKey(
        'Inventory.Inventory_ID'), primary_key=True)
    Quantity = Column(Integer, nullable=False)
    Amount = Column(DECIMAL(8, 2), nullable=False)
    Tax = Column(DECIMAL(8, 2), nullable=False)
    Created_At = Column(DateTime, default=func.now(), nullable=False)
    Updated_At = Column(DateTime, onupdate=func.utc_timestamp(), nullable=True)

    ordered = relationship('Order', back_populates='order_item')
    inventory_item_order = relationship(
        'Inventory', back_populates='order_item_inv')
