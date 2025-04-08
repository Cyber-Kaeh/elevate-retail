from sqlalchemy import Column, Integer, DECIMAL, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base


class OrderItem(Base):
    __tablename__ = 'order_item'
    order_id = Column(Integer, ForeignKey('order.id'), primary_key=True)
    inventory_id = Column(Integer, ForeignKey(
        'inventory.id'), primary_key=True)
    quantity = Column(Integer, nullable=False)
    amount = Column(DECIMAL(8, 2), nullable=False)
    tax = Column(DECIMAL(8, 2), nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(
        datetime.timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=lambda: datetime.now(
        datetime.timezone.utc), onupdate=lambda: datetime.now(datetime.timezone.utc), nullable=False)

    order = relationship('Order', back_populates='order_item')
    inventory = relationship('Inventory', back_populates='order_item')
