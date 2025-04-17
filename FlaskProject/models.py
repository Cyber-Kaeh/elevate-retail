import os
if os.getenv("FLASK_ENV") == "pos":
    from src.utils.db_utils import db
else:
    from database import db

class Customer(db.Model):
    __tablename__ = 'Customer'
    Customer_ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.String(255), nullable=False)
    Address = db.Column(db.String(255), nullable=False)
    Birthday = db.Column(db.String(10))
    Type = db.Column(db.String(50))

class Order(db.Model):
    __tablename__ = 'Order'
    Order_ID = db.Column(db.Integer, primary_key=True)
    Customer_ID = db.Column(db.Integer, db.ForeignKey('Customer.Customer_ID'), nullable=False)
    Type = db.Column(db.Float, nullable=False)
    Shipping_Option = db.Column(db.String(50), nullable=False)
    Shipping_Cost = db.Column(db.Float, nullable=False)

class Product(db.Model):
    __tablename__ = 'Product'
    Product_ID = db.Column(db.Integer, primary_key=True)
    Inventory_ID = db.Column(db.Integer)
    Product_name = db.Column(db.String(255), nullable=False)
    Price = db.Column(db.Float, nullable=False)
    Stock = db.Column(db.Integer, nullable=False)

class Shipping(db.Model):
    __tablename__ = 'Shipping'
    Shipping_ID = db.Column(db.Integer, primary_key=True)
    Address = db.Column(db.String(255), nullable=False)
    City = db.Column(db.String(100))
    Zip_Code = db.Column(db.String(20))
    State = db.Column(db.String(50))