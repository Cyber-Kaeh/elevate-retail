from sqlalchemy import Column, Integer, DateTime, ForeignKey, String
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base


class Product(Base):
    __tablename__ = 'Product'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(100), nullable=False)
    description = Column(String(1000))
    category_id = Column(Integer, ForeignKey(
        'Product_Category.Category_ID'), nullable=False)
    supplier_id = Column(Integer, ForeignKey(
        'Supplier.Supplier_ID'), nullable=False)
    image_url = Column(String(255))
    deleted_at = Column(DateTime, nullable=True)

    category = relationship("ProductCategory", back_populates="product")
    supplier = relationship("Supplier", back_populates="products")
    purchase_order_items = relationship(
        "PurchaseOrderItem", back_populates="product")
    inventory_items = relationship("Inventory", back_populates="product")
    discounts = relationship("Discount", back_populates="product")
