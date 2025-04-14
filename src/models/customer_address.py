from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base


class CustomerAddress(Base):
    __tablename__ = 'Customer_Address'
    Address_ID = Column(Integer, primary_key=True, autoincrement=True)
    Address_Line_1 = Column(String(50), nullable=False)
    Address_Line_2 = Column(String(35), nullable=True)
    City = Column(String(50), nullable=False)
    State = Column(String(50), nullable=False)
    Zip_Code = Column(String(10), nullable=False)
    Country = Column(String(50), nullable=False)
    Customer_ID = Column(Integer, ForeignKey(
        'Customer.Customer_ID'), nullable=False)
    Created_At = Column(DateTime, default=func.now(), nullable=False)
    Updated_At = Column(DateTime, onupdate=func.utc_timestamp(), nullable=True)
    deleted_at = Column(DateTime, nullable=True)

    customer = relationship("Customer", back_populates="addresses")

    def __repr__(self):
        return f"<CustomerAddress(id={self.id}, city='{self.city}', state='{self.state}', customer_id={self.customer_id})>"
    """helper function to return a string representation of the object if needed"""
