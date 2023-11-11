#!/usr/bin/python3
'''display number in a Flask web application'''
from flask import Flask

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    '''display Hello HBNB!'''
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    '''display HBNB'''
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_text(text):
    '''display c and text value'''
    n_text = text.replace('_', ' ')
    return "C {}".format(n_text)


@app.route("/python", strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def py_text(text="is cool"):
    '''display "Python" and text value'''
    py_text = text.replace('_', ' ')
    return "Python {}".format(py_text)


@app.route("/number/<n>", strict_slashes=False)
def num_n(n):
    '''display "n is a number" if n is an int'''
    if n is int:
        return "{} is a number".format(n)
    else:
        return NULL

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
