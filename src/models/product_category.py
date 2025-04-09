from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base


class ProductCategory(Base):
    __tablename__ = 'Product_Category'
    Category_ID = Column(Integer, primary_key=True)
    Name = Column(String(100))
    Description = Column(String(1000))

    products = relationship('Product', back_populates='category')
