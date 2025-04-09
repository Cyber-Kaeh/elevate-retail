from sqlalchemy import Column, DECIMAL, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .base import Base


class Member(Base):
    __tablename__ = "Member"
    Membership_Level = Column(String(50), primary_key=True)
    Discount_Rate = Column(DECIMAL(5, 2))

    customers = relationship("Customer", back_populates="member")
