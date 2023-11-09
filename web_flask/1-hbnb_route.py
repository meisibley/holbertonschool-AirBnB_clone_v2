#!/usr/bin/python3
'''Flask module documentation'''
from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_HBNB():
    '''method to print'''
    return 'Hello HBNB!'


@app.route('/hbnb')
def HBNB():
    '''method to print'''
    return 'HBNB'


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
