from sqlalchemy import Column, Integer, DECIMAL, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base


class Discount(Base):
    __tablename__ = 'discount'
    id = Column(Integer, primary_key=True, autoincrement=True)
    discount_type = Column(String(15), nullable=False)
    amount = Column(DECIMAL(5, 2), nullable=False)
    start_date = Column(DateTime, default=lambda: datetime.now(
        datetime.timezone.utc), nullable=False)
    end_date = Column(DateTime, default=lambda: datetime.now(
        datetime.timezone.utc), nullable=False)
    product_id = Column(Integer, ForeignKey('product.id'))
    order_id = Column(Integer, ForeignKey('order.id'))

    product = relationship("Product", back_populates="discounts")
    order = relationship("Order", back_populates="discounts")
