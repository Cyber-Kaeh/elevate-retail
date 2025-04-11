import secrets
from flask import Flask, redirect, render_template, session, url_for
from flask_session import Session
from werkzeug import *
from flask_wtf.csrf import CSRFProtect
from jinja2 import ChoiceLoader, FileSystemLoader

from database import db

from src.models.forms import LoginForm
from src.routes.inventory_routes import inventory_bp, single_checkout_bp
from src.routes.cart_routes import cart_bp

from src.purchasing.app.main import bp as main_bp
from src.purchasing.app.api import bp as api_bp

app = Flask(__name__)
csrf = CSRFProtect(app)

app.jinja_loader = ChoiceLoader({
    FileSystemLoader('templates'),
    FileSystemLoader('src/purchasing/app/templates')
})

app.config['SQLALCHEMY_DATABASE_URI'] = 'mssql+pyodbc://SA:Secure1passw0rd@127.0.0.1:1433/elevate_retail?driver=ODBC+Driver+18+for+SQL+Server&TrustServerCertificate=yes'
app.config['SECRET_KEY'] = secrets.token_hex(32)
app.config['SESSION_TYPE'] = 'sqlalchemy'
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'pool_size': 50,
    'max_overflow': 20,
    'pool_timeout': 30,
    'pool_recycle': 280
}
db.init_app(app)
app.config['SESSION_SQLALCHEMY'] = db

Session(app)

app.register_blueprint(inventory_bp)
app.register_blueprint(single_checkout_bp)
app.register_blueprint(cart_bp)

app.register_blueprint(main_bp, url_prefix='/purchasing')
app.register_blueprint(api_bp, url_prefix='/purchasing/api')


@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = 3600


@app.route('/')
def home():
    return render_template('landing.html')


@app.route('/checkout')
def checkout():
    return render_template('checkout.html')


@app.route('/inventory')
def inventory():
    return render_template('inventory.html')


@app.route('/purchasing')
def purchasing():
    return render_template('purchasing.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/guest-purchase-form')
def guest_purchase_form():
    return render_template('guest-purchase-form.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data
        password = form.password.data
        session['alert_message'] = "Login worked! Update me with real logic please!"
        return redirect(url_for('cart.view_cart'))
    return render_template('cart.html', form=form)


"""Probably need to make a new user authentication blueprint but this is more for testing
    the shopping cart UI and login modal - Anthony Allen"""


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
