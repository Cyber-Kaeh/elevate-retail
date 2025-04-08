from sqlalchemy import Column, DECIMAL, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from .base import Base


class Member(Base):
    __tablename__ = "member"
    membership_level = Column(String(50), primary_key=True)
    discount_rate = Column(DECIMAL(5, 2))

    customers = relationship("Customer", back_populates="member")
