# coding=utf-8

from index import db
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import Required

class NameForm(FlaskForm):
	name = StringField("What is your name?", validators=[Required()])
	submit = SubmitField("Submit")

class Role(db.Model):
	__tablename__ = 'roles'
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.Unicode(128),unique=True)
	users = db.relationship('User',backref='role')

	def __repr__(self):
		return "<Role %r>"%self.name

class User(db.Model):
	__tablename__ = 'users'
	id = db.Column(db.Integer, primary_key=True)
	username = db.Column(db.Unicode(128),unique=True,index=True)
	role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))

	def __repr__(self):
		return "<User %r>"%self.username