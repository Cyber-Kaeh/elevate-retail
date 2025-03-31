import secrets
from flask import Flask, render_template, session
from flask_sqlalchemy import SQLAlchemy
from flask_session import Session
from werkzeug import *
from src.routes.inventory_routes import inventory_bp, single_checkout_bp
from src.routes.cart_routes import cart_bp

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///elevate_retail.db'
app.config['SECRET_KEY'] = secrets.token_hex(32)
app.config['SESSION_TYPE'] = 'sqlalchemy'
app.config['SQLALCHEMY_ENGINE_OPTIONS'] = {
    'pool_size': 50,
    'max_overflow': 20,
    'pool_timeout': 30,
    'pool_recycle': 280
}
db = SQLAlchemy(app)  # Create a single SQLAlchemy instance
app.config['SESSION_SQLALCHEMY'] = db

Session(app)

app.register_blueprint(inventory_bp)
app.register_blueprint(single_checkout_bp)
app.register_blueprint(cart_bp)


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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
