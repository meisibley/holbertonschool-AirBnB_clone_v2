#!/usr/bin/python3
'''display python in a Flask web application'''
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


@app.route("/python")
@app.route("/python/<text>", strict_slashes=False)
def py_text(text="is cool"):
    '''display "Python" and text value'''
    py_text = text.replace('_', ' ')
    return "Python {}".formate(py_text)

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
