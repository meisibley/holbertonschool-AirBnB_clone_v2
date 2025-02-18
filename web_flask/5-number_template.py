#!/usr/bin/python3
'''display a HTML page'''
from flask import Flask, render_template

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


@app.route("/number/<int:n>", strict_slashes=False)
def num_n(n):
    '''display "n is a number" if n is an int'''
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def n_template(n):
    '''display a HTML page if n is int'''
    return render_template('5-number.html', num=n)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
