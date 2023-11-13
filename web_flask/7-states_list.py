#!/usr/bin/python3
'''using Flask to display HBNB data, list states'''
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def close_session(exc):
    '''close current SQLAlchemy session'''
    storage.close()


@app.route("/states_list", strict_slashes=False)
def states_list():
    '''using HTML page to display states list'''
    st_list = storage.all('State').values()
    return renden_template('7-states_list.html', states=st_list)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
