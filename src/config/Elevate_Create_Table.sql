-- Member Table: Stores membership levels and their discount rates.
CREATE TABLE Member (
    Membership_Level VARCHAR(50) PRIMARY KEY,
    Discount_Rate DECIMAL(5,2) NOT NULL CHECK (Discount_Rate >= 0)
);

-- Customer Table: Stores customer details.
CREATE TABLE Customer (
    Customer_ID INT IDENTITY(1,1) PRIMARY KEY,
    First_Name VARCHAR(50) NOT NULL,
    Last_Name VARCHAR(50) NOT NULL,
    Email VARCHAR(254) NOT NULL UNIQUE,
    Phone VARCHAR(20),
    Membership_Level VARCHAR(50) NOT NULL,
    Created_At DATETIME2 NOT NULL DEFAULT GETUTCDATE(),
    Updated_At DATETIME2 NULL,
    Deleted_At DATETIME2 NULL,
    CONSTRAINT FK_Customer_Member FOREIGN KEY (Membership_Level)
        REFERENCES Member(Membership_Level)
);

-- Customer_Address Table: Stores addresses associated with customers.
CREATE TABLE Customer_Address (
    Address_ID INT IDENTITY(1,1) PRIMARY KEY,
    Address_Line_1 VARCHAR(50) NOT NULL,
    Address_Line_2 VARCHAR(35) NULL,
    City VARCHAR(50) NOT NULL,
    State VARCHAR(50) NOT NULL,
    Zip_Code VARCHAR(10) NOT NULL,
    Country VARCHAR(50) NOT NULL,
    Customer_ID INT NOT NULL,
    Created_At DATETIME2 NOT NULL DEFAULT GETUTCDATE(),
    Updated_At DATETIME2 NULL,
    Deleted_At DATETIME2 NULL,
    CONSTRAINT FK_Address_Customer FOREIGN KEY (Customer_ID)
        REFERENCES Customer(Customer_ID)
);

-- Product_Category Table: Stores product category information.
CREATE TABLE Product_Category (
    Category_ID INT IDENTITY(1,1) PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Description VARCHAR(1000) NULL
);

-- Supplier Table: Stores supplier details.
CREATE TABLE Supplier (
    Supplier_ID INT IDENTITY(1,1) PRIMARY KEY,
    Supplier_Name VARCHAR(100) NOT NULL,
    Contact_Name VARCHAR(100) NOT NULL,
    Contact_Email VARCHAR(254) NOT NULL,
    Contact_Phone VARCHAR(20) NOT NULL
);

-- Product Table: Stores product information.
CREATE TABLE Product (
    Product_ID INT IDENTITY(1,1) PRIMARY KEY,
    Name VARCHAR(100) NOT NULL,
    Description VARCHAR(1000) NULL,
    Category_ID INT NOT NULL,
    Supplier_ID INT NOT NULL,
    Image_URL VARCHAR(255) NULL,
    Deleted_At DATETIME2 NULL,
    CONSTRAINT FK_Product_Category FOREIGN KEY (Category_ID)
        REFERENCES Product_Category(Category_ID),
    CONSTRAINT FK_Product_Supplier FOREIGN KEY (Supplier_ID)
        REFERENCES Supplier(Supplier_ID)
);

-- Purchase_Order Table: Stores purchase order details.
CREATE TABLE Purchase_Order (
    Purchase_Order_ID INT IDENTITY(1,1) PRIMARY KEY,
    Supplier_ID INT NOT NULL,
    Order_Date DATETIME2 NOT NULL DEFAULT GETUTCDATE(),
    Status VARCHAR(15) NOT NULL CHECK (Status IN ('Pending', 'Received', 'Cancelled')),
    CONSTRAINT FK_PO_Supplier FOREIGN KEY (Supplier_ID)
        REFERENCES Supplier(Supplier_ID)
);

-- Purchase_Order_Item Table: Stores items within a purchase order.
CREATE TABLE Purchase_Order_Item (
    Purchase_Order_Item_ID INT IDENTITY(1,1) PRIMARY KEY,
    Purchase_Order_ID INT NOT NULL,
    Product_ID INT NOT NULL,
    Quantity INT NOT NULL CHECK (Quantity > 0),
    Created_At DATETIME2 NOT NULL DEFAULT GETUTCDATE(),
    Updated_At DATETIME2 NULL,
    CONSTRAINT FK_POI_PO FOREIGN KEY (Purchase_Order_ID)
        REFERENCES Purchase_Order(Purchase_Order_ID),
    CONSTRAINT FK_POI_Product FOREIGN KEY (Product_ID)
        REFERENCES Product(Product_ID)
);

-- Inventory Table: Stores inventory records.
CREATE TABLE Inventory (
    Inventory_ID INT IDENTITY(1,1) PRIMARY KEY,
    Product_ID INT NOT NULL,
    Quantity INT NOT NULL CHECK (Quantity >= 0),
    Unit_Price DECIMAL(8,2) NOT NULL CHECK (Unit_Price >= 0),
    Deleted_At DATETIME2 NULL,
    CONSTRAINT FK_Inventory_Product FOREIGN KEY (Product_ID)
        REFERENCES Product(Product_ID)
);

