from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base


class Payment(Base):
    __tablename__ = 'Payment'
    Payment_ID = Column(Integer, primary_key=True, autoincrement=True)
    Order_ID = Column(Integer, ForeignKey('Order.Order_ID'), nullable=False)
    Method = Column(String(50), nullable=False)
    Status = Column(String(50))
    Created_At = Column(DateTime, default=func.now(), nullable=False)
    Updated_At = Column(DateTime, onupdate=func.utc_timestamp(), nullable=True)

    ordered_payment = relationship("Order", back_populates="payment")
