from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, EmailField, IntegerField, SubmitField
from wtforms.validators import DataRequired, Email
import email_validator


class LoginForm(FlaskForm):
    identifier = StringField('Email or Phone', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Login')


class RegisterForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired()])
    email = EmailField('Email', validators=[DataRequired(), Email()])
    phone = StringField('Phone', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    submit = SubmitField('Register')
