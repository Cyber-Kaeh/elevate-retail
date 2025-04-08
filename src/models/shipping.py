from sqlalchemy import Column, Integer, String, DateTime, DECIMAL, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base


class Shipping(Base):
    __tablename__ = 'shipping'
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('order.id'), nullable=False)
    cost = Column(DECIMAL(8, 2), nullable=False)
    shipped_on = Column(DateTime)
    expected_by = Column(DateTime)
    status = Column(String(15), nullable=False)
    carrier = Column(String(100), nullable=False)
    tracking_number = Column(String(50), nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(
        datetime.timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=lambda: datetime.now(
        datetime.timezone.utc), onupdate=lambda: datetime.now(datetime.timezone.utc), nullable=False)
    shipping_address_id = Column(Integer, ForeignKey(
        'customer_address.id'), nullable=False)
    billing_address_id = Column(Integer, ForeignKey(
        'customer_address.id'), nullable=False)

    order = relationship("Order", back_populates="shipping")
    shipping_address = relationship(
        "CustomerAddress", foreign_keys=[shipping_address_id])
    billing_address = relationship(
        "CustomerAddress", foreign_keys=[billing_address_id])
