#!/usr/bin/python3
'''using Flask to display HBNB data, list cities by states'''
from flask import Flask, render_template
from models import storage


app = Flask(__name__)


@app.teardown_appcontext
def close_session(exc):
    '''close current SQLAlchemy session'''
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def cities_list():
    '''using HTML page to display city lists of states'''
    states = storage.all('State')
    return render_template('8-cities_by_states.html', states=states)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
