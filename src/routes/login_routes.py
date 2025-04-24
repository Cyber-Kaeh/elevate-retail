from flask import Blueprint, render_template, request, redirect, url_for, session, flash
from flask_login import login_user, logout_user
from src.models import ShoppingCart, ShoppingCartItem
from src.models.forms import LoginForm, SignUpForm
from src.utils.db_utils import db
from src.models import Customer
from sqlalchemy.exc import SQLAlchemyError

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
            session['session_id'] = user.Customer_ID
            print(
                f"User {user.First_Name} logged in with session ID: {session['session_id']}")
            flash('Login successful!', 'success')

            session_id = request.cookies.get('session_id')
            if session_id:
                merge_temp_cart(session_id, user.Customer_ID)

            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('shop.view_shop'))
        else:
            flash('Invalid email or password.', 'danger')
    return render_template('login.html', form=form)


def merge_temp_cart(session_id, customer_id):
    try:
        temp_cart = db.session.query(ShoppingCart).filter_by(
            Session_ID=session_id).first()
        if not temp_cart:
            return

        user_cart = db.session.query(ShoppingCart).filter_by(
            Customer_ID=customer_id).first()
        if not user_cart:
            user_cart = ShoppingCart(Customer_ID=customer_id)
            db.session.add(user_cart)
            db.session.commit()

        # Merge items from the temporary cart into the user's cart
        temp_cart_items = db.session.query(ShoppingCartItem).filter_by(
            Cart_ID=temp_cart.Cart_ID).all()
        for temp_item in temp_cart_items:
            user_cart_item = db.session.query(ShoppingCartItem).filter_by(
                Cart_ID=user_cart.Cart_ID,
                Inventory_ID=temp_item.Inventory_ID
            ).first()

            if user_cart_item:
                # Update quantity if the item already exists in the user's cart
                user_cart_item.Quantity += temp_item.Quantity
            else:
                # Add the item to the user's cart
                new_item = ShoppingCartItem(
                    Cart_ID=user_cart.Cart_ID,
                    Inventory_ID=temp_item.Inventory_ID,
                    Quantity=temp_item.Quantity
                )
                db.session.add(new_item)
        db.session.commit()

        # Delete the temporary cart and its items
        db.session.query(ShoppingCartItem).filter_by(
            Cart_ID=temp_cart.Cart_ID).delete()
        db.session.delete(temp_cart)
        db.session.commit()

        print(
            f"Temporary cart merged into user cart for Customer_ID: {customer_id}")

    except SQLAlchemyError as e:
        db.session.rollback()
        flash('An error occurred while merging the cart.', 'danger')
        print(f"SQLAlchemy Error: {e}")


@login_bp.route('/logout')
def logout():
    logout_user()
    session.clear()
    response = redirect(url_for('login.login'))
    response.delete_cookie('session')
    response.delete_cookie('session_id')
    flash('You have been logged out.', 'info')
    return response


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
