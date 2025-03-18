import sys
import os

# Add the project root directory to the Python path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from sqlalchemy import create_engine
from src.models.inventory import Base, Inventory
from src.controllers.inventory_controller import create_inventory_item
from config.db_config import DATABASE_URL

def init_db():
    engine = create_engine(DATABASE_URL)
    Base.metadata.create_all(engine)
    print("Database initialized.")

def add_sample_data():
    create_inventory_item("Item A", 10, 5.99)
    create_inventory_item("Item B", 20, 9.99)
    create_inventory_item("Item C", 15, 2.49)
    print("Sample data added.")

if __name__ == "__main__":
    init_db()
    add_sample_data()
