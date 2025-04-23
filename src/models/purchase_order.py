from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .base import Base


class PurchaseOrder(Base):
    __tablename__ = 'Purchase_Order'
    Purchase_Order_ID = Column(Integer, primary_key=True, autoincrement=True)
    Supplier_ID = Column(Integer, ForeignKey(
        'Supplier.Supplier_ID'), nullable=False)
    Order_Date = Column(DateTime, default=lambda: datetime.now(
        datetime.timezone.utc), nullable=False)
    Purchase_Order_Status = Column(String(15), nullable=False)

    supplier = relationship("Supplier", back_populates="purchase_orders")
    items = relationship("PurchaseOrderItem", back_populates="purchase_order")
