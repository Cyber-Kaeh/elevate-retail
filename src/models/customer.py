from sqlalchemy import Column, Integer, Date, ForeignKey, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from src.models import Shopping_Cart

Base = declarative_base()


class Customer(Base):
    __tablename__ = "Customer"
    Cust_ID = Column(Integer, primary_key=True)
    First_Name = Column(String(255), nullable=False)
    Last_Name = Column(String(255), nullable=False)
    Email = Column(String(255), unique=True, nullable=False)
    Phone = Column()
    Password = Column(String(255), nullable=False)
    Created_At = Column(Date, nullable=False)
    Updated_At = Column(Date, nullable=False)

    shopping_cart = relationship("Shopping_Cart", back_populates="customer")
