from flask import render_template, request, redirect, url_for, flash
from flask_mail import Message
from itsdangerous import URLSafeTimedSerializer, SignatureExpired, BadSignature
from src.models import ForgotPasswordForm, ResetPasswordForm
from src.models import User, db
from . import mail

s = URLSafeTimedSerializer("your_secret_key")  # match app.secret_key!!


@auth.route('/forgot-password', methods=['GET', 'POST'])
def forgot_password():
    form = ForgotPasswordForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user:
            token = s.dumps(user.email, salt='password-reset-salt')
            reset_link = url_for('auth.reset_password',
                                 token=token, _external=True)
            msg = Message('Password Reset Request', recipients=[user.email])
            msg.body = f'Click the link to reset your password:\n{reset_link}'
            mail.send(msg)
        flash('If the email exists in our system, a reset link has been sent.')
        return redirect(url_for('auth.login'))
    return render_template('forgot_password.html', form=form)


@auth.route('/reset-password/<token>', methods=['GET', 'POST'])
def reset_password(token):
    try:
        email = s.loads(token, salt='password-reset-salt',
                        max_age=3600)  # 1 hour expiry
    except SignatureExpired:
        flash('This link has expired.', 'danger')
        return redirect(url_for('auth.forgot_password'))
    except BadSignature:
        flash('Invalid or expired token.', 'danger')
        return redirect(url_for('auth.forgot_password'))

    user = User.query.filter_by(email=email).first_or_404()
    form = ResetPasswordForm()
    if form.validate_on_submit():
        user.set_password(form.password.data)
        db.session.commit()
        flash('Your password has been updated. You can now log in.')
        return redirect(url_for('auth.login'))

    return render_template('reset_password.html', form=form)
