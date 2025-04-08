from sqlalchemy import Column, Integer, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from .base import Base


class Customer(Base):
    __tablename__ = "customer"
    id = Column(Integer, primary_key=True, autoincrement=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(String(50), nullable=False)
    email = Column(String(254), nullable=False, unique=True)
    # Password = Column(String(255), nullable=False)
    phone = Column(String(20))
    membership_level = Column(String(50), ForeignKey(
        'member.membership_level'), nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(
        datetime.timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=lambda: datetime.now(
        datetime.timezone.utc), onupdate=lambda: datetime.now(datetime.timezone.utc), nullable=False)
    deleted_at = Column(DateTime, nullable=True)

    member = relationship("Member", back_populates="customers")
    addresses = relationship("CustomerAddress", back_populates="customer")
    orders = relationship("Order", back_populates="customer")
    shopping_carts = relationship("ShoppingCart", back_populates="customer")

    """Commented out Password field because it is not on the EERD"""

    membership_level = relationship(
        "Membership_Level", back_populates="customer")

    """Functions to hash and check password"""

    def set_password(self, plaintext_password):
        """Hashes the plaintext password and stores it."""
        self.Password = generate_password_hash(plaintext_password)

    def check_password(self, plaintext_password):
        """Checks if the provided plaintext password matches the hashed password."""
        return check_password_hash(self.Password, plaintext_password)
