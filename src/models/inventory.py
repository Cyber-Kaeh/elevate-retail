from sqlalchemy import DECIMAL, Column, Date, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from src.models import Shopping_Cart_Item

Base = declarative_base()


class Inventory(Base):
    __tablename__ = 'Inventory'
    Inventory_ID = Column(Integer, primary_key=True)
    Product_ID = Column(Integer, ForeignKey(
        "Product.Product_ID"), nullable=False)
    Quantity = Column(Integer, nullable=False)
    Unit_Price = Column(DECIMAL(8, 2), nullable=False)
    Deleted_At = Column(Integer)

    product = relationship('Product', back_populates='inventory')

    def to_dict(self):
        return {
            'id': self.Inventory_ID,
            'name': self.name,
            'quantity': self.Quantity,
            'price': self.Unit_Price,
        }


class Product(Base):
    __tablename__ = 'Product'
    Product_ID = Column(Integer, primary_key=True)
    Name = Column(String(255))
    Description = Column(String(255))
    Category_ID = Column(String(100), ForeignKey(
        'Product_Category.Category_ID'))
    Supplier_ID = Column(Integer, ForeignKey('Supplier.Supplier_ID'))
    Image_URL = Column(String(255))
    Deleted_At = Column(Date)

    inventory = relationship(
        'Inventory', back_populates='product', uselist=False)
    cart_items = relationship('Shopping_Cart_Item', back_populates='inventory')


class Product_Category(Base):
    __tablename__ = 'Product_Category'
    Category_ID = Column(Integer, primary_key=True)
    Name = Column(String(255))
    Description = Column(String(255))

    category = relationship('Product', back_populates='product_category')
