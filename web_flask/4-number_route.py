#!/usr/bin/python3
'''Flask module documentation'''
from flask import Flask, render_template
from markupsafe import escape


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    '''method to print'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def HBNB():
    '''method to print'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def C_is(text):
    '''method to print'''
    text = text.replace('_', ' ')
    return f'C {escape(text)}'


@app.route('/python/<text>', strict_slashes=False)
def Python_is(text='is cool'):
    '''method to print'''
    text = text.replace('_', ' ')
    return f'Python {escape(text)}'


app.add_url_rule('/python', view_func=Python_is, strict_slashes=False)


@app.route('/number/<n>', strict_slashes=False)
def N_is(n):
    '''method to print'''
    if int(n):
        return f'{escape(n)} is a number'


app.add_url_rule('/number/<n>', view_func=N_is, strict_slashes=False)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
