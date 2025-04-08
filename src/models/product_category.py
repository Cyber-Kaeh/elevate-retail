from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base


class ProductCategory(Base):
    __tablename__ = 'product_category'
    category_id = Column(Integer, primary_key=True)
    name = Column(String(100))
    description = Column(String(1000))

    category = relationship('Product', back_populates='product_category')
