from flask import Blueprint, render_template, request, redirect, url_for, flash, session, make_response
from src.models.forms import LoginForm
from src.utils.db_utils import db
from src.models.customer import Customer
import random

login_bp = Blueprint('login', __name__)


@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        email = form.email.data

        try:
            user = db.session.query(Customer).filter_by(Email=email).first()

            if user:
                session_id = user.Customer_ID

                redirect_url = request.referrer or url_for(
                    'inventory.view_inventory')

                response = make_response(redirect(redirect_url))
                response.set_cookie('session_id', str(
                    session_id), max_age=60*60*24*365, httponly=True, secure=False)

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
