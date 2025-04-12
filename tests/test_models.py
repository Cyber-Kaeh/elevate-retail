import unittest
from src.config.test_config import session
from src.models import Customer, Member, CustomerAddress, ShoppingCart, ShoppingCartItem
from datetime import datetime
from decimal import Decimal


class TestModels(unittest.TestCase):
    def setUp(self):
        self.session = session

    def tearDown(self):
        self.session.rollback()
        self.session.close()

    def test_create_customer(self):
        # Create a new customer
        customer = Customer(First_Name='Frank', Last_Name='Burter', Email='frankieb@example.com',
                            Phone='1234560987', Membership_Level='Gold',
                            )
        self.session.add(customer)
        # self.session.commit()

        queried_customer = self.session.query(Customer).filter_by(
            Email='frankieb@example.com').first()

        # Update the new customer address
        customer_address = CustomerAddress(
            Address_Line_1='123 Main St',
            City='Springfield',
            State='IL',
            Zip_Code='62701',
            Country='USA',
            Customer_ID=queried_customer.Customer_ID
        )
        self.session.add(customer_address)

        queried_address = self.session.query(CustomerAddress).filter_by(
            Customer_ID=queried_customer.Customer_ID).first()
        self.assertEqual(queried_address.Address_Line_1, '123 Main St')
        self.assertEqual(queried_customer.First_Name,
                         'Frank'), 'Where is Frank?!'
        # self.assertEqual(queried_customer.Customer_ID.Custo)
        self.assertEqual(
            queried_customer.member.Discount_Rate, Decimal('0.15')), "Franks discount should be 0.15"

    def test_shopping_cart_items(self):
        # Add a customer
        customer = Customer(First_Name='Frank', Last_Name='Burter', Email='frankieb@example.com',
                            Phone='1234560987', Membership_Level='Gold',
                            )
        self.session.add(customer)

        queried_customer = self.session.query(Customer).filter_by(
            Email='frankieb@example.com').first()
        # Add a shopping cart and items for the customer
        shopping_cart = ShoppingCart(
            Cart_ID=queried_customer.Customer_ID, Customer_ID=queried_customer.Customer_ID)
        self.session.add(shopping_cart)
        # self.session.commit()

        cart_item1 = ShoppingCartItem(
            Cart_ID=shopping_cart.Cart_ID, Inventory_ID=1, Quantity=2)
        cart_item2 = ShoppingCartItem(
            Cart_ID=shopping_cart.Cart_ID, Inventory_ID=2, Quantity=1)
        self.session.add_all([cart_item1, cart_item2])
        # self.session.commit()

        # Query the shopping cart items for the customer
        queried_cart_items = self.session.query(ShoppingCartItem).join(ShoppingCart).filter(
            ShoppingCart.Customer_ID == customer.Customer_ID).all()

        # Assertions
        self.assertEqual(len(queried_cart_items), 2,
                         "Customer should have 2 items in the shopping cart")
        self.assertEqual(
            queried_cart_items[0].Quantity, 2, "First cart item quantity should be 2")
        self.assertEqual(
            queried_cart_items[1].Quantity, 1, "Second cart item quantity should be 1")


if __name__ == '__main__':
    unittest.main()
