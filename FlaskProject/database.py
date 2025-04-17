from flask_sqlalchemy import SQLAlchemy
import sqlite3
from FlaskProject.shipping_app import app

db = SQLAlchemy()

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://username:password@localhost/shipping_db'

connection = sqlite3.connect('shippingDatabase.db')
cursor = connection.cursor()

# Creating Customers Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS Customers (
    CustomerID INT PRIMARY KEY,
    Name VARCHAR(255),
    Address VARCHAR(255),
    Email VARCHAR(255),
    PhoneNumber VARCHAR(15)
)''')

# Creating Shipping Orders Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS ShippingOrders (
    OrderID INT PRIMARY KEY,
    CustomerID INT,
    ProductDetails VARCHAR(255),
    OrderDate DATE,
    ShippingDate DATE,
    Status VARCHAR(50),
    FOREIGN KEY (CustomerID) REFERENCES Customers(CustomerID)
)''')

# Create Shipping Providers Table
cursor.execute('''
CREATE TABLE IF NOT EXISTS ShippingProviders (
    ProviderID INT PRIMARY KEY,
    ProviderName VARCHAR(255),
    ContactInfo VARCHAR(255),
    ServiceTypes VARCHAR(255)
)''')

# Create Tracking Table
cursor.execute('''
CREATE TABLE Tracking (
    TrackingID INT PRIMARY KEY,
    OrderID INT,
    TrackingNumber VARCHAR(255),
    CurrentLocation VARCHAR(255),
    ExpectedDeliveryDate DATE,
    FOREIGN KEY (OrderID) REFERENCES ShippingOrders(OrderID)
)''')

connection.commit()
connection.close()