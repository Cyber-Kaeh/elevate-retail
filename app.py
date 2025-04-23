from src.models import Customer
from flask_login import LoginManager, login_required, current_user
from src.models.forms import LoginForm

import secrets
import uuid
import random
from flask import Flask, request, make_response, redirect, render_template, session, url_for, flash
from src.utils.db_utils import db, csrf, session as flask_session
from werkzeug import *
from flask_wtf.csrf import CSRFProtect
from jinja2 import ChoiceLoader, FileSystemLoader

from src.models.forms import LoginForm
from src.routes.shop_routes import shop_bp, single_checkout_bp
from src.routes.cart_routes import cart_bp
from src.routes.login_routes import login_bp
from src.routes.product_routes import product_bp

from src.purchasing.app.main import bp as main_bp
from src.purchasing.app.api import bp as api_bp
#from src.shipping.FlaskProject.shipping_routes import shipping_bp
from src.inventory.complete_inventory_app.routes import inventory_bp

# Flask-Login

# Create Flask app
app = Flask(__name__)

# Login Manager Setup
login_manager = LoginManager()
login_manager.login_view = 'login.login'
login_manager.init_app(app)


@login_manager.user_loader
def load_user(user_id):
    return db.session.query(Customer).get(int(user_id))


# Template loader (for global + sub-app templates)
app.jinja_loader = ChoiceLoader({
    FileSystemLoader('templates'),
    FileSystemLoader('src/purchasing/app/templates'),
    FileSystemLoader('src/inventory/complete_inventory_app/templates')
})

# Config
app.config['SQLALCHEMY_DATABASE_URI'] = "mssql+pyodbc://SA:Secure1passw0rd@127.0.0.1:1433/elevate_retail?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes"
app.config['SECRET_KEY'] = secrets.token_hex(32)
app.config['SESSION_TYPE'] = 'sqlalchemy'
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'pool_size': 50,
    'max_overflow': 20,
    'pool_timeout': 30,
    'pool_recycle': 280
}
app.config['SESSION_SQLALCHEMY'] = db

# Initialize extensions
db.init_app(app)
csrf.init_app(app)
flask_session.app = app

# Register Blueprints
app.register_blueprint(shop_bp)
app.register_blueprint(single_checkout_bp)
app.register_blueprint(cart_bp)
app.register_blueprint(product_bp)
app.register_blueprint(login_bp, url_prefix='/auth')

app.register_blueprint(main_bp, url_prefix='/purchasing')
app.register_blueprint(api_bp, url_prefix='/purchasing/api')
# app.register_blueprint(shipping_bp, url_prefix='/shipping')
# csrf.exempt(shipping_bp)
app.register_blueprint(inventory_bp, url_prefix='/inventory')
csrf.exempt(inventory_bp)


# Session helper
def generate_session_id():
    return str(uuid.uuid4())


def ensure_anonymous_user():
    session_id = request.cookies.get('session_id')
    if not session_id:
        session_id = generate_session_id()
        response = make_response(redirect(request.url))
        response.set_cookie('session_id', session_id,
                            max_age=60*60*24*365, httponly=True, secure=False)
        return response
    return None

# Inject global login form for templates


@app.context_processor
def inject_login_form():
    return {'form': LoginForm()}

# Ensure session exists and is permanent


@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = 3600
    response = ensure_anonymous_user()
    if response:
        return response

# ROUTES


@app.route('/')
def home():
    return render_template('landing.html')


@app.route('/shop')
def inventory():
    return render_template('shop.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/guest-purchase-form')
def guest_purchase_form():
    return render_template('guest-purchase-form.html')


# Run App
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
