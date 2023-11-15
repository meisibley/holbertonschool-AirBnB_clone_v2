#!/usr/bin/python3
'''using Flask to display a HTML page list
states, or cities w/ states, or not found
'''
from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.teardown_appcontext
def close_session(exc):
    '''close current SQLAlchemy session'''
    storage.close()


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def cities_states(id=None):
    '''using HTML page display cities of state'''
    states = storage.all('State')
    for state in states:
        if state.id == id and id is not None:
            return render_template('9-states.html', state,
                           id=id)
    return render_template('9-states.html', id=id)
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
