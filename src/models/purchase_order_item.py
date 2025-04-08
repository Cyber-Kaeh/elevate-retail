from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base


class PurchaseOrderItem(Base):
    __tablename__ = 'purchase_order_item'
    id = Column(Integer, primary_key=True, autoincrement=True)
    purchase_order_id = Column(Integer, ForeignKey(
        'purchase_order.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('product.id'), nullable=False)
    quantity = Column(Integer, nullable=False)
    created_at = Column(DateTime, default=lambda: datetime.now(
        datetime.timezone.utc), nullable=False)
    updated_at = Column(DateTime, default=lambda: datetime.now(
        datetime.timezone.utc), onupdate=lambda: datetime.now(datetime.timezone.utc), nullable=False)

    purchase_order = relationship("PurchaseOrder", back_populates="items")
    product = relationship("Product", back_populates="purchase_order_items")
