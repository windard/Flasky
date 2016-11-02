# coding=utf-8

from flask import Flask, request, redirect, abort, make_response, render_template, url_for, session, flash
from flask_script import Manager
from flask_bootstrap import Bootstrap
from flask_moment import Moment

from flask_wtf.csrf import CsrfProtect
from flask_sqlalchemy import SQLAlchemy

import os
from models import NameForm
from datetime import datetime

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(40)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://www-data:www-data@localhost/flasky'
app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
Bootstrap(app)
moment = Moment(app)
csrf = CsrfProtect(app)
db = SQLAlchemy(app)
# manager = Manager(app)

with app.app_context():
	db.create_all()

@app.route('/')
def index():
	# return "<h2>Hello World</h2>"
	return render_template("index.html",current_time=datetime.utcnow())

@app.route('/user/<name>')
def user(name):
	return "<h2>Hello %s!</h2>"%(name)

@app.route('/agent')
def agent():
	user_agent = request.headers.get('User-Agent')
	return "<p>Your User-Agent: %s</p>"%user_agent

@app.route("/login",methods=['GET','POST'])
def login():
	name = None
	form = NameForm()
	if form.validate_on_submit():
		name = form.name.data
		form.name.data = ""
		if name == "windard":
			session['name'] = form.name.data
			return redirect(url_for('index'))
		else:
			flash("Oops, It seems like you aren't him")
			return redirect(url_for('login'))
	return render_template("login.html",form=form,name=name)

@app.route('/baidu')
def baidu():
	return redirect("https://www.baidu.com")

@app.route("/test/<int:num>")
def test(num):
	if num >= 0:
		return "You Are No.%d"%num
	else:
		abort(404)

@app.route("/cookie")
def cookie():
	response = make_response("<h1>This document carries a cookies</h1>")
	response.set_cookie("admin",'1')
	return response

@app.route("/name/<name>")
def username(name):
	return render_template("user.html",name=name)

@app.route("/bad")
def bad():
	return "<h1>Bad Request</h1>",400
	
@app.route("/service")
def service():
	return "Service Unreliaziton",500

@app.errorhandler(404)
def page_not_found(error):
    # return "<p>Sorry,No Found</p>", 404
    return render_template("404.html"),404

if __name__ == '__main__':
	app.run(debug=True,threaded=True)
	# manager.run()