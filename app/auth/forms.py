# coding=utf-8

from ..models import User
from wtforms import ValidationError
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required, Length, Email, EqualTo

class LoginForm(FlaskForm):
	"""docstring for LoginForm"""
	email = StringField('Email',validators=[Required(),Length(1,64),Email()])
	password = PasswordField('Password',validators=[Required()])
	remember_me = BooleanField('Keep me logged in')
	submit = SubmitField('Log In')

class RegistrationForm(FlaskForm):
	"""docstring for RegistrationForm"""
	email = StringField('Email',validators=[Required(),Length(1,64),Email()])
	username = StringField('Username',validators=[Required(),Length(1,64)])
	password = PasswordField('Password',validators=[Required(),EqualTo('password2',message='Password must match')])
	password2 = PasswordField('Confirm password',validators=[Required()])
	submit = SubmitField('Register')
		
	def validate_email(self, field):
		if User.query.filter_by(email=field.data).first():
			raise ValidationError("Email already registered.")

	def validate_username(self, field):
		if User.query.filter_by(username=field.data).first():
			raise ValidationError('Username already in use.')

class ChangePasswordForm(FlaskForm):
	"""docstring for ChangePasswordForm"""
	old_password = PasswordField('Old password', validators=[Required()])
	password = PasswordField('New password',validators=[Required(),EqualTo('password2', message='Passwords must match')])
	password2 = PasswordField('Confirm new password',validators=[Required()])
	submit = SubmitField("Update Password")

class PasswordResetRequestForm(FlaskForm):
	"""docstring for PasswordResetRequestForm"""
	email = StringField('Email',validators=[Required(), Length(1, 64), Email()])
	submit = SubmitField('Reset Password')

class PasswordResetForm(FlaskForm):
	"""docstring for PasswordResetForm"""
	email = StringField('Email', validators=[Required(), Length(1, 64), Email()])
	password = PasswordField('New password',validators=[Required(),EqualTo('password2', message='Passwords must match')])
	password2 = PasswordField('Confirm new password',validators=[Required()])
	submit = SubmitField("Update Password")

class ChangeEmailForm(FlaskForm):
	"""docstring for ChangeEmailForm"""
	email = StringField('New Email', validators=[Required(), Length(1, 64), Email()])
	password = PasswordField('Password', validators=[Required()])
	submit = SubmitField('Update Email Address')

	def validate_email(self, field):
		if User.query.filter_by(email=field.data).first():
			raise ValidationError("Email already registered.")
