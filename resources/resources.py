from bottle import Bottle, route, get, response, request, redirect
# from resources import users
import settings

app = Bottle()
app.add_hook('after_request', settings.enable_cors)

@app.route('/', method='OPTIONS')
def cors():
    return {

    }

@app.get('/')
def index():
    return {
        'status': 'success',
        'message': 'Welcome to the API index page',
    }

