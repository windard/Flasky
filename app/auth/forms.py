# coding=utf-8

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
		
