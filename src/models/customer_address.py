from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base


class CustomerAddress(Base):
    __tablename__ = 'customer_address'
    id = Column(Integer, primary_key=True, autoincrement=True)
    address_line_1 = Column(String(50), nullable=False)
    address_line_2 = Column(String(35))
    city = Column(String(50), nullable=False)
    state = Column(String(50), nullable=False)
    zip_code = Column(String(10), nullable=False)
    country = Column(String(50), nullable=False)
    customer_id = Column(Integer, ForeignKey('customer.id'), nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(
        datetime.timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=lambda: datetime.now(
        datetime.timezone.utc), onupdate=lambda: datetime.now(datetime.timezone.utc), nullable=False)
    deleted_at = Column(DateTime, nullable=True)

    customer = relationship("Customer", back_populates="addresses")

    def __repr__(self):
        return f"<CustomerAddress(id={self.id}, city='{self.city}', state='{self.state}', customer_id={self.customer_id})>"
    """helper function to return a string representation of the object if needed"""
