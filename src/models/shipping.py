from sqlalchemy import Column, Integer, String, DateTime, DECIMAL, ForeignKey, func
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base


class Shipping(Base):
    __tablename__ = 'Shipping'
    Shipping_ID = Column(Integer, primary_key=True, autoincrement=True)
    Order_ID = Column(Integer, ForeignKey('Order.Order_ID'), nullable=False)
    Cost = Column(DECIMAL(8, 2), nullable=False)
    Shipped_On = Column(DateTime)
    Expected_By = Column(DateTime)
    Status = Column(String(15), nullable=False)
    Carrier = Column(String(100), nullable=False)
    Tracking_Number = Column(String(50), nullable=False)
    Created_At = Column(DateTime, default=func.now(), nullable=False)
    Updated_At = Column(DateTime, onupdate=func.utc_timestamp(), nullable=True)
    Shipping_Address_ID = Column(Integer, ForeignKey(
        'Customer_Address.Address_ID'), nullable=False)
    Billing_Address_ID = Column(Integer, ForeignKey(
        'Customer_Address.Address_ID'), nullable=False)

    shipping_order = relationship("Order", back_populates="order_shipping")
    shipping_address = relationship(
        "CustomerAddress", foreign_keys=[Shipping_Address_ID])
    billing_address = relationship(
        "CustomerAddress", foreign_keys=[Billing_Address_ID])
