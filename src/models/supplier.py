from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from .base import Base


class Supplier(Base):
    __tablename__ = "Supplier"
    Supplier_ID = Column(Integer, primary_key=True, autoincrement=True)
    Supplier_Name = Column(String(100), nullable=False)
    Contact_Name = Column(String(100), nullable=False)
    Contact_Email = Column(String(254), nullable=False)
    Contact_Phone = Column(String(20), nullable=False)

    # Relationships (if needed in the future)
    supplied_products = relationship("Product", back_populates="supplier")
    purchase_orders = relationship("PurchaseOrder", back_populates="supplier")

    def __repr__(self):
        return f"<Supplier(Supplier_ID={self.Supplier_ID}, Supplier_Name='{self.Supplier_Name}', Contact_Name='{self.Contact_Name}')>"
