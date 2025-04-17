'''
Shipping App: This is a backend for the elevate retail capstone project.
Author: Warren Whitcher
'''

# Import required modules
import os
from flask import Flask
from database import db
from shipping_routes import shipping_bp

if os.getenv("FLASK_ENV") == "pos":
    from src.utils.db_utils import db
else:
    from database import db

# Initialize Flask app
app = Flask(__name__)

# Configure the app securely
app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URI', 'mysql+pymysql://user:password@localhost/shipping_db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SESSION_TYPE'] = 'sqlalchemy'

# Initialize database
try:
    db.init_app(app)
except Exception as e:
    print(f"Error initializing the database: {e}")
    raise

# Register blueprints
app.register_blueprint(shipping_bp)

# Run the app
if __name__ == '__main__':
    app.run(debug=os.getenv('FLASK_DEBUG', 'false').lower() == 'true')