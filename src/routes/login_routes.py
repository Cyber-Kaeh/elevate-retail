from flask import Blueprint, render_template, request, redirect, url_for, flash, session, make_response
from src.models.forms import LoginForm
from src.utils.db_utils import db
from src.models.customer import Customer
import random

login_bp = Blueprint('login', __name__)

def generate_session_id():
    return str(random.randint(100000, 999999))

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        identifier = form.identifier.data
        password = form.password.data

        try:
            # Query the Customer table to validate the user
            user = db.session.query(Customer).filter(
                (Customer.Email == identifier) | (Customer.Phone == identifier)
            ).first()

            if user and password == 'pass':  # Replace with actual password check if needed
                session_id = request.cookies.get('session_id')
                if not session_id:
                    session_id = generate_session_id()
                    response = make_response(redirect(url_for('cart.view_cart')))
                    response.set_cookie('session_id', session_id, max_age=60*60*24*365, httponly=True, secure=False)
                else:
                    response = make_response(redirect(url_for('cart.view_cart')))

                session['user_id'] = user.Customer_ID
                flash('Login successful!', 'success')
                return response
            else:
                flash('Invalid credentials. Please try again.', 'danger')

        except Exception as e:
            db.session.rollback()
            flash('An error occurred during login. Please try again later.', 'danger')
            print(f"Error: {e}")

    return render_template('login.html', form=form)

@login_bp.route('/logout')
def logout():
    session.pop('user_id', None)
    response = make_response(redirect(url_for('login.login')))
    response.set_cookie('session_id', '', expires=0)
    flash('You have been logged out.', 'info')
    return response