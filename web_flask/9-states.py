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
def list_states():
    '''using HTML page display states'''
    states = storage.all('State').values()
    return render_template('9-states.html', states=states, display='states')


@app.route('/states/<id>', strict_slashes=False)
def list_cities(id):
    '''using HTML page display cities of state'''
    states = storage.all('State').values()
    for state in states:
        if state.id == id:
            return render_template('9-states.html', state=state,
                                   display='state')
    return render_template('9-states.html', display='nf')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
