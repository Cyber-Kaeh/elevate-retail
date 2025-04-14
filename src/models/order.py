from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base


class Order(Base):
    __tablename__ = 'Order'
    __table_args__ = {"quote": True}
    Order_ID = Column(Integer, primary_key=True, autoincrement=True)
    Customer_ID = Column(Integer, ForeignKey(
        'Customer.Customer_ID'), nullable=False)
    Order_Date = Column(DateTime, default=lambda: datetime.now(
        datetime.timezone.utc), nullable=False)

    customer = relationship("Customer", back_populates="customer_id")
    discounts = relationship("Discount", back_populates="order")
    order_item = relationship("OrderItem", back_populates="ordered")
    payment = relationship("Payment", back_populates="ordered_payment")
    order_shipping = relationship("Shipping", back_populates="shipping_order")
