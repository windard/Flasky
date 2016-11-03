# coding=utf-8

from flask import render_template, redirect, request, url_for, flash
from flask_login import login_required, login_user, logout_user, current_user
from . import auth
from .. import db
from ..models import User
from ..email import send_email
from .forms import LoginForm, RegistrationForm

@auth.route('/')
def authindex():
	return render_template('auth/index.html')

@auth.route('/login',methods=['GET','POST'])
def login():
	form = LoginForm()
	if form.validate_on_submit():
		user = User.query.filter_by(email=form.email.data).first()
		if user is not None and user.verify_password(form.password.data):
			login_user(user, form.remember_me.data)
			return redirect(request.args.get('next') or url_for('auth.authindex'))
		flash('Invalid username or password')	
	return render_template('auth/login.html',form=form)

@auth.route('/logout')
@login_required
def logout():
	logout_user()
	flash('You have been logged out')
	return redirect(url_for('main.index'))

@auth.route('/register',methods=['GET','POST'])
def register():
	form = RegistrationForm()
	if form.validate_on_submit():
		user = User(email=form.email.data,username=form.username.data,password=form.password.data)
		db.session.add(user)
		try:
			db.session.commit()
		except Exception,e:
			flash('Email Duplicate')
			print e
		else:
			token = user.generate_confirmation_token()
			send_email(user.email, "Confirm Your Account", 'auth/email/confirm',user=user,token=token)
			flash('A confirmation email has been send to you by email ')
		# db.session.commit()
		# flash('You can now login.')
		return redirect(url_for('auth.authindex'))
	return render_template('auth/register.html',form=form)

@auth.route('/confirm/<token>')
@login_required
def confirm(token):
	if current_user.confirmed:
		return redirect(url_for('main.index'))
	if current_user.confirm(token):
		flash('You have confirmed your account,thanks')
	else:
		flash('The confirmation link is invalid or has expired')
	return redirect(url_for('main.index'))

@auth.route('/secret')
@login_required
def secret():
	return "Only authenticated users are allowed!"