from sqlalchemy import Column, Integer, DECIMAL, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

Base = declarative_base()


class Customer(Base):
    __tablename__ = "Customer"
    Cust_ID = Column(Integer, primary_key=True)
    First_Name = Column(String(50), nullable=False)
    Last_Name = Column(String(50), nullable=False)
    Email = Column(String(255), nullable=False)
    Phone = Column(String(20), nullable=False)
    Membership_Level = Column(String(50), ForeignKey(
        "Member.Membership_Level"), nullable=False)
    # Password = Column(String(255), nullable=False)
    Created_At = Column(DateTime, default=lambda: datetime.now(
        datetime.timezone.utc), nullable=False)
    Updated_At = Column(DateTime, default=lambda: datetime.now(
        datetime.timezone.utc), onupdate=lambda: datetime.now(datetime.timezone.utc), nullable=False)
    Deleted_At = Column(DateTime, default=lambda: datetime.now(
        datetime.timezone.utc))

    """Commented out Password field because it is not on the EERD"""

    shopping_cart = relationship("Shopping_Cart", back_populates="customer")

    """Functions to hash and check password"""

    def set_password(self, plaintext_password):
        """Hashes the plaintext password and stores it."""
        self.Password = generate_password_hash(plaintext_password)

    def check_password(self, plaintext_password):
        """Checks if the provided plaintext password matches the hashed password."""
        return check_password_hash(self.Password, plaintext_password)


class Member(Base):
    __tablename__ = "Member"
    Membership_Level = Column(String(50), primary_key=True)
    Discount_Rate = Column(DECIMAL(5, 2))

    customers = relationship("Customer", back_populates="member")


class Customer_Address(Base):
    __tablename__ = "Customer_Address"
    Address_ID = Column(Integer, primary_key=True)
    Address_Line_1 = Column(String(50), nullable=False)
    Address_Line_2 = Column(String(35))
    City = Column(String(50), nullable=False)
    State = Column(String(50), nullable=False)
    Zip_Code = Column(String(10), nullable=False)
    Country = Column(String(50), nullable=False)
    Customer_ID = Column(Integer, ForeignKey(
        "Customer.Cust_ID"), nullable=False)
    Created_At = Column(DateTime, default=lambda: datetime.now(
        datetime.timezone.utc), nullable=False)
    Updated_At = Column(DateTime, default=lambda: datetime.now(
        datetime.timezone.utc), onupdate=lambda: datetime.now(datetime.timezone.utc), nullable=False)
    Deleted_At = Column(DateTime, default=lambda: datetime.now(
        datetime.timezone.utc))

    customer = relationship("Customer", back_populates="customer_addresses")
    customer_addresses = relationship(
        "Customer_Address", back_populates="customer")
