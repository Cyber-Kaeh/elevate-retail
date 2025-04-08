from sqlalchemy import DECIMAL, CheckConstraint, Column, DateTime, ForeignKey, Integer
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

Base = declarative_base()


class Inventory(Base):
    __tablename__ = 'inventory'
    inventory_id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey(
        "Product.Product_ID"), nullable=False)
    quantity = Column(Integer, nullable=False)
    unit_price = Column(DECIMAL(8, 2), nullable=False)
    deleted_at = Column(DateTime, nullable=True)

    # Define constraints to match the SQL script
    __table_args__ = (
        CheckConstraint('Quantity >= 0',
                        name='chk_inventory_quantity_non_negative'),
        CheckConstraint('Unit_Price >= 0',
                        name='chk_inventory_unit_price_non_negative'),
    )

    product = relationship('Product', back_populates='inventory')

    def to_dict(self):
        return {
            'id': self.inventory_id,
            'product_id': self.product_id,
            'quantity': self.quantity,
            'price': self.unit_price,
        }
    """Can probably remove this to_dict function if shopping cart 
        won't be stored in a dictionary"""
