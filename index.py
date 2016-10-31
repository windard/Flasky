# coding=utf-8

from flask import Flask, request, redirect, abort, make_response, render_template
from flask_script import Manager

app = Flask(__name__)
# app.config['debug']=True
# manager = Manager(app)

@app.route('/')
def index():
	return "<h2>Hello World</h2>"

@app.route('/user/<name>')
def user(name):
	return "It's Changed!"
	# return render_template("user.html",name=name)
	# return "<h2>Hello %s!</h2>"%(name)

@app.route('/agent')
def agent():
	user_agent = request.headers.get('User-Agent')
	return "<p>Your User-Agent: %s</p>"%user_agent

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

# @app.route("/name/<name>")
# def username(name):
# 	return render_template("user.html",name=name)

@app.route("/bad")
def bad():
	return "<h1>Bad Request</h1>",400
	
@app.route("/service")
def service():
	return "Service Unreliaziton",500

@app.errorhandler(404)
def page_not_found(error):
    return "<p>Sorry,No Found</p>", 404

if __name__ == '__main__':
	app.run(debug=True)
	# manager.run()