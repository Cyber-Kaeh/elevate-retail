from sqlalchemy import Column, Integer, DateTime, ForeignKey, func
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base


class PurchaseOrderItem(Base):
    __tablename__ = 'Purchase_Order_Item'
    Purchase_Order_Item_ID = Column(
        Integer, primary_key=True, autoincrement=True)
    Purchase_Order_ID = Column(Integer, ForeignKey(
        'Purchase_Order.id'), nullable=False)
    Product_ID = Column(Integer, ForeignKey(
        'Product.Product_ID'), nullable=False)
    Quantity = Column(Integer, nullable=False)
    Created_At = Column(DateTime, default=func.now(), nullable=False)
    Updated_At = Column(DateTime, onupdate=func.utc_timestamp(), nullable=True)

    purchase_order = relationship("PurchaseOrder", back_populates="items")
    ordered_product = relationship(
        "Product", back_populates="purchase_order_items")