-- Shopping_Cart Table: Stores customer shopping cart details.
CREATE TABLE Shopping_Cart (
    Cart_ID INT IDENTITY(1,1) PRIMARY KEY,
    Customer_ID INT NOT NULL,
    Created_At DATETIME2 NOT NULL DEFAULT GETUTCDATE(),
    Updated_At DATETIME2 NULL,
    CONSTRAINT FK_Cart_Customer FOREIGN KEY (Customer_ID)
        REFERENCES Customer(Customer_ID)
);

-- Shopping_Cart_Item Table: Stores items within a shopping cart.
CREATE TABLE Shopping_Cart_Item (
    Cart_ID INT NOT NULL,
    Inventory_ID INT NOT NULL,
    Quantity INT NOT NULL CHECK (Quantity > 0),
    Created_At DATETIME2 NOT NULL DEFAULT GETUTCDATE(),
    Updated_At DATETIME2 NULL,
    PRIMARY KEY (Cart_ID, Inventory_ID),
    CONSTRAINT FK_CartItem_Cart FOREIGN KEY (Cart_ID)
        REFERENCES Shopping_Cart(Cart_ID),
    CONSTRAINT FK_CartItem_Inventory FOREIGN KEY (Inventory_ID)
        REFERENCES Inventory(Inventory_ID)
);

-- [Order] Table: Enclose in brackets since ORDER is a reserved keyword.
CREATE TABLE [Order] (
    Order_ID INT IDENTITY(1,1) PRIMARY KEY,
    Customer_ID INT NOT NULL,
    Order_Date DATETIME2 NOT NULL DEFAULT GETUTCDATE(),
    CONSTRAINT FK_Order_Customer FOREIGN KEY (Customer_ID)
        REFERENCES Customer(Customer_ID)
);

-- Order_Item Table: Stores items within an order.
CREATE TABLE Order_Item (
    Order_ID INT NOT NULL,
    Inventory_ID INT NOT NULL,
    Quantity INT NOT NULL CHECK (Quantity > 0),
    Amount DECIMAL(8,2) NOT NULL CHECK (Amount >= 0),
    Tax DECIMAL(8,2) NOT NULL CHECK (Tax >= 0),
    Created_At DATETIME2 NOT NULL DEFAULT GETUTCDATE(),
    Updated_At DATETIME2 NULL,
    PRIMARY KEY (Order_ID, Inventory_ID),
    CONSTRAINT FK_OrderItem_Order FOREIGN KEY (Order_ID)
        REFERENCES [Order](Order_ID),
    CONSTRAINT FK_OrderItem_Inventory FOREIGN KEY (Inventory_ID)
        REFERENCES Inventory(Inventory_ID)
);

-- Payment Table: Stores payment details for an order.
CREATE TABLE Payment (
    Payment_ID INT IDENTITY(1,1) PRIMARY KEY,
    Order_ID INT NOT NULL,
    Method VARCHAR(50) NOT NULL,
    Status VARCHAR(50) NULL CHECK (Status IN ('Pending', 'Completed', 'Failed')),
    Created_At DATETIME2 NOT NULL DEFAULT GETUTCDATE(),
    Updated_At DATETIME2 NULL,
    CONSTRAINT FK_Payment_Order FOREIGN KEY (Order_ID)
        REFERENCES [Order](Order_ID)
);

-- Shipping Table: Stores shipping details for an order.
CREATE TABLE Shipping (
    Shipping_ID INT IDENTITY(1,1) PRIMARY KEY,
    Order_ID INT NOT NULL,
    Cost DECIMAL(8,2) NOT NULL CHECK (Cost >= 0),
    Shipped_On DATETIME2 NULL,
    Expected_By DATETIME2 NULL,
    Status VARCHAR(15) NOT NULL CHECK (Status IN ('Pending', 'Shipped', 'Delivered', 'Returned')),
    Carrier VARCHAR(100) NOT NULL,
    Tracking_Number VARCHAR(50) NOT NULL,
    Created_At DATETIME2 NOT NULL DEFAULT GETUTCDATE(),
    Updated_At DATETIME2 NULL,
    Shipping_Address_ID INT NOT NULL,
    Billing_Address_ID INT NOT NULL,
    CONSTRAINT FK_Shipping_Order FOREIGN KEY (Order_ID)
        REFERENCES [Order](Order_ID),
    CONSTRAINT FK_Shipping_Address FOREIGN KEY (Shipping_Address_ID)
        REFERENCES Customer_Address(Address_ID),
    CONSTRAINT FK_Billing_Address FOREIGN KEY (Billing_Address_ID)
        REFERENCES Customer_Address(Address_ID)
);

-- Discount Table: Stores discount details, may apply to a Product or an Order.
CREATE TABLE Discount (
    Discount_ID INT IDENTITY(1,1) PRIMARY KEY,
    Discount_Type VARCHAR(15) NOT NULL CHECK (Discount_Type IN ('Percentage', 'Flat')),
    Amount DECIMAL(5,2) NOT NULL CHECK (Amount >= 0),
    Start_Date DATE NOT NULL,
    End_Date DATE NOT NULL,
    Product_ID INT NULL,
    Order_ID INT NULL,
    CONSTRAINT FK_Discount_Product FOREIGN KEY (Product_ID)
        REFERENCES Product(Product_ID),
    CONSTRAINT FK_Discount_Order FOREIGN KEY (Order_ID)
        REFERENCES [Order](Order_ID)
);
