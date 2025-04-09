from sqlalchemy import Column, Integer, DECIMAL, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base


class Discount(Base):
    __tablename__ = 'discount'
    Discount_ID = Column(Integer, primary_key=True, autoincrement=True)
    Discount_Type = Column(String(15), nullable=False)
    Amount = Column(DECIMAL(5, 2), nullable=False)
    Start_Date = Column(DateTime, nullable=False)
    End_Date = Column(DateTime, nullable=False)
    Product_ID = Column(Integer, ForeignKey('Product.Product_ID'))
    Order_ID = Column(Integer, ForeignKey('Order.Order_ID'))

    discounted_product = relationship("Product", back_populates="discounts")
    order = relationship("Order", back_populates="discounts")
