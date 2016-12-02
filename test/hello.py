# coding=utf-8

from flask import Flask
# from twisted.internet import reactor

app = Flask(__name__)
# reactor.listenTCP(8080, app)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    # reactor.run()
    app.run(port=5008)


# from twisted.web import server, resource
# from twisted.internet import reactor

# class Simple(resource.Resource):
#     isLeaf = True
#     def render_GET(self, request):
#         return "<html>Hello, world!</html>"

# site = server.Site(Simple())
# reactor.listenTCP(8080, site)
# reactor.run()