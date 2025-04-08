-- Insert Membership Levels
INSERT INTO Member (Membership_Level, Discount_Rate)
VALUES 
  ('Basic', 0.05),   
  ('Silver', 0.10),  
  ('Gold', 0.15),    
  ('Platinum', 0.20);

-- Insert Customers (let the identity column auto-generate Customer_ID)
INSERT INTO Customer (First_Name, Last_Name, Email, Phone, Membership_Level)
VALUES
  ('Paula', 'Durham', 'paula_durham@hotmail.com', '336-636-3366', 'Basic'),
  ('Luis', 'Salem', 'luis.salem@gmail.com', '919-663-6363', 'Silver');

-- Insert Customer Addresses (omit Address_ID to auto-generate)
INSERT INTO Customer_Address (Address_Line_1, Address_Line_2, City, State, Zip_Code, Country, Customer_ID)
VALUES
  ('211 Silas Creek Pkwy', NULL, 'Winston Salem', 'NC', '27103', 'USA', 1),
  ('606 Coliseum Dr.', NULL, 'Winston Salem', 'NC', '27106', 'USA', 2);

-- Insert Product Categories (omit Category_ID)
INSERT INTO Product_Category (Name, Description)
VALUES 
  ('Haircare', 'Products related to haircare maintenance'), 
  ('Electronics', 'Products related to electronic devices, computers, cell-phones, and other electronic accessories');

-- Insert Suppliers (omit Supplier_ID)
INSERT INTO Supplier (Supplier_Name, Contact_Name, Contact_Email, Contact_Phone)
VALUES
  ('Beautisa', 'Laura Pierre', 'laura.p@beautisa.com', '919-991-1199'),
  ('Beats by Dre', 'John Smith', 'johnsmith@beatsbydre.com', '209-902-2200');

-- Insert Products (omit Product_ID)
INSERT INTO Product (Name, Description, Category_ID, Supplier_ID, Image_URL)
VALUES
  ('Hair Spray Bottle', 'Ultra fine mist water sprayer for hairstyling and cleaning 2 pack 6.8 oz', 1, 1, NULL),
  ('Beats Powerbeats Pro 2', 'Wireless bluetooth earbuds - noise cancelling', 2, 2, NULL);

-- Insert Purchase Orders (omit Purchase_Order_ID)
INSERT INTO Purchase_Order (Supplier_ID, Order_Date, Status)
VALUES
  (1, DATEADD(day, -5, GETUTCDATE()), 'Received'),
  (2, DATEADD(day, -3, GETUTCDATE()), 'Pending'),
  (1, DATEADD(day, -1, GETUTCDATE()), 'Pending');

-- Insert Purchase Order Items (omit Purchase_Order_Item_ID)
INSERT INTO Purchase_Order_Item (Purchase_Order_ID, Product_ID, Quantity)
VALUES
  (1, 1, 500),
  (2, 1, 250),
  (3, 2, 75);

-- Insert Inventory records (omit Inventory_ID)
INSERT INTO Inventory (Product_ID, Quantity, Unit_Price)
VALUES
  (1, 3000, 6.99),
  (2, 100, 249.00);

-- Insert Shopping Carts (omit Cart_ID)
INSERT INTO Shopping_Cart (Customer_ID, Created_At)
VALUES
  (1, DATEADD(day, -1, GETUTCDATE())),
  (2, DATEADD(day, -1, GETUTCDATE()));

-- Insert Shopping Cart Items
INSERT INTO Shopping_Cart_Item (Cart_ID, Inventory_ID, Quantity)
VALUES
  (1, 1, 3),
  (2, 2, 1);

-- Insert Customer Orders (omit Order_ID as identity)
INSERT INTO [Order] (Customer_ID, Order_Date)
VALUES
  (1, DATEADD(day, -2, GETUTCDATE())),
  (2, DATEADD(day, -1, GETUTCDATE()));

-- Insert Order Items
INSERT INTO Order_Item (Order_ID, Inventory_ID, Quantity, Amount, Tax)
VALUES
  (1, 1, 3, 13.98, 1.40),
  (2, 2, 1, 747.00, 50.00);

-- Insert Payments (omit Payment_ID)
INSERT INTO Payment (Order_ID, Method, Status, Created_At, Updated_At)
VALUES
  (1, 'Debit Card', 'Pending', DATEADD(day, -1, GETUTCDATE()), DATEADD(day, -1, GETUTCDATE())),
  (2, 'Credit Card', 'Completed', DATEADD(day, -1, GETUTCDATE()), DATEADD(day, -1, GETUTCDATE()));

-- Insert Shipping records (omit Shipping_ID)
INSERT INTO Shipping (Order_ID, Cost, Shipped_On, Expected_By, Status, Carrier, Tracking_Number, Updated_At, Shipping_Address_ID, Billing_Address_ID)
VALUES
  (1, 18.00, DATEADD(day, -1, GETUTCDATE()), DATEADD(day, 2, GETUTCDATE()), 'Pending', 'USPS', 'EK41235678US', GETUTCDATE(), 1, 1), 
  (2, 18.00, GETUTCDATE(), DATEADD(day, 3, GETUTCDATE()), 'Shipped', 'USPS', 'EK56789143US', GETUTCDATE(), 2, 2);

-- Insert Discounts (omit Discount_ID)
INSERT INTO Discount (Discount_Type, Amount, Start_Date, End_Date, Product_ID, Order_ID)
VALUES
  ('Percentage', 0.05, DATEADD(day, -3, GETUTCDATE()), DATEADD(day, 4, GETUTCDATE()), 1, 1),
  ('Percentage', 0.10, DATEADD(day, -2, GETUTCDATE()), DATEADD(day, 5, GETUTCDATE()), 2, 2);
