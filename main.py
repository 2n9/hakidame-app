# coding: utf-8
from bottle import route, run, Bottle
from bottle import post, get, put, delete, request, response, route

# import other files
from resources import resources

root: Bottle = Bottle()

# run server
if __name__ == "__main__":
    root.mount('/resources', resources.app)
    root.run(host='0.0.0.0', port=8080, reloader=True, debug=True)