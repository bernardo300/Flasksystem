from flask import abort
from flask import Flask
from flask import redirect

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Ola Flask</h1>'


@app.route('/user/<name>')
def user(name):
    return '<h1> Hello, {}</h1>'.format(name)


@app.route('/user/<id>')
def get_user(id):
    user = load_user(id)
    if not user:
        abort(404)
    return '<h1>Hello, {}</h1>'.format(user.name)


#app.add_url_rule('/', 'index', index)
