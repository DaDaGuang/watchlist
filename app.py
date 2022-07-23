from flask import Flask
from flask import url_for
from markupsafe import escape

app = Flask(__name__)

@app.route('/')
@app.route('/home')
@app.route('/index')
def hello():
    return ('Welcome to My WatchList')

@app.route('/user/<name>')
def user_page(name):
    return ('Hello, {}'.format(escape(name)))

@app.route('/test')
def test_url_for():
    print(url_for('hello'))
    print(url_for('user_page',name='cancan'))
    print(url_for('test_url_for',num=2))

    return ('Test Page')