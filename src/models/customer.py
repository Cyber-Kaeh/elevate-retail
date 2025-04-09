from sqlalchemy import Column, Integer, DateTime, ForeignKey, String, func
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from .base import Base
# from src.models.customer_address import CustomerAddress
# from src.models.order import Order
# from src.models.shopping_cart import ShoppingCart
# from src.models.member import Member
# from src.models import CustomerAddress, Order, ShoppingCart, Member


class Customer(Base):
    __tablename__ = "Customer"
    __table_args__ = {"quote": False}
    Customer_ID = Column(Integer, primary_key=True, autoincrement=True)
    First_Name = Column(String(50), nullable=False)
    Last_Name = Column(String(50), nullable=False)
    Email = Column(String(254), nullable=False, unique=True)
    # Password = Column(String(255), nullable=False)
    Phone = Column(String(20))
    Membership_Level = Column(String(50), ForeignKey(
        'Member.Membership_Level'), nullable=False)
    Created_At = Column(DateTime, default=func.now(), nullable=False)
    Updated_At = Column(
        DateTime, onupdate=func.utc_timestamp(), nullable=True)
    Deleted_At = Column(DateTime, nullable=True)

    member = relationship("Member", back_populates="customers")
    addresses = relationship(
        "CustomerAddress", back_populates="customer", cascade="all, delete-orphan")
    orders = relationship(
        "Order", back_populates="customer", overlaps="customer_id")
    shopping_carts = relationship("ShoppingCart", back_populates="customer")
    customer_id = relationship(
        "Order", back_populates="customer", overlaps="orders")

    """Commented out Password field because it is not on the EERD"""

    """Functions to hash and check password"""

    def set_password(self, plaintext_password):
        """Hashes the plaintext password and stores it."""
        self.Password = generate_password_hash(plaintext_password)

    def check_password(self, plaintext_password):
        """Checks if the provided plaintext password matches the hashed password."""
        return check_password_hash(self.Password, plaintext_password)
