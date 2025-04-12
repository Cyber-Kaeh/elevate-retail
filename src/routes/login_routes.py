from flask import Blueprint, render_template, request, redirect, url_for, flash
from src.models.forms import LoginForm, RegisterForm
from src.utils.db_utils import get_db_connection

login_bp = Blueprint('login', __name__)

@login_bp.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        identifier = form.identifier.data
        password = form.password.data

        # Mock authentication logic
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Customer WHERE Email = ? OR Phone = ?", (identifier, identifier))
        user = cursor.fetchone()

        if user and password == 'mockpassword':  # Replace with actual password check if needed
            flash('Login successful!', 'success')
            return redirect(url_for('index'))
        else:
            flash('Invalid credentials. Please try again.', 'danger')

    return render_template('login.html', form=form)

@login_bp.route('/logout')
def logout():
    flash('You have been logged out.', 'info')
    return redirect(url_for('login'))