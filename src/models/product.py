from sqlalchemy import Column, Integer, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base


class Product(Base):
    __tablename__ = 'Product'
    # __table_args__ = {'quote': True}
    Product_ID = Column(Integer, primary_key=True, autoincrement=True)
    Product_Name = Column(String(100), nullable=False)
    Product_Description = Column(String(1000))
    Category_ID = Column(Integer, ForeignKey(
        'Product_Category.Category_ID'), nullable=False)
    Supplier_ID = Column(Integer, ForeignKey(
        'Supplier.Supplier_ID'), nullable=False)
    Image_URL = Column(String(255))
    Deleted_At = Column(DateTime, nullable=True)

    category = relationship("ProductCategory", back_populates="products")
    supplier = relationship("Supplier", back_populates="supplied_products")
    purchase_order_items = relationship(
        "PurchaseOrderItem", back_populates="ordered_product")
    inventory = relationship("Inventory", back_populates="stored_product")
    discounts = relationship("Discount", back_populates="discounted_product")

    def to_dict(self):
        return {
            'id': self.Product_ID,
            'name': self.Product_Name,
            'description': self.Product_Description,
            'category_id': self.Category_ID,
            'supplier_id': self.Supplier_ID,
            'image_url': self.Image_URL,
            'deleted_at': self.Deleted_At,
        }
