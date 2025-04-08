import unittest
from config.test_config import session
from src.models.customer import Customer
from src.models.member import Member


class TestModels(unittest.TestCase):
    def setUp(self):
        self.session = session

    def tearDown(self):
        self.session.rollback()

    def test_create_member(self):
        member = Member(membership_level='Gold', discount_rate=20.00)
        self.session.add(member)
        self.session.commit()
        self.assertEqual(member.membership_level, 'Gold')

    def test_create_customer(self):
        member = Member(membership_level='Gold', discount_rate=20.00)
        customer = Customer(first_name='John', last_name='Doe', email='john.doe@example.com',
                            phone='1234567890', membership_level=member.membership_level)
        self.session.add(member)
        self.session.add(customer)
        self.session.commit()
        self.assertEqual(customer.first_name, 'John')
        self.assertEqual(customer.member.discount_rate, 20.00)


if __name__ == '__main__':
    unittest.main()
