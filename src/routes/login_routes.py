from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user
from src.models.forms import LoginForm, SignUpForm
from src.utils.db_utils import db
from src.models import Customer

# Make sure this matches what you use in login_view
login_bp = Blueprint('login', __name__)


@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = db.session.query(Customer).filter_by(
            Email=form.email.data).first()
        if user and user.check_password(form.password.data):
            login_user(user)
            flash('Login successful!', 'success')
            return redirect(url_for('inventory.view_inventory'))
        else:
            flash('Invalid email or password.', 'danger')
    return render_template('login.html', form=form)


@login_bp.route('/logout')
def logout():
    logout_user()
    flash('You have been logged out.', 'info')
    return redirect(url_for('login.login'))


@login_bp.route('/signup', methods=['GET', 'POST'])
def signup():
    form = SignUpForm()
    if form.validate_on_submit():
        existing_user = db.session.query(Customer).filter_by(
            Email=form.email.data).first()
        if existing_user:
            flash('Email already registered.', 'danger')
        else:
            user = Customer(
                First_Name=form.first_name.data,
                Last_Name=form.last_name.data,
                Email=form.email.data,
                PasswordHash=form.password.data,
                Phone=form.phone.data,
                Membership_Level='Basic'
            )
            user.set_password(form.password.data)
            db.session.add(user)
            db.session.commit()
            flash('Account created! You can now log in.', 'success')
            return redirect(url_for('login.login'))
    return render_template('signup.html', form=form)
