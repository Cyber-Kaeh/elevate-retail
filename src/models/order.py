from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base


class Order(Base):
    __tablename__ = 'order'
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customer.id'), nullable=False)
    order_date = Column(DateTime, default=lambda: datetime.now(
        datetime.timezone.utc), nullable=False)

    customer = relationship("Customer")
