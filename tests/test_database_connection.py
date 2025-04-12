import unittest
import pyodbc
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from src.config.test_config import SQLALCHEMY_DATABASE_URI, session


class TestDatabaseConnection(unittest.TestCase):
    def test_database_connection(self):
        try:
            # Create an engine and attempt to connect
            print(f"Attempting to connect to: {SQLALCHEMY_DATABASE_URI}")
            engine = create_engine(SQLALCHEMY_DATABASE_URI)
            connection = engine.connect()
            connection.close()
            print("Database connection successful!")
        except OperationalError as e:
            self.fail(f"Database connection failed: {e}")
        except Exception as e:
            self.fail(f"An unexpected error occurred: {e}")


if __name__ == '__main__':
    unittest.main()
