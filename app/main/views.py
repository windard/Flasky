# coding=utf-8

from datetime import datetime
from flask_login import login_required
from flask import render_template, session, redirect, url_for

from . import main
from .forms import NameForm
from .. import db
from ..models import User, Permission
from ..email import send_email
from ..decorators import admin_required, moderator_required

@main.route('/',methods=['GET','POST'])
def index():
	# form = NameForm()
	# if form.validate_on_submit():
	# 	user = User.query.filter_by(username=form.name.data).first()
	# 	if user is None:
	# 		user = User(username=form.name.data)
	# 		db.session.add(user)
	# 		session['known'] = False
	# 	else:
	# 		session['known'] = True
	# 		# send_mail('me@wenqiangyang.com',"New User",'mail/new_user',user=user)
	# 	session['name'] = form.name.data
	# 	form.name.data = ""
	# 	return redirect(url_for('.index'))
	# return render_template('login.html',form=form,name=session.get('name'),known=session.get('known',False))
	return render_template('index.html',current_time=datetime.utcnow())

@main.route('/secret')
@login_required
def secret():
	return "Only authenticated users are allowed!"
	
@main.route('/admin')
@login_required
@admin_required
def admin():
	return "Only Admin"

@main.route('/moderator')
@login_required
@moderator_required
def moderator():
	return "Only higher than moderator "
	