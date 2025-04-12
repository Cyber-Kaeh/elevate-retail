from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base


class PurchaseOrder(Base):
    __tablename__ = 'Purchase_Order'
    id = Column(Integer, primary_key=True, autoincrement=True)
    supplier_id = Column(Integer, ForeignKey(
        'Supplier.Supplier_ID'), nullable=False)
    order_date = Column(DateTime, default=lambda: datetime.now(
        datetime.timezone.utc), nullable=False)
    status = Column(String(15), nullable=False)

    supplier = relationship("Supplier", back_populates="purchase_orders")
    items = relationship("PurchaseOrderItem", back_populates="purchase_order")
