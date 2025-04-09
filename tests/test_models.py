import unittest
from src.config.test_config import session
from src.models import Customer
from datetime import datetime


class TestModels(unittest.TestCase):
    def setUp(self):
        self.session = session

    def tearDown(self):
        self.session.rollback()
        self.session.close()

    def test_create_customer(self):
        # customer = Customer(First_Name='John', Last_Name='Doe', Email='john.doe@example.com',
        #                     Phone='1234567890', Membership_Level='Gold',
        #                     )
        # self.session.add(customer)
        # accidently commited 'John Doe' to the database, leaving him here as reference
        customer = Customer(First_Name='Frank', Last_Name='Burter', Email='frankieb@example.com',
                            Phone='1234560987', Membership_Level='Gold',
                            )
        self.session.add(customer)
        # self.session.commit()
        self.assertEqual(customer.First_Name, 'Frank'), 'Where is Frank?!'
        self.assertEqual(
            customer.member.Discount_Rate, .15), "Franks discount should be 0.15"


if __name__ == '__main__':
    unittest.main()
