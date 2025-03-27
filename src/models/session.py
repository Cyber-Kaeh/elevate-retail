from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class Session(Base):
    __tablename__ = 'session'
    id = Column(Integer, primary_key=True)
    inventory_id = Column(Integer, nullable=False)
    quantity = Column(Integer, nullable=False)
