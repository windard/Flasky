# coding=utf-8

import os
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager, Shell
from flask_bootstrap import Bootstrap
from flask_moment import Moment
from flask import Flask, session, redirect, url_for, render_template
from flask_wtf import FlaskForm
from flask_migrate import Migrate, MigrateCommand
from wtforms import StringField, SubmitField
from wtforms.validators import Required
from threading import Thread

from flask_mail import Mail, Message

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(40)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://www-data:www-data@localhost/flasky'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

app.config['MAIL_SERVER'] = 'smtp.qq.com'
app.config['MAIL_PORT'] = 587
app.config['MAIL_USE_TLS'] = True
app.config['MAIL_USERNAME'] = os.environ.get('MAIL_USERNAME')
app.config['MAIL_PASSWORD'] = os.environ.get('MAIL_PASSWORD')

app.config['FLASK_MAIL_SUBJECT_PREFIX'] = '[Flasky]'
app.config['FLASK_MAIL_SENDER'] = '1106911190@qq.com'

Bootstrap(app)
manager = Manager(app)
moment = Moment(app)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
mail = Mail(app)

manager.add_command('db', MigrateCommand)

def send_async_mail(app,msg):
	with app.app_context():
		mail.send(msg)

def send_mail(to,subject,template,**kwargs):
	msg = Message(app.config['FLASK_MAIL_SUBJECT_PREFIX']+subject,sender = app.config['FLASK_MAIL_SENDER'],recipients = [to])
	# msg.body = render_template(template+'.txt',**kwargs)
	msg.html = render_template(template+'.html',**kwargs)
	thr = Thread(target=send_async_mail,args=[app,msg])
	# mail.send(msg)
	thr.start()
	return thr

class NameForm(FlaskForm):
	name = StringField("What is your name?", validators=[Required()])
	submit = SubmitField("Submit")

class Role(db.Model):
	__tablename__ = 'roles'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(128),unique=True)
	# users = db.relationship('User',backref='role')

	def __repr__(self):
		return "<Role %r>"%self.name

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.Unicode(128),unique=True,index=True)
	# role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

	def __repr__(self):
		return "<User %r>"%self.username

@app.route("/",methods=['GET','POST'])
def index():
	form = NameForm()
	if form.validate_on_submit():
		user = User.query.filter_by(username=form.name.data).first()
		if user is None:
			user = User(username=form.name.data)
			db.session.add(user)
			session['known'] = False
		else:
			session['known'] = True
			send_mail('me@wenqiangyang.com',"New User",'mail/new_user',user=user)
		session['name'] = form.name.data
		form.name.data = ""
		return redirect(url_for('index'))
	return render_template('login.html',form=form,name=session.get('name'),known=session.get('known',False))

if __name__ == '__main__':
	# app.run(debug=True,threaded=True)
	manager.run()