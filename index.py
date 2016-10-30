# coding=utf-8

from flask import Flask,request,redirect,abort

app = Flask(__name__)

@app.route('/')
def index():
	return "<h2>Hello World</h2>"

@app.route('/user/<name>')
def user(name):
	return "<h2>Hello %s!</h2>"%(name)

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

@app.errorhandler(404)
def page_not_found(error):
    return "<p>Sorry,No Found</p>", 404

if __name__ == '__main__':
	app.run(debug=True)